---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DisassociateRecoveryPointFromParent.html
---

# DisassociateRecoveryPointFromParent
<a name="API_DisassociateRecoveryPointFromParent"></a>

This action to a specific child (nested) recovery point removes the relationship between the specified recovery point and its parent (composite) recovery point.

## Request Syntax
<a name="API_DisassociateRecoveryPointFromParent_RequestSyntax"></a>

```
DELETE /backup-vaults/{{backupVaultName}}/recovery-points/{{recoveryPointArn}}/parentAssociation HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociateRecoveryPointFromParent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [backupVaultName](#API_DisassociateRecoveryPointFromParent_RequestSyntax) **   <a name="Backup-DisassociateRecoveryPointFromParent-request-uri-BackupVaultName"></a>
The name of a logical container where the child (nested) recovery point is stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created.
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`
Required: Yes

 ** [recoveryPointArn](#API_DisassociateRecoveryPointFromParent_RequestSyntax) **   <a name="Backup-DisassociateRecoveryPointFromParent-request-uri-RecoveryPointArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the child (nested) recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45.`
Required: Yes

## Request Body
<a name="API_DisassociateRecoveryPointFromParent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociateRecoveryPointFromParent_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DisassociateRecoveryPointFromParent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DisassociateRecoveryPointFromParent_Errors"></a>

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
<a name="API_DisassociateRecoveryPointFromParent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/DisassociateRecoveryPointFromParent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/DisassociateRecoveryPointFromParent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DisassociateRecoveryPointFromParent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/DisassociateRecoveryPointFromParent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DisassociateRecoveryPointFromParent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/DisassociateRecoveryPointFromParent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/DisassociateRecoveryPointFromParent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/DisassociateRecoveryPointFromParent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/DisassociateRecoveryPointFromParent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DisassociateRecoveryPointFromParent)
