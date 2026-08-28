---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalScribePostStreamActionSettings.html
---

# MedicalScribePostStreamActionSettings
<a name="API_MedicalScribePostStreamActionSettings"></a>

Settings for actions to perform after the audio stream ends

## Contents
<a name="API_MedicalScribePostStreamActionSettings_Contents"></a>

 ** clinicalNoteGenerationSettings **   <a name="connecthealth-Type-MedicalScribePostStreamActionSettings-clinicalNoteGenerationSettings"></a>
Settings for clinical note generation
Type: [ClinicalNoteGenerationSettings](API_ClinicalNoteGenerationSettings.md) object
Required: Yes

 ** outputS3Uri **   <a name="connecthealth-Type-MedicalScribePostStreamActionSettings-outputS3Uri"></a>

Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

## See Also
<a name="API_MedicalScribePostStreamActionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalScribePostStreamActionSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalScribePostStreamActionSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalScribePostStreamActionSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
