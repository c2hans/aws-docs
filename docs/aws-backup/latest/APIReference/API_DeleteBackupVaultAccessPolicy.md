---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteBackupVaultAccessPolicy.html
---

# DeleteBackupVaultAccessPolicy
<a name="API_DeleteBackupVaultAccessPolicy"></a>

Deletes the policy document that manages permissions on a backup vault.

## Request Syntax
<a name="API_DeleteBackupVaultAccessPolicy_RequestSyntax"></a>

```
DELETE /backup-vaults/{{backupVaultName}}/access-policy HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteBackupVaultAccessPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [backupVaultName](#API_DeleteBackupVaultAccessPolicy_RequestSyntax) **   <a name="Backup-DeleteBackupVaultAccessPolicy-request-uri-BackupVaultName"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`
Required: Yes

## Request Body
<a name="API_DeleteBackupVaultAccessPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteBackupVaultAccessPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteBackupVaultAccessPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteBackupVaultAccessPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
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
<a name="API_DeleteBackupVaultAccessPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/DeleteBackupVaultAccessPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/DeleteBackupVaultAccessPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DeleteBackupVaultAccessPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/DeleteBackupVaultAccessPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DeleteBackupVaultAccessPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/DeleteBackupVaultAccessPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/DeleteBackupVaultAccessPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/DeleteBackupVaultAccessPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/DeleteBackupVaultAccessPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DeleteBackupVaultAccessPolicy)
