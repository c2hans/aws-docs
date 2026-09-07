---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/export-a-report-of-aws-iam-identity-center-identities-and-their-assignments-by-using-powershell.html
---

# Export a report of AWS IAM Identity Center identities and their assignments by using PowerShell
<a name="export-a-report-of-aws-iam-identity-center-identities-and-their-assignments-by-using-powershell"></a>

*Jorge Pava, Frank Allotta, Manideep Reddy Gillela, and Chad Miles, Amazon Web Services*

## Summary
<a name="export-a-report-of-aws-iam-identity-center-identities-and-their-assignments-by-using-powershell-summary"></a>

When you use AWS IAM Identity Center (successor to AWS Single Sign-On) to centrally manage single sign-on (SSO) access to all of your Amazon Web Services (AWS) accounts and cloud applications, reporting and auditing those assignments through the AWS Management Console can be tedious and time consuming. This is especially true if you’re reporting on permissions for a user or group across dozens or hundreds of AWS accounts.

For many, the ideal tool to view this information would be in a spreadsheet application, such as Microsoft Excel. This can help you filter, search, and visualize the data for your entire organization, managed by AWS Organizations.

This pattern describes how to use AWS Tools for PowerShell to generate a report of SSO identity configurations in IAM Identity Center. The report is formatted as a CSV file, and it includes the identity name (principal), identity type (user or group), accounts the identity can access, and permission sets. After generating this report, you can open it in your preferred application to search, filter, and audit the data as needed. The following image shows sample data in a spreadsheet application.

![PowerShell script results viewed in spreadsheet application.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/46c7dc7f-c726-4754-b590-2f09d657b167/images/bbc21d8b-fc5d-4b5d-b159-81197a89823e.png)

|
|
| Important: Because this report contains sensitive information, we highly recommend you store it securely and share it only on a need-to-know basis. |
| --- |

## Prerequisites and limitations
<a name="export-a-report-of-aws-iam-identity-center-identities-and-their-assignments-by-using-powershell-prereqs"></a>

