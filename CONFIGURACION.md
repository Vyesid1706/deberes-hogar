# Configuración

Tres pasos: (1) crear el acceso de Google, (2) instalar en cada teléfono, (3) compartir el calendario. La app ya está publicada en:

> **https://vyesid1706.github.io/deberes-hogar/**

---

## 1. Crear el Client ID de Google (una vez, ~10 min)

Hazlo con la cuenta de Google del organizador (la persona que crea el calendario).

**a) Proyecto**
1. Entra a <https://console.cloud.google.com>.
2. Arriba: *Seleccionar proyecto → Nuevo proyecto* → nombre `Deberes del hogar` → **Crear**.

**b) Habilitar la API**
1. Menú ☰ → *APIs y servicios → Biblioteca*.
2. Busca **Google Calendar API** → **Habilitar**.

**c) Pantalla de consentimiento**
1. *APIs y servicios → Pantalla de consentimiento de OAuth*.
2. Tipo: **Externo** → **Crear**.
3. Nombre de la app: `Deberes del hogar`. Correo de asistencia y de contacto: el tuyo. **Guardar y continuar**.
4. *Usuarios de prueba* → **Agregar usuarios**: el correo de Google de **cada persona de la casa** (incluido el tuyo). Si falta uno, esa persona no podrá entrar.
5. Deja la app en modo **Prueba**. No hace falta publicarla ni verificarla.

**d) Credenciales**
1. *APIs y servicios → Credenciales → Crear credenciales → ID de cliente de OAuth*.
2. Tipo de aplicación: **Aplicación web**. Nombre: `Deberes web`.
3. **Orígenes de JavaScript autorizados → Agregar URI**, y añade exactamente estos dos:
   ```
   https://vyesid1706.github.io
   http://localhost:8000
   ```
   Solo el origen: `https://algo.github.io`, sin ruta y sin `/` al final.
4. **Crear** → copia el **ID de cliente** (termina en `.apps.googleusercontent.com`) y pásamelo. Lo dejo fijo dentro de la app para que nadie tenga que pegarlo.

> **Aviso de "app no verificada":** es normal. Toca *Configuración avanzada → Ir a Deberes del hogar (no seguro)*. Solo lo verán los usuarios de prueba.

---

## 2. Instalar en cada teléfono

1. Abre **https://vyesid1706.github.io/deberes-hogar/** en el celular.
2. Instálala como app:
   - **Android (Chrome):** menú ⋮ → *Instalar aplicación*.
   - **iPhone (Safari):** Compartir → *Añadir a pantalla de inicio*.
3. Pestaña **⚙️ Ajustes**. Si el Client ID no aparece ya rellenado, pégalo → **Guardar**.
4. Toca **🔑 Conectar con Google** y acepta los permisos con **la cuenta de Google de esa persona**.
5. La app busca sola el calendario de la familia. Si no lo encuentra, toca **🔎 Buscar el calendario de la familia**.

---

## 3. Compartir el calendario (solo el organizador, una vez)

En **👨‍👩‍👧 Familia**, agrega a cada persona con su correo y toca **👥 Compartir el calendario con la familia**. Eso les da permiso de **edición**: sin él pueden ver los eventos pero no marcar ni cambiar nada.

Cada persona recibe un correo de Google (*"X compartió un calendario contigo"*) y el calendario aparece solo en su Google Calendar.

---

## Uso diario

- **Semana:** ves el reparto y el avance (`3/8 deberes hechos`). Toca el círculo ✓ cuando esté hecho; toca el nombre para cambiar a quién le toca.
- **Deberes:** activa los que se reparten y pon día y hora. Se guarda solo (mira el estado arriba: *Guardando…* / *Conectado*).
- **Aviso de domingo:** en *Ajustes* puedes activar un recordatorio semanal (por defecto domingo 8:00 p. m.) que aparece en el calendario de toda la familia para elegir los deberes.
- **📅 Sincronizar:** crea/actualiza los eventos de las próximas semanas. Normalmente no hace falta: cada cambio se envía solo.
- **Días pasados:** nunca se crean eventos en fechas que ya pasaron; solo desde hoy en adelante.

---

## Problemas frecuentes

| Síntoma | Causa / solución |
|---|---|
| "El navegador bloqueó la ventana de Google" | Abre la app en Chrome/Safari (no dentro de otra app) e inténtalo de nuevo. |
| "La sesión de Google caducó" | Normal cada 1 hora: toca **Conectar con Google**. |
| "No encontré el calendario" | Falta compartirlo contigo, o el organizador aún no lo creó (**Ajustes → ➕ Crear**). |
| `403` o `access_denied` al conectar | Tu correo no está en *Usuarios de prueba* de la pantalla de consentimiento. |
| `redirect_uri_mismatch` / "origin mismatch" | El origen autorizado en Google no coincide con la dirección de la app. Debe ser solo `https://usuario.github.io`. |
| No veo el calendario en Google Calendar | En Google Calendar, *Otros calendarios → Añadir* → busca "Deberes del hogar". |
| Cambié algo y no se ve en otro teléfono | Toca **Sincronizar** o cierra y abre la app (se refresca sola al volver). |

## Límites conocidos

- Dos ediciones simultáneas de la configuración: gana la última. No rompe nada.
- Cuentas de Google Workspace (colegio/trabajo) pueden tener bloqueadas las apps externas; en ese caso usa una cuenta Gmail normal.
- El calendario pertenece a la cuenta que lo creó. Si esa cuenta se pierde, se pierde el calendario.
