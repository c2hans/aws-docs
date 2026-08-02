---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html
---

# ModifyCacheCluster
<a name="API_ModifyCacheCluster"></a>

Modifies the settings for a cluster. You can use this operation to change one or more cluster configuration parameters by specifying the parameters and the new values.

## Request Parameters
<a name="API_ModifyCacheCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheClusterId **
The cluster identifier. This value is stored as a lowercase string.
Type: String
Required: Yes

 ** ApplyImmediately **
If `true`, this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the `PreferredMaintenanceWindow` setting for the cluster.
If `false`, changes to the cluster are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.
If you perform a `ModifyCacheCluster` before a pending modification is applied, the pending modification is replaced by the newer modification.
Valid values: `true` \| `false`
Default: `false`
Type: Boolean
Required: No

 ** AuthToken **
Reserved parameter. The password used to access a password protected server. This parameter must be specified with the `auth-token-update` parameter. Password constraints:
+ Must be only printable ASCII characters
+ Must be at least 16 characters and no more than 128 characters in length
+ Cannot contain any of the following characters: '/', '"', or '@', '%'
 For more information, see AUTH password at [AUTH](http://redis.io/commands/AUTH).
Type: String
Required: No

 ** AuthTokenUpdateStrategy **
Specifies the strategy to use to update the AUTH token. This parameter must be specified with the `auth-token` parameter. Possible values:
+ ROTATE - default, if no update strategy is provided
+ SET - allowed only after ROTATE
+ DELETE - allowed only when transitioning to RBAC
 For more information, see [Authenticating Users with AUTH](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth.html)
Type: String
Valid Values: `SET | ROTATE | DELETE`
Required: No

 ** AutoMinorVersionUpgrade **
 If you are running Valkey 7.2 or Redis OSS engine version 6.0 or later, set this parameter to yes to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions.
Type: Boolean
Required: No

 ** AZMode **
Specifies whether the new nodes in this Memcached cluster are all created in a single Availability Zone or created across multiple Availability Zones.
Valid values: `single-az` \| `cross-az`.
This option is only supported for Memcached clusters.
You cannot specify `single-az` if the Memcached cluster already has cache nodes in different Availability Zones. If `cross-az` is specified, existing Memcached nodes remain in their current Availability Zone.
Only newly created nodes are located in different Availability Zones.
Type: String
Valid Values: `single-az | cross-az`
Required: No

 **CacheNodeIdsToRemove.CacheNodeId.N**
A list of cache node IDs to be removed. A node ID is a numeric identifier (0001, 0002, etc.). This parameter is only valid when `NumCacheNodes` is less than the existing number of cache nodes. The number of cache node IDs supplied in this parameter must match the difference between the existing number of cache nodes in the cluster or pending cache nodes, whichever is greater, and the value of `NumCacheNodes` in the request.
For example: If you have 3 active cache nodes, 7 pending cache nodes, and the number of cache nodes in this `ModifyCacheCluster` call is 5, you must list 2 (7 - 5) cache node IDs to remove.
Type: Array of strings
Required: No

 ** CacheNodeType **
A valid cache node type that you want to scale this cluster up to.
Type: String
Required: No

 ** CacheParameterGroupName **
The name of the cache parameter group to apply to this cluster. This change is asynchronously applied as soon as possible for parameters when the `ApplyImmediately` parameter is specified as `true` for this request.
Type: String
Required: No

 **CacheSecurityGroupNames.CacheSecurityGroupName.N**
A list of cache security group names to authorize on this cluster. This change is asynchronously applied as soon as possible.
You can use this parameter only with clusters that are created outside of an Amazon Virtual Private Cloud (Amazon VPC).
Constraints: Must contain no more than 255 alphanumeric characters. Must not be "Default".
Type: Array of strings
Required: No

 ** Engine **
The engine type used by the cache cluster. The options are valkey, memcached or redis.
Type: String
Required: No

 ** EngineVersion **
The upgraded version of the cache engine to be run on the cache nodes.
 **Important:** You can upgrade to a newer engine version (see [Selecting a Cache Engine and Version](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html#VersionManagement)), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster and create it anew with the earlier engine version.
Type: String
Required: No

 ** IpDiscovery **
The network type you choose when modifying a cluster, either `ipv4` \| `ipv6`. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/).
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 **LogDeliveryConfigurations.LogDeliveryConfigurationRequest.N**
Specifies the destination, format and type of the logs.
Type: Array of [LogDeliveryConfigurationRequest](API_LogDeliveryConfigurationRequest.md) objects
Required: No

 **NewAvailabilityZones.PreferredAvailabilityZone.N**
This option is only supported on Memcached clusters.
The list of Availability Zones where the new Memcached cache nodes are created.
This parameter is only valid when `NumCacheNodes` in the request is greater than the sum of the number of active cache nodes and the number of cache nodes pending creation (which may be zero). The number of Availability Zones supplied in this list must match the cache nodes being added in this request.
Scenarios:
+  **Scenario 1:** You have 3 active nodes and wish to add 2 nodes. Specify `NumCacheNodes=5` (3 \+ 2) and optionally specify two Availability Zones for the two new nodes.
+  **Scenario 2:** You have 3 active nodes and 2 nodes pending creation (from the scenario 1 call) and want to add 1 more node. Specify `NumCacheNodes=6` ((3 \+ 2) \+ 1) and optionally specify an Availability Zone for the new node.
+  **Scenario 3:** You want to cancel all pending operations. Specify `NumCacheNodes=3` to cancel all pending operations.
The Availability Zone placement of nodes pending creation cannot be modified. If you wish to cancel any nodes pending creation, add 0 nodes by setting `NumCacheNodes` to the number of current nodes.
If `cross-az` is specified, existing Memcached nodes remain in their current Availability Zone. Only newly created nodes can be located in different Availability Zones. For guidance on how to move existing Memcached nodes to different Availability Zones, see the **Availability Zone Considerations** section of [Cache Node Considerations for Memcached](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html).
 **Impact of new add/remove requests upon pending requests**
+ Scenario-1
  + Pending Action: Delete
  + New Request: Delete
  + Result: The new delete, pending or immediate, replaces the pending delete.
+ Scenario-2
  + Pending Action: Delete
  + New Request: Create
  + Result: The new create, pending or immediate, replaces the pending delete.
+ Scenario-3
  + Pending Action: Create
  + New Request: Delete
  + Result: The new delete, pending or immediate, replaces the pending create.
+ Scenario-4
  + Pending Action: Create
  + New Request: Create
  + Result: The new create is added to the pending create.
**Important**
 **Important:** If the new create request is **Apply Immediately - Yes**, all creates are performed immediately. If the new create request is **Apply Immediately - No**, all creates are pending.
Type: Array of strings
Required: No

 ** NotificationTopicArn **
The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.
The Amazon SNS topic owner must be same as the cluster owner.
Type: String
Required: No

 ** NotificationTopicStatus **
The status of the Amazon SNS notification topic. Notifications are sent only if the status is `active`.
Valid values: `active` \| `inactive`
Type: String
Required: No

 ** NumCacheNodes **
The number of cache nodes that the cluster should have. If the value for `NumCacheNodes` is greater than the sum of the number of current cache nodes and the number of cache nodes pending creation (which may be zero), more nodes are added. If the value is less than the number of existing cache nodes, nodes are removed. If the value is equal to the number of current cache nodes, any pending add or remove requests are canceled.
If you are removing cache nodes, you must use the `CacheNodeIdsToRemove` parameter to provide the IDs of the specific cache nodes to remove.
For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.
Adding or removing Memcached cache nodes can be applied immediately or as a pending operation (see `ApplyImmediately`).
A pending operation to modify the number of cache nodes in a cluster during its maintenance window, whether by adding or removing nodes in accordance with the scale out architecture, is not queued. The customer's latest request to add or remove nodes to the cluster overrides any previous pending operations to modify the number of cache nodes in the cluster. For example, a request to remove 2 nodes would override a previous pending operation to remove 3 nodes. Similarly, a request to add 2 nodes would override a previous pending operation to remove 3 nodes and vice versa. As Memcached cache nodes may now be provisioned in different Availability Zones with flexible cache node placement, a request to add nodes does not automatically override a previous pending operation to add nodes. The customer can modify the previous pending operation to add more nodes or explicitly cancel the pending request and retry the new request. To cancel pending operations to modify the number of cache nodes in a cluster, use the `ModifyCacheCluster` request and set `NumCacheNodes` equal to the number of cache nodes currently in the cluster.
Type: Integer
Required: No

 ** PreferredMaintenanceWindow **
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

 ** ScaleConfig **
Configures horizontal or vertical scaling for Memcached clusters, specifying the scaling percentage and interval.
Type: [ScaleConfig](API_ScaleConfig.md) object
Required: No

 **SecurityGroupIds.SecurityGroupId.N**
Specifies the VPC Security Groups associated with the cluster.
This parameter can be used only with clusters that are created in an Amazon Virtual Private Cloud (Amazon VPC).
Type: Array of strings
Required: No

 ** SnapshotRetentionLimit **
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set `SnapshotRetentionLimit` to 5, a snapshot that was taken today is retained for 5 days before being deleted.
If the value of `SnapshotRetentionLimit` is set to zero (0), backups are turned off.
Type: Integer
Required: No

 ** SnapshotWindow **
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.
Type: String
Required: No

## Response Elements
<a name="API_ModifyCacheCluster_ResponseElements"></a>

The following element is returned by the service.

 ** CacheCluster **
Contains all of the attributes of a specific cluster.
Type: [CacheCluster](API_CacheCluster.md) object

## Errors
<a name="API_ModifyCacheCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CacheClusterNotFound **
The requested cluster ID does not refer to an existing cluster.
HTTP Status Code: 404

 ** CacheParameterGroupNotFound **
The requested cache parameter group name does not refer to an existing cache parameter group.
HTTP Status Code: 404

 ** CacheSecurityGroupNotFound **
The requested cache security group name does not refer to an existing cache security group.
HTTP Status Code: 404

 ** InsufficientCacheClusterCapacity **
The requested cache node type is not available in the specified Availability Zone. For more information, see [InsufficientCacheClusterCapacity](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ErrorMessages.html#ErrorMessages.INSUFFICIENT_CACHE_CLUSTER_CAPACITY) in the ElastiCache User Guide.
HTTP Status Code: 400

 ** InvalidCacheClusterState **
The requested cluster is not in the `available` state.
HTTP Status Code: 400

 ** InvalidCacheSecurityGroupState **
The current state of the cache security group does not allow deletion.
HTTP Status Code: 400

 ** InvalidParameterCombination **
Two or more incompatible parameters were specified.
 ** message **
Two or more parameters that must not be used together were used together.
HTTP Status Code: 400

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** InvalidVPCNetworkStateFault **
The VPC network is in an invalid state.
HTTP Status Code: 400

 ** NodeQuotaForClusterExceeded **
The request cannot be processed because it would exceed the allowed number of cache nodes in a single cluster.
HTTP Status Code: 400

 ** NodeQuotaForCustomerExceeded **
The request cannot be processed because it would exceed the allowed number of cache nodes per customer.
HTTP Status Code: 400

## Examples
<a name="API_ModifyCacheCluster_Examples"></a>

### ModifyCacheCluster
<a name="API_ModifyCacheCluster_Example_1"></a>

This example illustrates one usage of ModifyCacheCluster.

#### Sample Request
<a name="API_ModifyCacheCluster_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=ModifyCacheCluster
   NumCacheNodes=5
   &CacheClusterId=simcoprod01
   &ApplyImmediately=true
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_ModifyCacheCluster_Example_1_Response"></a>

```
<ModifyCacheClusterResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
  <ModifyCacheClusterResult>
    <CacheCluster>
      <CacheParameterGroup>
        <ParameterApplyStatus>in-sync</ParameterApplyStatus>
        <CacheParameterGroupName>default.memcached1.4</CacheParameterGroupName>
        <CacheNodeIdsToReboot/>
      </CacheParameterGroup>
      <CacheClusterId>simcoprod01</CacheClusterId>
      <CacheClusterStatus>available</CacheClusterStatus>
      <ConfigurationEndpoint>
        <Port>11211</Port>
        <Address>simcoprod01.m2st2p.cfg.cache.amazonaws.com</Address>
      </ConfigurationEndpoint>
      <CacheNodeType>cache.m1.large</CacheNodeType>
      <Engine>memcached</Engine>
      <PendingModifiedValues>
        <NumCacheNodes>5</NumCacheNodes>
      </PendingModifiedValues>
      <PreferredAvailabilityZone>us-west-2b</PreferredAvailabilityZone>
      <CacheClusterCreateTime>2015-02-02T23:45:20.937Z</CacheClusterCreateTime>
      <EngineVersion>1.4.5</EngineVersion>
      <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
      <PreferredMaintenanceWindow>fri:04:30-fri:05:30</PreferredMaintenanceWindow>
      <CacheSecurityGroups>
        <CacheSecurityGroup>
          <CacheSecurityGroupName>default</CacheSecurityGroupName>
          <Status>active</Status>
        </CacheSecurityGroup>
      </CacheSecurityGroups>
      <NumCacheNodes>3</NumCacheNodes>
    </CacheCluster>
  </ModifyCacheClusterResult>
  <ResponseMetadata>
    <RequestId>d5786c6d-b7fe-11e0-9326-b7275b9d4a6c</RequestId>
  </ResponseMetadata>
</ModifyCacheClusterResponse>
```

## See Also
<a name="API_ModifyCacheCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/ModifyCacheCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/ModifyCacheCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ModifyCacheCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/ModifyCacheCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ModifyCacheCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/ModifyCacheCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/ModifyCacheCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/ModifyCacheCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/ModifyCacheCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ModifyCacheCluster)
