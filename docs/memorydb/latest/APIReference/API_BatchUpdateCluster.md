---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_BatchUpdateCluster.html
---

# BatchUpdateCluster
<a name="API_BatchUpdateCluster"></a>

Apply the service update to a list of clusters supplied. For more information on service updates and applying them, see [Applying the service updates](https://docs.aws.amazon.com/MemoryDB/latest/devguide/managing-updates.html#applying-updates).

## Request Syntax
<a name="API_BatchUpdateCluster_RequestSyntax"></a>

```
{
   "ClusterNames": [ "{{string}}" ],
   "ServiceUpdate": {
      "ServiceUpdateNameToApply": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_BatchUpdateCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterNames](#API_BatchUpdateCluster_RequestSyntax) **   <a name="MemoryDB-BatchUpdateCluster-request-ClusterNames"></a>
The cluster names to apply the updates.
Type: Array of strings
Array Members: Maximum number of 20 items.
Required: Yes

 ** [ServiceUpdate](#API_BatchUpdateCluster_RequestSyntax) **   <a name="MemoryDB-BatchUpdateCluster-request-ServiceUpdate"></a>
The unique ID of the service update
Type: [ServiceUpdateRequest](API_ServiceUpdateRequest.md) object
Required: No

## Response Syntax
<a name="API_BatchUpdateCluster_ResponseSyntax"></a>

```
{
   "ProcessedClusters": [
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
   "UnprocessedClusters": [
      {
         "ClusterName": "string",
         "ErrorMessage": "string",
         "ErrorType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchUpdateCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProcessedClusters](#API_BatchUpdateCluster_ResponseSyntax) **   <a name="MemoryDB-BatchUpdateCluster-response-ProcessedClusters"></a>
The list of clusters that have been updated.
Type: Array of [Cluster](API_Cluster.md) objects

 ** [UnprocessedClusters](#API_BatchUpdateCluster_ResponseSyntax) **   <a name="MemoryDB-BatchUpdateCluster-response-UnprocessedClusters"></a>
The list of clusters where updates have not been applied.
Type: Array of [UnprocessedCluster](API_UnprocessedCluster.md) objects

## Errors
<a name="API_BatchUpdateCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ServiceUpdateNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_BatchUpdateCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/BatchUpdateCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/BatchUpdateCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/BatchUpdateCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/BatchUpdateCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/BatchUpdateCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/BatchUpdateCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/BatchUpdateCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/BatchUpdateCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/BatchUpdateCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/BatchUpdateCluster)
