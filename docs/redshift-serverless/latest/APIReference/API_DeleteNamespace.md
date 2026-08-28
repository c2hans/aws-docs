---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_DeleteNamespace.html
---

# DeleteNamespace
<a name="API_DeleteNamespace"></a>

Deletes a namespace from Amazon Redshift Serverless. Before you delete the namespace, you can create a final snapshot that has all of the data within the namespace.

## Request Syntax
<a name="API_DeleteNamespace_RequestSyntax"></a>

```
{
   "finalSnapshotName": "{{string}}",
   "finalSnapshotRetentionPeriod": {{number}},
   "namespaceName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteNamespace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [finalSnapshotName](#API_DeleteNamespace_RequestSyntax) **   <a name="redshiftserverless-DeleteNamespace-request-finalSnapshotName"></a>
The name of the snapshot to be created before the namespace is deleted.
Type: String
Required: No

 ** [finalSnapshotRetentionPeriod](#API_DeleteNamespace_RequestSyntax) **   <a name="redshiftserverless-DeleteNamespace-request-finalSnapshotRetentionPeriod"></a>
How long to retain the final snapshot.
Type: Integer
Required: No

 ** [namespaceName](#API_DeleteNamespace_RequestSyntax) **   <a name="redshiftserverless-DeleteNamespace-request-namespaceName"></a>
The name of the namespace to delete.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteNamespace_ResponseSyntax"></a>

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
   }
}
```

## Response Elements
<a name="API_DeleteNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [namespace](#API_DeleteNamespace_ResponseSyntax) **   <a name="redshiftserverless-DeleteNamespace-response-namespace"></a>
The deleted namespace object.
Type: [Namespace](API_Namespace.md) object

## Errors
<a name="API_DeleteNamespace_Errors"></a>

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
<a name="API_DeleteNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/DeleteNamespace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/DeleteNamespace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/DeleteNamespace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/DeleteNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/DeleteNamespace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/DeleteNamespace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/DeleteNamespace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/DeleteNamespace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/DeleteNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/DeleteNamespace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
