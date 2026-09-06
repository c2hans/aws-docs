---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetChatControlsConfiguration.html
---

# GetChatControlsConfiguration
<a name="API_GetChatControlsConfiguration"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Gets information about chat controls configured for an existing Amazon Q Business application.

## Request Syntax
<a name="API_GetChatControlsConfiguration_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/chatcontrols?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetChatControlsConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetChatControlsConfiguration_RequestSyntax) **   <a name="qbusiness-GetChatControlsConfiguration-request-uri-applicationId"></a>
The identifier of the application for which the chat controls are configured.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [maxResults](#API_GetChatControlsConfiguration_RequestSyntax) **   <a name="qbusiness-GetChatControlsConfiguration-request-uri-maxResults"></a>
The maximum number of configured chat controls to return.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_GetChatControlsConfiguration_RequestSyntax) **   <a name="qbusiness-GetChatControlsConfiguration-request-uri-nextToken"></a>
If the `maxResults` response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business chat controls configured.
Length Constraints: Minimum length of 1. Maximum length of 800.

## Request Body
<a name="API_GetChatControlsConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetChatControlsConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "blockedPhrases": {
      "blockedPhrases": [ "string" ],
      "systemMessageOverride": "string"
   },
   "creatorModeConfiguration": {
      "creatorModeControl": "string"
   },
   "hallucinationReductionConfiguration": {
      "hallucinationReductionControl": "string"
   },
   "nextToken": "string",
   "orchestrationConfiguration": {
      "control": "string"
   },
   "responseScope": "string",
   "topicConfigurations": [
      {
         "description": "string",
         "exampleChatMessages": [ "string" ],
         "name": "string",
         "rules": [
            {
               "excludedUsersAndGroups": {
                  "userGroups": [ "string" ],
                  "userIds": [ "string" ]
               },
               "includedUsersAndGroups": {
                  "userGroups": [ "string" ],
                  "userIds": [ "string" ]
               },
               "ruleConfiguration": { ... },
               "ruleType": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetChatControlsConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [blockedPhrases](#API_GetChatControlsConfiguration_ResponseSyntax) **   <a name="qbusiness-GetChatControlsConfiguration-response-blockedPhrases"></a>
The phrases blocked from chat by your chat control configuration.
Type: [BlockedPhrasesConfiguration](API_BlockedPhrasesConfiguration.md) object

 ** [creatorModeConfiguration](#API_GetChatControlsConfiguration_ResponseSyntax) **   <a name="qbusiness-GetChatControlsConfiguration-response-creatorModeConfiguration"></a>
The configuration details for `CREATOR_MODE`.
Type: [AppliedCreatorModeConfiguration](API_AppliedCreatorModeConfiguration.md) object

 ** [hallucinationReductionConfiguration](#API_GetChatControlsConfiguration_ResponseSyntax) **   <a name="qbusiness-GetChatControlsConfiguration-response-hallucinationReductionConfiguration"></a>
 The hallucination reduction settings for your application.
Type: [HallucinationReductionConfiguration](API_HallucinationReductionConfiguration.md) object

 ** [nextToken](#API_GetChatControlsConfiguration_ResponseSyntax) **   <a name="qbusiness-GetChatControlsConfiguration-response-nextToken"></a>
If the `maxResults` response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business chat controls configured.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.

 ** [orchestrationConfiguration](#API_GetChatControlsConfiguration_ResponseSyntax) **   <a name="qbusiness-GetChatControlsConfiguration-response-orchestrationConfiguration"></a>
 The chat response orchestration settings for your application.
Chat orchestration is optimized to work for English language content. For more details on language support in Amazon Q Business, see [Supported languages](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-languages.html).
Type: [AppliedOrchestrationConfiguration](API_AppliedOrchestrationConfiguration.md) object

 ** [responseScope](#API_GetChatControlsConfiguration_ResponseSyntax) **   <a name="qbusiness-GetChatControlsConfiguration-response-responseScope"></a>
The response scope configured for a Amazon Q Business application. This determines whether your application uses its retrieval augmented generation (RAG) system to generate answers only from your enterprise data, or also uses the large language models (LLM) knowledge to respons to end user questions in chat.
Type: String
Valid Values: `ENTERPRISE_CONTENT_ONLY | EXTENDED_KNOWLEDGE_ENABLED`

 ** [topicConfigurations](#API_GetChatControlsConfiguration_ResponseSyntax) **   <a name="qbusiness-GetChatControlsConfiguration-response-topicConfigurations"></a>
The topic specific controls configured for a Amazon Q Business application.
Type: Array of [TopicConfiguration](API_TopicConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

## Errors
<a name="API_GetChatControlsConfiguration_Errors"></a>

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
<a name="API_GetChatControlsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/GetChatControlsConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/GetChatControlsConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/GetChatControlsConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/GetChatControlsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/GetChatControlsConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/GetChatControlsConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/GetChatControlsConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/GetChatControlsConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/GetChatControlsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/GetChatControlsConfiguration)
