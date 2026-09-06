---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ConfigurationSetInformation.html
---

# ConfigurationSetInformation
<a name="API_ConfigurationSetInformation"></a>

Information related to a given configuration set in your AWS account.

## Contents
<a name="API_ConfigurationSetInformation_Contents"></a>

 ** ConfigurationSetArn **   <a name="pinpoint-Type-ConfigurationSetInformation-ConfigurationSetArn"></a>
The Resource Name (ARN) of the ConfigurationSet.
Type: String
Required: Yes

 ** ConfigurationSetName **   <a name="pinpoint-Type-ConfigurationSetInformation-ConfigurationSetName"></a>
The name of the ConfigurationSet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** CreatedTimestamp **   <a name="pinpoint-Type-ConfigurationSetInformation-CreatedTimestamp"></a>
The time when the ConfigurationSet was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: Yes

 ** EventDestinations **   <a name="pinpoint-Type-ConfigurationSetInformation-EventDestinations"></a>
An array of EventDestination objects that describe any events to log and where to log them.
Type: Array of [EventDestination](API_EventDestination.md) objects
Required: Yes

 ** DefaultMessageFeedbackEnabled **   <a name="pinpoint-Type-ConfigurationSetInformation-DefaultMessageFeedbackEnabled"></a>
True if message feedback is enabled.
Type: Boolean
Required: No

 ** DefaultMessageType **   <a name="pinpoint-Type-ConfigurationSetInformation-DefaultMessageType"></a>
The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.
Type: String
Valid Values: `TRANSACTIONAL | PROMOTIONAL`
Required: No

 ** DefaultSenderId **   <a name="pinpoint-Type-ConfigurationSetInformation-DefaultSenderId"></a>
The default sender ID used by the ConfigurationSet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** ProtectConfigurationId **   <a name="pinpoint-Type-ConfigurationSetInformation-ProtectConfigurationId"></a>
The unique identifier for the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

## See Also
<a name="API_ConfigurationSetInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/ConfigurationSetInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/ConfigurationSetInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/ConfigurationSetInformation)
