---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeClusters.html
---

# DescribeClusters
<a name="API_DescribeClusters"></a>

Returns information about all provisioned clusters if no cluster identifier is specified, or about a specific cluster if a cluster name is supplied.

## Request Syntax
<a name="API_DescribeClusters_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ShowShardDetails": {{boolean}}
}
```

## Request Parameters
<a name="API_DescribeClusters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_DescribeClusters_RequestSyntax) **   <a name="MemoryDB-DescribeClusters-request-ClusterName"></a>
The name of the cluster.
Type: String
Required: No

 ** [MaxResults](#API_DescribeClusters_RequestSyntax) **   <a name="MemoryDB-DescribeClusters-request-MaxResults"></a>
The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeClusters_RequestSyntax) **   <a name="MemoryDB-DescribeClusters-request-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

 ** [ShowShardDetails](#API_DescribeClusters_RequestSyntax) **   <a name="MemoryDB-DescribeClusters-request-ShowShardDetails"></a>
An optional flag that can be included in the request to retrieve information about the individual shard(s).
Type: Boolean
Required: No

## Response Syntax
<a name="API_DescribeClusters_ResponseSyntax"></a>

```
{
   "Clusters": [
      {
         "ACLName": "string",
         "ARN": "string",
         "AutoMinorVersionUpgrade": boolean,
         "AvailabilityMode": "string",
         "ClusterEndpoint": {
            "Address": "string",
            "Port": number
         },
         "DataTiering": "string",
         "Description": "string",
         "Engine": "string",
         "EnginePatchVersion": "string",
         "EngineVersion": "string",
         "IpDiscovery": "string",
         "KmsKeyId": "string",
         "MaintenanceWindow": "string",
         "MultiRegionClusterName": "string",
         "Name": "string",
         "NetworkType": "string",
         "NodeType": "string",
         "NumberOfShards": number,
         "ParameterGroupName": "string",
         "ParameterGroupStatus": "string",
         "PendingUpdates": {
            "ACLs": {
               "ACLToApply": "string"
            },
            "Resharding": {
               "SlotMigration": {
                  "ProgressPercentage": number
               }
            },
            "ServiceUpdates": [
               {
                  "ServiceUpdateName": "string",
                  "Status": "string"
               }
            ]
         },
         "SecurityGroups": [
            {
               "SecurityGroupId": "string",
               "Status": "string"
            }
         ],
         "Shards": [
            {
               "Name": "string",
               "Nodes": [
                  {
                     "AvailabilityZone": "string",
                     "CreateTime": number,
                     "Endpoint": {
                        "Address": "string",
                        "Port": number
                     },
                     "Name": "string",
                     "Status": "string"
                  }
               ],
               "NumberOfNodes": number,
               "Slots": "string",
               "Status": "string"
            }
         ],
         "SnapshotRetentionLimit": number,
         "SnapshotWindow": "string",
         "SnsTopicArn": "string",
         "SnsTopicStatus": "string",
         "Status": "string",
         "SubnetGroupName": "string",
         "TLSEnabled": boolean
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeClusters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Clusters](#API_DescribeClusters_ResponseSyntax) **   <a name="MemoryDB-DescribeClusters-response-Clusters"></a>
A list of clusters
Type: Array of [Cluster](API_Cluster.md) objects

 ** [NextToken](#API_DescribeClusters_ResponseSyntax) **   <a name="MemoryDB-DescribeClusters-response-NextToken"></a>
An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

## Errors
<a name="API_DescribeClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFoundFault **

HTTP Status Code: 400

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_DescribeClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DescribeClusters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DescribeClusters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DescribeClusters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DescribeClusters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DescribeClusters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DescribeClusters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DescribeClusters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DescribeClusters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DescribeClusters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DescribeClusters)
