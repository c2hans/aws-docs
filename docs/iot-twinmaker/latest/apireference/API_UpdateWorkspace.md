---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_UpdateWorkspace.html
---

# UpdateWorkspace
<a name="API_UpdateWorkspace"></a>

Updates a workspace.

## Request Syntax
<a name="API_UpdateWorkspace_RequestSyntax"></a>

```
PUT /workspaces/{{workspaceId}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "role": "{{string}}",
   "s3Location": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateWorkspace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_UpdateWorkspace_RequestSyntax) **   <a name="tm-UpdateWorkspace-request-uri-workspaceId"></a>
The ID of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateWorkspace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateWorkspace_RequestSyntax) **   <a name="tm-UpdateWorkspace-request-description"></a>
The description of the workspace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** [role](#API_UpdateWorkspace_RequestSyntax) **   <a name="tm-UpdateWorkspace-request-role"></a>
The ARN of the execution role associated with the workspace.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iam::[0-9]{12}:role/.*`
Required: No

 ** [s3Location](#API_UpdateWorkspace_RequestSyntax) **   <a name="tm-UpdateWorkspace-request-s3Location"></a>
The ARN of the S3 bucket where resources associated with the workspace are stored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*(^arn:((aws)|(aws-cn)|(aws-us-gov)):s3:::)([a-zA-Z0-9_-]+$).*`
Required: No

## Response Syntax
<a name="API_UpdateWorkspace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "updateDateTime": number
}
```

## Response Elements
<a name="API_UpdateWorkspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [updateDateTime](#API_UpdateWorkspace_ResponseSyntax) **   <a name="tm-UpdateWorkspace-response-updateDateTime"></a>
The date and time of the current update.
Type: Timestamp

## Errors
<a name="API_UpdateWorkspace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

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
<a name="API_UpdateWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/UpdateWorkspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/UpdateWorkspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/UpdateWorkspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/UpdateWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/UpdateWorkspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/UpdateWorkspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/UpdateWorkspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/UpdateWorkspace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/UpdateWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/UpdateWorkspace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
