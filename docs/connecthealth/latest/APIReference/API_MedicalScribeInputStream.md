---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribeInputStream.html
---

# MedicalScribeInputStream
<a name="API_MedicalScribeInputStream"></a>

Input stream for Medical Scribe containing audio and configuration events

## Contents
<a name="API_MedicalScribeInputStream_Contents"></a>

 ** audioEvent **   <a name="connecthealth-Type-MedicalScribeInputStream-audioEvent"></a>

Type: [MedicalScribeAudioEvent](API_MedicalScribeAudioEvent.md) object
Required: No

 ** binaryAudioEvent **   <a name="connecthealth-Type-MedicalScribeInputStream-binaryAudioEvent"></a>
An event containing raw binary audio data for the Medical Scribe stream. The audio is sent as a raw binary payload rather than as a base64-encoded value.
Type: [MedicalScribeBinaryAudioEvent](API_MedicalScribeBinaryAudioEvent.md) object
Required: No

 ** configurationEvent **   <a name="connecthealth-Type-MedicalScribeInputStream-configurationEvent"></a>

Type: [MedicalScribeConfigurationEvent](API_MedicalScribeConfigurationEvent.md) object
Required: No

 ** sessionControlEvent **   <a name="connecthealth-Type-MedicalScribeInputStream-sessionControlEvent"></a>

Type: [MedicalScribeSessionControlEvent](API_MedicalScribeSessionControlEvent.md) object
Required: No

## See Also
<a name="API_MedicalScribeInputStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalScribeInputStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalScribeInputStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalScribeInputStream)
