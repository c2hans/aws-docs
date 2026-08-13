---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/pstools-getting-set-up-linux-mac.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Installing AWS Tools for PowerShell on Linux or macOS
<a name="pstools-getting-set-up-linux-mac"></a>

For information about the Tools for PowerShell that are pre-installed on AWS CloudShell, see [Installed on CloudShell](pstools-getting-set-up-cloudshell.md).

To install AWS Tools for PowerShell on a Linux or macOS computer, you can choose from two package options:
+ [**`AWS.Tools`**](install-aws.tools-on-linux-macos.md) – The modularized version of AWS Tools for PowerShell. Each AWS service is supported by its own individual, small module, with shared support modules `AWS.Tools.Common`.
+ [**AWSPowerShell.NetCore**](install-netcore-on-linux-macos.md) – The single, large-module version of AWS Tools for PowerShell. All AWS services are supported by this single, large module.
**Note**
Be aware that the single module might be too large to use with [AWS Lambda](https://aws.amazon.com/lambda/) functions. Instead, use the modularized version shown above.

Setting either of these up on a computer running Linux or macOS involves the following tasks, described in detail in subsequent topics:

1. Install PowerShell Core 6.0 or later on a supported system.

1. After installing PowerShell Core, start PowerShell by running `pwsh` in your system shell.

1. Install either `AWS.Tools` or AWSPowerShell.NetCore.

1. Run the appropriate `Import-Module` cmdlet to import the module into your PowerShell session.

1. Run the [Initialize-AWSDefaultConfiguration](https://docs.aws.amazon.com/powershell/v5/reference/items/Initialize-AWSDefaultConfiguration.html) cmdlet to provide your AWS credentials.

## Prerequisites
<a name="prerequisites"></a>

To run the AWS Tools for PowerShell Core, your computer must be running PowerShell Core 6.0 or later.
+ For a list of supported Linux platform releases and for information about how to install the latest version of PowerShell on a Linux-based computer, see [Installing PowerShell on Linux](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-linux) on Microsoft's website. Some Linux-based operating systems, such as Arch, Kali, and Raspbian, are not officially supported, but have varying levels of community support.
+ For information about supported macOS versions and about how to install the latest version of PowerShell on macOS, see [Installing PowerShell on macOS](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-macos) on Microsoft's website.

**Topics**
+ [Prerequisites](#prerequisites)
+ [Install `AWS.Tools` (recommended)](install-aws.tools-on-linux-macos.md)
+ [Install AWSPowerShell.NetCore](install-netcore-on-linux-macos.md)
