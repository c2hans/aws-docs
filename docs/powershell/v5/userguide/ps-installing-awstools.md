---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/ps-installing-awstools.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Install `AWS.Tools` on Windows (recommended)
<a name="ps-installing-awstools"></a>

For general information about installing the AWS Tools for PowerShell on Windows, including prerequisites and other options, see the [parent topic](pstools-getting-set-up-windows.md).

For information about the Tools for PowerShell that are pre-installed on AWS CloudShell, see [Installed on CloudShell](pstools-getting-set-up-cloudshell.md).

You can install the modularized version of the AWS Tools for PowerShell on computers that are running Windows with Windows PowerShell 5.1, or PowerShell Core 6.0 or later. For information about how to install PowerShell Core, see [Installing various versions of PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell) on Microsoft's Web site.

You can install `AWS.Tools` in one of three ways:
+ Using the cmdlets in the `AWS.Tools.Installer` module. This module simplifies the installation and update of other `AWS.Tools` modules. `AWS.Tools.Installer` requires `PowerShellGet`, and automatically downloads and installs an updated version of it. `AWS.Tools.Installer` automatically keeps your module versions in sync. When you install or update to a newer version of one module, the cmdlets in `AWS.Tools.Installer` automatically update all of your other `AWS.Tools` modules to the same version.

  This method is described in the procedure that follows.
+ Downloading the modules from `[AWS.Tools.zip](https://sdk-for-net.amazonwebservices.com/ps/v5/latest/AWS.Tools.zip)` and extracting them in one of the module folders. You can discover your module folders by displaying the value of the `PSModulePath` environment variable.
**Warning**
After downloading the ZIP file and before extracting the contents, you might need to unblock it. This is typically done by opening the properties of the file, viewing the **General** tab, and selecting the **Unblock** checkbox if one exists.
If the ZIP file needs to be unblocked but you don't do so, you might receive errors similar to the following: "Import-Module : Could not load file or assembly".
+ Installing each service module from the PowerShell Gallery using the `Install-Module` cmdlet.

**To install `AWS.Tools` on Windows using the `AWS.Tools.Installer` module**

1. Start a PowerShell session.
**Note**
We recommend that you *don't* run PowerShell as an administrator with elevated permissions except when required by the task at hand. This is because of the potential security risk and is inconsistent with the principle of least privilege.

1. To install the modularized `AWS.Tools` package, run the following command.

   ```
   PS > Install-Module -Name AWS.Tools.Installer

   Untrusted repository
   You are installing the modules from an untrusted repository. If you trust this repository, change its InstallationPolicy value by running the Set-PSRepository cmdlet. Are you sure
    you want to install the modules from 'PSGallery'?
   [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
   ```

   If you are notified that the repository is "untrusted", it asks you if you want to install anyway. Enter **y** to allow PowerShell to install the module. To avoid the prompt and install the module without trusting the repository, you can run the command with the `-Force` parameter.

   ```
   PS > Install-Module -Name AWS.Tools.Installer -Force
   ```

