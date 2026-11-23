---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateProject.html
---

# CreateProject

Creates a project: a workload boundary within the account that inference requests can be associated with.

## Request Syntax
<a name="API_CreateProject_RequestSyntax"></a>

```
POST /projects HTTP/1.1
Content-type: application/json

{
   "dataRetention": {
      "mode": "{{string}}"
   },
   "name": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateProject_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateProject_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dataRetention](#API_CreateProject_RequestSyntax) **   <a name="bedrock-CreateProject-request-dataRetention"></a>
The project's data-retention mode. If you omit this field, Amazon Bedrock sets the mode to `inherit`. The project then uses the account setting or the model default.
Type: [ProjectDataRetention](API_ProjectDataRetention.md) object
Required: No

 ** [name](#API_CreateProject_RequestSyntax) **   <a name="bedrock-CreateProject-request-name"></a>
The display name for the project. Project names do not have to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\S.*`
Required: Yes

 ** [tags](#API_CreateProject_RequestSyntax) **   <a name="bedrock-CreateProject-request-tags"></a>
The tags to associate with the project.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateProject_ResponseSyntax"></a>

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
<a name="API_CreateProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [archivedAt](#API_CreateProject_ResponseSyntax) **   <a name="bedrock-CreateProject-response-archivedAt"></a>
The time the project was archived.
Type: Timestamp

 ** [arn](#API_CreateProject_ResponseSyntax) **   <a name="bedrock-CreateProject-response-arn"></a>
The Amazon Resource Name (ARN) of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:bedrock:[0-9a-z-]{1,20}:[0-9]{12}:project/[a-zA-Z0-9_-]+`

 ** [createdAt](#API_CreateProject_ResponseSyntax) **   <a name="bedrock-CreateProject-response-createdAt"></a>
The time the project was created.
Type: Timestamp

 ** [dataRetention](#API_CreateProject_ResponseSyntax) **   <a name="bedrock-CreateProject-response-dataRetention"></a>
The project's data retention setting. A mode of `inherit` defers to the account setting or model default.
Type: [ProjectDataRetention](API_ProjectDataRetention.md) object

 ** [id](#API_CreateProject_ResponseSyntax) **   <a name="bedrock-CreateProject-response-id"></a>
The project ID. The account's default project uses `default`; a named project's generated ID starts with `proj_`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [name](#API_CreateProject_ResponseSyntax) **   <a name="bedrock-CreateProject-response-name"></a>
The project's display name. Project names do not have to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\S.*`

 ** [status](#API_CreateProject_ResponseSyntax) **   <a name="bedrock-CreateProject-response-status"></a>
The project's lifecycle status.
Type: String
Valid Values: `active | archived`

## Errors
<a name="API_CreateProject_Errors"></a>

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

 ** ServiceQuotaExceededException **
The number of requests exceeds the service quota. Resubmit your request later.
HTTP Status Code: 400

 ** ThrottlingException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 429

 ** TooManyTagsException **
The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request.
 ** resourceName **
The name of the resource with too many tags.
HTTP Status Code: 400

 ** ValidationException **
Input validation failed. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_CreateProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateProject)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateProject)
