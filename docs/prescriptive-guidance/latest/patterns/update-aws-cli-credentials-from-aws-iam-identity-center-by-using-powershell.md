---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/update-aws-cli-credentials-from-aws-iam-identity-center-by-using-powershell.html
---

# Update AWS CLI credentials from AWS IAM Identity Center by using PowerShell
<a name="update-aws-cli-credentials-from-aws-iam-identity-center-by-using-powershell"></a>

*Chad Miles and Andy Bowen, Amazon Web Services*

## Summary
<a name="update-aws-cli-credentials-from-aws-iam-identity-center-by-using-powershell-summary"></a>

If you want to use AWS IAM Identity Center (successor to AWS Single Sign-On) credentials with AWS Command Line Interface (AWS CLI), AWS SDKs, or AWS Cloud Development Kit (AWS CDK), you typically have to copy and paste the credentials from the IAM Identity Center console into the command line interface. This process can take a considerable amount of time and has to be repeated for each account that requires access.

One common solution is to use the AWS CLI `aws sso configure` command. This command adds an IAM Identity Center enabled profile to your AWS CLI or AWS SDK. However, the disadvantage of this solution is that you must run the command `aws sso login` for each AWS CLI profile or account that you have configured this way.

As an alternative solution, this pattern describes how to use AWS CLI [named profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-using-profiles) and AWS Tools for PowerShell to store and refresh credentials for multiple accounts from a single IAM Identity Center instance simultaneously. The script also stores IAM Identity Center session data in memory for refreshing credentials without logging into IAM Identity Center again.

## Prerequisites and limitations
<a name="update-aws-cli-credentials-from-aws-iam-identity-center-by-using-powershell-prereqs"></a>

