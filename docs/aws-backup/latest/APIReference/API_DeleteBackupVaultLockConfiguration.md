---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteBackupVaultLockConfiguration.html
---

# DeleteBackupVaultLockConfiguration
<a name="API_DeleteBackupVaultLockConfiguration"></a>

Deletes AWS Backup Vault Lock from a backup vault specified by a backup vault name.

If the Vault Lock configuration is immutable, then you cannot delete Vault Lock using API operations, and you will receive an `InvalidRequestException` if you attempt to do so. For more information, see [Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html) in the * AWS Backup Developer Guide*.

## Request Syntax
<a name="API_DeleteBackupVaultLockConfiguration_RequestSyntax"></a>

```
DELETE /backup-vaults/{{backupVaultName}}/vault-lock HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteBackupVaultLockConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [backupVaultName](#API_DeleteBackupVaultLockConfiguration_RequestSyntax) **   <a name="Backup-DeleteBackupVaultLockConfiguration-request-uri-BackupVaultName"></a>
The name of the backup vault from which to delete AWS Backup Vault Lock.
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`
Required: Yes

## Request Body
<a name="API_DeleteBackupVaultLockConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteBackupVaultLockConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteBackupVaultLockConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteBackupVaultLockConfiguration_Errors"></a>

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
<a name="API_DeleteBackupVaultLockConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/DeleteBackupVaultLockConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/DeleteBackupVaultLockConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DeleteBackupVaultLockConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/DeleteBackupVaultLockConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DeleteBackupVaultLockConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/DeleteBackupVaultLockConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/DeleteBackupVaultLockConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/DeleteBackupVaultLockConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/DeleteBackupVaultLockConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DeleteBackupVaultLockConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
