---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/accelerate-the-discovery-and-migration-of-microsoft-workloads-to-aws.html
---

# Accelerate the discovery and migration of Microsoft workloads to AWS
<a name="accelerate-the-discovery-and-migration-of-microsoft-workloads-to-aws"></a>

*Ali Alzand, Amazon Web Services*

## Summary
<a name="accelerate-the-discovery-and-migration-of-microsoft-workloads-to-aws-summary"></a>

This pattern shows you how to use the [Migration Validator Toolkit PowerShell module](https://github.com/aws-samples/migration-validator-toolkit-for-microsoft-workloads) to discover and migrate your Microsoft workloads to AWS. The module works by performing multiple checks and validations for common tasks associated with any Microsoft workload. For example, the module checks for instances that might have multiple disks attached to it or instances that use many IP addresses. For a full list of checks that the module can perform, see the [Checks](https://github.com/aws-samples/migration-validator-toolkit-for-microsoft-workloads#checks) section on the module's GitHub page.

The Migration Validator Toolkit PowerShell module can help your organization reduce the time and effort involved in discovering what applications and services are running on your Microsoft workloads. The module can also help you identify the configurations of your workloads so that you can find out if your configurations are supported on AWS. The module also provides recommendations for next steps and mitigation actions, so that you can avoid any misconfigurations before, during, or after your migration.

## Prerequisites and limitations
<a name="accelerate-the-discovery-and-migration-of-microsoft-workloads-to-aws-prereqs"></a>

**Prerequisites**
+ Local administrator account
+ PowerShell 4.0

**Limitations**
+ Works only on Microsoft Windows Server 2012 R2 or later

## Tools
<a name="accelerate-the-discovery-and-migration-of-microsoft-workloads-to-aws-tools"></a>

**Tools**
+ PowerShell 4.0

**Code repository**

The Migration Validator Toolkit PowerShell module for this pattern is available in the GitHub [migration-validator-toolkit-for-microsoft-workloads](https://github.com/aws-samples/migration-validator-toolkit-for-microsoft-workloads) repository.

## Epics
<a name="accelerate-the-discovery-and-migration-of-microsoft-workloads-to-aws-epics"></a>

### Run the Migration Validator Toolkit PowerShell module on a single target
<a name="run-the-migration-validator-toolkit-powershell-module-on-a-single-target"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download, extract, import, and invoke the module. | Choose one of the following methods to download and deploy the module:+ Run the PowerShell script<br />+ Download and extract the .zip file<br />+ Clone the GitHub repository<br />**Run the PowerShell script**<br />In PowerShell, run the following example code:<pre>#MigrationValidatorToolkit<br />$uri = 'https://github.com/aws-samples/migration-validator-toolkit-for-microsoft-workloads/archive/refs/heads/main.zip'<br />$destination = (Get-Location).Path<br />if ((Test-Path -Path "$destination\MigrationValidatorToolkit.zip" -PathType Leaf) -or (Test-Path -Path "$destination\MigrationValidatorToolkit")) {<br />    write-host "File $destination\MigrationValidatorToolkit.zip or folder $destination\MigrationValidatorToolkit found, exiting"<br />}else {<br />    Write-host "Enable TLS 1.2 for this PowerShell session only."<br />    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12<br />    $webClient = New-Object System.Net.WebClient<br />    Write-host "Downloading MigrationValidatorToolkit.zip"<br />    $webClient.DownloadFile($uri, "$destination\MigrationValidatorToolkit.zip")<br />    Write-host "MigrationValidatorToolkit.zip download successfully"<br />    Add-Type -Assembly "system.io.compression.filesystem"<br />    [System.IO.Compression.ZipFile]::ExtractToDirectory("$destination\MigrationValidatorToolkit.zip","$destination\MigrationValidatorToolkit")<br />    Write-host "Extracting MigrationValidatorToolkit.zip complete successfully"<br />    Import-Module "$destination\MigrationValidatorToolkit\migration-validator-toolkit-for-microsoft-workloads-main\MigrationValidatorToolkit.psm1"; Invoke-MigrationValidatorToolkit<br />}</pre><br />The code downloads the module from a .zip file. Then, the code extracts, imports, and invokes the module.<br />**Download and extract the .zip file**1. Download the [.zip file](https://github.com/aws-samples/migration-validator-toolkit-for-microsoft-workloads/archive/refs/heads/main.zip) (download).<br />2. Extract the .zip file.<br />3. Follow the steps in the *Invoke the module* *manually *story of this guide.<br />**Clone the GitHub repository**1. To clone the GitHub [migration-validator-toolkit-for-microsoft-workloads](https://github.com/aws-samples/migration-validator-toolkit-for-microsoft-workloads) repository, run the following Git command in a terminal window:<pre>git clone https://github.com/aws-samples/migration-validator-toolkit-for-microsoft-workloads.git</pre><br />2. Follow the steps in the *Invoke the module* *manually *story of this guide. | System Administrator |
| Invoke the module manually. | 1. Go to the directory where the downloaded module is stored.<br />2. To generate the output of your choice, run one of the following commands as an administrator in PowerShell:[Format-Table](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/format-table?view=powershell-7.3) format:<pre>Import-Module .\MigrationValidatorToolkit.psm1;Invoke-MigrationValidatorToolkit</pre><br />[Format-List](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/format-list?view=powershell-7.3) format:<pre>Import-Module .\MigrationValidatorToolkit.psm1;Invoke-MigrationValidatorToolkit -List</pre><br />[Out-GridView](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/out-gridview?view=powershell-7.3) format:<pre>Import-Module .\MigrationValidatorToolkit.psm1;Invoke-MigrationValidatorToolkit -GridView</pre><br />[ConvertTo-Csv](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertto-csv?view=powershell-7.3) format:<pre>Import-Module .\MigrationValidatorToolkit.psm1;Invoke-MigrationValidatorToolkit -csv</pre> | System Administrator |

### Run the Migration Validator Toolkit PowerShell module on multiple targets
<a name="run-the-migration-validator-toolkit-powershell-module-on-multiple-targets"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the .zip file or clone the GitHub repository. | Choose one of the following options:+ Download the [zip file.](https://github.com/aws-samples/migration-validator-toolkit-for-microsoft-workloads/archive/refs/heads/main.zip) (download).<br />+ To clone the GitHub [migration-validator-toolkit-for-microsoft-workloads](https://github.com/aws-samples/migration-validator-toolkit-for-microsoft-workloads) repository, run the following Git command in a terminal window:<pre>git clone https://github.com/aws-samples/migration-validator-toolkit-for-microsoft-workloads.git</pre> | System Administrator |
| Update the server.csv list. | If you downloaded the .zip file, follow these steps:1. Extract the .zip file.<br />2. Go to the `MigrationValidatorToolkit\Inputs\` directory.<br />3. Update `serverlist.csv` with the host name of your target computers. | System Administrator |
| Invoke the module. | You can use any computer within the domain that uses a domain user that has administrator access to target computers.1. Download the source code as a .zip file and extract the file.<br />2. As an administrator in PowerShell, run the following command:<pre>Import-Module .\MigrationValidatorToolkit.psm1;Invoke-DomainComputers</pre><br />The output .csv file is saved in `MigrationValidatorToolkit\Outputs\folder` with the prefix name `DomainComputers_MigrationAutomations_YYYY-MM-DDTHH-MM-SS`. | System Administrator |

## Troubleshooting
<a name="accelerate-the-discovery-and-migration-of-microsoft-workloads-to-aws-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| `MigrationValidatorToolkit` writes information about executions, commands, and errors to log files on the running host. | You can view log files manually in the following location:1. Go to the `MigrationValidatorToolkit\logs\` directory.<br />2. Locate the log file. The format of the log file name is: `ComputerName_MigrationValidatorToolkit_YYYY-MM-SSTHH-MM-SS.log` |

## Related resources
<a name="accelerate-the-discovery-and-migration-of-microsoft-workloads-to-aws-resources"></a>
+ [Options, tools, and best practices for migrating Microsoft workloads to AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-microsoft-workloads-aws/introduction.html) (AWS Prescriptive Guidance)
+ [Microsoft migration patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migration-migration-patterns-by-workload-microsoft-pattern-list.html) (AWS Prescriptive Guidance)
+ [Free Cloud Migration Services on AWS](https://aws.amazon.com/free/migration/) (AWS documentation)
+ [Predefined post-launch actions](https://docs.aws.amazon.com/mgn/latest/ug/predefined-post-launch-actions.html) (Application marketing documentation)

## Additional information
<a name="accelerate-the-discovery-and-migration-of-microsoft-workloads-to-aws-additional"></a>

**Frequently asked questions**

*Where can I run the Migration Validator Toolkit PowerShell module?*

You can run the module on Microsoft Windows Server 2012 R2 or later.

*When do I run this module?*

We recommend that you run the module during the [assess phase](https://aws.amazon.com/cloud-migration/how-to-migrate/) of the migration journey.

*Does the module modify my existing servers?*

No. All actions in this module are read-only.

*How long does it take to run the module?*

It typically takes 1–5 minutes to run the module, but it depends on the resource allocation of your server.

*What permissions does the module need to run?*

You must run the module from a local administrator account.

*Can I run the module on physical servers?*

Yes, as long as the operating system is Microsoft Windows Server 2012 R2 or later.

*How do I run the module at scale for multiple servers?*

To run the module on multiple domain-joined computers at scale, follow the steps in the *Run the Migration Validator Toolkit PowerShell module on multiple targets *epic of this guide. For non domain-joined computers, use a remote invocation or run the module locally by following the steps in the *Run the Migration Validator Toolkit PowerShell module on a single target* epic of this guide.
