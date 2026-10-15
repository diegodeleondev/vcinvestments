# vcinvestments

Fichas de cuentas de clientes: investigación, equipo, interacciones y pipeline de oportunidades.

## Clientes

| Cliente | Tipo | Sede | Etapa | Ficha |
|---|---|---|---|---|
| Konvoy Ventures | VC: gaming, deep tech, industrias críticas | Denver, CO | Prospecto | [clientes/konvoy](clientes/konvoy/README.md) |

## Estructura

```
clientes/
├── _plantilla/          # copiar para cada cliente nuevo
└── <cliente>/
    ├── README.md        # perfil e investigación
    ├── equipo.md        # personas clave y quién decide
    ├── interacciones.md # registro de contactos
    └── oportunidades.md # pipeline y próximos pasos
```

**Cliente nuevo:** `cp -r clientes/_plantilla clientes/<nombre>`, llenar el README y agregar una fila a la tabla de arriba.

> El repositorio es **público**: no guardes correos personales, teléfonos, montos confidenciales ni información privada del cliente.
