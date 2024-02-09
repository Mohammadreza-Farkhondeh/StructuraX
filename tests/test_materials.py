import unittest

from structurax.core.materials import BaseMaterial


class TestBaseMaterial(unittest.TestCase):
    def setUp(self):
        self.material = BaseMaterial(
            youngs_modulus=200e9,
            shear_modulus=78000,
            yield_tension=250e6,
            ultimate_tension=400e6,
            poisson_ratio=0.3,
            density=7850,
        )

    def test_material_initialization(self):
        self.assertEqual(self.material.youngs_modulus, 200e9)
        self.assertEqual(self.material.shear_modulus, 78000)
        self.assertEqual(self.material.yield_tension, 250e6)
        self.assertEqual(self.material.ultimate_tension, 400e6)
        self.assertEqual(self.material.poisson_ratio, 0.3)
        self.assertEqual(self.material.density, 7850)

    def test_check_yield_below_yield_tension(self):
        self.assertFalse(self.material.check_yield(200e6))

    def test_check_yield_at_yield_tension(self):
        self.assertTrue(self.material.check_yield(250e6))

    def test_check_yield_above_yield_tension(self):
        self.assertTrue(self.material.check_yield(300e6))

    def test_check_fail_below_ultimate_tension(self):
        self.assertFalse(self.material.check_fail(350e6))

    def test_check_fail_at_ultimate_tension(self):
        self.assertTrue(self.material.check_fail(400e6))

    def test_check_fail_above_ultimate_tension(self):
        self.assertTrue(self.material.check_fail(450e6))

    def test_calculate_stress_strain_response(self):
        strain = self.material.calculate_stress_strain_response(1000)
        expected_strain = 1000 / 200000  # stress = young's modulus * strain
        self.assertEqual(strain, expected_strain)

    def test_calculate_stress_strain_response_zero_stress(self):
        strain = self.material.calculate_stress_strain_response(0)
        self.assertEqual(strain, 0)

    def test_calculate_stress_strain_response_negative_stress(self):
        with self.assertRaises(ValueError):
            self.material.calculate_stress_strain_response(-1)

    def test_calculate_stress_strain_response_stress_equals_youngs_modulus(self):
        stress = self.material.youngs_modulus
        strain = self.material.calculate_stress_strain_response(stress)
        expected_strain = stress / self.material.youngs_modulus
        self.assertEqual(strain, expected_strain)

    def test_calculate_stress_strain_response_stress_greater_than_youngs_modulus(self):
        stress = self.material.youngs_modulus + 1000
        with self.assertRaises(ValueError):
            self.material.calculate_stress_strain_response(stress)


if __name__ == "__main__":
    unittest.main()
