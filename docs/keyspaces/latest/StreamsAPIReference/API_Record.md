---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_Record.html
---

# Record
<a name="API_Record"></a>

Represents a change data capture record for a row in an Amazon Keyspaces table, containing both the new and old states of the row.

## Contents
<a name="API_Record_Contents"></a>

 ** clusteringKeys **   <a name="keyspaces-Type-Record-clusteringKeys"></a>
The clustering key columns and their values for the affected row, which determine the order of rows within a partition.
Type: String to [KeyspacesCellValue](API_KeyspacesCellValue.md) object map
Required: No

 ** createdAt **   <a name="keyspaces-Type-Record-createdAt"></a>
The timestamp indicating when this change data capture record was created.
Type: Timestamp
Required: No

 ** eventVersion **   <a name="keyspaces-Type-Record-eventVersion"></a>
The version of the record format, used to track the evolution of the record structure over time.
Type: String
Required: No

 ** newImage **   <a name="keyspaces-Type-Record-newImage"></a>
The state of the row after the change operation that generated this record.
Type: [KeyspacesRow](API_KeyspacesRow.md) object
Required: No

 ** oldImage **   <a name="keyspaces-Type-Record-oldImage"></a>
The state of the row before the change operation that generated this record.
Type: [KeyspacesRow](API_KeyspacesRow.md) object
Required: No

 ** origin **   <a name="keyspaces-Type-Record-origin"></a>
The origin or source of this change data capture record.
Type: String
Valid Values: `USER | REPLICATION | TTL`
Required: No

 ** partitionKeys **   <a name="keyspaces-Type-Record-partitionKeys"></a>
The partition key columns and their values for the affected row.
Type: String to [KeyspacesCellValue](API_KeyspacesCellValue.md) object map
Required: No

 ** sequenceNumber **   <a name="keyspaces-Type-Record-sequenceNumber"></a>
A unique identifier assigned to this record within the shard, used for ordering and tracking purposes.
Type: String
Length Constraints: Minimum length of 21. Maximum length of 48.
Required: No

## See Also
<a name="API_Record_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspacesstreams-2024-09-09/Record)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspacesstreams-2024-09-09/Record)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/Record)
