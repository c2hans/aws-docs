---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheParameterGroup.html
---

# ModifyCacheParameterGroup
<a name="API_ModifyCacheParameterGroup"></a>

Modifies the parameters of a cache parameter group. You can modify up to 20 parameters in a single request by submitting a list parameter name and value pairs.

## Request Parameters
<a name="API_ModifyCacheParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheParameterGroupName **
The name of the cache parameter group to modify.
Type: String
Required: Yes

 **ParameterNameValues.ParameterNameValue.N**
An array of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be modified per request.
Type: Array of [ParameterNameValue](API_ParameterNameValue.md) objects
Required: Yes

## Response Elements
<a name="API_ModifyCacheParameterGroup_ResponseElements"></a>

The following element is returned by the service.

 ** CacheParameterGroupName **
The name of the cache parameter group.
Type: String

## Errors
<a name="API_ModifyCacheParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CacheParameterGroupNotFound **
The requested cache parameter group name does not refer to an existing cache parameter group.
HTTP Status Code: 404

 ** InvalidCacheParameterGroupState **
The current state of the cache parameter group does not allow the requested operation to occur.
HTTP Status Code: 400

 ** InvalidGlobalReplicationGroupState **
The Global datastore is not available or in primary-only state.
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

## Examples
<a name="API_ModifyCacheParameterGroup_Examples"></a>

### ModifyCacheParameterGroup
<a name="API_ModifyCacheParameterGroup_Example_1"></a>

This example illustrates one usage of ModifyCacheParameterGroup.

#### Sample Request
<a name="API_ModifyCacheParameterGroup_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=ModifyCacheParameterGroup
   &CacheParameterGroupName=mycacheparametergroup
   &ParameterNameValues.ParameterNameValue.1.ParameterName=chunk_size_growth_factor
   &ParameterNameValues.ParameterNameValue.1.ParameterValue=1.02
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_ModifyCacheParameterGroup_Example_1_Response"></a>

```
<ModifyCacheParameterGroupResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
  <ModifyCacheParameterGroupResult>
    <CacheParameterGroupName>mycacheparametergroup</CacheParameterGroupName>
  </ModifyCacheParameterGroupResult>
  <ResponseMetadata>
    <RequestId>fcedeef2-b7ff-11e0-9326-b7275b9d4a6c</RequestId>
  </ResponseMetadata>
</ModifyCacheParameterGroupResponse>
```

## See Also
<a name="API_ModifyCacheParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/ModifyCacheParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/ModifyCacheParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ModifyCacheParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/ModifyCacheParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ModifyCacheParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/ModifyCacheParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/ModifyCacheParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/ModifyCacheParameterGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/ModifyCacheParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ModifyCacheParameterGroup)
