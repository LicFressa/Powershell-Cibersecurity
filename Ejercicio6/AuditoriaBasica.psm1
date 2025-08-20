$moduloPath = "C:\Program Files\WindowsPowerShell\Modules\AuditoriaBasica" 
New-Item -Path $moduloPath -ItemType Directory 
Set-Location $moduloPath 


function Obtener-UsuariosInactivos {
    <#
    .SYNOPSYS
    Obtiene usuarios locales
    .DESCRIPTION
    Esta funcion busca cuentas loscales habilitadas que no tienen fecha de  último inicio de sesión
    .EXAMPLE
    Obtener-UsuariosInactivos
    .NOTES
    Puede ayudar a detectar cuentas innecesarias o riesgosas en auditorias básicas.
    #>
    Get-LocalUser | Where-Object{ $_.Enabled -eq $true -and -not $_.LastLogon }

}

function Obtener-ServiciosExternos {
    <#
    .SYNOPSIS
    Obtiene servicios en ejecución que no pertenecen explícitamente a Windows.
    .DESCRIPTION
    Filtra servicios activos cuyo nombre descriptivo no contiene el término "Windows".
    .EXAMPLE
    Obtener-ServiciosExternos
    .NOTES
    Úti para detectar software de terceros corriendo en segundo plano.

    #>
    Get-Service | Where-Object { $_.StaTUS -eq "Running" -and $_.DisplayName -notmatch "Windows"}
}

New-ModuleManifest -Path '.\AuditoriaBasica.psd1'`
    -RootModule 'AuditoriaBasica.psm1'`
    -ModuleVersion '1.0.0'`
    -Author 'Equipo de Ciberseguridad'`
    -Description 'Módulo para auditoría básica de usuarios y servicios'`
    -PowerShellVersion '5.1'
