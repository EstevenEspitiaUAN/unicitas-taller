
import unittest
from unicitas import reservar


class ReservaTest(unittest.TestCase):

    def test_no_confirma_dos_veces(self):
        libres = {"10:00"}

        self.assertTrue(reservar(libres, "10:00"))
        self.assertFalse(reservar(libres, "10:00"))
        self.assertEqual(libres, set())

    def test_horario_inexistente(self):
        libres = {"10:00"}

        self.assertFalse(reservar(libres, "12:00"))
        self.assertEqual(libres, {"10:00"})

    def test_dos_horarios_diferentes(self):
        libres = {"10:00", "11:00"}

        self.assertTrue(reservar(libres, "10:00"))
        self.assertTrue(reservar(libres, "11:00"))
        self.assertEqual(libres, set())

    def test_rechazo_conserva_los_demas_horarios(self):
        libres = {"10:00", "11:00"}

        self.assertFalse(reservar(libres, "12:00"))
        self.assertEqual(libres, {"10:00", "11:00"})


if __name__ == "__main__":
    unittest.main()
