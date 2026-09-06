---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_KinesisSettings.html
---

# KinesisSettings
<a name="API_KinesisSettings"></a>

Provides information that describes an Amazon Kinesis Data Stream endpoint. This information includes the output format of records applied to the endpoint and details of transaction and control table data information.

## Contents
<a name="API_KinesisSettings_Contents"></a>

 ** IncludeControlDetails **   <a name="DMS-Type-KinesisSettings-IncludeControlDetails"></a>
Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output. The default is `false`.
Type: Boolean
Required: No

 ** IncludeNullAndEmpty **   <a name="DMS-Type-KinesisSettings-IncludeNullAndEmpty"></a>
Include NULL and empty columns for records migrated to the endpoint. The default is `false`.
Type: Boolean
Required: No

 ** IncludePartitionValue **   <a name="DMS-Type-KinesisSettings-IncludePartitionValue"></a>
Shows the partition value within the Kinesis message output, unless the partition type is `schema-table-type`. The default is `false`.
Type: Boolean
Required: No

 ** IncludeTableAlterOperations **   <a name="DMS-Type-KinesisSettings-IncludeTableAlterOperations"></a>
Includes any data definition language (DDL) operations that change the table in the control data, such as `rename-table`, `drop-table`, `add-column`, `drop-column`, and `rename-column`. The default is `false`.
Type: Boolean
Required: No

 ** IncludeTransactionDetails **   <a name="DMS-Type-KinesisSettings-IncludeTransactionDetails"></a>
Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for `transaction_id`, previous `transaction_id`, and `transaction_record_id` (the record offset within a transaction). The default is `false`.
Type: Boolean
Required: No

 ** MessageFormat **   <a name="DMS-Type-KinesisSettings-MessageFormat"></a>
The output format for the records created on the endpoint. The message format is `JSON` (default) or `JSON_UNFORMATTED` (a single line with no tab).
Type: String
Valid Values: `json | json-unformatted`
Required: No

 ** NoHexPrefix **   <a name="DMS-Type-KinesisSettings-NoHexPrefix"></a>
Set this optional parameter to `true` to avoid adding a '0x' prefix to raw data in hexadecimal format. For example, by default, AWS DMS adds a '0x' prefix to the LOB column type in hexadecimal format moving from an Oracle source to an Amazon Kinesis target. Use the `NoHexPrefix` endpoint setting to enable migration of RAW data type columns without adding the '0x' prefix.
Type: Boolean
Required: No

 ** PartitionIncludeSchemaTable **   <a name="DMS-Type-KinesisSettings-PartitionIncludeSchemaTable"></a>
Prefixes schema and table names to partition values, when the partition type is `primary-key-type`. Doing this increases data distribution among Kinesis shards. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same shard, which causes throttling. The default is `false`.
Type: Boolean
Required: No

 ** ServiceAccessRoleArn **   <a name="DMS-Type-KinesisSettings-ServiceAccessRoleArn"></a>
The Amazon Resource Name (ARN) for the IAM role that AWS DMS uses to write to the Kinesis data stream. The role must allow the `iam:PassRole` action.
Type: String
Required: No

 ** StreamArn **   <a name="DMS-Type-KinesisSettings-StreamArn"></a>
The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.
Type: String
Required: No

 ** UseLargeIntegerValue **   <a name="DMS-Type-KinesisSettings-UseLargeIntegerValue"></a>
Specifies using the large integer value with Kinesis.
Type: Boolean
Required: No

## See Also
<a name="API_KinesisSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/KinesisSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/KinesisSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/KinesisSettings)
