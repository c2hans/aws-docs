---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_PriorityCount.html
---

# PriorityCount
<a name="API_PriorityCount"></a>

Pair of a recommendation Priority and the number of recommendations attributed to it in a CoverageSummary.

## Contents
<a name="API_PriorityCount_Contents"></a>

 ** count **   <a name="wellarchitected-Type-PriorityCount-count"></a>
Non-negative count of recommendations in the report that are attributed to this priority.
Type: Long
Required: Yes

 ** priority **   <a name="wellarchitected-Type-PriorityCount-priority"></a>
Priority this count is attributed to.
Type: String
Valid Values: `HIGH | MEDIUM | LOW`
Required: Yes

## See Also
<a name="API_PriorityCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/PriorityCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/PriorityCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/PriorityCount)
