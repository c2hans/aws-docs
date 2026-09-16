---
source_url: https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-voice-message.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Voice Message
<a name="v1-sms-voice-voice-message"></a>

The Amazon Pinpoint SMS and Voice API lets you create voice messages from a text script, and then deliver those messages to your customers over the phone.

## URI
<a name="v1-sms-voice-voice-message-url"></a>

`/v1/sms-voice/voice/message`

## HTTP methods
<a name="v1-sms-voice-voice-message-http-methods"></a>

### POST
<a name="v1-sms-voice-voice-messagepost"></a>

**Operation ID:** `SendVoiceMessage`

Creates a new voice message and sends it to a recipient's phone number.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | SendVoiceMessageResponse | An object that contains the Message ID of a voice message that was sent successfully. |
| 400 | BadRequestException | The destination number is blocked by AWS because it has a high risk of being used for fraudulent activities, or because of regulatory reasons. |
| 429 | TooManyRequestsException | You've issued too many requests to the resource. Wait a few minutes, and then try again. |
| 500 | InternalServiceErrorException | The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future. |

### OPTIONS
<a name="v1-sms-voice-voice-messageoptions"></a>

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="v1-sms-voice-voice-message-schemas"></a>

### Request bodies
<a name="v1-sms-voice-voice-message-request-examples"></a>

#### POST schema
<a name="v1-sms-voice-voice-message-request-body-post-example"></a>

```
{
  "Content": {
    "CallInstructionsMessage": {
      "Text": "string"
    },
    "PlainTextMessage": {
      "LanguageCode": "string",
      "Text": "string",
      "VoiceId": "string"
    },
    "SSMLMessage": {
      "LanguageCode": "string",
      "Text": "string",
      "VoiceId": "string"
    }
  },
  "OriginationPhoneNumber": "string",
  "ConfigurationSetName": "string",
  "DestinationPhoneNumber": "string",
  "CallerId": "string"
}
```

### Response bodies
<a name="v1-sms-voice-voice-message-response-examples"></a>

#### SendVoiceMessageResponse schema
<a name="v1-sms-voice-voice-message-response-body-sendvoicemessageresponse-example"></a>

```
{
  "MessageId": "string"
}
```

#### BadRequestException schema
<a name="v1-sms-voice-voice-message-response-body-badrequestexception-example"></a>

```
{
  "Message": "string"
}
```

#### TooManyRequestsException schema
<a name="v1-sms-voice-voice-message-response-body-toomanyrequestsexception-example"></a>

```
{
  "Message": "string"
}
```

#### InternalServiceErrorException schema
<a name="v1-sms-voice-voice-message-response-body-internalserviceerrorexception-example"></a>

```
{
  "Message": "string"
}
```

## Properties
<a name="v1-sms-voice-voice-message-properties"></a>

### BadRequestException
<a name="v1-sms-voice-voice-message-model-badrequestexception"></a>

The input that you provided to the API is invalid.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### CallInstructionsMessageType
<a name="v1-sms-voice-voice-message-model-callinstructionsmessagetype"></a>

An object that defines a message that contains text formatted using Amazon Pinpoint Call Instructions markup.

**Note**
The ability to send messages using Amazon Pinpoint Call Instructions is currently a pre-production feature. It isn't currently available to all customers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Text | string | True | The text, in Amazon Pinpoint Call Instructions markup, to deliver to the recipient. |

### InternalServiceErrorException
<a name="v1-sms-voice-voice-message-model-internalserviceerrorexception"></a>

This error occurs when there is an unexpected issue with the Amazon Pinpoint SMS and Voice API service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### PlainTextMessageType
<a name="v1-sms-voice-voice-message-model-plaintextmessagetype"></a>

An object that defines a message that contains unformatted text.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| LanguageCode | string | False | The language to use when delivering the message. For a complete list of supported languages, see the [Amazon Polly Developer Guide](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html). |
| Text | string | True | The plain (not SSML-formatted) text to deliver to the recipient. |
| VoiceId | string | False | The name of the voice that you want to use to deliver the message. For a complete list of supported voices, see the [Amazon Polly Developer Guide](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html). |

