---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnectorGroup.html
---

# CreateVoiceConnectorGroup
<a name="API_voice-chime_CreateVoiceConnectorGroup"></a>

Creates an Amazon Chime SDK Voice Connector group under the administrator's AWS account. You can associate Amazon Chime SDK Voice Connectors with the Voice Connector group by including `VoiceConnectorItems` in the request.

You can include Voice Connectors from different AWS Regions in your group. This creates a fault tolerant mechanism for fallback in case of availability events.

## Request Syntax
<a name="API_voice-chime_CreateVoiceConnectorGroup_RequestSyntax"></a>

```
POST /voice-connector-groups HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}",
   "VoiceConnectorItems": [
      {
         "Priority": {{number}},
         "VoiceConnectorId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_voice-chime_CreateVoiceConnectorGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_voice-chime_CreateVoiceConnectorGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_voice-chime_CreateVoiceConnectorGroup_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceConnectorGroup-request-Name"></a>
The name of the Voice Connector group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.-]+`
Required: Yes

 ** [VoiceConnectorItems](#API_voice-chime_CreateVoiceConnectorGroup_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceConnectorGroup-request-VoiceConnectorItems"></a>
Lists the Voice Connectors that inbound calls are routed to.
Type: Array of [VoiceConnectorItem](API_voice-chime_VoiceConnectorItem.md) objects
Required: No

## Response Syntax
<a name="API_voice-chime_CreateVoiceConnectorGroup_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "VoiceConnectorGroup": {
      "CreatedTimestamp": "string",
      "Name": "string",
      "UpdatedTimestamp": "string",
      "VoiceConnectorGroupArn": "string",
      "VoiceConnectorGroupId": "string",
      "VoiceConnectorItems": [
         {
            "Priority": number,
            "VoiceConnectorId": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_voice-chime_CreateVoiceConnectorGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [VoiceConnectorGroup](#API_voice-chime_CreateVoiceConnectorGroup_ResponseSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceConnectorGroup-response-VoiceConnectorGroup"></a>
The details of the Voice Connector group.
Type: [VoiceConnectorGroup](API_voice-chime_VoiceConnectorGroup.md) object

## Errors
<a name="API_voice-chime_CreateVoiceConnectorGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** AccessDeniedException **
You don't have the permissions needed to run this action.
HTTP Status Code: 403

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
HTTP Status Code: 400

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The number of customer requests exceeds the request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client isn't authorized to request a resource.
HTTP Status Code: 401

## See Also
<a name="API_voice-chime_CreateVoiceConnectorGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/CreateVoiceConnectorGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/CreateVoiceConnectorGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/CreateVoiceConnectorGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/CreateVoiceConnectorGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/CreateVoiceConnectorGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/CreateVoiceConnectorGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/CreateVoiceConnectorGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/CreateVoiceConnectorGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/CreateVoiceConnectorGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/CreateVoiceConnectorGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
