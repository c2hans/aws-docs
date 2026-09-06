---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_TableStatistics.html
---

# TableStatistics
<a name="API_TableStatistics"></a>

Provides a collection of table statistics in response to a request by the `DescribeTableStatistics` operation.

## Contents
<a name="API_TableStatistics_Contents"></a>

 ** AppliedDdls **   <a name="DMS-Type-TableStatistics-AppliedDdls"></a>
The number of data definition language (DDL) statements used to build and modify the structure of your tables applied on the target.
Type: Long
Required: No

 ** AppliedDeletes **   <a name="DMS-Type-TableStatistics-AppliedDeletes"></a>
The number of delete actions applied on a target table.
Type: Long
Required: No

 ** AppliedInserts **   <a name="DMS-Type-TableStatistics-AppliedInserts"></a>
The number of insert actions applied on a target table.
Type: Long
Required: No

 ** AppliedUpdates **   <a name="DMS-Type-TableStatistics-AppliedUpdates"></a>
The number of update actions applied on a target table.
Type: Long
Required: No

 ** Ddls **   <a name="DMS-Type-TableStatistics-Ddls"></a>
The data definition language (DDL) used to build and modify the structure of your tables.
Type: Long
Required: No

 ** Deletes **   <a name="DMS-Type-TableStatistics-Deletes"></a>
The number of delete actions performed on a table.
Type: Long
Required: No

 ** FullLoadCondtnlChkFailedRows **   <a name="DMS-Type-TableStatistics-FullLoadCondtnlChkFailedRows"></a>
The number of rows that failed conditional checks during the full load operation (valid only for migrations where DynamoDB is the target).
Type: Long
Required: No

 ** FullLoadEndTime **   <a name="DMS-Type-TableStatistics-FullLoadEndTime"></a>
The time when the full load operation completed.
Type: Timestamp
Required: No

 ** FullLoadErrorRows **   <a name="DMS-Type-TableStatistics-FullLoadErrorRows"></a>
The number of rows that failed to load during the full load operation (valid only for migrations where DynamoDB is the target).
Type: Long
Required: No

 ** FullLoadReloaded **   <a name="DMS-Type-TableStatistics-FullLoadReloaded"></a>
A value that indicates if the table was reloaded (`true`) or loaded as part of a new full load operation (`false`).
Type: Boolean
Required: No

 ** FullLoadRows **   <a name="DMS-Type-TableStatistics-FullLoadRows"></a>
The number of rows added during the full load operation.
Type: Long
Required: No

 ** FullLoadStartTime **   <a name="DMS-Type-TableStatistics-FullLoadStartTime"></a>
The time when the full load operation started.
Type: Timestamp
Required: No

 ** Inserts **   <a name="DMS-Type-TableStatistics-Inserts"></a>
The number of insert actions performed on a table.
Type: Long
Required: No

 ** LastUpdateTime **   <a name="DMS-Type-TableStatistics-LastUpdateTime"></a>
The last time a table was updated.
Type: Timestamp
Required: No

 ** ResyncProgress **   <a name="DMS-Type-TableStatistics-ResyncProgress"></a>
Calculates the percentage of failed validations that were successfully resynced to the system.
Type: Double
Required: No

 ** ResyncRowsAttempted **   <a name="DMS-Type-TableStatistics-ResyncRowsAttempted"></a>
Records the total number of mismatched data rows where the system attempted to apply fixes in the target database.
Type: Long
Required: No

 ** ResyncRowsFailed **   <a name="DMS-Type-TableStatistics-ResyncRowsFailed"></a>
Records the total number of mismatched data rows where fix attempts failed in the target database.
Type: Long
Required: No

 ** ResyncRowsSucceeded **   <a name="DMS-Type-TableStatistics-ResyncRowsSucceeded"></a>
Records the total number of mismatched data rows where fixes were successfully applied in the target database.
Type: Long
Required: No

 ** ResyncState **   <a name="DMS-Type-TableStatistics-ResyncState"></a>
Records the current state of table resynchronization in the migration task.
This parameter can have the following values:
+ Not enabled – Resync is not enabled for the table in the migration task.
+ Pending – The tables are waiting for resync.
+ In progress – Resync in progress for some records in the table.
+ No primary key – The table could not be resynced because it has no primary key.
+ Last resync at: `date/time` – Resync session is finished at time. Time provided in UTC format.
Type: String
Required: No

 ** SchemaName **   <a name="DMS-Type-TableStatistics-SchemaName"></a>
The schema name.
Type: String
Required: No

 ** TableName **   <a name="DMS-Type-TableStatistics-TableName"></a>
The name of the table.
Type: String
Required: No

 ** TableState **   <a name="DMS-Type-TableStatistics-TableState"></a>
The state of the tables described.
Valid states: Table does not exist \| Before load \| Full load \| Table completed \| Table cancelled \| Table error \| Table is being reloaded
Type: String
Required: No

 ** Updates **   <a name="DMS-Type-TableStatistics-Updates"></a>
The number of update actions performed on a table.
Type: Long
Required: No

 ** ValidationFailedRecords **   <a name="DMS-Type-TableStatistics-ValidationFailedRecords"></a>
The number of records that failed validation.
Type: Long
Required: No

 ** ValidationPendingRecords **   <a name="DMS-Type-TableStatistics-ValidationPendingRecords"></a>
The number of records that have yet to be validated.
Type: Long
Required: No

 ** ValidationState **   <a name="DMS-Type-TableStatistics-ValidationState"></a>
The validation state of the table.
This parameter can have the following values:
+ Not enabled – Validation isn't enabled for the table in the migration task.
+ Pending records – Some records in the table are waiting for validation.
+ Mismatched records – Some records in the table don't match between the source and target.
+ Suspended records – Some records in the table couldn't be validated.
+ No primary key –The table couldn't be validated because it has no primary key.
+ Table error – The table wasn't validated because it's in an error state and some data wasn't migrated.
+ Validated – All rows in the table are validated. If the table is updated, the status can change from Validated.
+ Error – The table couldn't be validated because of an unexpected error.
+ Pending validation – The table is waiting validation.
+ Preparing table – Preparing the table enabled in the migration task for validation.
+ Pending revalidation – All rows in the table are pending validation after the table was updated.
Type: String
Required: No

 ** ValidationStateDetails **   <a name="DMS-Type-TableStatistics-ValidationStateDetails"></a>
Additional details about the state of validation.
Type: String
Required: No

 ** ValidationSuspendedRecords **   <a name="DMS-Type-TableStatistics-ValidationSuspendedRecords"></a>
The number of records that couldn't be validated.
Type: Long
Required: No

## See Also
<a name="API_TableStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/TableStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/TableStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/TableStatistics)
