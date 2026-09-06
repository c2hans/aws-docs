---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateChatResponseConfiguration.html
---

# CreateChatResponseConfiguration
<a name="API_CreateChatResponseConfiguration"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Creates a new chat response configuration for an Amazon Q Business application. This operation establishes a set of parameters that define how the system generates and formats responses to user queries in chat interactions.

## Request Syntax
<a name="API_CreateChatResponseConfiguration_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/chatresponseconfigurations HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "displayName": "{{string}}",
   "responseConfigurations": {
      "{{string}}" : {
         "instructionCollection": {
            "customInstructions": "{{string}}",
            "examples": "{{string}}",
            "identity": "{{string}}",
            "outputStyle": "{{string}}",
            "perspective": "{{string}}",
            "responseLength": "{{string}}",
            "targetAudience": "{{string}}",
            "tone": "{{string}}"
         }
      }
   },
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateChatResponseConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_CreateChatResponseConfiguration_RequestSyntax) **   <a name="qbusiness-CreateChatResponseConfiguration-request-uri-applicationId"></a>
The unique identifier of the Amazon Q Business application for which to create the new chat response configuration.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_CreateChatResponseConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateChatResponseConfiguration_RequestSyntax) **   <a name="qbusiness-CreateChatResponseConfiguration-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request. This helps prevent the same configuration from being created multiple times if retries occur.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [displayName](#API_CreateChatResponseConfiguration_RequestSyntax) **   <a name="qbusiness-CreateChatResponseConfiguration-request-displayName"></a>
A human-readable name for the new chat response configuration, making it easier to identify and manage among multiple configurations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [responseConfigurations](#API_CreateChatResponseConfiguration_RequestSyntax) **   <a name="qbusiness-CreateChatResponseConfiguration-request-responseConfigurations"></a>
A collection of response configuration settings that define how Amazon Q Business will generate and format responses to user queries in chat interactions.
Type: String to [ResponseConfiguration](API_ResponseConfiguration.md) object map
Map Entries: Maximum number of 1 item.
Valid Keys: `ALL`
Required: Yes

 ** [tags](#API_CreateChatResponseConfiguration_RequestSyntax) **   <a name="qbusiness-CreateChatResponseConfiguration-request-tags"></a>
A list of key-value pairs to apply as tags to the new chat response configuration, enabling categorization and management of resources across AWS services.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateChatResponseConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "chatResponseConfigurationArn": "string",
   "chatResponseConfigurationId": "string"
}
```

## Response Elements
<a name="API_CreateChatResponseConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [chatResponseConfigurationArn](#API_CreateChatResponseConfiguration_ResponseSyntax) **   <a name="qbusiness-CreateChatResponseConfiguration-response-chatResponseConfigurationArn"></a>
The Amazon Resource Name (ARN) of the newly created chat response configuration, which uniquely identifies the resource across all AWS services.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [chatResponseConfigurationId](#API_CreateChatResponseConfiguration_ResponseSyntax) **   <a name="qbusiness-CreateChatResponseConfiguration-response-chatResponseConfigurationId"></a>
The unique identifier assigned to a newly created chat response configuration, used for subsequent operations on this resource.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

## Errors
<a name="API_CreateChatResponseConfiguration_Errors"></a>

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
<a name="API_CreateChatResponseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/CreateChatResponseConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/CreateChatResponseConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/CreateChatResponseConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/CreateChatResponseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/CreateChatResponseConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/CreateChatResponseConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/CreateChatResponseConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/CreateChatResponseConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/CreateChatResponseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/CreateChatResponseConfiguration)
