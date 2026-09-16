---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheParameterGroup.html
---

# CreateCacheParameterGroup
<a name="API_CreateCacheParameterGroup"></a>

Creates a new Amazon ElastiCache cache parameter group. An ElastiCache cache parameter group is a collection of parameters and their values that are applied to all of the nodes in any cluster or replication group using the CacheParameterGroup.

A newly created CacheParameterGroup is an exact duplicate of the default parameter group for the CacheParameterGroupFamily. To customize the newly created CacheParameterGroup you can change the values of specific parameters. For more information, see:
+  [ModifyCacheParameterGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheParameterGroup.html) in the ElastiCache API Reference.
+  [Parameters and Parameter Groups](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ParameterGroups.html) in the ElastiCache User Guide.

## Request Parameters
<a name="API_CreateCacheParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheParameterGroupFamily **
The name of the cache parameter group family that the cache parameter group can be used with.
Valid values are: `valkey8` \| `valkey7` \| `memcached1.4` \| `memcached1.5` \| `memcached1.6` \| `redis2.6` \| `redis2.8` \| `redis3.2` \| `redis4.0` \| `redis5.0` \| `redis6.x` \| `redis7`
Type: String
Required: Yes

 ** CacheParameterGroupName **
A user-specified name for the cache parameter group. This value is stored as a lowercase string.
Type: String
Required: Yes

 ** Description **
A user-specified description for the cache parameter group.
Type: String
Required: Yes

 **Tags.Tag.N**
A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Elements
<a name="API_CreateCacheParameterGroup_ResponseElements"></a>

The following element is returned by the service.

 ** CacheParameterGroup **
Represents the output of a `CreateCacheParameterGroup` operation.
Type: [CacheParameterGroup](API_CacheParameterGroup.md) object

## Errors
<a name="API_CreateCacheParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CacheParameterGroupAlreadyExists **
A cache parameter group with the requested name already exists.
HTTP Status Code: 400

 ** CacheParameterGroupQuotaExceeded **
The request cannot be processed because it would exceed the maximum number of cache security groups.
HTTP Status Code: 400

 ** InvalidCacheParameterGroupState **
The current state of the cache parameter group does not allow the requested operation to occur.
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

 ** TagQuotaPerResourceExceeded **
The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.
HTTP Status Code: 400

## Examples
<a name="API_CreateCacheParameterGroup_Examples"></a>

### CreateCacheParameterGroup
<a name="API_CreateCacheParameterGroup_Example_1"></a>

This example illustrates one usage of CreateCacheParameterGroup.

#### Sample Request
<a name="API_CreateCacheParameterGroup_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=CreateCacheParameterGroup
   &CacheParameterGroupFamily=memcached1.4
   &CacheParameterGroupName=mycacheparametergroup1
   &Description=My%20custom%20Redis%20cache%20parameter%20group
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &Version=2015-02-02
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_CreateCacheParameterGroup_Example_1_Response"></a>

```
<CreateCacheParameterGroupResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
  <CreateCacheParameterGroupResult>
    <CacheParameterGroup>
      <CacheParameterGroupName>mycacheparametergroup1</CacheParameterGroupName>
      <CacheParameterGroupFamily>memcached1.4</CacheParameterGroupFamily>
      <Description>My first cache parameter group</Description>
    </CacheParameterGroup>
  </CreateCacheParameterGroupResult>
  <ResponseMetadata>
    <RequestId>05699541-b7f9-11e0-9326-b7275b9d4a6c</RequestId>
  </ResponseMetadata>
</CreateCacheParameterGroupResponse>
```

## See Also
<a name="API_CreateCacheParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/CreateCacheParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/CreateCacheParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CreateCacheParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/CreateCacheParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CreateCacheParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/CreateCacheParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/CreateCacheParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/CreateCacheParameterGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/CreateCacheParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CreateCacheParameterGroup)
