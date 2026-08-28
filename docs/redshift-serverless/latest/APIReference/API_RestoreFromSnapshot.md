---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_RestoreFromSnapshot.html
---

# RestoreFromSnapshot
<a name="API_RestoreFromSnapshot"></a>

Restores a namespace from a snapshot.

## Request Syntax
<a name="API_RestoreFromSnapshot_RequestSyntax"></a>

```
{
   "adminPasswordSecretKmsKeyId": "{{string}}",
   "manageAdminPassword": {{boolean}},
   "namespaceName": "{{string}}",
   "ownerAccount": "{{string}}",
   "snapshotArn": "{{string}}",
   "snapshotName": "{{string}}",
   "workgroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_RestoreFromSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [adminPasswordSecretKmsKeyId](#API_RestoreFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreFromSnapshot-request-adminPasswordSecretKmsKeyId"></a>
The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.
Type: String
Required: No

 ** [manageAdminPassword](#API_RestoreFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreFromSnapshot-request-manageAdminPassword"></a>
If `true`, Amazon Redshift uses AWS Secrets Manager to manage the restored snapshot's admin credentials. If `MmanageAdminPassword` is false or not set, Amazon Redshift uses the admin credentials that the namespace or cluster had at the time the snapshot was taken.
Type: Boolean
Required: No

 ** [namespaceName](#API_RestoreFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreFromSnapshot-request-namespaceName"></a>
The name of the namespace to restore the snapshot to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** [ownerAccount](#API_RestoreFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreFromSnapshot-request-ownerAccount"></a>
The AWS account that owns the snapshot.
Type: String
Required: No

 ** [snapshotArn](#API_RestoreFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreFromSnapshot-request-snapshotArn"></a>
The Amazon Resource Name (ARN) of the snapshot to restore from. Required if restoring from a provisioned cluster to Amazon Redshift Serverless. Must not be specified at the same time as `snapshotName`.
The format of the ARN is arn:aws:redshift:<region>:<account\_id>:snapshot:<cluster\_identifier>/<snapshot\_identifier>.
Type: String
Required: No

 ** [snapshotName](#API_RestoreFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreFromSnapshot-request-snapshotName"></a>
The name of the snapshot to restore from. Must not be specified at the same time as `snapshotArn`.
Type: String
Required: No

 ** [workgroupName](#API_RestoreFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreFromSnapshot-request-workgroupName"></a>
The name of the workgroup used to restore the snapshot.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_RestoreFromSnapshot_ResponseSyntax"></a>

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
   "ownerAccount": "string",
   "snapshotName": "string"
}
```

## Response Elements
<a name="API_RestoreFromSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [namespace](#API_RestoreFromSnapshot_ResponseSyntax) **   <a name="redshiftserverless-RestoreFromSnapshot-response-namespace"></a>
A collection of database objects and users.
Type: [Namespace](API_Namespace.md) object

 ** [ownerAccount](#API_RestoreFromSnapshot_ResponseSyntax) **   <a name="redshiftserverless-RestoreFromSnapshot-response-ownerAccount"></a>
The owner AWS; account of the snapshot that was restored.
Type: String

 ** [snapshotName](#API_RestoreFromSnapshot_ResponseSyntax) **   <a name="redshiftserverless-RestoreFromSnapshot-response-snapshotName"></a>
The name of the snapshot used to restore the namespace.
Type: String

## Errors
<a name="API_RestoreFromSnapshot_Errors"></a>

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

 ** ServiceQuotaExceededException **
The service limit was exceeded.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_RestoreFromSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/RestoreFromSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/RestoreFromSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/RestoreFromSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/RestoreFromSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/RestoreFromSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/RestoreFromSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/RestoreFromSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/RestoreFromSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/RestoreFromSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/RestoreFromSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
