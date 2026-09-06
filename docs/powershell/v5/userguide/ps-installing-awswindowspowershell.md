---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/ps-installing-awswindowspowershell.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Install AWSPowerShell on Windows PowerShell (legacy)
<a name="ps-installing-awswindowspowershell"></a>

For general information about installing the AWS Tools for PowerShell on Windows, including prerequisites and other options, see the [parent topic](pstools-getting-set-up-windows.md).

For information about the Tools for PowerShell that are pre-installed on AWS CloudShell, see [Installed on CloudShell](pstools-getting-set-up-cloudshell.md).

**Note**
AWSPowerShell is not the recommended method for installing the AWS Tools for PowerShell. For the recommended method, see [Install `AWS.Tools` (recommended)](ps-installing-awstools.md) instead.

You can install the AWS Tools for Windows PowerShell in one of two ways:
+ Downloading the module from [AWSPowerShell.zip](https://sdk-for-net.amazonwebservices.com/ps/v5/latest/AWSPowerShell.zip) and extracting it in one of the module directories. You can discover your module directories by displaying the value of the `PSModulePath` environment variable.
**Warning**
After downloading the ZIP file and before extracting the contents, you might need to unblock it. This is typically done by opening the properties of the file, viewing the **General** tab, and selecting the **Unblock** checkbox if one exists.
If the ZIP file needs to be unblocked but you don't do so, you might receive errors similar to the following: "Import-Module : Could not load file or assembly".
+ Installing from the PowerShell Gallery using the `Install-Module` cmdlet as described in the following procedure.

**To install AWSPowerShell from the PowerShell Gallery using the Install-Module cmdlet**

You can install the AWSPowerShell from the PowerShell Gallery if you are running PowerShell 5.0 or later, or have installed [PowerShellGet](https://www.powershellgallery.com/packages/PowerShellGet) on PowerShell 3 or later. You can install and update AWSPowerShell from Microsoft's [PowerShell Gallery](https://www.powershellgallery.com/packages/AWSPowerShell) by running the following command.

```
 PS > Install-Module -Name AWSPowerShell
```

To load the AWSPowerShell module into a PowerShell session automatically, add the previous `import-module` cmdlet to your PowerShell profile. For more information about editing your PowerShell profile, see [About Profiles](https://docs.microsoft.com/powershell/module/microsoft.powershell.core/about/about_profiles?view=powershell-6) in the PowerShell documentation.

## Enable Script Execution
<a name="enable-script-execution-windows-ps"></a>

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
<a name="pstools-versioning-windows-ps"></a>

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
<a name="pstools-updating-windows-ps"></a>

Periodically, as updated versions of the AWS Tools for PowerShell are released, you should update the version that you are running locally.

### Update the Tools for Windows PowerShell
<a name="update-the-tools-for-windows-powershell"></a>

Run the `Get-AWSPowerShellVersion` cmdlet to determine the version that you are running, and compare that with the version of Tools for Windows PowerShell that is available on the [PowerShell Gallery](https://www.powershellgallery.com/packages/AWSPowerShell) website. We suggest you check every two to three weeks. Support for new commands and AWS services is available only after you update to a version with that support.
+ If you installed by using the `Install-Module` cmdlet, run the following commands.

  ```
  PS > Uninstall-Module -Name AWSPowerShell -AllVersions
  PS > Install-Module -Name AWSPowerShell
  ```
+ If you installed by using a downloaded ZIP file:

  1. Download the most recent version from the [Tools for PowerShell](https://aws.amazon.com/powershell/) web site. Compare the package version number in the downloaded file name with the version number you get when you run the `Get-AWSPowerShellVersion` cmdlet.

  1. If the download version is a higher number than the version you have installed, close all Tools for Windows PowerShell consoles.

  1. Install the newer version of the Tools for Windows PowerShell.

After installation, run `Import-Module AWSPowerShell` to load the updated cmdlets into your PowerShell session. Or run the custom AWS Tools for PowerShell console from your **Start** menu.