1. You can now install the module for each AWS service that you want to use by using the `Install-AWSToolsModule` cmdlet. For example, the following command installs the Amazon EC2 and Amazon S3 modules. This command also installs any dependent modules that are required for the specified module to work. For example, when you install your first `AWS.Tools` service module, it also installs `AWS.Tools.Common`. This is a shared module required by all AWS service modules. It also removes older versions of the modules, and updates other modules to the same newer version.

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
The `Install-AWSToolsModule` cmdlet downloads all requested modules from the `PSRepository` named `PSGallery` ([https://www.powershellgallery.com/](https://www.powershellgallery.com/)) and considers it a trusted source. Use the command `Get-PSRepository -Name PSGallery` for more information about this `PSRepository`.

   By default, the previous command installs modules into the `%USERPROFILE%\Documents\WindowsPowerShell\Modules` folder. To install the AWS Tools for PowerShell for all users of a computer, you must run the following command in a PowerShell session that you started as an administrator. For example, the following command installs the IAM module to the `%ProgramFiles%\WindowsPowerShell\Modules` folder that is accessible by all users.

   ```
   PS > Install-AWSToolsModule AWS.Tools.IdentityManagement -Scope AllUsers
   ```

   To install other modules, run similar commands with the appropriate module names, as found in the [PowerShell Gallery](https://www.powershellgallery.com/packages?q=aws).

## Enable Script Execution
<a name="enable-script-execution-aws-tools"></a>

To load the AWS Tools for PowerShell modules, you must enable PowerShell script execution. To enable script execution, run the `Set-ExecutionPolicy` cmdlet to set a policy of `RemoteSigned`. For more information, see [About Execution Policies](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies) on the Microsoft Technet website.

**Note**
This is a requirement only for computers that are running Windows. The `ExecutionPolicy` security restriction is not present on other operating systems.

 **To enable script execution**

1. Administrator rights are required to set the execution policy. If you are not logged in as a user with administrator rights, open a PowerShell session as Administrator. Choose **Start**, and then choose **All Programs**. Choose **Accessories**, and then choose **Windows PowerShell**. Right-click **Windows PowerShell**, and on the context menu, choose **Run as administrator**.

1. At the command prompt, enter the following.

   ```
   PS > Set-ExecutionPolicy RemoteSigned
   ```

**Note**
On a 64-bit system, you must do this separately for the 32-bit version of PowerShell, **Windows PowerShell (x86)**.

If you don't have the execution policy set correctly, PowerShell shows the following error whenever you try to run a script, such as your profile.

```
File C:\Users\{{username}}\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1 cannot be loaded because the execution
 of scripts is disabled on this system. Please see "get-help about_signing" for more details.
At line:1 char:2
+ . <<<<  'C:\Users\{{username}}\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1'
    + CategoryInfo          : NotSpecified: (:) [], PSSecurityException
    + FullyQualifiedErrorId : RuntimeException
```

The Tools for Windows PowerShell installer automatically updates the [PSModulePath](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_psmodulepath) to include the location of the directory that contains the `AWSPowerShell` module.

Because the `PSModulePath` includes the location of the AWS module's directory, the `Get-Module -ListAvailable` cmdlet shows the module.

```
PS > Get-Module -ListAvailable

ModuleType Name                      ExportedCommands
---------- ----                      ----------------
Manifest   AppLocker                 {}
Manifest   BitsTransfer              {}
Manifest   PSDiagnostics             {}
Manifest   TroubleshootingPack       {}
Manifest   AWSPowerShell             {Update-EBApplicationVersion, Set-DPStatus, Remove-IAMGroupPol...
```

## Versioning
<a name="pstools-versioning-aws-tools"></a>

AWS releases new versions of the AWS Tools for PowerShell periodically to support new AWS services and features. To determine the version of the Tools that you have installed, run the [Get-AWSPowerShellVersion](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-AWSPowerShellVersion.html) cmdlet.

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

You can also add the `-ListServiceVersionInfo` parameter to a [Get-AWSPowerShellVersion](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-AWSPowerShellVersion.html) command to see a list of the AWS services that are supported in the current version of the tools. If you use the modularized `AWS.Tools.*` option, only the modules that you currently have imported are displayed.

For example:

```
PS > Get-AWSPowerShellVersion -ListServiceVersionInfo
...

Service                            Noun Prefix Module Name                       SDK
                                                                                 Assembly
                                                                                 Version
-------                            ----------- -----------                       -----------
AWS IAM Access Analyzer            IAMAA       AWS.Tools.AccessAnalyzer          3.7.400.33
AWS Account                        ACCT        AWS.Tools.Account                 3.7.400.33
AWS Certificate Manager Private... PCA         AWS.Tools.ACMPCA                  3.7.400.34
AWS Amplify                        AMP         AWS.Tools.Amplify                 3.7.401.28
Amplify Backend                    AMPB        AWS.Tools.AmplifyBackend          3.7.400.33
...
```

To determine the version of PowerShell that you are running, enter `$PSVersionTable` to view the contents of the $PSVersionTable [automatic variable](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_automatic_variables?view=powershell-6).

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

## Updating the AWS Tools for PowerShell on Windows
<a name="pstools-updating-awstools"></a>

Periodically, as updated versions of the AWS Tools for PowerShell are released, you should update the version that you are running locally.

### Update the modularized `AWS.Tools` modules
<a name="update-the-tools-for-powershell-awstools"></a>

To update your `AWS.Tools` modules to the latest version, run the following command:

```
PS > Update-AWSToolsModule -CleanUp
```

This command updates all of the currently installed `AWS.Tools` modules and, after a successful update, removes the earlier versions.

**Note**
The `Update-AWSToolsModule` cmdlet downloads all modules from the `PSRepository` named `PSGallery` ([https://www.powershellgallery.com/](https://www.powershellgallery.com/)) and considers it a trusted source. Use the `Get-PSRepository -Name PSGallery` command for more information about this `PSRepository`.
