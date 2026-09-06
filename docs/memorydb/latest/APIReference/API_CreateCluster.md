---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateCluster.html
---

# CreateCluster
<a name="API_CreateCluster"></a>

Creates a cluster. All nodes in the cluster run the same protocol-compliant engine software.

## Request Syntax
<a name="API_CreateCluster_RequestSyntax"></a>

```
{
   "ACLName": "{{string}}",
   "AutoMinorVersionUpgrade": {{boolean}},
   "ClusterName": "{{string}}",
   "DataTiering": {{boolean}},
   "Description": "{{string}}",
   "Engine": "{{string}}",
   "EngineVersion": "{{string}}",
   "IpDiscovery": "{{string}}",
   "KmsKeyId": "{{string}}",
   "MaintenanceWindow": "{{string}}",
   "MultiRegionClusterName": "{{string}}",
   "NetworkType": "{{string}}",
   "NodeType": "{{string}}",
   "NumReplicasPerShard": {{number}},
   "NumShards": {{number}},
   "ParameterGroupName": "{{string}}",
   "Port": {{number}},
   "SecurityGroupIds": [ "{{string}}" ],
   "SnapshotArns": [ "{{string}}" ],
   "SnapshotName": "{{string}}",
   "SnapshotRetentionLimit": {{number}},
   "SnapshotWindow": "{{string}}",
   "SnsTopicArn": "{{string}}",
   "SubnetGroupName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TLSEnabled": {{boolean}}
}
```

