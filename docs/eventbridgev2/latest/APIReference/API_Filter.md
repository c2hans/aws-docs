---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A single filter entry within a FilterConfiguration.

## Contents
<a name="API_Filter_Contents"></a>

 ** Pattern **   <a name="eventbridgev2-Type-Filter-Pattern"></a>
An event pattern, as a JSON string, that selects which events match.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: Yes

 ** Scope **   <a name="eventbridgev2-Type-Filter-Scope"></a>
Scope of a filter pattern within a FilterConfiguration.
Type: String
Valid Values: `DATA | METADATA | SYSTEM_METADATA`
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/Filter)
