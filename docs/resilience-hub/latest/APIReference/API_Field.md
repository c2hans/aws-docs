---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_Field.html
---

# Field
<a name="API_Field"></a>

Indicates the field or attribute of a resource or data structure on which a condition is being applied or evaluated.

## Contents
<a name="API_Field_Contents"></a>

 ** name **   <a name="resiliencehub-Type-Field-name"></a>
Name of the field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** aggregation **   <a name="resiliencehub-Type-Field-aggregation"></a>
(Optional) Indicates the type of aggregation or summary operation (such as Sum, Average, and so on) to be performed on a particular field or set of data.
Type: String
Valid Values: `Min | Max | Sum | Avg | Count`
Required: No

## See Also
<a name="API_Field_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/Field)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/Field)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/Field)
