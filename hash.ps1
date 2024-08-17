$System32Path = "C:\Windows\System32"
$ExeFiles = Get-ChildItem -Path $System32Path -Filter *.exe

foreach ($File in $ExeFiles) {
    $Hash = Get-FileHash -Path $File.FullName -Algorithm SHA256
    $Hash | Out-File -FilePath "C:\OriginalHashes\$($File.Name).hash"
}