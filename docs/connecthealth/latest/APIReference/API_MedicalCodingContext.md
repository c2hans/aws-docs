---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalCodingContext.html
---

# MedicalCodingContext
<a name="API_MedicalCodingContext"></a>

Patient and encounter context for medical code generation. Providing this information can improve the accuracy of the medical codes. To provide it, you must also set enabled to true in medicalCodeGenerationSettings. All fields are optional. The service generates medical codes without any field that you leave out.

## Contents
<a name="API_MedicalCodingContext_Contents"></a>

 ** afterHours **   <a name="connecthealth-Type-MedicalCodingContext-afterHours"></a>
Specifies whether the encounter took place outside regular business hours.
Type: Boolean
Required: No

 ** dateOfBirth **   <a name="connecthealth-Type-MedicalCodingContext-dateOfBirth"></a>
The date of birth of the patient, in YYYY-MM-DD format. The date can't be after the current date in UTC.
Type: String
Pattern: `\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])`
Required: No

 ** encounterDate **   <a name="connecthealth-Type-MedicalCodingContext-encounterDate"></a>
The date of the encounter, in YYYY-MM-DD format. The date can't be more than one day after the current date in UTC.
Type: String
Pattern: `\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])`
Required: No

 ** encounterReason **   <a name="connecthealth-Type-MedicalCodingContext-encounterReason"></a>
The reason for the encounter. The reason can contain letters, numbers, spaces, periods, commas, and hyphens, and can't contain only spaces.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9 .,-]+`
Required: No

 ** encounterType **   <a name="connecthealth-Type-MedicalCodingContext-encounterType"></a>
The type of the encounter, either in person or telehealth.
Type: String
Valid Values: `TELEHEALTH | IN_PERSON`
Required: No

 ** sex **   <a name="connecthealth-Type-MedicalCodingContext-sex"></a>
The sex of the patient.
Type: String
Valid Values: `MALE | FEMALE | NON_BINARY | UNKNOWN`
Required: No

 ** status **   <a name="connecthealth-Type-MedicalCodingContext-status"></a>
The status of the patient, either new or established.
Type: String
Valid Values: `NEW | ESTABLISHED`
Required: No

## See Also
<a name="API_MedicalCodingContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalCodingContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalCodingContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalCodingContext)
