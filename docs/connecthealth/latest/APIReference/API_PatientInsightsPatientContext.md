---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_PatientInsightsPatientContext.html
---

# PatientInsightsPatientContext
<a name="API_PatientInsightsPatientContext"></a>

Details for a patient

## Contents
<a name="API_PatientInsightsPatientContext_Contents"></a>

 ** patientId **   <a name="connecthealth-Type-PatientInsightsPatientContext-patientId"></a>
Unique identifier of the patient
Type: String
Pattern: `.*[\s\S]*\S[\s\S]*.*`
Required: Yes

 ** dateOfBirth **   <a name="connecthealth-Type-PatientInsightsPatientContext-dateOfBirth"></a>
Date of birth of the patient.
Type: String
Pattern: `\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])`
Required: No

 ** pronouns **   <a name="connecthealth-Type-PatientInsightsPatientContext-pronouns"></a>
Pronouns preferred by the patient.
Type: String
Valid Values: `HE_HIM | SHE_HER | THEY_THEM`
Required: No

## See Also
<a name="API_PatientInsightsPatientContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/PatientInsightsPatientContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/PatientInsightsPatientContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/PatientInsightsPatientContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
