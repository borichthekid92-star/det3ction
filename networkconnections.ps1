# Get all network connections
$connections = Get-NetTCPConnection -State Established

# Create a file to store the output
$outputFile = "$env:USERPROFILE\Desktop\NetworkConnections.txt"
"Network Connections:" | Out-File -FilePath $outputFile -Encoding utf8

# Loop through the connections and extract the relevant information
foreach ($connection in $connections) {
  $localAddress = $connection.LocalAddress
  $localPort = $connection.LocalPort
  $remoteAddress = $connection.RemoteAddress
  $remotePort = $connection.RemotePort
  $processId = $connection.OwningProcess
  $processName = (Get-Process -Id $processId).ProcessName

  # Output the connection information to the file
  "Connection found:" | Out-File -FilePath $outputFile -Encoding utf8 -Append
  "  Local Address: $localAddress" | Out-File -FilePath $outputFile -Encoding utf8 -Append
  "  Local Port: $localPort" | Out-File -FilePath $outputFile -Encoding utf8 -Append
  "  Remote Address: $remoteAddress" | Out-File -FilePath $outputFile -Encoding utf8 -Append
  "  Remote Port: $remotePort" | Out-File -FilePath $outputFile -Encoding utf8 -Append
  "  Process ID: $processId" | Out-File -FilePath $outputFile -Encoding utf8 -Append
  "  Process Name: $processName" | Out-File -FilePath $outputFile -Encoding utf8 -Append
  "" | Out-File -FilePath $outputFile -Encoding utf8 -Append

}
