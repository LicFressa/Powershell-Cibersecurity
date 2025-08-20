$usuarios = Get-LocalUser
$sinlogon = @()
$conlogon = @()

foreach ($u in $usuarios) {
    if (-not $u.LastLogon){
        $sinlogon += "$($u.Name): Estado = $($u.Enabled), Último acceso: NUNCA"
    } else {
        $conlogon += "$($u.Name): Estado = $($u.Enabled), Último acceso: $($u.LastLogon)"
    }
    
}
#Guardamos en archivos separados
$sinlogon | Out-File -FilePath "$env:C\Users\TTOCI\OneDrive\Escritorio\usuarios_sin_logon.txt"
$conlogon | Out-File -FilePath "$env:C\Users\TTOCI\OneDrive\Escritorio\usuarios_con_logon.txt"
#Mostrar en pantalla
Write-Output "`n Usuarios que NUNCA  han iniciado sesión:"
$sinlogon | ForEach-Object {Write-Output $_}
Write-Output "`n Usuarios que SÍ han iniciado sesión:"
$conlogon | ForEach-Object {Write-Output $_}