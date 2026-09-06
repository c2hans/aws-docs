---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribePostStreamActionSettingsResponse.html
---

# MedicalScribePostStreamActionSettingsResponse
<a name="API_MedicalScribePostStreamActionSettingsResponse"></a>

Response containing settings for post-stream actions

## Contents
<a name="API_MedicalScribePostStreamActionSettingsResponse_Contents"></a>

 ** clinicalNoteGenerationSettings **   <a name="connecthealth-Type-MedicalScribePostStreamActionSettingsResponse-clinicalNoteGenerationSettings"></a>
Settings for clinical note generation
Type: [ClinicalNoteGenerationSettingsResponse](API_ClinicalNoteGenerationSettingsResponse.md) object
Required: Yes

 ** outputS3Uri **   <a name="connecthealth-Type-MedicalScribePostStreamActionSettingsResponse-outputS3Uri"></a>

Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

## See Also
<a name="API_MedicalScribePostStreamActionSettingsResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalScribePostStreamActionSettingsResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalScribePostStreamActionSettingsResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalScribePostStreamActionSettingsResponse)
