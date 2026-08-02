---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeConfigurationEvent.html
---

# MedicalScribeConfigurationEvent
<a name="API_MedicalScribeConfigurationEvent"></a>

An event containing configuration for the Medical Scribe session

## Contents
<a name="API_MedicalScribeConfigurationEvent_Contents"></a>

 ** postStreamActionSettings **   <a name="connecthealth-Type-MedicalScribeConfigurationEvent-postStreamActionSettings"></a>
Settings for actions to perform after the stream ends
Type: [MedicalScribePostStreamActionSettings](API_MedicalScribePostStreamActionSettings.md) object
Required: Yes

 ** channelDefinitions **   <a name="connecthealth-Type-MedicalScribeConfigurationEvent-channelDefinitions"></a>
Channel definitions for the audio stream
Type: Array of [MedicalScribeChannelDefinition](API_MedicalScribeChannelDefinition.md) objects
Array Members: Fixed number of 2 items.
Required: No

 ** encounterContext **   <a name="connecthealth-Type-MedicalScribeConfigurationEvent-encounterContext"></a>
Context information about the clinical encounter
Type: [EncounterContext](API_EncounterContext.md) object
Required: No

## See Also
<a name="API_MedicalScribeConfigurationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalScribeConfigurationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalScribeConfigurationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalScribeConfigurationEvent)