**Prerequisites**
+ IAM Identity Center and AWS Organizations, configured and enabled.
+ PowerShell, installed and configured. For more information, see [Installing PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) (Microsoft documentation).
+ AWS Tools for PowerShell, installed and configured. For performance reasons, we highly recommend that you install the modularized version of AWS Tools for PowerShell, called `AWS.Tools`. Each AWS service is supported by its own individual, small module. In the PowerShell shell, enter the following commands to install the modules needed for this pattern: `AWS.Tools.Installer`, `Organizations`, `SSOAdmin`, and `IdentityStore`.

  ```
  Install-Module AWS.Tools.Installer
  Install-AWSToolsModule -Name Organizations, SSOAdmin, IdentityStore
  ```

  For more information, see [Install AWS.Tools on Windows](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up-windows.html#ps-installing-awstools) or [Install AWS.Tools on Linux or macOS](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up-linux-mac.html#install-aws.tools-on-linux-macos) (AWS Tools for PowerShell documentation). If you receive an error when installing the modules, see the [Troubleshooting](#export-a-report-of-aws-iam-identity-center-identities-and-their-assignments-by-using-powershell-troubleshooting) section of this pattern.
+ AWS Command Line Interface (AWS CLI) or the AWS SDK must be previously configured with working credentials by doing one of the following:
  + Use the AWS CLI `aws configure` For more information, see [Quick configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config) (AWS CLI documentation).
  + Configure AWS CLI or AWS Cloud Development Kit (AWS CDK) to get temporary access through an AWS Identity and Access Management (IAM) role. For more information, see [Getting IAM role credentials for CLI access](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html) (IAM Identity Center documentation).
+ A named profile for the AWS CLI that has saved credentials for an IAM principal that:
  + Has access to the AWS Organizations management account or the delegated administrator account for IAM Identity Center
  + Has the `AWSSSOReadOnly` and `AWSSSODirectoryReadOnly` AWS managed policies applied to it

  For more information, see [Using named profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-using-profiles) (AWS CLI documentation) and [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) (IAM documentation).

**Limitations**
+ The target AWS accounts must be managed as an organization in AWS Organizations.

**Product versions**
+ For all operating systems, it is recommended that you use [PowerShell version 7.0](https://github.com/powershell/powershell) or later.

## Architecture
<a name="export-a-report-of-aws-iam-identity-center-identities-and-their-assignments-by-using-powershell-architecture"></a>

**Target architecture**

![Script using AWS CLI named profile to create a report of SSO identities in IAM Identity Center.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/46c7dc7f-c726-4754-b590-2f09d657b167/images/ae5189aa-8197-4a05-88df-7c0294a679a1.png)

1. The user runs the script in a PowerShell command line.

1. The script assumes the named profile for AWS CLI. This grants access to IAM Identity Center.

1. The script retrieves the SSO identity configurations from IAM Identity Center.

1. The script generates a CSV file in the same directory on the local workstation where the script is saved.

## Tools
<a name="export-a-report-of-aws-iam-identity-center-identities-and-their-assignments-by-using-powershell-tools"></a>

**AWS services**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) helps you centrally manage single sign-on (SSO) access to all of your AWS accounts and cloud applications.
+ [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-welcome.html) are a set of PowerShell modules that help you script operations on your AWS resources from the PowerShell command line.

**Other tools**
+ [PowerShell](https://learn.microsoft.com/en-us/powershell/) is a Microsoft automation and configuration management program that runs on Windows, Linux, and macOS.

## Epics
<a name="export-a-report-of-aws-iam-identity-center-identities-and-their-assignments-by-using-powershell-epics"></a>

### Generate the report
<a name="generate-the-report"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the script. | 1. Copy the PowerShell script in the [Additional information](#export-a-report-of-aws-iam-identity-center-identities-and-their-assignments-by-using-powershell-additional) section of this pattern.<br />2. In the `Param` section, for your AWS environment, define the values for the following variables:`OutputFile` – The file name of the report.`ProfileName` – The AWS CLI named profile that you want to use to generate the report.`Region` – The AWS Region in which IAM Identity Center is deployed. For a complete list of Regions and their codes, see [Regional endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints).<br />3. Save the script with the file name `SSO-Report.ps1`. | Cloud administrator |
| Run the script. | It is recommended that you run your custom script in the PowerShell shell with the following command.<pre>.\SSO-Report.ps1</pre><br />Alternatively, you can run the script from another shell by entering the following command.<pre>pwsh .\SSO-Report.ps1</pre><br />The script generates a CSV file in the same directory as the script file. | Cloud administrator |
| Analyze report data. | The output CSV file has the headers **AccountName**, **PermissionSet**, **Principal**, and **Type**. Open this file in your preferred spreadsheet application. You can create a data table to filter and sort the output. | Cloud administrator |

## Troubleshooting
<a name="export-a-report-of-aws-iam-identity-center-identities-and-their-assignments-by-using-powershell-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| `The term ‘Get-<parameter>’ is not recognized as the name of a cmdlet, function, script file, or operable program.` error | AWS Tools for PowerShell or its modules are not installed. In the PowerShell shell, enter the following commands to install AWS Tools for PowerShell and the modules needed for this pattern: `AWS.Tools.Installer`, `Organizations`, `SSOAdmin`, and `IdentityStore`.<pre>Install-Module AWS.Tools.Installer<br />Install-AWSToolsModule -Name Organizations, SSOAdmin, IdentityStore</pre> |
| `No credentials specified or obtained from persisted/shell defaults` error | In *Prepare the script* in the [Epics](#export-a-report-of-aws-iam-identity-center-identities-and-their-assignments-by-using-powershell-epics) section, confirm that you have correctly entered the `ProfileName` and `Region` variables. Make sure that the settings and credentials in the named profile have sufficient permissions to administer IAM Identity Center. |
| `Authenticode Issuer …` error when installing the AWS.Tools modules | Add the `-SkipPublisherCheck` parameter to the end of the `Install-AWSToolsModule` command. |
| `Get-ORGAccountList : Assembly AWSSDK.SSO could not be found or loaded.` error | This error can occur when named AWS CLI profiles are specified, AWS CLI is configured to authenticate users with IAM Identity Center, and AWS CLI is configured to automatically retrieve refreshed authentication tokens. To resolve this error, do the following:1. Enter the following command to confirm that the `SSO` and `SSOOIDC` modules are installed.<pre>Install-AWSToolsModule SSO, SSOOIDC</pre><br />2. Insert the following lines into the script below the `param()` block.<pre>Import-Module AWS.Tools.SSO </pre><pre>Import-Module AWS.Tools.SSOOIDC</pre> |

## Related resources
<a name="export-a-report-of-aws-iam-identity-center-identities-and-their-assignments-by-using-powershell-resources"></a>
+ [Where are configuration settings stored?](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-where) (AWS CLI documentation)
+ [Configuring the AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) (AWS CLI documentation)
+ [Using named profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-using-profiles) (AWS CLI documentation)

## Additional information
<a name="export-a-report-of-aws-iam-identity-center-identities-and-their-assignments-by-using-powershell-additional"></a>

In the following script, determine whether you need to update the values for the following parameters:
+ If you’re using a named profile in AWS CLI to access the account in which IAM Identity Center is configured, update the `$ProfileName` value.
+ If IAM Identity Center is deployed in a different AWS Region than the default Region for your AWS CLI or AWS SDK configuration, update the `$Region` value to use the Region where IAM Identity Center is deployed.
+ If neither of these situations apply, then no script update is required.

```
param (
    # The name of the output CSV file
    [String] $OutputFile  = "SSO-Assignments.csv",
    # The AWS CLI named profile
    [String] $ProfileName = "",
    # The AWS Region in which IAM Identity Center is configured
    [String] $Region      = ""
)
$Start = Get-Date; $OrgParams = @{}
If ($Region){ $OrgParams.Region = $Region}
if ($ProfileName){$OrgParams.ProfileName = $ProfileName}
$SSOParams   = $OrgParams.Clone(); $IdsParams = $OrgParams.Clone()
$AccountList = Get-ORGAccountList @OrgParams | Select-Object Id, Name
$SSOinstance = Get-SSOADMNInstanceList @OrgParams
$SSOParams['InstanceArn']       = $SSOinstance.InstanceArn
$IdsParams['IdentityStoreId']   = $SSOinstance.IdentityStoreId
$PSsets       = @{}; $Principals   = @{}
$Assignments  = @(); $AccountCount = 1; Write-Host ""
foreach ($Account in $AccountList) {
    $Duration = New-Timespan -Start $Start -End (Get-Date) | ForEach-Object {[Timespan]::New($_.Days, $_.Hours, $_.Minutes, $_.Seconds)}
    Write-Host "`r$Duration - Account $AccountCount of $($AccountList.Count) (Assignments:$($Assignments.Count))        " -NoNewline
    $AccountCount++
    foreach ($PS in Get-SSOADMNPermissionSetsProvisionedToAccountList -AccountId $Account.Id @SSOParams) {
        if (-not $PSsets[$PS]) {$PSsets[$PS] = (Get-SSOADMNPermissionSet @SSOParams -PermissionSetArn $PS).Name;$APICalls++}
        $AssignmentsResponse = Get-SSOADMNAccountAssignmentList @SSOParams -PermissionSetArn $PS -AccountId $Account.Id
        if ($AssignmentsResponse.NextToken) {$AccountAssignments = $AssignmentsResponse.AccountAssignments}
        else {$AccountAssignments = $AssignmentsResponse}
        While ($AssignmentsResponse.NextToken) {
            $AssignmentsResponse = Get-SSOADMNAccountAssignmentList @SSOParams -PermissionSetArn $PS -AccountId $Account.Id -NextToken $AssignmentsResponse.NextToken
            $AccountAssignments += $AssignmentsResponse.AccountAssignments}
        foreach ($Assignment in $AccountAssignments) {
            if (-not $Principals[$Assignment.PrincipalId]) {
                $AssignmentType = $Assignment.PrincipalType.Value
                $Expression     = "Get-IDS"+$AssignmentType+" @IdsParams -"+$AssignmentType+"Id "+$Assignment.PrincipalId
                $Principal      = Invoke-Expression $Expression
                if ($Assignment.PrincipalType.Value -eq "GROUP") { $Principals[$Assignment.PrincipalId] = $Principal.DisplayName }
                else { $Principals[$Assignment.PrincipalId] = $Principal.UserName }
            }
            $Assignments += [PSCustomObject]@{
                AccountName     = $Account.Name
                PermissionSet   = $PSsets[$PS]
                Principal       = $Principals[$Assignment.PrincipalId]
                Type            = $Assignment.PrincipalType.Value}
        }
    }
}
$Duration = New-Timespan -Start $Start -End (Get-Date) | ForEach-Object {[Timespan]::New($_.Days, $_.Hours, $_.Minutes, $_.Seconds)}
Write-Host "`r$($AccountList.Count) accounts done in $Duration. Outputting result to $OutputFile"
$Assignments | Sort-Object Account | Export-CSV -Path $OutputFile -Force
```
