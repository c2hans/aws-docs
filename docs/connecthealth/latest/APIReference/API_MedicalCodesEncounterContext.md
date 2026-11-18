---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_MedicalCodesEncounterContext.html
---

# MedicalCodesEncounterContext
<a name="API_MedicalCodesEncounterContext"></a>

Encounter context for a medical coding job. All fields are optional.

## Contents
<a name="API_MedicalCodesEncounterContext_Contents"></a>

 ** afterHours **   <a name="connecthealth-Type-MedicalCodesEncounterContext-afterHours"></a>
Specifies whether the encounter took place outside regular business hours.
Type: Boolean
Required: No

 ** encounterDate **   <a name="connecthealth-Type-MedicalCodesEncounterContext-encounterDate"></a>
The date of the encounter, in YYYY-MM-DD format. The date can't be more than one day after the current date in UTC.
Type: String
Pattern: `\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])`
Required: No

 ** encounterDurationMinutes **   <a name="connecthealth-Type-MedicalCodesEncounterContext-encounterDurationMinutes"></a>
The duration of the encounter, in minutes, from 1 to 1440.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1440.
Required: No

 ** encounterReason **   <a name="connecthealth-Type-MedicalCodesEncounterContext-encounterReason"></a>
The reason for the encounter. The reason can contain letters, numbers, spaces, periods, commas, and hyphens, and can't contain only spaces.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9 .,-]+`
Required: No

 ** encounterType **   <a name="connecthealth-Type-MedicalCodesEncounterContext-encounterType"></a>
The type of the encounter, either in person or telehealth.
Type: String
Valid Values: `TELEHEALTH | IN_PERSON`
Required: No

## See Also
<a name="API_MedicalCodesEncounterContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/MedicalCodesEncounterContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/MedicalCodesEncounterContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/MedicalCodesEncounterContext)
