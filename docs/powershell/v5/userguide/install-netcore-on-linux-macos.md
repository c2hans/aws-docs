---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/install-netcore-on-linux-macos.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Install AWSPowerShell.NetCore on Linux or macOS
<a name="install-netcore-on-linux-macos"></a>

For general information about installing the AWS Tools for PowerShell on Linux or macOS, including prerequisites and other options, see the [parent topic](pstools-getting-set-up-linux-mac.md).

For information about the Tools for PowerShell that are pre-installed on AWS CloudShell, see [Installed on CloudShell](pstools-getting-set-up-cloudshell.md).

**Note**
AWSPowerShell.NetCore is not the recommended method for installing the AWS Tools for PowerShell. For the recommended method, see [Install `AWS.Tools` (recommended)](install-aws.tools-on-linux-macos.md) instead.

To upgrade to a newer release of AWSPowerShell.NetCore, follow the instructions in [Updating the AWS Tools for PowerShell on Linux or macOS](#pstools-updating-linux-netcore). Uninstall earlier versions of AWSPowerShell.NetCore first.

You can install AWSPowerShell.NetCore in one of two ways:
+ Downloading the module from `[AWSPowerShell.NetCore.zip](https://sdk-for-net.amazonwebservices.com/ps/v5/latest/AWSPowerShell.NetCore.zip)` and extracting it in one of the module directories. You can discover your module directories by printing the value of the `$Env:PSModulePath` variable.
+ Installing from the PowerShell Gallery using the `Install-Module` cmdlet as described in the following procedure.

**To install AWSPowerShell.NetCore on Linux or macOS using the Install-Module cmdlet**

Start a PowerShell Core session by running the following command.

```
$ pwsh
```

**Note**
We recommend that you *don't* start PowerShell by running `sudo pwsh` to run PowerShell with elevated, administrator rights. This is because of the potential security risk and is inconsistent with the principle of least privilege.

To install the AWSPowerShell.NetCore single-module package from the PowerShell Gallery, run the following command.

```
PS > Install-Module -Name AWSPowerShell.NetCore

Untrusted repository
You are installing the modules from an untrusted repository. If you trust this repository, change its InstallationPolicy value by running the Set-PSRepository cmdlet. Are you sure
 you want to install the modules from 'PSGallery'?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

If you are notified that the repository is "untrusted", you are asked if you want to install anyway. Enter **y** to allow PowerShell to install the module. To avoid the prompt without trusting the repository, you can run the following command.

```
PS > Install-Module -Name AWSPowerShell.NetCore -Force
```

You don't have to run this command as root, unless you want to install the AWS Tools for PowerShell for all users of a computer. To do this, run the following command in a PowerShell session that you have started with `sudo pwsh`.

```
PS > Install-Module -Scope AllUsers -Name AWSPowerShell.NetCore -Force
```

## Script Execution
<a name="enable-script-execution-netcore"></a>

The `Set-ExecutionPolicy` command isn't available on non-Windows systems. You can run `Get-ExecutionPolicy`, which shows that the default execution policy setting in PowerShell Core running on non-Windows systems is `Unrestricted`. For more information, see [About Execution Policies](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-5.1) on the Microsoft Technet website.

 Because the `PSModulePath` includes the location of the AWS module's directory, the `Get-Module -ListAvailable` cmdlet shows the module that you installed.

**AWSPowerShell.NetCore**

```
PS > Get-Module -ListAvailable

Directory: /Users/{{username}}/.local/share/powershell/Modules

ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Binary     3.3.563.1  AWSPowerShell.NetCore
```

## Configure a PowerShell Console to Use the AWS Tools for PowerShell Core (AWSPowerShell.NetCore Only)
<a name="pstools-config-ps-window-netcore"></a>

PowerShell Core typically loads modules automatically whenever you run a cmdlet in the module. But this doesn't work for AWSPowerShell.NetCore because of its large size. To start running AWSPowerShell.NetCore cmdlets, you must first run the `Import-Module AWSPowerShell.NetCore` command. This isn't required for cmdlets in `AWS.Tools` modules.

## Initialize Your PowerShell Session
<a name="linux-config-init-netcore"></a>

When you start PowerShell on a Linux-based or macOS-based system after you have installed the AWS Tools for PowerShell, you must run [Initialize-AWSDefaultConfiguration](https://docs.aws.amazon.com/powershell/v5/reference/items/Initialize-AWSDefaultConfiguration.html) to specify which AWS access key to use. For more information about `Initialize-AWSDefaultConfiguration`, see [Using AWS Credentials](specifying-your-aws-credentials.md).

**Note**
In earlier (before 3.3.96.0) releases of the AWS Tools for PowerShell, this cmdlet was named `Initialize-AWSDefaults`.

## Versioning
<a name="pstools-versioning-netcore"></a>

AWS releases new versions of the AWS Tools for PowerShell periodically to support new AWS services and features. To determine the version of the AWS Tools for PowerShell that you have installed, run the [Get-AWSPowerShellVersion](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-AWSPowerShellVersion.html) cmdlet.

For example:

```
PS > Get-AWSPowerShellVersion

AWS Tools for PowerShell
Version 5.0.3
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

Amazon Web Services SDK for .NET
Core Runtime Version 4.0.0.13
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

Release notes: https://github.com/aws/aws-tools-for-powershell/blob/main/changelogs/CHANGELOG.ALL.md

This software includes third party software subject to the following copyrights:
- Logging from log4net, Apache License
[http://logging.apache.org/log4net/license.html]
```

To see a list of the supported AWS services in the current version of the tools, add the `-ListServiceVersionInfo` parameter to a [Get-AWSPowerShellVersion](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-AWSPowerShellVersion.html) cmdlet.

To determine the version of PowerShell that you are running, enter `$PSVersionTable` to view the contents of the `$PSVersionTable` [automatic variable](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_automatic_variables?view=powershell-6).

For example:

```
PS > $PSVersionTable
Name                           Value
----                           -----
PSVersion                      6.2.2
PSEdition                      Core
GitCommitId                    6.2.2
OS                             Darwin 18.7.0 Darwin Kernel Version 18.7.0: Tue Aug 20 16:57:14 PDT 2019; root:xnu-4903.271.2~2/RELEASE_X86_64
Platform                       Unix
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0…}
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1
WSManStackVersion              3.0
```

## Updating the AWS Tools for PowerShell on Linux or macOS
<a name="pstools-updating-linux-netcore"></a>

Periodically, as updated versions of the AWS Tools for PowerShell are released, you should update the version that you are running locally.

### Update the Tools for PowerShell Core
<a name="update-netcore-all-systems"></a>

Run the `Get-AWSPowerShellVersion` cmdlet to determine the version that you are running, and compare that with the version of Tools for Windows PowerShell that is available on the [PowerShell Gallery](https://www.powershellgallery.com/packages/AWSPowerShell) website. We suggest you check every two to three weeks. Support for new commands and AWS services is available only after you update to a version with that support.

Before you install a newer release of AWSPowerShell.NetCore, uninstall the existing module. Close any open PowerShell sessions before you uninstall the existing package. Run the following command to uninstall the package.

```
PS > Uninstall-Module -Name AWSPowerShell.NetCore -AllVersions
```

After the package is uninstalled, install the updated module by running the following command.

```
PS > Install-Module -Name AWSPowerShell.NetCore
```

After installation, run the command `Import-Module AWSPowerShell.NetCore` to load the updated cmdlets into your PowerShell session.

## Related Information
<a name="pstools-seealso-setup-netcore"></a>
+  [Configuring and using the AWS Tools for PowerShell](pstools-getting-started.md)
+  [Calling AWS services in the AWS Tools for PowerShell](pstools-using.md)
