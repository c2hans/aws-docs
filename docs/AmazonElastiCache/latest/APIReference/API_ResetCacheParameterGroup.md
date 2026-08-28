---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ResetCacheParameterGroup.html
---

# ResetCacheParameterGroup
<a name="API_ResetCacheParameterGroup"></a>

Modifies the parameters of a cache parameter group to the engine or system default value. You can reset specific parameters by submitting a list of parameter names. To reset the entire cache parameter group, specify the `ResetAllParameters` and `CacheParameterGroupName` parameters.

## Request Parameters
<a name="API_ResetCacheParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheParameterGroupName **
The name of the cache parameter group to reset.
Type: String
Required: Yes

 **ParameterNameValues.ParameterNameValue.N**
An array of parameter names to reset to their default values. If `ResetAllParameters` is `true`, do not use `ParameterNameValues`. If `ResetAllParameters` is `false`, you must specify the name of at least one parameter to reset.
Type: Array of [ParameterNameValue](API_ParameterNameValue.md) objects
Required: No

 ** ResetAllParameters **
If `true`, all parameters in the cache parameter group are reset to their default values. If `false`, only the parameters listed by `ParameterNameValues` are reset to their default values.
Valid values: `true` \| `false`
Type: Boolean
Required: No

## Response Elements
<a name="API_ResetCacheParameterGroup_ResponseElements"></a>

The following element is returned by the service.

 ** CacheParameterGroupName **
The name of the cache parameter group.
Type: String

## Errors
<a name="API_ResetCacheParameterGroup_Errors"></a>

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
<a name="API_ResetCacheParameterGroup_Examples"></a>

### ResetCacheParameterGroup
<a name="API_ResetCacheParameterGroup_Example_1"></a>

This example illustrates one usage of ResetCacheParameterGroup.

#### Sample Request
<a name="API_ResetCacheParameterGroup_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=ResetCacheParameterGroup
   &ResetAllParameters=true
   &CacheParameterGroupName=mycacheparametergroup1
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_ResetCacheParameterGroup_Example_1_Response"></a>

```
<ResetCacheParameterGroupResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
   <ResetCacheParameterGroupResult>
      <CacheParameterGroupName>mycacheparametergroup1</CacheParameterGroupName>
   </ResetCacheParameterGroupResult>
   <ResponseMetadata>
      <RequestId>cb7cc855-b9d2-11e3-8a16-7978bb24ffdf</RequestId>
   </ResponseMetadata>
</ResetCacheParameterGroupResponse>
```

## See Also
<a name="API_ResetCacheParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/ResetCacheParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/ResetCacheParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ResetCacheParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/ResetCacheParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ResetCacheParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/ResetCacheParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/ResetCacheParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/ResetCacheParameterGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/ResetCacheParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ResetCacheParameterGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