**Prerequisites**
+ PowerShell, installed and configured. For more information, see [Installing PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.3) (Microsoft documentation).
+ AWS Tools for PowerShell, installed and configured. For performance reasons, we highly recommend that you install the modularized version of AWS Tools for PowerShell, called `AWS.Tools`. Each AWS service is supported by its own individual, small module. In the PowerShell prompt, enter the following commands to install the modules needed for this pattern: `AWS.Tools.Installer`, `SSO`, and `SSOIDC`.

  ```
  Install-Module AWS.Tools.Installer
  Install-AWSToolsModule SSO, SSOOIDC
  ```

  For more information, see [Install AWS.Tools on Windows](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up-windows.html#ps-installing-awstools) or [Install AWS.Tools on Linux or macOS](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up-linux-mac.html#install-aws.tools-on-linux-macos).
+ AWS CLI or the AWS SDK must be previously configured with working credentials by doing one of the following:
  + Use the AWS CLI `aws configure` command. For more information, see [Quick configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config) (AWS CLI documentation).
  + Configure AWS CLI or AWS CDK to get temporary access through an IAM role. For more information, see [Getting IAM role credentials for CLI access](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html) (IAM Identity Center documentation).

**Limitations**
+ This script can’t be used in a pipeline or fully automated solution. When you deploy this script, you must manually authorize access from IAM Identity Center. The script then continues automatically.

**Product versions**
+ For all operating systems, it is recommended that you use [PowerShell version 7.0](https://github.com/powershell/powershell) or later.

## Architecture
<a name="update-aws-cli-credentials-from-aws-iam-identity-center-by-using-powershell-architecture"></a>

You can use the script in this pattern to simultaneously refresh multiple IAM Identity Center credentials, and you can create a credential file for use with AWS CLI, AWS SDKs, or AWS CDK.

![Using a PowerShell script to update credentials in AWS CLI, AWS CDK, or AWS SKDs.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/6d54a6bb-01ac-4736-9b78-40921fcc9056/images/01e0fcb6-3b48-422c-8868-07a7de83b3e3.png)

## Tools
<a name="update-aws-cli-credentials-from-aws-iam-identity-center-by-using-powershell-tools"></a>

**AWS services**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) helps you centrally manage single sign-on (SSO) access to all of your AWS accounts and cloud applications.
+ [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-welcome.html) are a set of PowerShell modules that help you script operations on your AWS resources from the PowerShell command line.

**Other tools**
+ [PowerShell](https://learn.microsoft.com/en-us/powershell/) is a Microsoft automation and configuration management program that runs on Windows, Linux, and macOS.

## Best practices
<a name="update-aws-cli-credentials-from-aws-iam-identity-center-by-using-powershell-best-practices"></a>

Keep one copy of this script for each IAM Identity Center instance. Using one script for multiple instances is not supported.

## Epics
<a name="update-aws-cli-credentials-from-aws-iam-identity-center-by-using-powershell-epics"></a>

### Run the SSO script
<a name="run-the-sso-script"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Customize the SSO script. | 1. Copy the SSO script in the [Additional information](#update-aws-cli-credentials-from-aws-iam-identity-center-by-using-powershell-additional) section.<br />2. In the `Param` section, for your AWS environment, define the values for the following variables:`DefaultRoleName` – The IAM role or permission set to use by default.`Region` – The AWS Region in which IAM Identity Center is deployed. For a complete list of Regions and their codes, see [Regional endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints).`StartUrl` – The URL used to access your IAM Identity Center login page. Use the same format as the example value in the script.`EnvironmentName` – A short name to reference this copy of the script, to be used when you’re running multiple script copies in the same session.<br />3. Under line 10, which reads `# Add your Account Information`, edit the following values in the hash tables to reflect your environment:`Profile` – The AWS CLI profile name in which to store the temporary credentials.`AccountId` – The ID of the AWS account for which you are retrieving credentials.`RoleName` – The name of the IAM Identity Center role or permission set you want to use. You can leave this as `$DefaultRoleName` if you want to use the same role you defined in the `Param` section.<br />Each line in the hash table must end with a comma except the last one. | Cloud administrator |
| Run the SSO script. | It is recommended that you run your custom script in the PowerShell shell with the following command.<pre>./Set-AwsCliSsoCredentials.ps1</pre><br />Alternatively, you can run the script from another shell by entering the following command.<pre>pwsh Set-AwsCliSsoCredentials.ps1</pre> | Cloud administrator |

## Troubleshooting
<a name="update-aws-cli-credentials-from-aws-iam-identity-center-by-using-powershell-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| `No Access` error | The IAM role that you are using doesn’t have permissions to access the role or permission set that you defined in a `RoleName` parameter. Update the permissions for the role you are using, or define a different role or permission set in the script. |

## Related resources
<a name="update-aws-cli-credentials-from-aws-iam-identity-center-by-using-powershell-resources"></a>
+ [Where are configuration settings stored?](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-where) (AWS CLI documentation)
+ [Configuring the AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) (AWS CLI documentation)
+ [Using named profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-using-profiles) (AWS CLI documentation)

## Additional information
<a name="update-aws-cli-credentials-from-aws-iam-identity-center-by-using-powershell-additional"></a>

**SSO script**

In the following script, replace placeholders in angle brackets (<>) with your own information and remove the angle brackets.

```
Set-AwsCliSsoCredentials.ps1
Param(
    $DefaultRoleName = '<AWSAdministratorAccess>',
    $Region          = '<us-west-2>',
    $StartUrl        = "<https://d-12345abcde.awsapps.com/start/>",
    $EnvironmentName = "<CompanyName>"
)
Try {$SsoAwsAccounts = (Get-Variable -name "$($EnvironmentName)SsoAwsAccounts" -Scope Global -ErrorAction 'SilentlyContinue').Value.Clone()}
Catch {$SsoAwsAccounts = $False}
if (-not $SsoAwsAccounts) { $SsoAwsAccounts = @(
# Add your account information in the list of hash tables below, expand as necessary, and do not forget the commas
    @{Profile = "<Account1>"      ; AccountId = "<012345678901 >"; RoleName = $DefaultRoleName },
    @{Profile = "<Account2>"      ; AccountId = "<123456789012>"; RoleName = "<AWSReadOnlyAccess>" }
)}
$ErrorActionPreference = "Stop"
if (-not (Test-Path ~\.aws))      { New-Item ~\.aws -type Directory }
if (-not (Test-Path ~\.aws\credentials)) { New-Item ~\.aws\credentials -type File }
$CredentialFile = Resolve-Path ~\.aws\credentials
$PsuedoCreds    = @{AccessKey = 'AKAEXAMPLE123ACCESS';SecretKey='PsuedoS3cret4cceSSKey123PsuedoS3cretKey'} # Pseudo Creds, do not edit.
Try {$SSOTokenExpire = (Get-Variable -Scope Global -Name "$($EnvironmentName)SSOTokenExpire" -ErrorAction 'SilentlyContinue').Value} Catch {$SSOTokenExpire = $False}
Try {$SSOToken       = (Get-Variable -Scope Global -Name "$($EnvironmentName)SSOToken" -ErrorAction 'SilentlyContinue').Value }      Catch {$SSOToken       = $False}
if ( $SSOTokenExpire -lt (Get-Date) ) {
    $SSOToken = $Null
    $Client   = Register-SSOOIDCClient -ClientName cli-sso-client -ClientType public -Region $Region @PsuedoCreds
    $Device   = $Client | Start-SSOOIDCDeviceAuthorization -StartUrl $StartUrl -Region $Region @PsuedoCreds
    Write-Host "A Browser window should open. Please login there and click ALLOW." -NoNewline
    Start-Process $Device.VerificationUriComplete
    While (-Not $SSOToken){
        Try {$SSOToken = $Client | New-SSOOIDCToken -DeviceCode $Device.DeviceCode -GrantType "urn:ietf:params:oauth:grant-type:device_code" -Region $Region @PsuedoCreds}
        Catch {If ($_.Exception.Message -notlike "*AuthorizationPendingException*"){Write-Error $_.Exception} ; Start-Sleep 1}
    }
    $SSOTokenExpire = (Get-Date).AddSeconds($SSOToken.ExpiresIn)
    Set-Variable -Name "$($EnvironmentName)SSOToken" -Value $SSOToken -Scope Global
    Set-Variable -Name "$($EnvironmentName)SSOTokenExpire" -Value $SSOTokenExpire -Scope Global
}
$CredsTime     = $SSOTokenExpire - (Get-Date)
$CredsTimeText = ('{0:D2}:{1:D2}:{2:D2} left on SSO Token' -f $CredsTime.Hours, $CredsTime.Minutes, $CredsTime.Seconds).TrimStart("0 :")
for ($i = 0; $i -lt $SsoAwsAccounts.Count; $i++) {
    if (([DateTimeOffset]::FromUnixTimeSeconds($SsoAwsAccounts[$i].CredsExpiration / 1000)).DateTime -lt (Get-Date).ToUniversalTime()) {
        Write-host "`r                                                                     `rRegistering Profile $($SsoAwsAccounts[$i].Profile)" -NoNewline
        $TempCreds = $SSOToken | Get-SSORoleCredential -AccountId $SsoAwsAccounts[$i].AccountId -RoleName $SsoAwsAccounts[$i].RoleName -Region $Region @PsuedoCreds
        [PSCustomObject]@{AccessKey = $TempCreds.AccessKeyId; SecretKey = $TempCreds.SecretAccessKey; SessionToken = $TempCreds.SessionToken
        } | Set-AWSCredential -StoreAs $SsoAwsAccounts[$i].Profile -ProfileLocation $CredentialFile
        $SsoAwsAccounts[$i].CredsExpiration = $TempCreds.Expiration
    }
}
Set-Variable -name "$($EnvironmentName)SsoAwsAccounts" -Value $SsoAwsAccounts.Clone() -Scope Global
Write-Host "`r$($SsoAwsAccounts.Profile) Profiles registered, $CredsTimeText"
```
