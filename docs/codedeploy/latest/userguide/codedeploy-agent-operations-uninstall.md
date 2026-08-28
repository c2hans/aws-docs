---
source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-uninstall.html
---

# Uninstall the CodeDeploy agent
<a name="codedeploy-agent-operations-uninstall"></a>

You can remove the CodeDeploy agent from instances when it is no longer needed or when you want to perform a fresh installation.

## Uninstall the CodeDeploy agent from Amazon Linux or RHEL
<a name="codedeploy-agent-operations-uninstall-linux"></a>

To uninstall the CodeDeploy agent, sign in to the instance and run the following command:

```
sudo yum erase codedeploy-agent
```

## Uninstall the CodeDeploy agent from Ubuntu Server
<a name="codedeploy-agent-operations-uninstall-ubuntu"></a>

To uninstall the CodeDeploy agent, sign in to the instance and run the following command:

```
sudo dpkg --purge codedeploy-agent
```

## Uninstall the CodeDeploy agent from Windows Server
<a name="codedeploy-agent-operations-uninstall-windows"></a>

To uninstall the CodeDeploy agent, sign in to the instance and run the following three commands, one at a time:

```
wmic
product where name="CodeDeploy Host Agent" call uninstall /nointeractive
exit
```

**Note**
On Windows Server 2025 and later, `wmic` is deprecated. Use the following PowerShell command instead:

```
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*' |
  Where-Object DisplayName -eq 'CodeDeploy Host Agent' |
  ForEach-Object { Start-Process msiexec.exe -ArgumentList "/x $($_.PSChildName) /quiet" -Wait }
```

You can also sign in to the instance, and in **Control Panel**, open **Programs and Features**, choose **CodeDeploy Host Agent**, and then choose **Uninstall**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
