---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DataMigrationStatistics.html
---

# DataMigrationStatistics
<a name="API_DataMigrationStatistics"></a>

Information about the data migration run, including start and stop time, latency, and migration progress.

## Contents
<a name="API_DataMigrationStatistics_Contents"></a>

 ** CDCLatency **   <a name="DMS-Type-DataMigrationStatistics-CDCLatency"></a>
The current latency of the change data capture (CDC) operation.
Type: Integer
Required: No

 ** ElapsedTimeMillis **   <a name="DMS-Type-DataMigrationStatistics-ElapsedTimeMillis"></a>
The elapsed duration of the data migration run.
Type: Long
Required: No

 ** FullLoadPercentage **   <a name="DMS-Type-DataMigrationStatistics-FullLoadPercentage"></a>
The data migration's progress in the full-load migration phase.
Type: Integer
Required: No

 ** StartTime **   <a name="DMS-Type-DataMigrationStatistics-StartTime"></a>
The time when the migration started.
Type: Timestamp
Required: No

 ** StopTime **   <a name="DMS-Type-DataMigrationStatistics-StopTime"></a>
The time when the migration stopped or failed.
Type: Timestamp
Required: No

 ** TablesErrored **   <a name="DMS-Type-DataMigrationStatistics-TablesErrored"></a>
The number of tables that DMS failed to process.
Type: Integer
Required: No

 ** TablesLoaded **   <a name="DMS-Type-DataMigrationStatistics-TablesLoaded"></a>
The number of tables loaded in the current data migration run.
Type: Integer
Required: No

 ** TablesLoading **   <a name="DMS-Type-DataMigrationStatistics-TablesLoading"></a>
The data migration's table loading progress.
Type: Integer
Required: No

 ** TablesQueued **   <a name="DMS-Type-DataMigrationStatistics-TablesQueued"></a>
The number of tables that are waiting for processing.
Type: Integer
Required: No

## See Also
<a name="API_DataMigrationStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DataMigrationStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DataMigrationStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DataMigrationStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
