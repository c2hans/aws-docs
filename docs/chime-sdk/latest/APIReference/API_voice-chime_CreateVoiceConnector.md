---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnector.html
---

# CreateVoiceConnector
<a name="API_voice-chime_CreateVoiceConnector"></a>

Creates an Amazon Chime SDK Voice Connector. For more information about Voice Connectors, see [Managing Amazon Chime SDK Voice Connector groups](https://docs.aws.amazon.com/chime-sdk/latest/ag/voice-connector-groups.html) in the *Amazon Chime SDK Administrator Guide*.

## Request Syntax
<a name="API_voice-chime_CreateVoiceConnector_RequestSyntax"></a>

```
POST /voice-connectors HTTP/1.1
Content-type: application/json

{
   "AwsRegion": "{{string}}",
   "IntegrationType": "{{string}}",
   "Name": "{{string}}",
   "NetworkType": "{{string}}",
   "RequireEncryption": {{boolean}},
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_voice-chime_CreateVoiceConnector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_voice-chime_CreateVoiceConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AwsRegion](#API_voice-chime_CreateVoiceConnector_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceConnector-request-AwsRegion"></a>
The AWS Region in which the Amazon Chime SDK Voice Connector is created. Default value: `us-east-1` .
Type: String
Valid Values: `us-east-1 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | ap-northeast-2 | ap-northeast-1 | ap-southeast-1 | ap-southeast-2`
Required: No

 ** [IntegrationType](#API_voice-chime_CreateVoiceConnector_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceConnector-request-IntegrationType"></a>
The connectors for use with Connect Customer.
The following options are available:
+  `CONNECT_CALL_TRANSFER_CONNECTOR` - Enables enterprises to integrate Connect Customer with other voice systems to directly transfer voice calls and metadata without using the public telephone network. They can use Connect Customer telephony and Interactive Voice Response (IVR) with their existing voice systems to modernize the IVR experience of their existing contact center and their enterprise and branch voice systems. Additionally, enterprises migrating their contact center to Connect Customer can start with Connect telephony and IVR for immediate modernization ahead of agent migration.
**Note**
This integration is a gated feature. Please reach out to your account team to discuss this feature with a Connect Specialist.
+  `CONNECT_ANALYTICS_CONNECTOR` - Enables enterprises to integrate Connect Customer with other voice systems for real-time and post-call analytics. They can use Connect Customer Contact Lens with their existing voice systems to provides call recordings, conversational analytics (including contact transcript, sensitive data redaction, content categorization, theme detection, sentiment analysis, real-time alerts, and post-contact summary), and agent performance evaluations (including evaluation forms, automated evaluation, supervisor review) with a rich user experience to display, search and filter customer interactions, and programmatic access to data streams and the data lake. Additionally, enterprises migrating their contact center to Connect Customer can start with Contact Lens analytics and performance insights ahead of agent migration.
Type: String
Valid Values: `CONNECT_CALL_TRANSFER_CONNECTOR | CONNECT_ANALYTICS_CONNECTOR`
Required: No

 ** [Name](#API_voice-chime_CreateVoiceConnector_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceConnector-request-Name"></a>
The name of the Voice Connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.-]+`
Required: Yes

 ** [NetworkType](#API_voice-chime_CreateVoiceConnector_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceConnector-request-NetworkType"></a>
The type of network for the Voice Connector.
Type: String
Valid Values: `IPV4_ONLY | DUAL_STACK`
Required: No

 ** [RequireEncryption](#API_voice-chime_CreateVoiceConnector_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceConnector-request-RequireEncryption"></a>
Enables or disables encryption for the Voice Connector.
Type: Boolean
Required: Yes

 ** [Tags](#API_voice-chime_CreateVoiceConnector_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceConnector-request-Tags"></a>
The tags assigned to the Voice Connector.
Type: Array of [Tag](API_voice-chime_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_voice-chime_CreateVoiceConnector_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_voice-chime_CreateVoiceConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [VoiceConnector](#API_voice-chime_CreateVoiceConnector_ResponseSyntax) **   <a name="chimesdk-voice-chime_CreateVoiceConnector-response-VoiceConnector"></a>
The details of the Voice Connector.
Type: [VoiceConnector](API_voice-chime_VoiceConnector.md) object

## Errors
<a name="API_voice-chime_CreateVoiceConnector_Errors"></a>

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
<a name="API_voice-chime_CreateVoiceConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/CreateVoiceConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/CreateVoiceConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/CreateVoiceConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/CreateVoiceConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/CreateVoiceConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/CreateVoiceConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/CreateVoiceConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/CreateVoiceConnector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/CreateVoiceConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/CreateVoiceConnector)