### SSMLMessageType
<a name="v1-sms-voice-voice-message-model-ssmlmessagetype"></a>

An object that defines a message that contains SSML-formatted text.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| LanguageCode | string | False | The language to use when delivering the message. For a complete list of supported languages, see the [Amazon Polly Developer Guide](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html). |
| Text | string | True | The SSML-formatted text to deliver to the recipient. |
| VoiceId | string | False | The name of the voice that you want to use to deliver the message. For a complete list of supported voices, see the [Amazon Polly Developer Guide](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html). |

### SendVoiceMessageRequest
<a name="v1-sms-voice-voice-message-model-sendvoicemessagerequest"></a>

A request to create and send a new voice message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| CallerId | string | False | The phone number that appears on recipients' devices when they receive the message. You can't specify a `CallerId` parameter if your account is in the sandbox.  |
| ConfigurationSetName | string | False | The name of the configuration set that you want to use to send the message. |
| Content | [VoiceMessageContent](#v1-sms-voice-voice-message-model-voicemessagecontent) | False | An object that contains a voice message and information about the recipient that you want to send it to. |
| DestinationPhoneNumber | string | True | The phone number that you want to send the voice message to.<br />Although it isn't required, we recommend that you specify the phone number in E.164 format to ensure prompt and accurate delivery. You can use the [Phone Number Validate](https://docs.aws.amazon.com/pinpoint/latest/apireference/phone-number-validate.html) resource in the Amazon Pinpoint API to convert phone numbers to E.164 format. |
| OriginationPhoneNumber | string | True | The long code to send the message from. This value should be one of the dedicated long codes that's assigned to your AWS account. Although it isn't required, we recommend that you specify the long code in E.164 format, for example \+12065550100, to ensure prompt and accurate delivery of your message.<br />This isn't necessarily the phone number that appears on recipients' devices when they receive the message, because you can specify the `CallerId` property in the request. |

### SendVoiceMessageResponse
<a name="v1-sms-voice-voice-message-model-sendvoicemessageresponse"></a>

An object that contains the Message ID of a voice message that was sent successfully.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| MessageId | string | False | A unique identifier for the voice message. |

### TooManyRequestsException
<a name="v1-sms-voice-voice-message-model-toomanyrequestsexception"></a>

This error occurs when there is an unexpected issue with the Amazon Pinpoint SMS and Voice API service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### VoiceMessageContent
<a name="v1-sms-voice-voice-message-model-voicemessagecontent"></a>

An object that contains the voice message that you want to send.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| CallInstructionsMessage | [CallInstructionsMessageType](#v1-sms-voice-voice-message-model-callinstructionsmessagetype) | False | An object that defines a message formatted using Amazon Pinpoint Call Instructions markup. |
| PlainTextMessage | [PlainTextMessageType](#v1-sms-voice-voice-message-model-plaintextmessagetype) | False | An object that defines a message that contains unformatted text. |
| SSMLMessage | [SSMLMessageType](#v1-sms-voice-voice-message-model-ssmlmessagetype) | False | An object that defines a message that contains SSML-formatted text. |

## See also
<a name="v1-sms-voice-voice-message-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### SendVoiceMessage
<a name="SendVoiceMessage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-sms-voice-2018-09-05/SendVoiceMessage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-sms-voice-2018-09-05/SendVoiceMessage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-sms-voice-2018-09-05/SendVoiceMessage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-sms-voice-2018-09-05/SendVoiceMessage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-sms-voice-2018-09-05/SendVoiceMessage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-sms-voice-2018-09-05/SendVoiceMessage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-sms-voice-2018-09-05/SendVoiceMessage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-sms-voice-2018-09-05/SendVoiceMessage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-sms-voice-2018-09-05/SendVoiceMessage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-sms-voice-2018-09-05/SendVoiceMessage)
