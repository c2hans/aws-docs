---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AttachDataSource.html
---

# AttachDataSource
<a name="API_AttachDataSource"></a>

Attaches a data source to an OpenSearch application. The data source must be an Amazon OpenSearch Service domain. If both the application and the data source are active, the attachment completes immediately with a status of `ATTACHED`. Otherwise, the operation returns `PENDING` and completes the attachment automatically once both become active. If the attachment cannot be completed, its status becomes `FAILED`. This operation is idempotent: If the data source is already attached or pending, the operation returns the existing attachment.

## Request Syntax
<a name="API_AttachDataSource_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/application/{{id}}/attachDataSource HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "dataSourceArn": "{{string}}",
   "workspaceConfiguration": {
      "name": "{{string}}",
      "workspaceType": "{{string}}"
   },
   "workspaceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AttachDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_AttachDataSource_RequestSyntax) **   <a name="opensearchservice-AttachDataSource-request-uri-id"></a>
The unique identifier or name of the OpenSearch application to attach the data source to. This is the same identifier used with `UpdateApplication`, `GetApplication`, and `DeleteApplication`.
Pattern: `[a-z0-9]{3,30}`
Required: Yes

## Request Body
<a name="API_AttachDataSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_AttachDataSource_RequestSyntax) **   <a name="opensearchservice-AttachDataSource-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request. If you retry a request with the same client token and the same parameters, the retry succeeds without performing any further actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [dataSourceArn](#API_AttachDataSource_RequestSyntax) **   <a name="opensearchservice-AttachDataSource-request-dataSourceArn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: Yes

 ** [workspaceConfiguration](#API_AttachDataSource_RequestSyntax) **   <a name="opensearchservice-AttachDataSource-request-workspaceConfiguration"></a>
Configuration for creating a new workspace during the attachment. If specified, a workspace is created and linked to the data source after the attachment completes. Mutually exclusive with `workspaceId`.
Type: [WorkspaceConfigurationInput](API_WorkspaceConfigurationInput.md) object
Required: No

 ** [workspaceId](#API_AttachDataSource_RequestSyntax) **   <a name="opensearchservice-AttachDataSource-request-workspaceId"></a>
The identifier of an existing workspace to update with the new data source. Mutually exclusive with `workspaceConfiguration`.
Type: String
Required: No

## Response Syntax
<a name="API_AttachDataSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "attachmentId": "string",
   "dataSourceArn": "string",
   "id": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_AttachDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_AttachDataSource_ResponseSyntax) **   <a name="opensearchservice-AttachDataSource-response-arn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`

 ** [attachmentId](#API_AttachDataSource_ResponseSyntax) **   <a name="opensearchservice-AttachDataSource-response-attachmentId"></a>
The unique identifier assigned to the data source attachment.
Type: String

 ** [dataSourceArn](#API_AttachDataSource_ResponseSyntax) **   <a name="opensearchservice-AttachDataSource-response-dataSourceArn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`

 ** [id](#API_AttachDataSource_ResponseSyntax) **   <a name="opensearchservice-AttachDataSource-response-id"></a>
The unique identifier of the OpenSearch application.
Type: String
Pattern: `[a-z0-9]{3,30}`

 ** [status](#API_AttachDataSource_ResponseSyntax) **   <a name="opensearchservice-AttachDataSource-response-status"></a>
The status of the data source attachment. Valid values are `PENDING` (waiting for resources to become active), `ATTACHED` (successfully attached), and `FAILED` (attachment timed out or encountered a non-retryable error).
Type: String
Valid Values: `PENDING | ATTACHED | FAILED`

## Errors
<a name="API_AttachDataSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** ConflictException **
An error occurred because the client attempts to remove a resource that is currently in use.
HTTP Status Code: 409

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_AttachDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/AttachDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/AttachDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AttachDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/AttachDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AttachDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/AttachDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/AttachDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/AttachDataSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/AttachDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AttachDataSource)
