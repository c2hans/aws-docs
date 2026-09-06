---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_MetricSearchCriteria.html
---

# MetricSearchCriteria
<a name="API_MetricSearchCriteria"></a>

Defines the search criteria for filtering metrics.

## Contents
<a name="API_MetricSearchCriteria_Contents"></a>

 ** AndConditions **   <a name="connect-Type-MetricSearchCriteria-AndConditions"></a>
A list of conditions that must all be satisfied.
Type: Array of [MetricSearchCriteria](#API_MetricSearchCriteria) objects
Required: No

 ** BooleanCondition **   <a name="connect-Type-MetricSearchCriteria-BooleanCondition"></a>
A boolean search condition for Search APIs.
Type: [BooleanCondition](API_BooleanCondition.md) object
Required: No

 ** OrConditions **   <a name="connect-Type-MetricSearchCriteria-OrConditions"></a>
A list of conditions to be met, where at least one condition must be satisfied.
Type: Array of [MetricSearchCriteria](#API_MetricSearchCriteria) objects
Required: No

 ** StringCondition **   <a name="connect-Type-MetricSearchCriteria-StringCondition"></a>
A leaf node condition which can be used to specify a string condition.
Type: [StringCondition](API_StringCondition.md) object
Required: No

## See Also
<a name="API_MetricSearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/MetricSearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/MetricSearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/MetricSearchCriteria)
