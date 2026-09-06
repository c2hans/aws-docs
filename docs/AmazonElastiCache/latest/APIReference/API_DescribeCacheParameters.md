---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeCacheParameters.html
---

# DescribeCacheParameters
<a name="API_DescribeCacheParameters"></a>

Returns the detailed parameter list for a particular cache parameter group.

## Request Parameters
<a name="API_DescribeCacheParameters_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheParameterGroupName **
The name of a specific cache parameter group to return details for.
Type: String
Required: Yes

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

 ** Source **
The parameter types to return.
Valid values: `user` \| `system` \| `engine-default`
Type: String
Required: No

## Response Elements
<a name="API_DescribeCacheParameters_ResponseElements"></a>

The following elements are returned by the service.

 **CacheNodeTypeSpecificParameters.CacheNodeTypeSpecificParameter.N**
A list of parameters specific to a particular cache node type. Each element in the list contains detailed information about one parameter.
Type: Array of [CacheNodeTypeSpecificParameter](API_CacheNodeTypeSpecificParameter.md) objects

 ** Marker **
Provides an identifier to allow retrieval of paginated results.
Type: String

 **Parameters.Parameter.N**
A list of [Parameter](API_Parameter.md) instances.
Type: Array of [Parameter](API_Parameter.md) objects

## Errors
<a name="API_DescribeCacheParameters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CacheParameterGroupNotFound **
The requested cache parameter group name does not refer to an existing cache parameter group.
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
<a name="API_DescribeCacheParameters_Examples"></a>

### DescribeCacheParameters
<a name="API_DescribeCacheParameters_Example_1"></a>

Some of the output has been omitted for brevity.

#### Sample Request
<a name="API_DescribeCacheParameters_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=DescribeCacheParameters
   &CacheParameterGroupName=default.memcached1.4
   &MaxRecords=100
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_DescribeCacheParameters_Example_1_Response"></a>

```
<DescribeCacheParametersResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
  <DescribeCacheParametersResult>
    <CacheNodeTypeSpecificParameters>
      <CacheNodeTypeSpecificParameter>
        <CacheNodeTypeSpecificValues>
          <CacheNodeTypeSpecificValue>
            <CacheNodeType>cache.c1.xlarge</CacheNodeType>
            <Value>6000</Value>
          </CacheNodeTypeSpecificValue>

 (...output omitted...)

        </CacheNodeTypeSpecificValues>
        <DataType>integer</DataType>
        <Source>system</Source>
        <IsModifiable>false</IsModifiable>
        <Description>The maximum configurable amount of memory to use to store items, in megabytes.</Description>
        <AllowedValues>1-100000</AllowedValues>
        <ParameterName>max_cache_memory</ParameterName>
        <MinimumEngineVersion>1.4.5</MinimumEngineVersion>
      </CacheNodeTypeSpecificParameter>
      <CacheNodeTypeSpecificParameter>

 (...output omitted...)

      </CacheNodeTypeSpecificParameter>
    </CacheNodeTypeSpecificParameters>
    <Parameters>
      <Parameter>
        <ParameterValue>1024</ParameterValue>
        <DataType>integer</DataType>
        <Source>system</Source>
        <IsModifiable>false</IsModifiable>
        <Description>The backlog queue limit.</Description>
        <AllowedValues>1-10000</AllowedValues>
        <ParameterName>backlog_queue_limit</ParameterName>
        <MinimumEngineVersion>1.4.5</MinimumEngineVersion>
      </Parameter>

 (...output omitted...)

    </Parameters>
  </DescribeCacheParametersResult>
  <ResponseMetadata>
    <RequestId>0c507368-b7fe-11e0-9326-b7275b9d4a6c</RequestId>
  </ResponseMetadata>
</DescribeCacheParametersResponse>
```

## See Also
<a name="API_DescribeCacheParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DescribeCacheParameters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DescribeCacheParameters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DescribeCacheParameters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DescribeCacheParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DescribeCacheParameters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DescribeCacheParameters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DescribeCacheParameters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DescribeCacheParameters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DescribeCacheParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DescribeCacheParameters)
