---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/using-powershell-files-with-session-scripts.html
---

# Using Windows PowerShell Files
<a name="using-powershell-files-with-session-scripts"></a>

To use Windows PowerShell files, specify the full path to the PowerShell file in the **filename** parameter:

```
"filename":
"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
```

Then specify your session script in the **arguments** parameter:

```
"arguments": "-File \"C:\\path\\to\\session\\script.ps1\"",
```

Finally, verify that the PowerShell Execution Policy allows your PowerShell file to run.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
