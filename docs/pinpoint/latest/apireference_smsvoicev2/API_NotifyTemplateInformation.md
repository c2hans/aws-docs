---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_NotifyTemplateInformation.html
---

# NotifyTemplateInformation
<a name="API_NotifyTemplateInformation"></a>

The information for a system-managed notify template in an AWS account.

## Contents
<a name="API_NotifyTemplateInformation_Contents"></a>

 ** Channels **   <a name="pinpoint-Type-NotifyTemplateInformation-Channels"></a>
The channels for the template. Supported values are `SMS` and `VOICE`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SMS | VOICE | MMS | RCS`
Required: Yes

 ** CreatedTimestamp **   <a name="pinpoint-Type-NotifyTemplateInformation-CreatedTimestamp"></a>
The time when the notify template was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: Yes

 ** TemplateId **   <a name="pinpoint-Type-NotifyTemplateInformation-TemplateId"></a>
The unique identifier for the template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `([A-Za-z0-9_-]*|UNSET_DEFAULT_TEMPLATE)`
Required: Yes

 ** TemplateType **   <a name="pinpoint-Type-NotifyTemplateInformation-TemplateType"></a>
The type of the template.
Type: String
Valid Values: `OTP_VERIFICATION`
Required: Yes

 ** Version **   <a name="pinpoint-Type-NotifyTemplateInformation-Version"></a>
The version of the template.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** Content **   <a name="pinpoint-Type-NotifyTemplateInformation-Content"></a>
The content of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** LanguageCode **   <a name="pinpoint-Type-NotifyTemplateInformation-LanguageCode"></a>
The language code for the template.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Pattern: `[a-z]{2}(-[A-Z]{2})?`
Required: No

 ** Status **   <a name="pinpoint-Type-NotifyTemplateInformation-Status"></a>
The current status of the template.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** SupportedCountries **   <a name="pinpoint-Type-NotifyTemplateInformation-SupportedCountries"></a>
An array of supported country codes for the template.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: No

 ** SupportedVoiceIds **   <a name="pinpoint-Type-NotifyTemplateInformation-SupportedVoiceIds"></a>
An array of supported voice IDs for voice templates.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 60 items.
Valid Values: `AMY | ASTRID | BIANCA | BRIAN | CAMILA | CARLA | CARMEN | CELINE | CHANTAL | CONCHITA | CRISTIANO | DORA | EMMA | ENRIQUE | EWA | FILIZ | GERAINT | GIORGIO | GWYNETH | HANS | INES | IVY | JACEK | JAN | JOANNA | JOEY | JUSTIN | KARL | KENDRA | KIMBERLY | LEA | LIV | LOTTE | LUCIA | LUPE | MADS | MAJA | MARLENE | MATHIEU | MATTHEW | MAXIM | MIA | MIGUEL | MIZUKI | NAJA | NICOLE | PENELOPE | RAVEENA | RICARDO | RUBEN | RUSSELL | SALLI | SEOYEON | TAKUMI | TATYANA | VICKI | VITORIA | ZEINA | ZHIYU`
Required: No

 ** TierAccess **   <a name="pinpoint-Type-NotifyTemplateInformation-TierAccess"></a>
The tier access level for the template.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `BASIC | ADVANCED`
Required: No

 ** Variables **   <a name="pinpoint-Type-NotifyTemplateInformation-Variables"></a>
An array of template variable metadata for the template.
Type: String to [TemplateVariableMetadata](API_TemplateVariableMetadata.md) object map
Required: No

## See Also
<a name="API_NotifyTemplateInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/NotifyTemplateInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/NotifyTemplateInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/NotifyTemplateInformation)
