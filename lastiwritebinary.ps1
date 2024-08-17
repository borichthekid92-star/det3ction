$System32Path = "C:\Windows\System32"
$ExeFiles = Get-ChildItem -Path $System32Path -Filter *.exe

$LastWriteTime = @{}

foreach ($File in $ExeFiles) {
    $LastWriteTime[$File.Name] = $File.LastWriteTime
}

# Save the last write times to a file
$LastWriteTime | ConvertTo-Json | Out-File -FilePath "C:\LastWriteTimes.json"

# Later, when you want to detect changes
$CurrentLastWriteTime = @{}
foreach ($File in $ExeFiles) {
    $CurrentLastWriteTime[$File.Name] = $File.LastWriteTime
}

$PreviousLastWriteTime = Get-Content -Path "C:\LastWriteTimes.json" | ConvertFrom-Json

$ChangedFiles = @()

foreach ($File in $ExeFiles) {
    if ($CurrentLastWriteTime[$File.Name] -ne $PreviousLastWriteTime[$File.Name]) {
        $ChangedFiles += $File.Name
    }
}

if ($ChangedFiles.Count -gt 0) {
    Write-Output "The following files have been modified:"
    $ChangedFiles | ForEach-Object { Write-Output $_ }
    Exit 1
} else {
    Write-Output "No changes detected"
    Exit 0
}
