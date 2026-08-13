---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FieldIndex.html
---

# FieldIndex
<a name="API_FieldIndex"></a>

This structure describes one log event field that is used as an index in at least one index policy in this account.

## Contents
<a name="API_FieldIndex_Contents"></a>

 ** fieldIndexName **   <a name="CWL-Type-FieldIndex-fieldIndexName"></a>
The string that this field index matches.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** firstEventTime **   <a name="CWL-Type-FieldIndex-firstEventTime"></a>
The time and date of the earliest log event that matches this field index, after the index policy that contains it was created.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** indexCategory **   <a name="CWL-Type-FieldIndex-indexCategory"></a>
The category of the field index:
+  `DEFAULT`: Fields that CloudWatch Logs indexes by default. Examples include `@logStream` and `@data_format`.
+  `CUSTOM`: Fields that you added manually to the field index policy. CloudWatch Logs always indexes these fields. These fields count toward the quota of 20 fields for each log group.
+  `AUTO`: Fields that CloudWatch Logs indexes automatically based on your query patterns and usage. These fields do not count toward the field index quota. CloudWatch Logs might update these fields based on changes in your query patterns. To keep a field indexed permanently, add it to an account-level or log-group level field index policy.
+  `INACTIVE`: Fields that CloudWatch Logs indexed before but does not index now. This happens if you remove a field from the field index policy or if CloudWatch Logs automatically selects a different field based on your queries.
For more information about automatically indexed fields, see [Automatically indexed fields](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-Automatic.html).
Type: String
Valid Values: `DEFAULT | CUSTOM | AUTO | INACTIVE`
Required: No

 ** lastEventTime **   <a name="CWL-Type-FieldIndex-lastEventTime"></a>
The time and date of the most recent log event that matches this field index.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** lastScanTime **   <a name="CWL-Type-FieldIndex-lastScanTime"></a>
The most recent time that CloudWatch Logs scanned ingested log events to search for this field index to improve the speed of future CloudWatch Logs Insights queries that search for this field index.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** logGroupIdentifier **   <a name="CWL-Type-FieldIndex-logGroupIdentifier"></a>
If this field index appears in an index policy that applies only to a single log group, the ARN of that log group is displayed here.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: No

 ** type **   <a name="CWL-Type-FieldIndex-type"></a>
The type of index. Specify `FACET` for facet-based indexing or `FIELD_INDEX` for field-based indexing. This determines how the field is indexed and can be queried.
Type: String
Valid Values: `FACET | FIELD_INDEX`
Required: No

## See Also
<a name="API_FieldIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/FieldIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/FieldIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/FieldIndex)
