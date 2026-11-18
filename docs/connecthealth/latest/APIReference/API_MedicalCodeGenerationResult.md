---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalCodeGenerationResult.html
---

# MedicalCodeGenerationResult
<a name="API_MedicalCodeGenerationResult"></a>

Results of medical code generation, including the medical codes and the medical coding job.

## Contents
<a name="API_MedicalCodeGenerationResult_Contents"></a>

 ** jobId **   <a name="connecthealth-Type-MedicalCodeGenerationResult-jobId"></a>
The identifier of the medical coding job that generated the medical codes. To submit feedback on the medical codes, use this value as the artifactSourceId, with the artifactType MEDICAL\_CODES, in SubmitFeedback.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: No

 ** medicalCodesResult **   <a name="connecthealth-Type-MedicalCodeGenerationResult-medicalCodesResult"></a>
Details about the generated medical codes. If the status is SKIPPED, medical codes weren't generated, for example because the clinical note wasn't generated or had no content.
Type: [ArtifactDetails](API_ArtifactDetails.md) object
Required: No

## See Also
<a name="API_MedicalCodeGenerationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalCodeGenerationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalCodeGenerationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalCodeGenerationResult)
