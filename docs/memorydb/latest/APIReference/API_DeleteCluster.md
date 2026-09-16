---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteCluster.html
---

# DeleteCluster
<a name="API_DeleteCluster"></a>

Deletes a cluster. It also deletes all associated nodes and node endpoints.

**Note**
 `CreateSnapshot` permission is required to create a final snapshot. Without this permission, the API call will fail with an `Access Denied` exception.

## Request Syntax
<a name="API_DeleteCluster_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "FinalSnapshotName": "{{string}}",
   "MultiRegionClusterName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_DeleteCluster_RequestSyntax) **   <a name="MemoryDB-DeleteCluster-request-ClusterName"></a>
The name of the cluster to be deleted
Type: String
Required: Yes

 ** [FinalSnapshotName](#API_DeleteCluster_RequestSyntax) **   <a name="MemoryDB-DeleteCluster-request-FinalSnapshotName"></a>
The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. MemoryDB creates the snapshot, and then deletes the cluster immediately afterward.
Type: String
Required: No

 ** [MultiRegionClusterName](#API_DeleteCluster_RequestSyntax) **   <a name="MemoryDB-DeleteCluster-request-MultiRegionClusterName"></a>
The name of the multi-Region cluster to be deleted.
Type: String
Required: No

## Response Syntax
<a name="API_DeleteCluster_ResponseSyntax"></a>

```
{
   "Cluster": {
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
}
```

## Response Elements
<a name="API_DeleteCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Cluster](#API_DeleteCluster_ResponseSyntax) **   <a name="MemoryDB-DeleteCluster-response-Cluster"></a>
The cluster object that has been deleted.
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_DeleteCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFoundFault **

HTTP Status Code: 400

 ** InvalidClusterStateFault **

HTTP Status Code: 400

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

 ** SnapshotAlreadyExistsFault **

HTTP Status Code: 400

## See Also
<a name="API_DeleteCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DeleteCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DeleteCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DeleteCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DeleteCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DeleteCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DeleteCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DeleteCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DeleteCluster)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DeleteCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DeleteCluster)
