# Get all credentials from the Credential Manager
$credentials = cmdkey /list

# Create a file to store the output
$outputFile = "C:\CmdkeyCredentials.txt"
"Cmdkey Credentials:" | Out-File -FilePath $outputFile -Encoding utf8

# Loop through the credentials and extract the relevant information
foreach ($credential in $credentials) {
  $targetName = $credential.Split(':')[0].Trim()
  $username = $credential.Split(':')[1].Trim()
  $password = cmdkey /v:$targetName

  # Output the credential information to the file
  "Credential found:" | Out-File -FilePath $outputFile -Encoding utf8 -Append
  "  Target Name: $targetName" | Out-File -FilePath $outputFile -Encoding utf8 -Append
  "  Username: $username" | Out-File -FilePath $outputFile -Encoding utf8 -Append
  "  Password: $password" | Out-File -FilePath $outputFile -Encoding utf8 -Append
  "" | Out-File -FilePath $outputFile -Encoding utf8 -Append
}