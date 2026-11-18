---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalCodesPatientContext.html
---

# MedicalCodesPatientContext
<a name="API_MedicalCodesPatientContext"></a>

Patient context for a medical coding job. All fields are optional.

## Contents
<a name="API_MedicalCodesPatientContext_Contents"></a>

 ** dateOfBirth **   <a name="connecthealth-Type-MedicalCodesPatientContext-dateOfBirth"></a>
The date of birth of the patient, in YYYY-MM-DD format. The date can't be after the current date in UTC.
Type: String
Pattern: `\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])`
Required: No

 ** insurance **   <a name="connecthealth-Type-MedicalCodesPatientContext-insurance"></a>
The insurance of the patient.
Type: String
Pattern: `.*[\s\S]*\S[\s\S]*.*`
Required: No

 ** sex **   <a name="connecthealth-Type-MedicalCodesPatientContext-sex"></a>
The sex of the patient.
Type: String
Valid Values: `MALE | FEMALE | NON_BINARY | UNKNOWN`
Required: No

 ** status **   <a name="connecthealth-Type-MedicalCodesPatientContext-status"></a>
The status of the patient, either new or established.
Type: String
Valid Values: `NEW | ESTABLISHED`
Required: No

## See Also
<a name="API_MedicalCodesPatientContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalCodesPatientContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalCodesPatientContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalCodesPatientContext)
