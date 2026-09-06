---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AutomatedSnapshotPauseOptions.html
---

# AutomatedSnapshotPauseOptions
<a name="API_AutomatedSnapshotPauseOptions"></a>

Specifies the automated snapshot pause options for the domain. These options allow you to temporarily pause automated snapshots for a specified time period.

## Contents
<a name="API_AutomatedSnapshotPauseOptions_Contents"></a>

 ** Enabled **   <a name="opensearchservice-Type-AutomatedSnapshotPauseOptions-Enabled"></a>
Whether automated snapshot pause is enabled for the domain.
Type: Boolean
Required: Yes

 ** EndTime **   <a name="opensearchservice-Type-AutomatedSnapshotPauseOptions-EndTime"></a>
The timestamp at which the automated snapshot pause ends.
Type: Timestamp
Required: No

 ** StartTime **   <a name="opensearchservice-Type-AutomatedSnapshotPauseOptions-StartTime"></a>
The timestamp at which the automated snapshot pause begins.
Type: Timestamp
Required: No

 ** State **   <a name="opensearchservice-Type-AutomatedSnapshotPauseOptions-State"></a>
The current state of the automated snapshot pause. Valid values are `Active`, `Completed`, `Scheduled`, and `Disabled`.
Type: String
Valid Values: `Active | Completed | Scheduled | Disabled`
Required: No

## See Also
<a name="API_AutomatedSnapshotPauseOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AutomatedSnapshotPauseOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AutomatedSnapshotPauseOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AutomatedSnapshotPauseOptions)
