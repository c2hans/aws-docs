---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_RemoveTagsFromResource.html
---

# RemoveTagsFromResource
<a name="API_RemoveTagsFromResource"></a>

Removes the tags identified by the `TagKeys` list from the named resource. A tag is a key-value pair where the key and value are case-sensitive. You can use tags to categorize and track all your ElastiCache resources, with the exception of global replication group. When you add or remove tags on replication groups, those actions will be replicated to all nodes in the replication group. For more information, see [Resource-level permissions](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/IAM.ResourceLevelPermissions.html).

## Request Parameters
<a name="API_RemoveTagsFromResource_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceName **
The Amazon Resource Name (ARN) of the resource from which you want the tags removed, for example `arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster` or `arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot`.
For more information about ARNs, see [Amazon Resource Names (ARNs) and Amazon Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Required: Yes

 **TagKeys.member.N**
A list of `TagKeys` identifying the tags you want removed from the named resource.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_RemoveTagsFromResource_ResponseElements"></a>

The following element is returned by the service.

 **TagList.Tag.N**
A list of tags as key-value pairs.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_RemoveTagsFromResource_Errors"></a>

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

 ** CacheSubnetGroupNotFoundFault **
The requested cache subnet group name does not refer to an existing cache subnet group.
HTTP Status Code: 400

 ** InvalidARN **
The requested Amazon Resource Name (ARN) does not refer to an existing resource.
HTTP Status Code: 400

 ** InvalidReplicationGroupState **
The requested replication group is not in the `available` state.
HTTP Status Code: 400

 ** InvalidServerlessCacheSnapshotStateFault **
The state of the serverless cache snapshot was not received. Available for Valkey, Redis OSS and Serverless Memcached only.
HTTP Status Code: 400

 ** InvalidServerlessCacheStateFault **
The account for these credentials is not currently active.
HTTP Status Code: 400

 ** ReplicationGroupNotFoundFault **
The specified replication group does not exist.
HTTP Status Code: 404

 ** ReservedCacheNodeNotFound **
The requested reserved cache node was not found.
HTTP Status Code: 404

 ** ServerlessCacheNotFoundFault **
The serverless cache was not found or does not exist.
HTTP Status Code: 404

 ** ServerlessCacheSnapshotNotFoundFault **
This serverless cache snapshot could not be found or does not exist. Available for Valkey, Redis OSS and Serverless Memcached only.
HTTP Status Code: 404

 ** SnapshotNotFoundFault **
The requested snapshot name does not refer to an existing snapshot.
HTTP Status Code: 404

 ** TagNotFound **
The requested tag was not found on this resource.
HTTP Status Code: 404

 ** UserGroupNotFound **
The user group was not found or does not exist
HTTP Status Code: 404

 ** UserNotFound **
The user does not exist or could not be found.
HTTP Status Code: 404

## Examples
<a name="API_RemoveTagsFromResource_Examples"></a>

### RemoveTagsFromResource
<a name="API_RemoveTagsFromResource_Example_1"></a>

This example illustrates one usage of RemoveTagsFromResource.

#### Sample Request
<a name="API_RemoveTagsFromResource_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=RemoveTagsFromResource
   &ResourceName=arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &TagKeys.TagKey.1=service
   &TagKeys.TagKey.2=organization
   &Version=2015-02-02
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

## See Also
<a name="API_RemoveTagsFromResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/RemoveTagsFromResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/RemoveTagsFromResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/RemoveTagsFromResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/RemoveTagsFromResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/RemoveTagsFromResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/RemoveTagsFromResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/RemoveTagsFromResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/RemoveTagsFromResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/RemoveTagsFromResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/RemoveTagsFromResource)
