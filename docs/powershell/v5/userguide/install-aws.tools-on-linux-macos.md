---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/install-aws.tools-on-linux-macos.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Install `AWS.Tools` on Linux or macOS (recommended)
<a name="install-aws.tools-on-linux-macos"></a>

For general information about installing the AWS Tools for PowerShell on Linux or macOS, including prerequisites and other options, see the [parent topic](pstools-getting-set-up-linux-mac.md).

For information about the Tools for PowerShell that are pre-installed on AWS CloudShell, see [Installed on CloudShell](pstools-getting-set-up-cloudshell.md).

You can install the modularized version of AWS Tools for PowerShell on computers that are running PowerShell Core 6.0 or later. For information about how to install PowerShell Core, see [Installing various versions of PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell) on the Microsoft PowerShell website.

You can install `AWS.Tools` in one of three ways:
+ Using the cmdlets in the `AWS.Tools.Installer` module. This module simplifies the installation and update of other `AWS.Tools` modules. `AWS.Tools.Installer` requires `PowerShellGet`, and automatically downloads and installs an updated version of it. `AWS.Tools.Installer` automatically keeps your module versions in sync. When you install or update to a newer version of one module, the cmdlets in `AWS.Tools.Installer` automatically update all of your other `AWS.Tools` modules to the same version.

  This method is described in the procedure that follows.
+ Downloading the modules from `[AWS.Tools.zip](https://sdk-for-net.amazonwebservices.com/ps/v5/latest/AWS.Tools.zip)` and extracting them in one of the module directories. You can discover your module directories by printing the value of the `$Env:PSModulePath` variable.
+ Installing each service module from the PowerShell Gallery using the `Install-Module` cmdlet.

**To install `AWS.Tools` on Linux or macOS using the `AWS.Tools.Installer` module**

1. Start a PowerShell Core session by running the following command.

   ```
   $ pwsh
   ```
**Note**
We recommend that you *don't* run PowerShell as an administrator with elevated permissions except when required by the task at hand. This is because of the potential security risk and is inconsistent with the principle of least privilege.

1. To install the modularized `AWS.Tools` package using the `AWS.Tools.Installer` module, run the following command.

   ```
   PS > Install-Module -Name AWS.Tools.Installer

   Untrusted repository
   You are installing the modules from an untrusted repository. If you trust this repository, change its InstallationPolicy value by running the Set-PSRepository cmdlet. Are you sure
    you want to install the modules from 'PSGallery'?
   [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
   ```

   If you are notified that the repository is "untrusted", you are asked if you want to install anyway. Enter **y** to allow PowerShell to install the module. To avoid the prompt and install the module without trusting the repository, you can run the following command.

   ```
   PS > Install-Module -Name AWS.Tools.Installer -Force
   ```

1. You can now install the module for each service that you want to use. For example, the following command installs the Amazon EC2 and Amazon S3 modules. This command also installs any dependent modules that are required for the specified module to work. For example, when you install your first `AWS.Tools` service module, it also installs `AWS.Tools.Common`. This is a shared module required by all AWS service modules. It also removes older versions of the modules, and updates other modules to the same newer version.

   ```
   PS > Install-AWSToolsModule AWS.Tools.EC2,AWS.Tools.S3 -CleanUp
   Confirm
   Are you sure you want to perform this action?
     Performing the operation "Install-AWSToolsModule" on target "AWS Tools version 4.0.0.0".
     [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):

     Installing module AWS.Tools.Common version 4.0.0.0
     Installing module AWS.Tools.EC2 version 4.0.0.0
     Installing module AWS.Tools.Glacier version 4.0.0.0
     Installing module AWS.Tools.S3 version 4.0.0.0

     Uninstalling AWS.Tools version 3.3.618.0
     Uninstalling module AWS.Tools.Glacier
     Uninstalling module AWS.Tools.S3
     Uninstalling module AWS.Tools.SimpleNotificationService
     Uninstalling module AWS.Tools.SQS
     Uninstalling module AWS.Tools.Common
   ```
