---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/pstools-getting-set-up-windows.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Installing the AWS Tools for PowerShell on Windows
<a name="pstools-getting-set-up-windows"></a>

For information about the Tools for PowerShell that are pre-installed on AWS CloudShell, see [Installed on CloudShell](pstools-getting-set-up-cloudshell.md).

A Windows-based computer can run any of the AWS Tools for PowerShell package options:
+ [**`AWS.Tools`**](ps-installing-awstools.md) - The modularized version of AWS Tools for PowerShell. Each AWS service is supported by its own individual, small module, with shared support modules `AWS.Tools.Common` and `AWS.Tools.Installer`.
+ [**AWSPowerShell.NetCore**](ps-installing-awspowershellnetcore.md) - The single, large-module version of AWS Tools for PowerShell. All AWS services are supported by this single, large module.
**Note**
Be aware that the single module might be too large to use with [AWS Lambda](https://aws.amazon.com/lambda/) functions. Instead, use the modularized version shown above.
+ [**AWSPowerShell**](ps-installing-awswindowspowershell.md) - The legacy, Windows-specific, single, large-module version of AWS Tools for PowerShell. All AWS services are supported by this single, large module.

The package you choose depends on the release and edition of Windows that you are running.

**Note**
The AWS Tools for PowerShell are installed by default on all Windows-based Amazon Machine Images (AMIs). The option that is installed depends on the AMI. Many AMIs have the AWSPowerShell module, but some might have a different option. For example, Amazon EC2 AMIs for Windows Server 2025 use the modular `AWS.Tools` option.

Setting up the AWS Tools for PowerShell involves the following high-level tasks, described in detail in subsequent topics.

1. Install the AWS Tools for PowerShell package option that's appropriate for your environment.

1. Verify that script execution is enabled by running the `Get-ExecutionPolicy` cmdlet.

1. Import the AWS Tools for PowerShell module into your PowerShell session.

## Prerequisites
<a name="prerequisites"></a>

Newer versions of PowerShell, including PowerShell Core, are available as downloads from Microsoft at [Installing various versions of PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell) on Microsoft's Web site.

**Topics**
+ [Prerequisites](#prerequisites)
+ [Install `AWS.Tools` (recommended)](ps-installing-awstools.md)
+ [Install AWSPowerShell.NetCore](ps-installing-awspowershellnetcore.md)
+ [Install AWSPowerShell (legacy)](ps-installing-awswindowspowershell.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
