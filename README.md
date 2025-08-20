# Powershell-Cibersecurity
By LicFressa

Este repositorio contiene una colección de tres scripts en PowerShell desarrollados como ejercicios prácticos de auditoría básica en sistemas Windows. Los scripts permiten realizar análisis iniciales de archivos, usuarios locales y servicios activos, constituyendo una introducción al uso de PowerShell en tareas de ciberseguridad defensiva y administración de sistemas.

**Contenido del repositorio**

**Validar-Archivo.ps1**
Funcionalidad:
Valida la existencia y accesibilidad de un archivo en el sistema. En caso de ser accesible, muestra su tamaño en bytes; en caso contrario, devuelve un error controlado.
Resulta útil en la seguridad para comprobar la integridad y disponibilidad de archivos críticos en auditorías forenses o de cumplimiento.

**Auditoria_Usuarios.ps1**
Funcionalidad:
Recolecta la información de todos los usuarios locales en el sistema y clasifica aquellos que nunca han iniciado sesión y los que sí lo han hecho.
Exporta la información a dos archivos de texto (usuarios_sin_logon.txt y usuarios_con_logon.txt).
Muestra los resultados en consola para su revisión inmediata.
Permite detectar cuentas inactivas que podrían representar un riesgo de seguridad si permanecen habilitadas sin supervisión.


**Módulo AuditoriaBasica (carpeta dedicada con manifiesto, módulo y script principal):**
Archivos incluidos:
AuditoriaBasica.psd1 → Manifiesto del módulo con metadatos (versión, autoría, compatibilidad).
AuditoriaBasica.psm1 → Definición de funciones reutilizables para auditoría.
MainAuditoria.ps1 → Script principal que interactúa con el usuario.

Funciones principales:
Obtener-UsuariosInactivos: lista las cuentas locales habilitadas que nunca han iniciado sesión.
Obtener-ServiciosExternos: identifica servicios en ejecución que no pertenecen al núcleo de Windows.
Aporta gran utilidad en la ciberseguridad al facilitar la detección de cuentas innecesarias y servicios de terceros activos, aspectos claves en auditorías preventivas para reducir la superficie de ataque.

Genera archivos con la información organizada de manera visual:
CSV con usuarios inactivos.
HTML con los servicios externos activos.
