---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeCacheClusters.html
---

# DescribeCacheClusters
<a name="API_DescribeCacheClusters"></a>

Returns information about all provisioned clusters if no cluster identifier is specified, or about a specific cache cluster if a cluster identifier is supplied.

By default, abbreviated information about the clusters is returned. You can use the optional *ShowCacheNodeInfo* flag to retrieve detailed information about the cache nodes associated with the clusters. These details include the DNS address and port for the cache node endpoint.

If the cluster is in the *creating* state, only cluster-level information is displayed until all of the nodes are successfully provisioned.

If the cluster is in the *deleting* state, only cluster-level information is displayed.

If cache nodes are currently being added to the cluster, node endpoint information and creation time for the additional nodes are not displayed until they are completely provisioned. When the cluster state is *available*, the cluster is ready for use.

If cache nodes are currently being removed from the cluster, no endpoint information for the removed nodes is displayed.

## Request Parameters
<a name="API_DescribeCacheClusters_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheClusterId **
The user-supplied cluster identifier. If this parameter is specified, only information about that specific cluster is returned. This parameter isn't case sensitive.
Type: String
Required: No

 ** Marker **
An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** MaxRecords **
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: minimum 20; maximum 100.
Type: Integer
Required: No

 ** ShowCacheClustersNotInReplicationGroups **
An optional flag that can be included in the `DescribeCacheCluster` request to show only nodes (API/CLI: clusters) that are not members of a replication group. In practice, this means Memcached and single node Valkey or Redis OSS clusters.
Type: Boolean
Required: No

 ** ShowCacheNodeInfo **
An optional flag that can be included in the `DescribeCacheCluster` request to retrieve information about the individual cache nodes.
Type: Boolean
Required: No

## Response Elements
<a name="API_DescribeCacheClusters_ResponseElements"></a>

The following elements are returned by the service.

 **CacheClusters.CacheCluster.N**
A list of clusters. Each item in the list contains detailed information about one cluster.
Type: Array of [CacheCluster](API_CacheCluster.md) objects

 ** Marker **
Provides an identifier to allow retrieval of paginated results.
Type: String

## Errors
<a name="API_DescribeCacheClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CacheClusterNotFound **
The requested cluster ID does not refer to an existing cluster.
HTTP Status Code: 404

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

## Examples
<a name="API_DescribeCacheClusters_Examples"></a>

### DescribeCacheClusters
<a name="API_DescribeCacheClusters_Example_1"></a>

This example illustrates one usage of DescribeCacheClusters.

#### Sample Request
<a name="API_DescribeCacheClusters_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=DescribeCacheClusters
   &MaxRecords=100
   &ShowCacheNodeInfo=false
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_DescribeCacheClusters_Example_1_Response"></a>

```
<DescribeCacheClustersResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
  <DescribeCacheClustersResult>
    <CacheClusters>
      <CacheCluster>
        <CacheParameterGroup>
          <ParameterApplyStatus>in-sync</ParameterApplyStatus>
          <CacheParameterGroupName>default.memcached1.4</CacheParameterGroupName>
          <CacheNodeIdsToReboot/>
        </CacheParameterGroup>
        <CacheClusterId>simcoprod42</CacheClusterId>
        <CacheClusterStatus>available</CacheClusterStatus>
        <ConfigurationEndpoint>
          <Port>11211</Port>
          <Address>simcoprod42.m2st2p.cfg.cache.amazonaws.com</Address>
        </ConfigurationEndpoint>
        <ClientDownloadLandingPage>
          https://console.aws.amazon.com/elasticache/home#client-download:
        </ClientDownloadLandingPage>
        <CacheNodeType>cache.m1.large</CacheNodeType>
        <Engine>memcached</Engine>
        <PendingModifiedValues/>
        <PreferredAvailabilityZone>us-west-2c</PreferredAvailabilityZone>
        <CacheClusterCreateTime>2015-02-02T01:21:46.607Z</CacheClusterCreateTime>
        <EngineVersion>1.4.5</EngineVersion>
        <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
        <PreferredMaintenanceWindow>fri:08:30-fri:09:30</PreferredMaintenanceWindow>
        <CacheSecurityGroups>
          <CacheSecurityGroup>
            <CacheSecurityGroupName>default</CacheSecurityGroupName>
            <Status>active</Status>
          </CacheSecurityGroup>
        </CacheSecurityGroups>
        <NotificationConfiguration>
          <TopicStatus>active</TopicStatus>
          <TopicArn>arn:aws:sns:us-west-2:123456789012:ElastiCacheNotifications</TopicArn>
        </NotificationConfiguration>
        <NumCacheNodes>6</NumCacheNodes>
      </CacheCluster>
    </CacheClusters>
  </DescribeCacheClustersResult>
  <ResponseMetadata>
    <RequestId>f270d58f-b7fb-11e0-9326-b7275b9d4a6c</RequestId>
  </ResponseMetadata>
</DescribeCacheClustersResponse>
```

## See Also
<a name="API_DescribeCacheClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DescribeCacheClusters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DescribeCacheClusters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DescribeCacheClusters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DescribeCacheClusters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DescribeCacheClusters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DescribeCacheClusters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DescribeCacheClusters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DescribeCacheClusters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DescribeCacheClusters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DescribeCacheClusters)
