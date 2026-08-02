---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_WindowStartTime.html
---

# WindowStartTime
<a name="API_WindowStartTime"></a>

The desired start time for an [off-peak maintenance window](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_OffPeakWindow.html).

## Contents
<a name="API_WindowStartTime_Contents"></a>

 ** Hours **   <a name="opensearchservice-Type-WindowStartTime-Hours"></a>
The start hour of the window in Coordinated Universal Time (UTC), using 24-hour time. For example, `17` refers to 5:00 P.M. UTC.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 23.
Required: Yes

 ** Minutes **   <a name="opensearchservice-Type-WindowStartTime-Minutes"></a>
The start minute of the window, in UTC.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 59.
Required: Yes

## See Also
<a name="API_WindowStartTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/WindowStartTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/WindowStartTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/WindowStartTime)
