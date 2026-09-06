---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetCodeSecurityIntegration.html
---

# GetCodeSecurityIntegration
<a name="API_GetCodeSecurityIntegration"></a>

Retrieves information about a code security integration.

## Request Syntax
<a name="API_GetCodeSecurityIntegration_RequestSyntax"></a>

```
POST /codesecurity/integration/get HTTP/1.1
Content-type: application/json

{
   "integrationArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_GetCodeSecurityIntegration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetCodeSecurityIntegration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [integrationArn](#API_GetCodeSecurityIntegration_RequestSyntax) **   <a name="inspector2-GetCodeSecurityIntegration-request-integrationArn"></a>
The Amazon Resource Name (ARN) of the code security integration to retrieve.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration/[a-f0-9-]{36}`
Required: Yes

 ** [tags](#API_GetCodeSecurityIntegration_RequestSyntax) **   <a name="inspector2-GetCodeSecurityIntegration-request-tags"></a>
The tags associated with the code security integration.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_GetCodeSecurityIntegration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "authorizationUrl": "string",
   "createdOn": number,
   "integrationArn": "string",
   "lastUpdateOn": number,
   "name": "string",
   "status": "string",
   "statusReason": "string",
   "tags": {
      "string" : "string"
   },
   "type": "string"
}
```

## Response Elements
<a name="API_GetCodeSecurityIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authorizationUrl](#API_GetCodeSecurityIntegration_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityIntegration-response-authorizationUrl"></a>
The URL used to authorize the integration with the repository provider. This is only returned if reauthorization is required to fix a connection issue. Otherwise, it is null.
Type: String

 ** [createdOn](#API_GetCodeSecurityIntegration_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityIntegration-response-createdOn"></a>
The timestamp when the code security integration was created.
Type: Timestamp

 ** [integrationArn](#API_GetCodeSecurityIntegration_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityIntegration-response-integrationArn"></a>
The Amazon Resource Name (ARN) of the code security integration.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration/[a-f0-9-]{36}`

 ** [lastUpdateOn](#API_GetCodeSecurityIntegration_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityIntegration-response-lastUpdateOn"></a>
The timestamp when the code security integration was last updated.
Type: Timestamp

 ** [name](#API_GetCodeSecurityIntegration_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityIntegration-response-name"></a>
The name of the code security integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[a-zA-Z0-9-_$:.]*`

 ** [status](#API_GetCodeSecurityIntegration_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityIntegration-response-status"></a>
The current status of the code security integration.
Type: String
Valid Values: `PENDING | IN_PROGRESS | ACTIVE | INACTIVE | DISABLING`

 ** [statusReason](#API_GetCodeSecurityIntegration_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityIntegration-response-statusReason"></a>
The reason for the current status of the code security integration.
Type: String

 ** [tags](#API_GetCodeSecurityIntegration_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityIntegration-response-tags"></a>
The tags associated with the code security integration.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [type](#API_GetCodeSecurityIntegration_ResponseSyntax) **   <a name="inspector2-GetCodeSecurityIntegration-response-type"></a>
The type of repository provider for the integration.
Type: String
Valid Values: `GITLAB_SELF_MANAGED | GITHUB`

## Errors
<a name="API_GetCodeSecurityIntegration_Errors"></a>

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
<a name="API_GetCodeSecurityIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/GetCodeSecurityIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/GetCodeSecurityIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GetCodeSecurityIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/GetCodeSecurityIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GetCodeSecurityIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/GetCodeSecurityIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/GetCodeSecurityIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/GetCodeSecurityIntegration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/GetCodeSecurityIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GetCodeSecurityIntegration)
