# Unicitas Taller

Taller de pruebas automatizadas e integración continua.

## Objetivo

Verificar que un horario disponible solo pueda reservarse una vez.

## Ejecutar las pruebas

```bash
python -m unittest discover -s tests -v
```

El proyecto incluye pruebas para reservas repetidas, horarios inexistentes y conservación de la disponibilidad.