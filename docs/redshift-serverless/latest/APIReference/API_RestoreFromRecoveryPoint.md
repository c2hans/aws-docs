---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_RestoreFromRecoveryPoint.html
---

# RestoreFromRecoveryPoint
<a name="API_RestoreFromRecoveryPoint"></a>

Restore the data from a recovery point.

## Request Syntax
<a name="API_RestoreFromRecoveryPoint_RequestSyntax"></a>

```
{
   "namespaceName": "{{string}}",
   "recoveryPointId": "{{string}}",
   "workgroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_RestoreFromRecoveryPoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [namespaceName](#API_RestoreFromRecoveryPoint_RequestSyntax) **   <a name="redshiftserverless-RestoreFromRecoveryPoint-request-namespaceName"></a>
The name of the namespace to restore data into.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** [recoveryPointId](#API_RestoreFromRecoveryPoint_RequestSyntax) **   <a name="redshiftserverless-RestoreFromRecoveryPoint-request-recoveryPointId"></a>
The unique identifier of the recovery point to restore from.
Type: String
Required: Yes

 ** [workgroupName](#API_RestoreFromRecoveryPoint_RequestSyntax) **   <a name="redshiftserverless-RestoreFromRecoveryPoint-request-workgroupName"></a>
The name of the workgroup used to restore data.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_RestoreFromRecoveryPoint_ResponseSyntax"></a>

```
{
   "namespace": {
      "adminPasswordSecretArn": "string",
      "adminPasswordSecretKmsKeyId": "string",
      "adminUsername": "string",
      "catalogArn": "string",
      "creationDate": "string",
      "dbName": "string",
      "defaultIamRoleArn": "string",
      "iamRoles": [ "string" ],
      "kmsKeyId": "string",
      "lakehouseRegistrationStatus": "string",
      "logExports": [ "string" ],
      "namespaceArn": "string",
      "namespaceId": "string",
      "namespaceName": "string",
      "status": "string"
   },
   "recoveryPointId": "string"
}
```

## Response Elements
<a name="API_RestoreFromRecoveryPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [namespace](#API_RestoreFromRecoveryPoint_ResponseSyntax) **   <a name="redshiftserverless-RestoreFromRecoveryPoint-response-namespace"></a>
The namespace that data was restored into.
Type: [Namespace](API_Namespace.md) object

 ** [recoveryPointId](#API_RestoreFromRecoveryPoint_ResponseSyntax) **   <a name="redshiftserverless-RestoreFromRecoveryPoint-response-recoveryPointId"></a>
The unique identifier of the recovery point used for the restore.
Type: String

## Errors
<a name="API_RestoreFromRecoveryPoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_RestoreFromRecoveryPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/RestoreFromRecoveryPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/RestoreFromRecoveryPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/RestoreFromRecoveryPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/RestoreFromRecoveryPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/RestoreFromRecoveryPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/RestoreFromRecoveryPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/RestoreFromRecoveryPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/RestoreFromRecoveryPoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/RestoreFromRecoveryPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/RestoreFromRecoveryPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
