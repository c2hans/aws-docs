---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ArchiveProject.html
---

# ArchiveProject

Archives a project. Archiving is terminal; there is no delete. Archiving an already-archived project succeeds without effect. The default project cannot be archived.

## Request Syntax
<a name="API_ArchiveProject_RequestSyntax"></a>

```
POST /projects/{{projectIdentifier}}/archive HTTP/1.1
```

## URI Request Parameters
<a name="API_ArchiveProject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [projectIdentifier](#API_ArchiveProject_RequestSyntax) **   <a name="bedrock-ArchiveProject-request-uri-projectIdentifier"></a>
The id or ARN of the project to archive.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `([a-zA-Z0-9_-]+|arn:aws(-[^:]+)?:bedrock:[0-9a-z-]{1,20}:[0-9]{12}:project/[a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_ArchiveProject_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ArchiveProject_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "archivedAt": "string",
   "arn": "string",
   "createdAt": "string",
   "dataRetention": {
      "mode": "string"
   },
   "id": "string",
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_ArchiveProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [archivedAt](#API_ArchiveProject_ResponseSyntax) **   <a name="bedrock-ArchiveProject-response-archivedAt"></a>
The time the project was archived.
Type: Timestamp

 ** [arn](#API_ArchiveProject_ResponseSyntax) **   <a name="bedrock-ArchiveProject-response-arn"></a>
The Amazon Resource Name (ARN) of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:bedrock:[0-9a-z-]{1,20}:[0-9]{12}:project/[a-zA-Z0-9_-]+`

 ** [createdAt](#API_ArchiveProject_ResponseSyntax) **   <a name="bedrock-ArchiveProject-response-createdAt"></a>
The time the project was created.
Type: Timestamp

 ** [dataRetention](#API_ArchiveProject_ResponseSyntax) **   <a name="bedrock-ArchiveProject-response-dataRetention"></a>
The project's data retention setting. A mode of `inherit` defers to the account setting or model default.
Type: [ProjectDataRetention](API_ProjectDataRetention.md) object

 ** [id](#API_ArchiveProject_ResponseSyntax) **   <a name="bedrock-ArchiveProject-response-id"></a>
The project ID. The account's default project uses `default`; a named project's generated ID starts with `proj_`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [name](#API_ArchiveProject_ResponseSyntax) **   <a name="bedrock-ArchiveProject-response-name"></a>
The project's display name. Project names do not have to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\S.*`

 ** [status](#API_ArchiveProject_ResponseSyntax) **   <a name="bedrock-ArchiveProject-response-status"></a>
The project's lifecycle status.
Type: String
Valid Values: `active | archived`

## Errors
<a name="API_ArchiveProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because of missing access permissions.
HTTP Status Code: 403

 ** ConflictException **
Error occurred because of a conflict while performing an operation.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.
HTTP Status Code: 404

 ** ThrottlingException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 429

 ** ValidationException **
Input validation failed. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_ArchiveProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ArchiveProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ArchiveProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ArchiveProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ArchiveProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ArchiveProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ArchiveProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ArchiveProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ArchiveProject)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ArchiveProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ArchiveProject)