**Note**
The `Install-AWSToolsModule` cmdlet downloads all requested modules from the `PSRepository` named `PSGallery` ([https://www.powershellgallery.com/](https://www.powershellgallery.com/)) and considers the repository as a trusted source. Use the command `Get-PSRepository -Name PSGallery` for more information about this `PSRepository`.

   The previous command installs modules into the default directories on your system. The actual directories depend on your operating system distribution and version and on the version of PowerShell you installed. For example, if you installed PowerShell 7 on a RHEL-like system, the default modules are most likely located in `/opt/microsoft/powershell/7/Modules` (or `$PSHOME/Modules`) and user modules are most likely located in `~/.local/share/powershell/Modules`. For more information, see [Install PowerShell on Linux](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-linux) on the Microsoft PowerShell website. To see where modules are installed, run the following command:

   ```
   PS > Get-Module -ListAvailable
   ```

   To install other modules, run similar commands with the appropriate module names, as found in the [PowerShell Gallery](https://www.powershellgallery.com/packages?q=aws).

## Script Execution
<a name="enable-script-execution-aws-tools"></a>

The `Set-ExecutionPolicy` command isn't available on non-Windows systems. You can run `Get-ExecutionPolicy`, which shows that the default execution policy setting in PowerShell Core running on non-Windows systems is `Unrestricted`. For more information, see [About Execution Policies](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-5.1) on the Microsoft Technet website.

 Because the `PSModulePath` includes the location of the AWS module's directory, the `Get-Module -ListAvailable` cmdlet shows the module that you installed.

**`AWS.Tools`**

```
PS > Get-Module -ListAvailable

    Directory: /Users/{{username}}/.local/share/powershell/Modules

ModuleType Version    Name                                PSEdition ExportedCommands
---------- -------    ----                                --------- ----------------
Binary     3.3.563.1  AWS.Tools.Common                    Desk      {Clear-AWSHistory, Set-AWSHistoryConfiguration, Initialize-AWSDefaultConfiguration, Clear-AWSDefaultConfigurat…
```

## Initialize Your PowerShell Session
<a name="linux-config-init-aws-tools"></a>

When you start PowerShell on a Linux-based or macOS-based system after you have installed the AWS Tools for PowerShell, you must run [Initialize-AWSDefaultConfiguration](https://docs.aws.amazon.com/powershell/v5/reference/items/Initialize-AWSDefaultConfiguration.html) to specify which AWS access key to use. For more information about `Initialize-AWSDefaultConfiguration`, see [Using AWS Credentials](specifying-your-aws-credentials.md).

**Note**
In earlier (before 3.3.96.0) releases of the AWS Tools for PowerShell, this cmdlet was named `Initialize-AWSDefaults`.

## Versioning
<a name="pstools-versioning-aws-tools"></a>

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
<a name="pstools-updating-linux-aws-tools"></a>

Periodically, as updated versions of the AWS Tools for PowerShell are released, you should update the version that you are running locally.

### Update the modularized `AWS.Tools` modules
<a name="update-aws.tools-all-systems"></a>

To update your `AWS.Tools` modules to the latest version, run the following command:

```
PS > Update-AWSToolsModule -CleanUp
```

This command updates all of the currently installed `AWS.Tools` modules and, after a successful update, removes the earlier versions.

**Note**
The `Update-AWSToolsModule` cmdlet downloads all modules from the `PSRepository` named `PSGallery` ([https://www.powershellgallery.com/](https://www.powershellgallery.com/)) and considers it a trusted source. Use the `Get-PSRepository -Name PSGallery` command for more information about this `PSRepository`.

## Related Information
<a name="pstools-seealso-setup-aws-tools"></a>
+  [Configuring and using the AWS Tools for PowerShell](pstools-getting-started.md)
+  [Calling AWS services in the AWS Tools for PowerShell](pstools-using.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
