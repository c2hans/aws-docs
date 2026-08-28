---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-updates-managed-powershell.html
---

# Enable updates for license included applications on image builder with Powershell
<a name="enable-updates-managed-powershell"></a>

To enable updates for license included applications on image builder with Powershell, follow these steps.
+ Run the following command with PowerShell as an administrator:

  `Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Office\ClickToRun\Configuration" -Name UpdatesEnabled -Value True `

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
