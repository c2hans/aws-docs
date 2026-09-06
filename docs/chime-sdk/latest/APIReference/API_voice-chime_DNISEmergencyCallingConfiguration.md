---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DNISEmergencyCallingConfiguration.html
---

# DNISEmergencyCallingConfiguration
<a name="API_voice-chime_DNISEmergencyCallingConfiguration"></a>

The Dialed Number Identification Service (DNIS) emergency calling configuration details associated with an Amazon Chime SDK Voice Connector's emergency calling configuration.

## Contents
<a name="API_voice-chime_DNISEmergencyCallingConfiguration_Contents"></a>

 ** CallingCountry **   <a name="chimesdk-Type-voice-chime_DNISEmergencyCallingConfiguration-CallingCountry"></a>
The country from which emergency calls are allowed, in ISO 3166-1 alpha-2 format.
Type: String
Pattern: `[A-Z]{2}`
Required: Yes

 ** EmergencyPhoneNumber **   <a name="chimesdk-Type-voice-chime_DNISEmergencyCallingConfiguration-EmergencyPhoneNumber"></a>
The DNIS phone number that you route emergency calls to, in E.164 format.
Type: String
Pattern: `^\+?[1-9]\d{1,14}$`
Required: Yes

 ** TestPhoneNumber **   <a name="chimesdk-Type-voice-chime_DNISEmergencyCallingConfiguration-TestPhoneNumber"></a>
The DNIS phone number for routing test emergency calls to, in E.164 format.
Type: String
Pattern: `^\+?[1-9]\d{1,14}$`
Required: No

## See Also
<a name="API_voice-chime_DNISEmergencyCallingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/DNISEmergencyCallingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/DNISEmergencyCallingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/DNISEmergencyCallingConfiguration)
