---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SipMediaApplicationAlexaSkillConfiguration.html
---

# SipMediaApplicationAlexaSkillConfiguration
<a name="API_voice-chime_SipMediaApplicationAlexaSkillConfiguration"></a>

The Alexa Skill configuration of a SIP media application.

**Important**
Due to changes made by the Amazon Alexa service, this data type is no longer available for use. For more information, refer to the [Alexa Smart Properties](https://developer.amazon.com/en-US/alexa/alexasmartproperties) page.

## Contents
<a name="API_voice-chime_SipMediaApplicationAlexaSkillConfiguration_Contents"></a>

 ** AlexaSkillIds **   <a name="chimesdk-Type-voice-chime_SipMediaApplicationAlexaSkillConfiguration-AlexaSkillIds"></a>
The ID of the Alexa Skill configuration.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Maximum length of 64.
Pattern: `amzn1\.application-oa2-client\.[0-9a-fA-F]{32}`
Required: Yes

 ** AlexaSkillStatus **   <a name="chimesdk-Type-voice-chime_SipMediaApplicationAlexaSkillConfiguration-AlexaSkillStatus"></a>
The status of the Alexa Skill configuration.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

## See Also
<a name="API_voice-chime_SipMediaApplicationAlexaSkillConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/SipMediaApplicationAlexaSkillConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/SipMediaApplicationAlexaSkillConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/SipMediaApplicationAlexaSkillConfiguration)
