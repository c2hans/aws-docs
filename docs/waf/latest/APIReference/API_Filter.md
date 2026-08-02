---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A single logging filter, used in [LoggingFilter](API_LoggingFilter.md).

## Contents
<a name="API_Filter_Contents"></a>

 ** Behavior **   <a name="WAF-Type-Filter-Behavior"></a>
How to handle logs that satisfy the filter's conditions and requirement.
Type: String
Valid Values: `KEEP | DROP`
Required: Yes

 ** Conditions **   <a name="WAF-Type-Filter-Conditions"></a>
Match conditions for the filter.
Type: Array of [Condition](API_Condition.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** Requirement **   <a name="WAF-Type-Filter-Requirement"></a>
Logic to apply to the filtering conditions. You can specify that, in order to satisfy the filter, a log must match all conditions or must match at least one condition.
Type: String
Valid Values: `MEETS_ALL | MEETS_ANY`
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/Filter)
