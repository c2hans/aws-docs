---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeSnapshots.html
---

# DescribeSnapshots
<a name="API_DescribeSnapshots"></a>

Returns information about cluster or replication group snapshots. By default, `DescribeSnapshots` lists all of your snapshots; it can optionally describe a single snapshot, or just the snapshots associated with a particular cache cluster.

**Note**
This operation is valid for Valkey or Redis OSS only.

## Request Parameters
<a name="API_DescribeSnapshots_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheClusterId **
A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cluster are described.
Type: String
Required: No

 ** Marker **
An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** MaxRecords **
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a marker is included in the response so that the remaining results can be retrieved.
Default: 50
Constraints: minimum 20; maximum 50.
Type: Integer
Required: No

 ** ReplicationGroupId **
A user-supplied replication group identifier. If this parameter is specified, only snapshots associated with that specific replication group are described.
Type: String
Required: No

 ** ShowNodeGroupConfig **
A Boolean value which if true, the node group (shard) configuration is included in the snapshot description.
Type: Boolean
Required: No

 ** SnapshotName **
A user-supplied name of the snapshot. If this parameter is specified, only this snapshot are described.
Type: String
Required: No

 ** SnapshotSource **
If set to `system`, the output shows snapshots that were automatically created by ElastiCache. If set to `user` the output shows snapshots that were manually created. If omitted, the output shows both automatically and manually created snapshots.
Type: String
Required: No

## Response Elements
<a name="API_DescribeSnapshots_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **
An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

 **Snapshots.Snapshot.N**
A list of snapshots. Each item in the list contains detailed information about one snapshot.
Type: Array of [Snapshot](API_Snapshot.md) objects

## Errors
<a name="API_DescribeSnapshots_Errors"></a>

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

 ** SnapshotNotFoundFault **
The requested snapshot name does not refer to an existing snapshot.
HTTP Status Code: 404

## Examples
<a name="API_DescribeSnapshots_Examples"></a>

### DescribeSnapshots
<a name="API_DescribeSnapshots_Example_1"></a>

This example illustrates one usage of DescribeSnapshots.

#### Sample Request
<a name="API_DescribeSnapshots_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=DescribeSnapshots
   &MaxRecords=50
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_DescribeSnapshots_Example_1_Response"></a>

```
<DescribeSnapshotsResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
   <DescribeSnapshotsResult>
      <Snapshots>
         <Snapshot>
            <CacheClusterId>my-redis-primary</CacheClusterId>
            <Port>6379</Port>
            <CacheNodeType>cache.m1.small</CacheNodeType>
            <CacheParameterGroupName>default.redis2.8</CacheParameterGroupName>
            <Engine>redis</Engine>
            <PreferredAvailabilityZone>us-west-2c</PreferredAvailabilityZone>
            <CacheClusterCreateTime>2015-02-02T18:46:57.972Z</CacheClusterCreateTime>
            <EngineVersion>2.8.6</EngineVersion>
            <SnapshotSource>manual</SnapshotSource>
            <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
            <PreferredMaintenanceWindow>wed:09:00-wed:10:00</PreferredMaintenanceWindow>
            <SnapshotName>my-manual-snapshot</SnapshotName>
            <SnapshotRetentionLimit>5</SnapshotRetentionLimit>
            <NodeSnapshots>
               <NodeSnapshot>
                  <SnapshotCreateTime>2015-02-02T18:54:12Z</SnapshotCreateTime>
                  <CacheNodeCreateTime>2015-02-02T18:46:57.972Z</CacheNodeCreateTime>
                  <CacheNodeId>0001</CacheNodeId>
                  <CacheSize>3 MB</CacheSize>
               </NodeSnapshot>
            </NodeSnapshots>
            <SnapshotStatus>creating</SnapshotStatus>
            <NumCacheNodes>1</NumCacheNodes>
            <SnapshotWindow>07:30-08:30</SnapshotWindow>
         </Snapshot>
      </Snapshots>
   </DescribeSnapshotsResult>
   <ResponseMetadata>
      <RequestId>51b0b25e-b9cf-11e3-8a16-7978bb24ffdf</RequestId>
   </ResponseMetadata>
</DescribeSnapshotsResponse>
```

## See Also
<a name="API_DescribeSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DescribeSnapshots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DescribeSnapshots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DescribeSnapshots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DescribeSnapshots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DescribeSnapshots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DescribeSnapshots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DescribeSnapshots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DescribeSnapshots)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DescribeSnapshots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DescribeSnapshots)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
