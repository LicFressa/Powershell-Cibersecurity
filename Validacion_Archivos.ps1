function Validar-Archivo {
    param ([string]$Ruta)

    try {
        if (Test-Path $Ruta) {
            $contenido = Get-content $Ruta -ErrorAction Stop
            $peso = (Get-Item $Ruta | Measure-Object -Property Length -Sum).Sum
            return "Archivo accesible: $Ruta `nPeso del Archivo: $peso bytes" 
            
        } else {
            throw "El archivo no existe" 
        }
    }
    catch {
        return "Error: $_" 
    }
    Finally {
        Write-Host "Evaluación terminada para: $Ruta `n" -ForegroundColor Cyan
    }
}

