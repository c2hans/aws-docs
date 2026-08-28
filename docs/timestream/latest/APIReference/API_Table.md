---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_Table.html
---

# Table
<a name="API_Table"></a>

Represents a database table in Timestream. Tables contain one or more related time series. You can modify the retention duration of the memory store and the magnetic store for a table.

## Contents
<a name="API_Table_Contents"></a>

 ** Arn **   <a name="timestream-Type-Table-Arn"></a>
The Amazon Resource Name that uniquely identifies this table.
Type: String
Required: No

 ** CreationTime **   <a name="timestream-Type-Table-CreationTime"></a>
The time when the Timestream table was created.
Type: Timestamp
Required: No

 ** DatabaseName **   <a name="timestream-Type-Table-DatabaseName"></a>
The name of the Timestream database that contains this table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Required: No

 ** LastUpdatedTime **   <a name="timestream-Type-Table-LastUpdatedTime"></a>
The time when the Timestream table was last updated.
Type: Timestamp
Required: No

 ** MagneticStoreWriteProperties **   <a name="timestream-Type-Table-MagneticStoreWriteProperties"></a>
Contains properties to set on the table when enabling magnetic store writes.
Type: [MagneticStoreWriteProperties](API_MagneticStoreWriteProperties.md) object
Required: No

 ** RetentionProperties **   <a name="timestream-Type-Table-RetentionProperties"></a>
The retention duration for the memory store and magnetic store.
Type: [RetentionProperties](API_RetentionProperties.md) object
Required: No

 ** Schema **   <a name="timestream-Type-Table-Schema"></a>
 The schema of the table.
Type: [Schema](API_Schema.md) object
Required: No

 ** TableName **   <a name="timestream-Type-Table-TableName"></a>
The name of the Timestream table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Required: No

 ** TableStatus **   <a name="timestream-Type-Table-TableStatus"></a>
The current state of the table:
+  `DELETING` - The table is being deleted.
+  `ACTIVE` - The table is ready for use.
Type: String
Valid Values: `ACTIVE | DELETING | RESTORING`
Required: No

## See Also
<a name="API_Table_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/Table)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/Table)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/Table)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
