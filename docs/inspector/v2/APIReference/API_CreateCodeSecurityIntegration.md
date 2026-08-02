---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateCodeSecurityIntegration.html
---

# CreateCodeSecurityIntegration
<a name="API_CreateCodeSecurityIntegration"></a>

Creates a code security integration with a source code repository provider.

After calling the `CreateCodeSecurityIntegration` operation, you complete authentication and authorization with your provider. Next you call the `UpdateCodeSecurityIntegration` operation to provide the `details` to complete the integration setup

## Request Syntax
<a name="API_CreateCodeSecurityIntegration_RequestSyntax"></a>

```
POST /codesecurity/integration/create HTTP/1.1
Content-type: application/json

{
   "details": { ... },
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateCodeSecurityIntegration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCodeSecurityIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [details](#API_CreateCodeSecurityIntegration_RequestSyntax) **   <a name="inspector2-CreateCodeSecurityIntegration-request-details"></a>
The integration details specific to the repository provider type.
Type: [CreateIntegrationDetail](API_CreateIntegrationDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [name](#API_CreateCodeSecurityIntegration_RequestSyntax) **   <a name="inspector2-CreateCodeSecurityIntegration-request-name"></a>
The name of the code security integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[a-zA-Z0-9-_$:.]*`
Required: Yes

 ** [tags](#API_CreateCodeSecurityIntegration_RequestSyntax) **   <a name="inspector2-CreateCodeSecurityIntegration-request-tags"></a>
The tags to apply to the code security integration.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [type](#API_CreateCodeSecurityIntegration_RequestSyntax) **   <a name="inspector2-CreateCodeSecurityIntegration-request-type"></a>
The type of repository provider for the integration.
Type: String
Valid Values: `GITLAB_SELF_MANAGED | GITHUB`
Required: Yes

## Response Syntax
<a name="API_CreateCodeSecurityIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "authorizationUrl": "string",
   "integrationArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateCodeSecurityIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authorizationUrl](#API_CreateCodeSecurityIntegration_ResponseSyntax) **   <a name="inspector2-CreateCodeSecurityIntegration-response-authorizationUrl"></a>
The URL used to authorize the integration with the repository provider.
Type: String

 ** [integrationArn](#API_CreateCodeSecurityIntegration_ResponseSyntax) **   <a name="inspector2-CreateCodeSecurityIntegration-response-integrationArn"></a>
The Amazon Resource Name (ARN) of the created code security integration.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration/[a-f0-9-]{36}`

 ** [status](#API_CreateCodeSecurityIntegration_ResponseSyntax) **   <a name="inspector2-CreateCodeSecurityIntegration-response-status"></a>
The current status of the code security integration.
Type: String
Valid Values: `PENDING | IN_PROGRESS | ACTIVE | INACTIVE | DISABLING`

## Errors
<a name="API_CreateCodeSecurityIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** ConflictException **
A conflict occurred. This exception occurs when the same resource is being modified by concurrent requests.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.
 ** resourceId **
The ID of the resource that exceeds a service quota.
HTTP Status Code: 402

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
<a name="API_CreateCodeSecurityIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/CreateCodeSecurityIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/CreateCodeSecurityIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CreateCodeSecurityIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/CreateCodeSecurityIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CreateCodeSecurityIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/CreateCodeSecurityIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/CreateCodeSecurityIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/CreateCodeSecurityIntegration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/CreateCodeSecurityIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CreateCodeSecurityIntegration)
