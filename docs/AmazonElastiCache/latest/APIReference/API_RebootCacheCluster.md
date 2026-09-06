---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_RebootCacheCluster.html
---

# RebootCacheCluster
<a name="API_RebootCacheCluster"></a>

Reboots some, or all, of the cache nodes within a provisioned cluster. This operation applies any modified cache parameter groups to the cluster. The reboot operation takes place as soon as possible, and results in a momentary outage to the cluster. During the reboot, the cluster status is set to REBOOTING.

The reboot causes the contents of the cache (for each cache node being rebooted) to be lost.

When the reboot is complete, a cluster event is created.

Rebooting a cluster is currently supported on Memcached, Valkey and Redis OSS (cluster mode disabled) clusters. Rebooting is not supported on Valkey or Redis OSS (cluster mode enabled) clusters.

If you make changes to parameters that require a Valkey or Redis OSS (cluster mode enabled) cluster reboot for the changes to be applied, see [Rebooting a Cluster](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/nodes.rebooting.html) for an alternate process.

## Request Parameters
<a name="API_RebootCacheCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheClusterId **
The cluster identifier. This parameter is stored as a lowercase string.
Type: String
Required: Yes

 **CacheNodeIdsToReboot.CacheNodeId.N**
A list of cache node IDs to reboot. A node ID is a numeric identifier (0001, 0002, etc.). To reboot an entire cluster, specify all of the cache node IDs.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_RebootCacheCluster_ResponseElements"></a>

The following element is returned by the service.

 ** CacheCluster **
Contains all of the attributes of a specific cluster.
Type: [CacheCluster](API_CacheCluster.md) object

## Errors
<a name="API_RebootCacheCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CacheClusterNotFound **
The requested cluster ID does not refer to an existing cluster.
HTTP Status Code: 404

 ** InvalidCacheClusterState **
The requested cluster is not in the `available` state.
HTTP Status Code: 400

## Examples
<a name="API_RebootCacheCluster_Examples"></a>

### RebootCacheCluster
<a name="API_RebootCacheCluster_Example_1"></a>

This example illustrates one usage of RebootCacheCluster.

#### Sample Request
<a name="API_RebootCacheCluster_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=RebootCacheCluster
   &CacheClusterId=mycache
   &CacheNodeIdsToReboot.CacheNodeId.1=0001
   &CacheNodeIdsToReboot.CacheNodeId.2=0002
   &CacheNodeIdsToReboot.CacheNodeId.3=0003
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_RebootCacheCluster_Example_1_Response"></a>

```
<RebootCacheClusterResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
   <RebootCacheClusterResult>
      <CacheCluster>
         <CacheClusterStatus>rebooting cluster nodes</CacheClusterStatus>
         <CacheParameterGroup>
            <CacheParameterGroupName>default.memcached1.4</CacheParameterGroupName>
            <ParameterApplyStatus>in-sync</ParameterApplyStatus>
            <CacheNodeIdsToReboot />
         </CacheParameterGroup>
         <CacheClusterId>mycache</CacheClusterId>
         <ConfigurationEndpoint>
            <Port>11211</Port>
            <Address>mycache.q68zge.cfg.use1devo.elmo-dev.amazonaws.com</Address>
         </ConfigurationEndpoint>
         <CacheNodeType>cache.m1.small</CacheNodeType>
         <Engine>memcached</Engine>
         <PendingModifiedValues />
         <PreferredAvailabilityZone>us-west-2b</PreferredAvailabilityZone>
         <CacheClusterCreateTime>2015-02-02T19:04:12.812Z</CacheClusterCreateTime>
         <EngineVersion>1.4.17</EngineVersion>
         <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
         <PreferredMaintenanceWindow>wed:09:00-wed:10:00</PreferredMaintenanceWindow>
         <ClientDownloadLandingPage>https://console.aws.amazon.com/elasticache/home#client-download:</ClientDownloadLandingPage>
         <CacheSecurityGroups>
            <CacheSecurityGroup>
               <CacheSecurityGroupName>default</CacheSecurityGroupName>
               <Status>active</Status>
            </CacheSecurityGroup>
         </CacheSecurityGroups>
         <NumCacheNodes>3</NumCacheNodes>
      </CacheCluster>
   </RebootCacheClusterResult>
   <ResponseMetadata>
      <RequestId>cf7e6fc4-b9d1-11e3-8a16-7978bb24ffdf</RequestId>
   </ResponseMetadata>
</RebootCacheClusterResponse>
```

## See Also
<a name="API_RebootCacheCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/RebootCacheCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/RebootCacheCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/RebootCacheCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/RebootCacheCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/RebootCacheCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/RebootCacheCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/RebootCacheCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/RebootCacheCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/RebootCacheCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/RebootCacheCluster)
