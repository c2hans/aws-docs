---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationStats.html
---

# ReplicationStats
<a name="API_ReplicationStats"></a>

This object provides a collection of statistics about a serverless replication.

## Contents
<a name="API_ReplicationStats_Contents"></a>

 ** ElapsedTimeMillis **   <a name="DMS-Type-ReplicationStats-ElapsedTimeMillis"></a>
The elapsed time of the replication, in milliseconds.
Type: Long
Required: No

 ** FreshStartDate **   <a name="DMS-Type-ReplicationStats-FreshStartDate"></a>
The date the replication was started either with a fresh start or a target reload.
Type: Timestamp
Required: No

 ** FullLoadFinishDate **   <a name="DMS-Type-ReplicationStats-FullLoadFinishDate"></a>
The date the replication full load was finished.
Type: Timestamp
Required: No

 ** FullLoadProgressPercent **   <a name="DMS-Type-ReplicationStats-FullLoadProgressPercent"></a>
The percent complete for the full load serverless replication.
Type: Integer
Required: No

 ** FullLoadStartDate **   <a name="DMS-Type-ReplicationStats-FullLoadStartDate"></a>
The date the replication full load was started.
Type: Timestamp
Required: No

 ** StartDate **   <a name="DMS-Type-ReplicationStats-StartDate"></a>
The date the replication is scheduled to start.
Type: Timestamp
Required: No

 ** StopDate **   <a name="DMS-Type-ReplicationStats-StopDate"></a>
The date the replication was stopped.
Type: Timestamp
Required: No

 ** TablesErrored **   <a name="DMS-Type-ReplicationStats-TablesErrored"></a>
The number of errors that have occured for this replication.
Type: Integer
Required: No

 ** TablesLoaded **   <a name="DMS-Type-ReplicationStats-TablesLoaded"></a>
The number of tables loaded for this replication.
Type: Integer
Required: No

 ** TablesLoading **   <a name="DMS-Type-ReplicationStats-TablesLoading"></a>
The number of tables currently loading for this replication.
Type: Integer
Required: No

 ** TablesQueued **   <a name="DMS-Type-ReplicationStats-TablesQueued"></a>
The number of tables queued for this replication.
Type: Integer
Required: No

## See Also
<a name="API_ReplicationStats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ReplicationStats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ReplicationStats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ReplicationStats)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
