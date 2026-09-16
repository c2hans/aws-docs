---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteCacheCluster.html
---

# DeleteCacheCluster
<a name="API_DeleteCacheCluster"></a>

Deletes a previously provisioned cluster. `DeleteCacheCluster` deletes all associated cache nodes, node endpoints and the cluster itself. When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the cluster; you cannot cancel or revert this operation.

This operation is not valid for:
+ Valkey or Redis OSS (cluster mode enabled) clusters
+ Valkey or Redis OSS (cluster mode disabled) clusters
+ A cluster that is the last read replica of a replication group
+ A cluster that is the primary node of a replication group
+ A node group (shard) that has Multi-AZ mode enabled
+ A cluster from a Valkey or Redis OSS (cluster mode enabled) replication group
+ A cluster that is not in the `available` state

## Request Parameters
<a name="API_DeleteCacheCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheClusterId **
The cluster identifier for the cluster to be deleted. This parameter is not case sensitive.
Type: String
Required: Yes

 ** FinalSnapshotIdentifier **
The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. ElastiCache creates the snapshot, and then deletes the cluster immediately afterward.
Type: String
Required: No

## Response Elements
<a name="API_DeleteCacheCluster_ResponseElements"></a>

The following element is returned by the service.

 ** CacheCluster **
Contains all of the attributes of a specific cluster.
Type: [CacheCluster](API_CacheCluster.md) object

## Errors
<a name="API_DeleteCacheCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CacheClusterNotFound **
The requested cluster ID does not refer to an existing cluster.
HTTP Status Code: 404

 ** InvalidCacheClusterState **
The requested cluster is not in the `available` state.
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

 ** SnapshotAlreadyExistsFault **
You already have a snapshot with the given name.
HTTP Status Code: 400

 ** SnapshotFeatureNotSupportedFault **
You attempted one of the following operations:
+ Creating a snapshot of a Valkey or Redis OSS cluster running on a `cache.t1.micro` cache node.
+ Creating a snapshot of a cluster that is running Memcached rather than Valkey or Redis OSS.
Neither of these are supported by ElastiCache.
HTTP Status Code: 400

 ** SnapshotQuotaExceededFault **
The request cannot be processed because it would exceed the maximum number of snapshots.
HTTP Status Code: 400

## Examples
<a name="API_DeleteCacheCluster_Examples"></a>

### DeleteCacheCluster
<a name="API_DeleteCacheCluster_Example_1"></a>

This example illustrates one usage of DeleteCacheCluster.

#### Sample Request
<a name="API_DeleteCacheCluster_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=DeleteCacheCluster
   &CacheClusterId=simcoprod43
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_DeleteCacheCluster_Example_1_Response"></a>

```
<DeleteCacheClusterResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
   <DeleteCacheClusterResult>
      <CacheCluster>
         <CacheParameterGroup>
            <ParameterApplyStatus>in-sync</ParameterApplyStatus>
            <CacheParameterGroupName>default.memcached1.4</CacheParameterGroupName>
            <CacheNodeIdsToReboot/>
         </CacheParameterGroup>
         <CacheClusterId>simcoprod43</CacheClusterId>
         <CacheClusterStatus>deleting</CacheClusterStatus>
         <ConfigurationEndpoint>
            <Port>11211</Port>
            <Address>simcoprod43.m2st2p.cfg.cache.amazonaws.com</Address>
         </ConfigurationEndpoint>
         <CacheNodeType>cache.m1.large</CacheNodeType>
         <Engine>memcached</Engine>
         <PendingModifiedValues/>
         <PreferredAvailabilityZone>us-west-2b</PreferredAvailabilityZone>
         <CacheClusterCreateTime>2015-02-02T02:18:26.497Z</CacheClusterCreateTime>
         <EngineVersion>1.4.5</EngineVersion>
         <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
         <PreferredMaintenanceWindow>mon:05:00-mon:06:00</PreferredMaintenanceWindow>
         <CacheSecurityGroups>
            <CacheSecurityGroup>
               <CacheSecurityGroupName>default</CacheSecurityGroupName>
               <Status>active</Status>
            </CacheSecurityGroup>
         </CacheSecurityGroups>
         <NumCacheNodes>3</NumCacheNodes>
      </CacheCluster>
   </DeleteCacheClusterResult>
   <ResponseMetadata>
      <RequestId>ab84aa7e-b7fa-11e0-9b0b-a9261be2b354</RequestId>
   </ResponseMetadata>
</DeleteCacheClusterResponse>
```

## See Also
<a name="API_DeleteCacheCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DeleteCacheCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DeleteCacheCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DeleteCacheCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DeleteCacheCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DeleteCacheCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DeleteCacheCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DeleteCacheCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DeleteCacheCluster)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DeleteCacheCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DeleteCacheCluster)
