---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-updates-managed-powershell.html
---

# Enable updates for license included applications on image builder with Powershell
<a name="enable-updates-managed-powershell"></a>

To enable updates for license included applications on image builder with Powershell, follow these steps.
+ Run the following command with PowerShell as an administrator:

  `Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Office\ClickToRun\Configuration" -Name UpdatesEnabled -Value True `
