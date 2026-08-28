---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeCacheEngineVersions.html
---

# DescribeCacheEngineVersions
<a name="API_DescribeCacheEngineVersions"></a>

Returns a list of the available cache engines and their versions.

## Request Parameters
<a name="API_DescribeCacheEngineVersions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheParameterGroupFamily **
The name of a specific cache parameter group family to return details for.
Valid values are: `memcached1.4` \| `memcached1.5` \| `memcached1.6` \| `redis2.6` \| `redis2.8` \| `redis3.2` \| `redis4.0` \| `redis5.0` \| `redis6.x` \| `redis6.2` \| `redis7` \| `valkey7`
Constraints:
+ Must be 1 to 255 alphanumeric characters
+ First character must be a letter
+ Cannot end with a hyphen or contain two consecutive hyphens
Type: String
Required: No

 ** DefaultOnly **
If `true`, specifies that only the default version of the specified engine or engine and major version combination is to be returned.
Type: Boolean
Required: No

 ** Engine **
The cache engine to return. Valid values: `memcached` \| `redis`
Type: String
Required: No

 ** EngineVersion **
The cache engine version to return.
Example: `1.4.14`
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

## Response Elements
<a name="API_DescribeCacheEngineVersions_ResponseElements"></a>

The following elements are returned by the service.

 **CacheEngineVersions.CacheEngineVersion.N**
A list of cache engine version details. Each element in the list contains detailed information about one cache engine version.
Type: Array of [CacheEngineVersion](API_CacheEngineVersion.md) objects

 ** Marker **
Provides an identifier to allow retrieval of paginated results.
Type: String

## Errors
<a name="API_DescribeCacheEngineVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeCacheEngineVersions_Examples"></a>

### DescribeCacheEngineVersions
<a name="API_DescribeCacheEngineVersions_Example_1"></a>

This example illustrates one usage of DescribeCacheEngineVersions.

#### Sample Request
<a name="API_DescribeCacheEngineVersions_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=DescribeCacheEngineVersions
   &MaxRecords=100
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_DescribeCacheEngineVersions_Example_1_Response"></a>

```
<DescribeCacheEngineVersionsResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
  <DescribeCacheEngineVersionsResult>
    <CacheEngineVersions>
      <CacheEngineVersion>
        <CacheParameterGroupFamily>memcached1.4</CacheParameterGroupFamily>
        <Engine>memcached</Engine>
        <CacheEngineVersionDescription>memcached version 1.4.14</CacheEngineVersionDescription>
        <CacheEngineDescription>memcached</CacheEngineDescription>
        <EngineVersion>1.4.14</EngineVersion>
      </CacheEngineVersion>
      <CacheEngineVersion>
        <CacheParameterGroupFamily>memcached1.4</CacheParameterGroupFamily>
        <Engine>memcached</Engine>
        <CacheEngineVersionDescription>memcached version 1.4.5</CacheEngineVersionDescription>
        <CacheEngineDescription>memcached</CacheEngineDescription>
        <EngineVersion>1.4.5</EngineVersion>
      </CacheEngineVersion>
    </CacheEngineVersions>
  </DescribeCacheEngineVersionsResult>
  <ResponseMetadata>
    <RequestId>a6ac9ad2-f8a4-11e1-a4d1-a345e5370093</RequestId>
  </ResponseMetadata>
</DescribeCacheEngineVersionsResponse>
```

## See Also
<a name="API_DescribeCacheEngineVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DescribeCacheEngineVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DescribeCacheEngineVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DescribeCacheEngineVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DescribeCacheEngineVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DescribeCacheEngineVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DescribeCacheEngineVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DescribeCacheEngineVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DescribeCacheEngineVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DescribeCacheEngineVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DescribeCacheEngineVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
