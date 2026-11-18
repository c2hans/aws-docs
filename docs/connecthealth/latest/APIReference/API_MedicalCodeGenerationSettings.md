---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalCodeGenerationSettings.html
---

# MedicalCodeGenerationSettings
<a name="API_MedicalCodeGenerationSettings"></a>

Settings for generating medical codes from the clinical note after the session ends. Medical code generation is in preview release and is subject to change. Medical code generation is available in the US East (N. Virginia) and US West (Oregon) AWS Regions.

## Contents
<a name="API_MedicalCodeGenerationSettings_Contents"></a>

 ** enabled **   <a name="connecthealth-Type-MedicalCodeGenerationSettings-enabled"></a>
Specifies whether to generate medical codes for the session. If you set this to true, the service generates medical codes from the clinical note after the session ends, using your permissions for medical coding, the output Amazon S3 location, and the AWS KMS key. You can set this to true only in a Region where medical code generation is available. To provide a medicalCodingContext, you must set this to true.
Type: Boolean
Required: Yes

## See Also
<a name="API_MedicalCodeGenerationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalCodeGenerationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalCodeGenerationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalCodeGenerationSettings)
