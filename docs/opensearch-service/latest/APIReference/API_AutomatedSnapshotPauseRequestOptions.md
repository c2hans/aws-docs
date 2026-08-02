---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AutomatedSnapshotPauseRequestOptions.html
---

# AutomatedSnapshotPauseRequestOptions
<a name="API_AutomatedSnapshotPauseRequestOptions"></a>

Specifies the automated snapshot pause request options for the domain.

**Important**
Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.

Maximum suspension duration: 3 days.

## Contents
<a name="API_AutomatedSnapshotPauseRequestOptions_Contents"></a>

 ** Enabled **   <a name="opensearchservice-Type-AutomatedSnapshotPauseRequestOptions-Enabled"></a>
Whether to enable or disable automated snapshot pause for the domain.
Type: Boolean
Required: Yes

 ** EndTime **   <a name="opensearchservice-Type-AutomatedSnapshotPauseRequestOptions-EndTime"></a>
The timestamp at which the automated snapshot pause should end. The maximum allowed duration between `StartTime` and `EndTime` is 3 days.
Type: Timestamp
Required: No

 ** StartTime **   <a name="opensearchservice-Type-AutomatedSnapshotPauseRequestOptions-StartTime"></a>
The timestamp at which the automated snapshot pause should begin.
Type: Timestamp
Required: No

## See Also
<a name="API_AutomatedSnapshotPauseRequestOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AutomatedSnapshotPauseRequestOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AutomatedSnapshotPauseRequestOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AutomatedSnapshotPauseRequestOptions)
