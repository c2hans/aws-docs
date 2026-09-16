---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetChatResponseConfiguration.html
---

# GetChatResponseConfiguration
<a name="API_GetChatResponseConfiguration"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Retrieves detailed information about a specific chat response configuration from an Amazon Q Business application. This operation returns the complete configuration settings and metadata.

## Request Syntax
<a name="API_GetChatResponseConfiguration_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/chatresponseconfigurations/{{chatResponseConfigurationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetChatResponseConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetChatResponseConfiguration_RequestSyntax) **   <a name="qbusiness-GetChatResponseConfiguration-request-uri-applicationId"></a>
The unique identifier of the Amazon Q Business application containing the chat response configuration to retrieve.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [chatResponseConfigurationId](#API_GetChatResponseConfiguration_RequestSyntax) **   <a name="qbusiness-GetChatResponseConfiguration-request-uri-chatResponseConfigurationId"></a>
The unique identifier of the chat response configuration to retrieve from the specified application.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_GetChatResponseConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetChatResponseConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "chatResponseConfigurationArn": "string",
   "chatResponseConfigurationId": "string",
   "createdAt": number,
   "displayName": "string",
   "inUseConfiguration": {
      "error": {
         "errorCode": "string",
         "errorMessage": "string"
      },
      "responseConfigurations": {
         "string" : {
            "instructionCollection": {
               "customInstructions": "string",
               "examples": "string",
               "identity": "string",
               "outputStyle": "string",
               "perspective": "string",
               "responseLength": "string",
               "targetAudience": "string",
               "tone": "string"
            }
         }
      },
      "responseConfigurationSummary": "string",
      "status": "string",
      "updatedAt": number
   },
   "lastUpdateConfiguration": {
      "error": {
         "errorCode": "string",
         "errorMessage": "string"
      },
      "responseConfigurations": {
         "string" : {
            "instructionCollection": {
               "customInstructions": "string",
               "examples": "string",
               "identity": "string",
               "outputStyle": "string",
               "perspective": "string",
               "responseLength": "string",
               "targetAudience": "string",
               "tone": "string"
            }
         }
      },
      "responseConfigurationSummary": "string",
      "status": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_GetChatResponseConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [chatResponseConfigurationArn](#API_GetChatResponseConfiguration_ResponseSyntax) **   <a name="qbusiness-GetChatResponseConfiguration-response-chatResponseConfigurationArn"></a>
The Amazon Resource Name (ARN) of the retrieved chat response configuration, which uniquely identifies the resource across all AWS services.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [chatResponseConfigurationId](#API_GetChatResponseConfiguration_ResponseSyntax) **   <a name="qbusiness-GetChatResponseConfiguration-response-chatResponseConfigurationId"></a>
The unique identifier of the retrieved chat response configuration.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [createdAt](#API_GetChatResponseConfiguration_ResponseSyntax) **   <a name="qbusiness-GetChatResponseConfiguration-response-createdAt"></a>
The timestamp indicating when the chat response configuration was initially created.
Type: Timestamp

 ** [displayName](#API_GetChatResponseConfiguration_ResponseSyntax) **   <a name="qbusiness-GetChatResponseConfiguration-response-displayName"></a>
The human-readable name of the retrieved chat response configuration, making it easier to identify among multiple configurations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [inUseConfiguration](#API_GetChatResponseConfiguration_ResponseSyntax) **   <a name="qbusiness-GetChatResponseConfiguration-response-inUseConfiguration"></a>
The currently active configuration settings that are being used to generate responses in the Amazon Q Business application.
Type: [ChatResponseConfigurationDetail](API_ChatResponseConfigurationDetail.md) object

 ** [lastUpdateConfiguration](#API_GetChatResponseConfiguration_ResponseSyntax) **   <a name="qbusiness-GetChatResponseConfiguration-response-lastUpdateConfiguration"></a>
Information about the most recent update to the configuration, including timestamp and modification details.
Type: [ChatResponseConfigurationDetail](API_ChatResponseConfigurationDetail.md) object

## Errors
<a name="API_GetChatResponseConfiguration_Errors"></a>

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
<a name="API_GetChatResponseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/GetChatResponseConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/GetChatResponseConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/GetChatResponseConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/GetChatResponseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/GetChatResponseConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/GetChatResponseConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/GetChatResponseConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/GetChatResponseConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/GetChatResponseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/GetChatResponseConfiguration)
