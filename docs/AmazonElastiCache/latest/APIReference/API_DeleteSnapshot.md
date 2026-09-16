---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteSnapshot.html
---

# DeleteSnapshot
<a name="API_DeleteSnapshot"></a>

Deletes an existing snapshot. When you receive a successful response from this operation, ElastiCache immediately begins deleting the snapshot; you cannot cancel or revert this operation.

**Note**
This operation is valid for Valkey or Redis OSS only.

## Request Parameters
<a name="API_DeleteSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SnapshotName **
The name of the snapshot to be deleted.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** Snapshot **
Represents a copy of an entire Valkey or Redis OSS cluster as of the time when the snapshot was taken.
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_DeleteSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** InvalidSnapshotState **
The current state of the snapshot does not allow the requested operation to occur.
HTTP Status Code: 400

 ** SnapshotNotFoundFault **
The requested snapshot name does not refer to an existing snapshot.
HTTP Status Code: 404

## Examples
<a name="API_DeleteSnapshot_Examples"></a>

### DeleteSnapshot
<a name="API_DeleteSnapshot_Example_1"></a>

This example illustrates one usage of DeleteSnapshot.

#### Sample Request
<a name="API_DeleteSnapshot_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=DeleteSnapshot
   &SnapshotName=my-manual-snapshot
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_DeleteSnapshot_Example_1_Response"></a>

```
<DeleteSnapshotResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
   <DeleteSnapshotResult>
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
         <SnapshotStatus>deleting</SnapshotStatus>
         <NumCacheNodes>1</NumCacheNodes>
         <SnapshotWindow>07:30-08:30</SnapshotWindow>
      </Snapshot>
   </DeleteSnapshotResult>
   <ResponseMetadata>
      <RequestId>694d7017-b9d2-11e3-8a16-7978bb24ffdf</RequestId>
   </ResponseMetadata>
</DeleteSnapshotResponse>
```

## See Also
<a name="API_DeleteSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DeleteSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DeleteSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DeleteSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DeleteSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DeleteSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DeleteSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DeleteSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DeleteSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DeleteSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DeleteSnapshot)
