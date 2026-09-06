---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetWebExperience.html
---

# GetWebExperience
<a name="API_GetWebExperience"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Gets information about an existing Amazon Q Business web experience.

## Request Syntax
<a name="API_GetWebExperience_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/experiences/{{webExperienceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWebExperience_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetWebExperience_RequestSyntax) **   <a name="qbusiness-GetWebExperience-request-uri-applicationId"></a>
The identifier of the Amazon Q Business application linked to the web experience.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [webExperienceId](#API_GetWebExperience_RequestSyntax) **   <a name="qbusiness-GetWebExperience-request-uri-webExperienceId"></a>
The identifier of the Amazon Q Business web experience.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`
Required: Yes

## Request Body
<a name="API_GetWebExperience_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWebExperience_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string",
   "authenticationConfiguration": { ... },
   "browserExtensionConfiguration": {
      "enabledBrowserExtensions": [ "string" ]
   },
   "createdAt": number,
   "customizationConfiguration": {
      "customCSSUrl": "string",
      "faviconUrl": "string",
      "fontUrl": "string",
      "logoUrl": "string"
   },
   "defaultEndpoint": "string",
   "error": {
      "errorCode": "string",
      "errorMessage": "string"
   },
   "identityProviderConfiguration": { ... },
   "origins": [ "string" ],
   "roleArn": "string",
   "samplePromptsControlMode": "string",
   "status": "string",
   "subtitle": "string",
   "title": "string",
   "updatedAt": number,
   "webExperienceArn": "string",
   "webExperienceId": "string",
   "welcomeMessage": "string"
}
```

## Response Elements
<a name="API_GetWebExperience_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-applicationId"></a>
The identifier of the Amazon Q Business application linked to the web experience.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [authenticationConfiguration](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-authenticationConfiguration"></a>
 *This parameter has been deprecated.*
The authentication configuration information for your Amazon Q Business web experience.
Type: [WebExperienceAuthConfiguration](API_WebExperienceAuthConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [browserExtensionConfiguration](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-browserExtensionConfiguration"></a>
The browser extension configuration for an Amazon Q Business web experience.
Type: [BrowserExtensionConfiguration](API_BrowserExtensionConfiguration.md) object

 ** [createdAt](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-createdAt"></a>
The Unix timestamp when the Amazon Q Business web experience was last created.
Type: Timestamp

 ** [customizationConfiguration](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-customizationConfiguration"></a>
Gets the custom logo, favicon, font, and color used in the Amazon Q web experience.
Type: [CustomizationConfiguration](API_CustomizationConfiguration.md) object

 ** [defaultEndpoint](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-defaultEndpoint"></a>
The endpoint of your Amazon Q Business web experience.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(https?|ftp|file)://([^\s]*)`

 ** [error](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-error"></a>
When the `Status` field value is `FAILED`, the `ErrorMessage` field contains a description of the error that caused the data source connector to fail.
Type: [ErrorDetail](API_ErrorDetail.md) object

 ** [identityProviderConfiguration](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-identityProviderConfiguration"></a>
Information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
Type: [IdentityProviderConfiguration](API_IdentityProviderConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [origins](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-origins"></a>
Gets the website domain origins that are allowed to embed the Amazon Q Business web experience. The *domain origin* refers to the base URL for accessing a website including the protocol (`http/https`), the domain name, and the port number (if specified).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(http://|https://)[a-zA-Z0-9-_.]+(?::[0-9]{1,5})?`

 ** [roleArn](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-roleArn"></a>
 The Amazon Resource Name (ARN) of the service role attached to your web experience.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [samplePromptsControlMode](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-samplePromptsControlMode"></a>
Determines whether sample prompts are enabled in the web experience for an end user.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [status](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-status"></a>
The current status of the Amazon Q Business web experience. When the `Status` field value is `FAILED`, the `ErrorMessage` field contains a description of the error that caused the data source connector to fail.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | PENDING_AUTH_CONFIG`

 ** [subtitle](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-subtitle"></a>
The subtitle for your Amazon Q Business web experience.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`

 ** [title](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-title"></a>
The title for your Amazon Q Business web experience.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`

 ** [updatedAt](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-updatedAt"></a>
The Unix timestamp when the Amazon Q Business web experience was last updated.
Type: Timestamp

 ** [webExperienceArn](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-webExperienceArn"></a>
The Amazon Resource Name (ARN) of the role with the permission to access the Amazon Q Business web experience and required resources.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [webExperienceId](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-webExperienceId"></a>
The identifier of the Amazon Q Business web experience.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`

 ** [welcomeMessage](#API_GetWebExperience_ResponseSyntax) **   <a name="qbusiness-GetWebExperience-response-welcomeMessage"></a>
The customized welcome message for end users of an Amazon Q Business web experience.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.

## Errors
<a name="API_GetWebExperience_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.
 ** message **
The message describing a `ResourceNotFoundException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_GetWebExperience_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/GetWebExperience)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/GetWebExperience)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/GetWebExperience)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/GetWebExperience)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/GetWebExperience)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/GetWebExperience)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/GetWebExperience)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/GetWebExperience)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/GetWebExperience)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/GetWebExperience)
