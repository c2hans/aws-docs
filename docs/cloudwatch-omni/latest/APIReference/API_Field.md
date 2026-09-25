---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_Field.html
---

# Field
<a name="API_Field"></a>

A telemetry field available for use in query expressions.

## Contents
<a name="API_Field_Contents"></a>

 ** name **   <a name="cloudwatchomni-Type-Field-name"></a>
The name of the field. Field names are case-sensitive and must be used exactly as returned when referencing them in query expressions.
Type: String
Required: Yes

 ** children **   <a name="cloudwatchomni-Type-Field-children"></a>
Child fields nested under this field.
Type: Array of [Field](#API_Field) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: No

## See Also
<a name="API_Field_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/Field)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/Field)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/Field)
