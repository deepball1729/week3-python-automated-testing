import unittest
from student_grades import calculate_average, get_grade, build_report

class TestCalculateAverage(unittest.TestCase):
    def test_average(self):
        self.assertEqual(calculate_average([80, 90, 100]), 90.0)
    def test_generator_input(self):
        self.assertEqual(calculate_average(x for x in [10, 20]), 15.0)
    def test_single_score(self):
        self.assertEqual(calculate_average([75]), 75.0)
    def test_empty_input(self):
        with self.assertRaises(ValueError): calculate_average([])
    def test_non_numeric_input(self):
        with self.assertRaises(TypeError): calculate_average([80, "90"])
    def test_boolean_input(self):
        with self.assertRaises(TypeError): calculate_average([True, 80])
    def test_out_of_range_input(self):
        for score in (-1, 101):
            with self.subTest(score=score):
                with self.assertRaises(ValueError): calculate_average([score])

class TestGetGrade(unittest.TestCase):
    def test_grade_boundaries(self):
        cases = [(100,"A"),(90,"A"),(89.9,"B"),(80,"B"),(79.9,"C"),
                 (70,"C"),(69.9,"D"),(60,"D"),(59.9,"F"),(0,"F")]
        for score, expected in cases:
            with self.subTest(score=score): self.assertEqual(get_grade(score), expected)
    def test_rejects_text(self):
        with self.assertRaises(TypeError): get_grade("88")
    def test_rejects_boolean(self):
        with self.assertRaises(TypeError): get_grade(False)
    def test_rejects_out_of_range(self):
        with self.assertRaises(ValueError): get_grade(120)

class TestBuildReport(unittest.TestCase):
    def test_report_summary(self):
        report = build_report({"Asha":95,"Ravi":75,"Meera":85})
        self.assertEqual(report["grades"], {"Asha":"A","Ravi":"C","Meera":"B"})
        self.assertAlmostEqual(report["class_average"], 85.0)
        self.assertEqual(report["highest_score"], 95.0)
        self.assertEqual(report["lowest_score"], 75.0)
        self.assertEqual(report["student_count"], 3)
    def test_trims_name(self):
        self.assertEqual(build_report({" Asha ":90})["grades"], {"Asha":"A"})
    def test_empty_report(self):
        with self.assertRaises(ValueError): build_report({})
    def test_wrong_container(self):
        with self.assertRaises(TypeError): build_report([("Asha",90)])
    def test_blank_name(self):
        with self.assertRaises(ValueError): build_report({"   ":90})
    def test_invalid_score(self):
        with self.assertRaises(ValueError): build_report({"Asha":150})

if __name__ == "__main__":
    unittest.main(verbosity=2)
