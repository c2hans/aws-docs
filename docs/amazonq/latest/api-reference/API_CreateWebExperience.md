---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateWebExperience.html
---

# CreateWebExperience
<a name="API_CreateWebExperience"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Creates an Amazon Q Business web experience.

## Request Syntax
<a name="API_CreateWebExperience_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/experiences HTTP/1.1
Content-type: application/json

{
   "browserExtensionConfiguration": {
      "enabledBrowserExtensions": [ "{{string}}" ]
   },
   "clientToken": "{{string}}",
   "customizationConfiguration": {
      "customCSSUrl": "{{string}}",
      "faviconUrl": "{{string}}",
      "fontUrl": "{{string}}",
      "logoUrl": "{{string}}"
   },
   "identityProviderConfiguration": { ... },
   "origins": [ "{{string}}" ],
   "roleArn": "{{string}}",
   "samplePromptsControlMode": "{{string}}",
   "subtitle": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "title": "{{string}}",
   "welcomeMessage": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWebExperience_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_CreateWebExperience_RequestSyntax) **   <a name="qbusiness-CreateWebExperience-request-uri-applicationId"></a>
The identifier of the Amazon Q Business web experience.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_CreateWebExperience_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [browserExtensionConfiguration](#API_CreateWebExperience_RequestSyntax) **   <a name="qbusiness-CreateWebExperience-request-browserExtensionConfiguration"></a>
The browser extension configuration for an Amazon Q Business web experience.
 For Amazon Q Business application using external OIDC-compliant identity providers (IdPs). The IdP administrator must add the browser extension sign-in redirect URLs to the IdP application. For more information, see [Configure external OIDC identity provider for your browser extensions.](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/browser-extensions.html).
Type: [BrowserExtensionConfiguration](API_BrowserExtensionConfiguration.md) object
Required: No

 ** [clientToken](#API_CreateWebExperience_RequestSyntax) **   <a name="qbusiness-CreateWebExperience-request-clientToken"></a>
A token you provide to identify a request to create an Amazon Q Business web experience.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [customizationConfiguration](#API_CreateWebExperience_RequestSyntax) **   <a name="qbusiness-CreateWebExperience-request-customizationConfiguration"></a>
Sets the custom logo, favicon, font, and color used in the Amazon Q web experience.
Type: [CustomizationConfiguration](API_CustomizationConfiguration.md) object
Required: No

 ** [identityProviderConfiguration](#API_CreateWebExperience_RequestSyntax) **   <a name="qbusiness-CreateWebExperience-request-identityProviderConfiguration"></a>
Information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
Type: [IdentityProviderConfiguration](API_IdentityProviderConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [origins](#API_CreateWebExperience_RequestSyntax) **   <a name="qbusiness-CreateWebExperience-request-origins"></a>
Sets the website domain origins that are allowed to embed the Amazon Q Business web experience. The *domain origin* refers to the base URL for accessing a website including the protocol (`http/https`), the domain name, and the port number (if specified).
You must only submit a *base URL* and not a full path. For example, `https://docs.aws.amazon.com`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(http://|https://)[a-zA-Z0-9-_.]+(?::[0-9]{1,5})?`
Required: No

 ** [roleArn](#API_CreateWebExperience_RequestSyntax) **   <a name="qbusiness-CreateWebExperience-request-roleArn"></a>
The Amazon Resource Name (ARN) of the service role attached to your web experience.
The `roleArn` parameter is required when your Amazon Q Business application is created with IAM Identity Center. It is not required for SAML-based applications.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** [samplePromptsControlMode](#API_CreateWebExperience_RequestSyntax) **   <a name="qbusiness-CreateWebExperience-request-samplePromptsControlMode"></a>
Determines whether sample prompts are enabled in the web experience for an end user.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [subtitle](#API_CreateWebExperience_RequestSyntax) **   <a name="qbusiness-CreateWebExperience-request-subtitle"></a>
A subtitle to personalize your Amazon Q Business web experience.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

 ** [tags](#API_CreateWebExperience_RequestSyntax) **   <a name="qbusiness-CreateWebExperience-request-tags"></a>
A list of key-value pairs that identify or categorize your Amazon Q Business web experience. You can also use tags to help control access to the web experience. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [title](#API_CreateWebExperience_RequestSyntax) **   <a name="qbusiness-CreateWebExperience-request-title"></a>
The title for your Amazon Q Business web experience.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

 ** [welcomeMessage](#API_CreateWebExperience_RequestSyntax) **   <a name="qbusiness-CreateWebExperience-request-welcomeMessage"></a>
The customized welcome message for end users of an Amazon Q Business web experience.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Required: No

## Response Syntax
<a name="API_CreateWebExperience_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "webExperienceArn": "string",
   "webExperienceId": "string"
}
```

## Response Elements
<a name="API_CreateWebExperience_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [webExperienceArn](#API_CreateWebExperience_ResponseSyntax) **   <a name="qbusiness-CreateWebExperience-response-webExperienceArn"></a>
 The Amazon Resource Name (ARN) of an Amazon Q Business web experience.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [webExperienceId](#API_CreateWebExperience_ResponseSyntax) **   <a name="qbusiness-CreateWebExperience-response-webExperienceId"></a>
The identifier of the Amazon Q Business web experience.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`

## Errors
<a name="API_CreateWebExperience_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** ConflictException **
You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.
 ** message **
The message describing a `ConflictException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
You have exceeded the set limits for your Amazon Q Business service.
 ** message **
The message describing a `ServiceQuotaExceededException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 402

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
<a name="API_CreateWebExperience_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/CreateWebExperience)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/CreateWebExperience)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/CreateWebExperience)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/CreateWebExperience)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/CreateWebExperience)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/CreateWebExperience)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/CreateWebExperience)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/CreateWebExperience)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/CreateWebExperience)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/CreateWebExperience)
