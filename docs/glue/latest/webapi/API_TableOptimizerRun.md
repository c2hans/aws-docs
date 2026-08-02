---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TableOptimizerRun.html
---

# TableOptimizerRun
<a name="API_TableOptimizerRun"></a>

Contains details for a table optimizer run.

## Contents
<a name="API_TableOptimizerRun_Contents"></a>

 ** compactionMetrics **   <a name="Glue-Type-TableOptimizerRun-compactionMetrics"></a>
A `CompactionMetrics` object containing metrics for the optimizer run.
Type: [CompactionMetrics](API_CompactionMetrics.md) object
Required: No

 ** compactionStrategy **   <a name="Glue-Type-TableOptimizerRun-compactionStrategy"></a>
The strategy used for the compaction run. Indicates which algorithm was applied to determine how files were selected and combined during the compaction process. Valid values are:
+  `binpack`: Combines small files into larger files, typically targeting sizes over 100MB, while applying any pending deletes. This is the recommended compaction strategy for most use cases.
+  `sort`: Organizes data based on specified columns which are sorted hierarchically during compaction, improving query performance for filtered operations. This strategy is recommended when your queries frequently filter on specific columns. To use this strategy, you must first define a sort order in your Iceberg table properties using the `sort_order` table property.
+  `z-order`: Optimizes data organization by blending multiple attributes into a single scalar value that can be used for sorting, allowing efficient querying across multiple dimensions. This strategy is recommended when you need to query data across multiple dimensions simultaneously. To use this strategy, you must first define a sort order in your Iceberg table properties using the `sort_order` table property.
Type: String
Valid Values: `binpack | sort | z-order`
Required: No

 ** endTimestamp **   <a name="Glue-Type-TableOptimizerRun-endTimestamp"></a>
Represents the epoch timestamp at which the compaction job ended.
Type: Timestamp
Required: No

 ** error **   <a name="Glue-Type-TableOptimizerRun-error"></a>
An error that occured during the optimizer run.
Type: String
Required: No

 ** eventType **   <a name="Glue-Type-TableOptimizerRun-eventType"></a>
An event type representing the status of the table optimizer run.
Type: String
Valid Values: `starting | completed | failed | in_progress`
Required: No

 ** metrics **   <a name="Glue-Type-TableOptimizerRun-metrics"></a>
A `RunMetrics` object containing metrics for the optimizer run.
This member is deprecated. See the individual metric members for compaction, retention, and orphan file deletion.
Type: [RunMetrics](API_RunMetrics.md) object
Required: No

 ** orphanFileDeletionMetrics **   <a name="Glue-Type-TableOptimizerRun-orphanFileDeletionMetrics"></a>
An `OrphanFileDeletionMetrics` object containing metrics for the optimizer run.
Type: [OrphanFileDeletionMetrics](API_OrphanFileDeletionMetrics.md) object
Required: No

 ** retentionMetrics **   <a name="Glue-Type-TableOptimizerRun-retentionMetrics"></a>
A `RetentionMetrics` object containing metrics for the optimizer run.
Type: [RetentionMetrics](API_RetentionMetrics.md) object
Required: No

 ** startTimestamp **   <a name="Glue-Type-TableOptimizerRun-startTimestamp"></a>
Represents the epoch timestamp at which the compaction job was started within Lake Formation.
Type: Timestamp
Required: No

## See Also
<a name="API_TableOptimizerRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TableOptimizerRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TableOptimizerRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TableOptimizerRun)
