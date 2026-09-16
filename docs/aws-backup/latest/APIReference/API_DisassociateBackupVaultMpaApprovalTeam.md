---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DisassociateBackupVaultMpaApprovalTeam.html
---

# DisassociateBackupVaultMpaApprovalTeam
<a name="API_DisassociateBackupVaultMpaApprovalTeam"></a>

Removes the association between an MPA approval team and a backup vault, disabling the MPA approval workflow for restore operations.

## Request Syntax
<a name="API_DisassociateBackupVaultMpaApprovalTeam_RequestSyntax"></a>

```
POST /backup-vaults/{{backupVaultName}}/mpaApprovalTeam?delete HTTP/1.1
Content-type: application/json

{
   "RequesterComment": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DisassociateBackupVaultMpaApprovalTeam_RequestParameters"></a>

The request uses the following URI parameters.

 ** [backupVaultName](#API_DisassociateBackupVaultMpaApprovalTeam_RequestSyntax) **   <a name="Backup-DisassociateBackupVaultMpaApprovalTeam-request-uri-BackupVaultName"></a>
The name of the backup vault from which to disassociate the MPA approval team.
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`
Required: Yes

## Request Body
<a name="API_DisassociateBackupVaultMpaApprovalTeam_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RequesterComment](#API_DisassociateBackupVaultMpaApprovalTeam_RequestSyntax) **   <a name="Backup-DisassociateBackupVaultMpaApprovalTeam-request-RequesterComment"></a>
An optional comment explaining the reason for disassociating the MPA approval team from the backup vault.
Type: String
Required: No

## Response Syntax
<a name="API_DisassociateBackupVaultMpaApprovalTeam_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DisassociateBackupVaultMpaApprovalTeam_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DisassociateBackupVaultMpaApprovalTeam_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** MissingParameterValueException **
Indicates that a required parameter is missing.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_DisassociateBackupVaultMpaApprovalTeam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/DisassociateBackupVaultMpaApprovalTeam)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/DisassociateBackupVaultMpaApprovalTeam)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DisassociateBackupVaultMpaApprovalTeam)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/DisassociateBackupVaultMpaApprovalTeam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DisassociateBackupVaultMpaApprovalTeam)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/DisassociateBackupVaultMpaApprovalTeam)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/DisassociateBackupVaultMpaApprovalTeam)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/DisassociateBackupVaultMpaApprovalTeam)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/DisassociateBackupVaultMpaApprovalTeam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DisassociateBackupVaultMpaApprovalTeam)
