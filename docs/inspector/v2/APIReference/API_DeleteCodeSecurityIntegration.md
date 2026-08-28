---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_DeleteCodeSecurityIntegration.html
---

# DeleteCodeSecurityIntegration
<a name="API_DeleteCodeSecurityIntegration"></a>

Deletes a code security integration.

## Request Syntax
<a name="API_DeleteCodeSecurityIntegration_RequestSyntax"></a>

```
POST /codesecurity/integration/delete HTTP/1.1
Content-type: application/json

{
   "integrationArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteCodeSecurityIntegration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteCodeSecurityIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [integrationArn](#API_DeleteCodeSecurityIntegration_RequestSyntax) **   <a name="inspector2-DeleteCodeSecurityIntegration-request-integrationArn"></a>
The Amazon Resource Name (ARN) of the code security integration to delete.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration/[a-f0-9-]{36}`
Required: Yes

## Response Syntax
<a name="API_DeleteCodeSecurityIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "integrationArn": "string"
}
```

## Response Elements
<a name="API_DeleteCodeSecurityIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [integrationArn](#API_DeleteCodeSecurityIntegration_ResponseSyntax) **   <a name="inspector2-DeleteCodeSecurityIntegration-response-integrationArn"></a>
The Amazon Resource Name (ARN) of the deleted code security integration.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration/[a-f0-9-]{36}`

## Errors
<a name="API_DeleteCodeSecurityIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access an invalid resource. Make sure the resource is specified correctly.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_DeleteCodeSecurityIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/DeleteCodeSecurityIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/DeleteCodeSecurityIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/DeleteCodeSecurityIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/DeleteCodeSecurityIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/DeleteCodeSecurityIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/DeleteCodeSecurityIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/DeleteCodeSecurityIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/DeleteCodeSecurityIntegration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/DeleteCodeSecurityIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/DeleteCodeSecurityIntegration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
