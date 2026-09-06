---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_TreatmentOverrides.html
---

# TreatmentOverrides
<a name="API_TreatmentOverrides"></a>

Treatment assignment overrides that assign specific entity IDs to treatments, bypassing random assignment.

## Contents
<a name="API_TreatmentOverrides_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Inline **   <a name="appconfig-Type-TreatmentOverrides-Inline"></a>
A map of entity IDs to treatment keys. Each entry assigns the specified entity to the specified treatment, bypassing random assignment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 32 items.
Key Length Constraints: Minimum length of 1. Maximum length of 2048.
Value Pattern: `^[a-zA-Z0-9]{1,8}`
Required: No

## See Also
<a name="API_TreatmentOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/TreatmentOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/TreatmentOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/TreatmentOverrides)
