# Deberes del Hogar

App instalable (PWA) para repartir los deberes de la casa entre la familia, con rotación semanal automática y todo sincronizado en un calendario compartido de Google.

## Qué hace

- **Deberes:** eliges cuáles se reparten (activar/desactivar), día y hora de cada uno. Puedes agregar los tuyos.
- **Familia:** cada persona con su correo de Google. Cada una entra con su propia cuenta desde su teléfono.
- **Rotación:** los deberes activos giran entre las personas cada semana, sin que nadie tenga que repartir a mano. Si una semana quieres cambiar a alguien, tocas su nombre.
- **Hecho:** cualquiera marca ✓ en el deber que hizo, y todos lo ven al instante. Si lo marca otra persona, queda registrado quién lo hizo.
- **Ruleta:** eliges un deber, giras la ruleta y decide a quién le toca esta semana; puedes asignarlo con un toque.
- **Aviso de domingo:** un recordatorio semanal (evento recurrente) para que todos revisen el reparto.
- **Cierre de mes:** después del último domingo, la app prepara una imagen por persona con lo que completó, lo que le faltó y quién lo hizo por ella; al confirmar, borra esos deberes del calendario y guarda el resumen.
- **Google Calendar:** un evento por deber, con recordatorio 30 min antes. Al re-sincronizar los eventos se actualizan, no se duplican, y nunca se crean para días ya pasados.

## Cómo funciona (importante)

**No hay servidor ni base de datos.** El calendario compartido *"Deberes del hogar"* **es** la base de datos:

- La configuración (personas, deberes, rotación) se guarda en la descripción del calendario.
- Cada deber es un evento con propiedades privadas (`dhKey`, `dhDone`, `dhBy`) para encontrarlo y actualizarlo desde cualquier teléfono.
- La rotación se calcula a partir de la fecha, así que todos los teléfonos llegan al mismo reparto sin coordinarse.

Por eso todos ven lo mismo y no cuesta nada mantenerlo.

### Lo que esto implica

- Cada persona necesita una cuenta de Google y el calendario **compartido con permiso de edición**.
- Si dos personas cambian la configuración exactamente a la vez, gana el último cambio (no se corrompe nada).
- La sesión de Google dura 1 hora; la app vuelve a pedir permiso cuando hace falta.
- Los datos del teléfono son solo una copia: si borras los datos de la app, al reconectar vuelve a leer todo del calendario.

## Configuración

Ver **[CONFIGURACION.md](CONFIGURACION.md)**.

## Archivos

| Archivo | Para qué |
|---|---|
| `index.html` | Toda la app (sin dependencias ni build) |
| `manifest.json` | Para instalarla como app |
| `sw.js` | Caché para que abra sin internet |
| `icon-*.png`, `heart.svg` | Iconos y logo pixelado |
| `tools/make-icons.py` | Regenera los iconos desde el logo |

### Publicar una actualización

Editas `index.html` y subes el cambio. Si cambiaste `sw.js` o los iconos, sube también el número de `CACHE` en `sw.js` para que los teléfonos tomen la versión nueva.
