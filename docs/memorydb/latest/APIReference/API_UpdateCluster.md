---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateCluster.html
---

# UpdateCluster
<a name="API_UpdateCluster"></a>

Modifies the settings for a cluster. You can use this operation to change one or more cluster configuration settings by specifying the settings and the new values.

## Request Syntax
<a name="API_UpdateCluster_RequestSyntax"></a>

```
{
   "ACLName": "{{string}}",
   "ClusterName": "{{string}}",
   "Description": "{{string}}",
   "Engine": "{{string}}",
   "EngineVersion": "{{string}}",
   "IpDiscovery": "{{string}}",
   "MaintenanceWindow": "{{string}}",
   "NodeType": "{{string}}",
   "ParameterGroupName": "{{string}}",
   "ReplicaConfiguration": {
      "ReplicaCount": {{number}}
   },
   "SecurityGroupIds": [ "{{string}}" ],
   "ShardConfiguration": {
      "ShardCount": {{number}}
   },
   "SnapshotRetentionLimit": {{number}},
   "SnapshotWindow": "{{string}}",
   "SnsTopicArn": "{{string}}",
   "SnsTopicStatus": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ACLName](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-ACLName"></a>
The Access Control List that is associated with the cluster.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

 ** [ClusterName](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-ClusterName"></a>
The name of the cluster to update.
Type: String
Required: Yes

 ** [Description](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-Description"></a>
The description of the cluster to update.
Type: String
Required: No

 ** [Engine](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-Engine"></a>
The name of the engine to be used for the cluster.
Type: String
Required: No

 ** [EngineVersion](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-EngineVersion"></a>
The upgraded version of the engine to be run on the nodes. You can upgrade to a newer engine version, but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster and create it anew with the earlier engine version.
Type: String
Required: No

 ** [IpDiscovery](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-IpDiscovery"></a>
The mechanism for discovering IP addresses for the cluster discovery protocol. Valid values are 'ipv4' or 'ipv6'. When set to 'ipv4', cluster discovery functions such as cluster slots, cluster shards, and cluster nodes will return IPv4 addresses for cluster nodes. When set to 'ipv6', the cluster discovery functions return IPv6 addresses for cluster nodes. The value must be compatible with the NetworkType parameter. If not specified, the default is 'ipv4'.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** [MaintenanceWindow](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-MaintenanceWindow"></a>
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

 ** [NodeType](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-NodeType"></a>
A valid node type that you want to scale this cluster up or down to.
Type: String
Required: No

 ** [ParameterGroupName](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-ParameterGroupName"></a>
The name of the parameter group to update.
Type: String
Required: No

 ** [ReplicaConfiguration](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-ReplicaConfiguration"></a>
The number of replicas that will reside in each shard.
Type: [ReplicaConfigurationRequest](API_ReplicaConfigurationRequest.md) object
Required: No

 ** [SecurityGroupIds](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-SecurityGroupIds"></a>
The SecurityGroupIds to update.
Type: Array of strings
Required: No

 ** [ShardConfiguration](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-ShardConfiguration"></a>
The number of shards in the cluster.
Type: [ShardConfigurationRequest](API_ShardConfigurationRequest.md) object
Required: No

 ** [SnapshotRetentionLimit](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-SnapshotRetentionLimit"></a>
The number of days for which MemoryDB retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.
Type: Integer
Required: No

 ** [SnapshotWindow](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-SnapshotWindow"></a>
The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your cluster.
Type: String
Required: No

 ** [SnsTopicArn](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-SnsTopicArn"></a>
The SNS topic ARN to update.
Type: String
Required: No

 ** [SnsTopicStatus](#API_UpdateCluster_RequestSyntax) **   <a name="MemoryDB-UpdateCluster-request-SnsTopicStatus"></a>
The status of the Amazon SNS notification topic. Notifications are sent only if the status is active.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateCluster_ResponseSyntax"></a>

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
<a name="API_UpdateCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Cluster](#API_UpdateCluster_ResponseSyntax) **   <a name="MemoryDB-UpdateCluster-response-Cluster"></a>
The updated cluster.
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_UpdateCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ACLNotFoundFault **

HTTP Status Code: 400

 ** ClusterNotFoundFault **

HTTP Status Code: 400

 ** ClusterQuotaForCustomerExceededFault **

HTTP Status Code: 400

 ** InvalidACLStateFault **

HTTP Status Code: 400

 ** InvalidClusterStateFault **

HTTP Status Code: 400

 ** InvalidKMSKeyFault **

HTTP Status Code: 400

 ** InvalidNodeStateFault **

HTTP Status Code: 400

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** InvalidVPCNetworkStateFault **

HTTP Status Code: 400

 ** NodeQuotaForClusterExceededFault **

HTTP Status Code: 400

 ** NodeQuotaForCustomerExceededFault **

HTTP Status Code: 400

 ** NoOperationFault **

HTTP Status Code: 400

 ** ParameterGroupNotFoundFault **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

 ** ShardsPerClusterQuotaExceededFault **

HTTP Status Code: 400

## See Also
<a name="API_UpdateCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/UpdateCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/UpdateCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/UpdateCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/UpdateCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/UpdateCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/UpdateCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/UpdateCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/UpdateCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/UpdateCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/UpdateCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
