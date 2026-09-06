---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetWorkspace.html
---

# GetWorkspace
<a name="API_GetWorkspace"></a>

Retrieves information about a workspace.

## Request Syntax
<a name="API_GetWorkspace_RequestSyntax"></a>

```
GET /workspaces/{{workspaceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWorkspace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_GetWorkspace_RequestSyntax) **   <a name="tm-GetWorkspace-request-uri-workspaceId"></a>
The ID of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+$|^arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_GetWorkspace_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWorkspace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationDateTime": number,
   "description": "string",
   "linkedServices": [ "string" ],
   "role": "string",
   "s3Location": "string",
   "updateDateTime": number,
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_GetWorkspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetWorkspace_ResponseSyntax) **   <a name="tm-GetWorkspace-response-arn"></a>
The ARN of the workspace.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`

 ** [creationDateTime](#API_GetWorkspace_ResponseSyntax) **   <a name="tm-GetWorkspace-response-creationDateTime"></a>
The date and time when the workspace was created.
Type: Timestamp

 ** [description](#API_GetWorkspace_ResponseSyntax) **   <a name="tm-GetWorkspace-response-description"></a>
The description of the workspace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

 ** [linkedServices](#API_GetWorkspace_ResponseSyntax) **   <a name="tm-GetWorkspace-response-linkedServices"></a>
A list of services that are linked to the workspace.
Type: Array of strings
Pattern: `[a-zA-Z_0-9]+`

 ** [role](#API_GetWorkspace_ResponseSyntax) **   <a name="tm-GetWorkspace-response-role"></a>
The ARN of the execution role associated with the workspace.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iam::[0-9]{12}:role/.*`

 ** [s3Location](#API_GetWorkspace_ResponseSyntax) **   <a name="tm-GetWorkspace-response-s3Location"></a>
The ARN of the Amazon S3 bucket where resources associated with the workspace are stored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*(^arn:((aws)|(aws-cn)|(aws-us-gov)):s3:::)([a-zA-Z0-9_-]+$).*`

 ** [updateDateTime](#API_GetWorkspace_ResponseSyntax) **   <a name="tm-GetWorkspace-response-updateDateTime"></a>
The date and time when the workspace was last updated.
Type: Timestamp

 ** [workspaceId](#API_GetWorkspace_ResponseSyntax) **   <a name="tm-GetWorkspace-response-workspaceId"></a>
The ID of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`

## Errors
<a name="API_GetWorkspace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource wasn't found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_GetWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/GetWorkspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/GetWorkspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/GetWorkspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/GetWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/GetWorkspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/GetWorkspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/GetWorkspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/GetWorkspace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/GetWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/GetWorkspace)
