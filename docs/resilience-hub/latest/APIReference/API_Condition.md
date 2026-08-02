---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_Condition.html
---

# Condition
<a name="API_Condition"></a>

Indicates the condition based on which you want to filter the metrics.

## Contents
<a name="API_Condition_Contents"></a>

 ** field **   <a name="resiliencehub-Type-Condition-field"></a>
Indicates the field in the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** operator **   <a name="resiliencehub-Type-Condition-operator"></a>
Indicates the type of operator or comparison to be used when evaluating a condition against the specified field.
Type: String
Valid Values: `Equals | NotEquals | GreaterThen | GreaterOrEquals | LessThen | LessOrEquals`
Required: Yes

 ** value **   <a name="resiliencehub-Type-Condition-value"></a>
Indicates the value or data against which a condition is evaluated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_Condition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/Condition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/Condition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/Condition)
