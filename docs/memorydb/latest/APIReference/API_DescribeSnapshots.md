---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeSnapshots.html
---

# DescribeSnapshots
<a name="API_DescribeSnapshots"></a>

Returns information about cluster snapshots. By default, DescribeSnapshots lists all of your snapshots; it can optionally describe a single snapshot, or just the snapshots associated with a particular cluster.

## Request Syntax
<a name="API_DescribeSnapshots_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ShowDetail": {{boolean}},
   "SnapshotName": "{{string}}",
   "Source": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSnapshots_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_DescribeSnapshots_RequestSyntax) **   <a name="MemoryDB-DescribeSnapshots-request-ClusterName"></a>
A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cluster are described.
Type: String
Required: No

 ** [MaxResults](#API_DescribeSnapshots_RequestSyntax) **   <a name="MemoryDB-DescribeSnapshots-request-MaxResults"></a>
The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeSnapshots_RequestSyntax) **   <a name="MemoryDB-DescribeSnapshots-request-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

 ** [ShowDetail](#API_DescribeSnapshots_RequestSyntax) **   <a name="MemoryDB-DescribeSnapshots-request-ShowDetail"></a>
A Boolean value which if true, the shard configuration is included in the snapshot description.
Type: Boolean
Required: No

 ** [SnapshotName](#API_DescribeSnapshots_RequestSyntax) **   <a name="MemoryDB-DescribeSnapshots-request-SnapshotName"></a>
A user-supplied name of the snapshot. If this parameter is specified, only this named snapshot is described.
Type: String
Required: No

 ** [Source](#API_DescribeSnapshots_RequestSyntax) **   <a name="MemoryDB-DescribeSnapshots-request-Source"></a>
If set to system, the output shows snapshots that were automatically created by MemoryDB. If set to user the output shows snapshots that were manually created. If omitted, the output shows both automatically and manually created snapshots.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeSnapshots_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Snapshots": [
      {
         "ARN": "string",
         "ClusterConfiguration": {
            "Description": "string",
            "Engine": "string",
            "EngineVersion": "string",
            "MaintenanceWindow": "string",
            "MultiRegionClusterName": "string",
            "MultiRegionParameterGroupName": "string",
            "Name": "string",
            "NodeType": "string",
            "NumShards": number,
            "ParameterGroupName": "string",
            "Port": number,
            "Shards": [
               {
                  "Configuration": {
                     "ReplicaCount": number,
                     "Slots": "string"
                  },
                  "Name": "string",
                  "Size": "string",
                  "SnapshotCreationTime": number
               }
            ],
            "SnapshotRetentionLimit": number,
            "SnapshotWindow": "string",
            "SubnetGroupName": "string",
            "TopicArn": "string",
            "VpcId": "string"
         },
         "DataTiering": "string",
         "KmsKeyId": "string",
         "Name": "string",
         "Source": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSnapshots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeSnapshots_ResponseSyntax) **   <a name="MemoryDB-DescribeSnapshots-response-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

 ** [Snapshots](#API_DescribeSnapshots_ResponseSyntax) **   <a name="MemoryDB-DescribeSnapshots-response-Snapshots"></a>
A list of snapshots. Each item in the list contains detailed information about one snapshot.
Type: Array of [Snapshot](API_Snapshot.md) objects

## Errors
<a name="API_DescribeSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

 ** SnapshotNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_DescribeSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DescribeSnapshots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DescribeSnapshots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DescribeSnapshots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DescribeSnapshots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DescribeSnapshots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DescribeSnapshots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DescribeSnapshots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DescribeSnapshots)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DescribeSnapshots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DescribeSnapshots)
