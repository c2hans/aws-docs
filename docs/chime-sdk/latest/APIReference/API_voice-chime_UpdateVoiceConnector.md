---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnector.html
---

# UpdateVoiceConnector
<a name="API_voice-chime_UpdateVoiceConnector"></a>

Updates the details for the specified Amazon Chime SDK Voice Connector.

## Request Syntax
<a name="API_voice-chime_UpdateVoiceConnector_RequestSyntax"></a>

```
PUT /voice-connectors/{{voiceConnectorId}} HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}",
   "RequireEncryption": {{boolean}}
}
```

## URI Request Parameters
<a name="API_voice-chime_UpdateVoiceConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [voiceConnectorId](#API_voice-chime_UpdateVoiceConnector_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateVoiceConnector-request-uri-VoiceConnectorId"></a>
The Voice Connector ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_UpdateVoiceConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_voice-chime_UpdateVoiceConnector_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateVoiceConnector-request-Name"></a>
The name of the Voice Connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.-]+`
Required: Yes

 ** [RequireEncryption](#API_voice-chime_UpdateVoiceConnector_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateVoiceConnector-request-RequireEncryption"></a>
When enabled, requires encryption for the Voice Connector.
Type: Boolean
Required: Yes

## Response Syntax
<a name="API_voice-chime_UpdateVoiceConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "VoiceConnector": {
      "AwsRegion": "string",
      "CreatedTimestamp": "string",
      "IntegrationType": "string",
      "Name": "string",
      "NetworkType": "string",
      "OutboundHostName": "string",
      "RequireEncryption": boolean,
      "UpdatedTimestamp": "string",
      "VoiceConnectorArn": "string",
      "VoiceConnectorId": "string"
   }
}
```

## Response Elements
<a name="API_voice-chime_UpdateVoiceConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VoiceConnector](#API_voice-chime_UpdateVoiceConnector_ResponseSyntax) **   <a name="chimesdk-voice-chime_UpdateVoiceConnector-response-VoiceConnector"></a>
The updated Voice Connector details.
Type: [VoiceConnector](API_voice-chime_VoiceConnector.md) object

## Errors
<a name="API_voice-chime_UpdateVoiceConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
The requested resource couldn't be found.
HTTP Status Code: 404

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
<a name="API_voice-chime_UpdateVoiceConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/UpdateVoiceConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/UpdateVoiceConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/UpdateVoiceConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/UpdateVoiceConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/UpdateVoiceConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/UpdateVoiceConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/UpdateVoiceConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/UpdateVoiceConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/UpdateVoiceConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/UpdateVoiceConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
