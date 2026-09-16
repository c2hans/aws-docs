---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_QuoteConstraint.html
---

# QuoteConstraint
<a name="API_QuoteConstraint"></a>

A physical constraint for a quote.

## Contents
<a name="API_QuoteConstraint_Contents"></a>

 ** QuoteConstraintType **   <a name="outposts-Type-QuoteConstraint-QuoteConstraintType"></a>
The type of constraint. Valid values are `RACK_MAXIMUM`, `RACK_MAX_POWER_KVA`, `RACK_MAX_WEIGHT_LBS`, and `RACK_SPACE_CONSTRAINED`.
Type: String
Valid Values: `RACK_MAXIMUM | RACK_MAX_POWER_KVA | RACK_MAX_WEIGHT_LBS | RACK_SPACE_CONSTRAINED`
Required: No

 ** Value **   <a name="outposts-Type-QuoteConstraint-Value"></a>
The value of the constraint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\S \n]+$`
Required: No

## See Also
<a name="API_QuoteConstraint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/QuoteConstraint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/QuoteConstraint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/QuoteConstraint)
