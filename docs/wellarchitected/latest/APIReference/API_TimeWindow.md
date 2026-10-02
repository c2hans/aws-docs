---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_TimeWindow.html
---

# TimeWindow
<a name="API_TimeWindow"></a>

An inclusive time window used by Organizational Report filters. Both bounds are optional, but at least one of from or to must be set when the structure is present.

## Contents
<a name="API_TimeWindow_Contents"></a>

 ** from **   <a name="wellarchitected-Type-TimeWindow-from"></a>
Lower bound of the window (inclusive). Absent means no lower bound.
Type: Timestamp
Required: No

 ** to **   <a name="wellarchitected-Type-TimeWindow-to"></a>
Upper bound of the window (inclusive). Absent means no upper bound.
Type: Timestamp
Required: No

## See Also
<a name="API_TimeWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/TimeWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/TimeWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/TimeWindow)