## Request Parameters
<a name="API_CreateCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ACLName](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-ACLName"></a>
The name of the Access Control List to associate with the cluster.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: Yes

 ** [AutoMinorVersionUpgrade](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-AutoMinorVersionUpgrade"></a>
When set to true, the cluster will automatically receive minor engine version upgrades after launch.
Type: Boolean
Required: No

 ** [ClusterName](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-ClusterName"></a>
The name of the cluster. This value must be unique as it also serves as the cluster identifier. This value is stored as a lowercase string.
Type: String
Required: Yes

 ** [DataTiering](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-DataTiering"></a>
Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html).
Type: Boolean
Required: No

 ** [Description](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-Description"></a>
An optional description of the cluster.
Type: String
Required: No

 ** [Engine](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-Engine"></a>
The name of the engine to be used for the cluster.
Type: String
Required: No

 ** [EngineVersion](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-EngineVersion"></a>
The version number of the Redis OSS engine to be used for the cluster.
Type: String
Required: No

 ** [IpDiscovery](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-IpDiscovery"></a>
The mechanism for discovering IP addresses for the cluster discovery protocol. Valid values are 'ipv4' or 'ipv6'. When set to 'ipv4', cluster discovery functions such as cluster slots, cluster shards, and cluster nodes return IPv4 addresses for cluster nodes. When set to 'ipv6', the cluster discovery functions return IPv6 addresses for cluster nodes. The value must be compatible with the NetworkType parameter. If not specified, the default is 'ipv4'.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** [KmsKeyId](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-KmsKeyId"></a>
The ID of the KMS key used to encrypt the cluster.
Type: String
Required: No

 ** [MaintenanceWindow](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-MaintenanceWindow"></a>
Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
Valid values for `ddd` are:
+  `sun`
+  `mon`
+  `tue`
+  `wed`
+  `thu`
+  `fri`
+  `sat`
Example: `sun:23:00-mon:01:30`
Type: String
Required: No

 ** [MultiRegionClusterName](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-MultiRegionClusterName"></a>
The name of the multi-Region cluster to be created.
Type: String
Required: No

 ** [NetworkType](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-NetworkType"></a>
Specifies the IP address type for the cluster. Valid values are 'ipv4', 'ipv6', or 'dual\_stack'. When set to 'ipv4', the cluster will only be accessible via IPv4 addresses. When set to 'ipv6', the cluster will only be accessible via IPv6 addresses. When set to 'dual\_stack', the cluster will be accessible via both IPv4 and IPv6 addresses. If not specified, the default is 'ipv4'.
Type: String
Valid Values: `ipv4 | ipv6 | dual_stack`
Required: No

 ** [NodeType](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-NodeType"></a>
The compute and memory capacity of the nodes in the cluster.
Type: String
Required: Yes

 ** [NumReplicasPerShard](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-NumReplicasPerShard"></a>
The number of replicas to apply to each shard. The default value is 1. The maximum is 5.
Type: Integer
Required: No

 ** [NumShards](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-NumShards"></a>
The number of shards the cluster will contain. The default value is 1.
Type: Integer
Required: No

 ** [ParameterGroupName](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-ParameterGroupName"></a>
The name of the parameter group associated with the cluster.
Type: String
Required: No

 ** [Port](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-Port"></a>
The port number on which each of the nodes accepts connections.
Type: Integer
Required: No

 ** [SecurityGroupIds](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-SecurityGroupIds"></a>
A list of security group names to associate with this cluster.
Type: Array of strings
Required: No

 ** [SnapshotArns](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-SnapshotArns"></a>
A list of Amazon Resource Names (ARN) that uniquely identify the RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new cluster. The Amazon S3 object name in the ARN cannot contain any commas.
Type: Array of strings
Required: No

 ** [SnapshotName](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-SnapshotName"></a>
The name of a snapshot from which to restore data into the new cluster. The snapshot status changes to restoring while the new cluster is being created.
Type: String
Required: No

 ** [SnapshotRetentionLimit](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-SnapshotRetentionLimit"></a>
The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.
Type: Integer
Required: No

 ** [SnapshotWindow](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-SnapshotWindow"></a>
The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard.
 Example: 05:00-09:00
 If you do not specify this parameter, MemoryDB automatically chooses an appropriate time range.
Type: String
Required: No

 ** [SnsTopicArn](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-SnsTopicArn"></a>
The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.
Type: String
Required: No

 ** [SubnetGroupName](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-SubnetGroupName"></a>
The name of the subnet group to be used for the cluster.
Type: String
Required: No

 ** [Tags](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-Tags"></a>
A list of tags to be added to this resource. Tags are comma-separated key,value pairs (e.g. Key=myKey, Value=myKeyValue. You can include multiple tags as shown following: Key=myKey, Value=myKeyValue Key=mySecondKey, Value=mySecondKeyValue.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** [TLSEnabled](#API_CreateCluster_RequestSyntax) **   <a name="MemoryDB-CreateCluster-request-TLSEnabled"></a>
A flag to enable in-transit encryption on the cluster.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateCluster_ResponseSyntax"></a>

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
<a name="API_CreateCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Cluster](#API_CreateCluster_ResponseSyntax) **   <a name="MemoryDB-CreateCluster-response-Cluster"></a>
The newly-created cluster.
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_CreateCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ACLNotFoundFault **

HTTP Status Code: 400

 ** ClusterAlreadyExistsFault **

HTTP Status Code: 400

 ** ClusterQuotaForCustomerExceededFault **

HTTP Status Code: 400

 ** InsufficientClusterCapacityFault **

HTTP Status Code: 400

 ** InvalidACLStateFault **

HTTP Status Code: 400

 ** InvalidCredentialsException **

HTTP Status Code: 400

 ** InvalidMultiRegionClusterStateFault **
The requested operation cannot be performed on the multi-Region cluster in its current state.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** InvalidVPCNetworkStateFault **

HTTP Status Code: 400

 ** MultiRegionClusterNotFoundFault **
The specified multi-Region cluster does not exist.
HTTP Status Code: 400

 ** NodeQuotaForClusterExceededFault **

HTTP Status Code: 400

 ** NodeQuotaForCustomerExceededFault **

HTTP Status Code: 400

 ** ParameterGroupNotFoundFault **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

 ** ShardsPerClusterQuotaExceededFault **

HTTP Status Code: 400

 ** SubnetGroupNotFoundFault **

HTTP Status Code: 400

 ** TagQuotaPerResourceExceeded **

HTTP Status Code: 400

## See Also
<a name="API_CreateCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/CreateCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/CreateCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/CreateCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/CreateCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/CreateCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/CreateCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/CreateCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/CreateCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/CreateCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/CreateCluster)
