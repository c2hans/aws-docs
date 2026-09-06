---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeCacheSecurityGroups.html
---

# DescribeCacheSecurityGroups
<a name="API_DescribeCacheSecurityGroups"></a>

Returns a list of cache security group descriptions. If a cache security group name is specified, the list contains only the description of that group. This applicable only when you have ElastiCache in Classic setup

## Request Parameters
<a name="API_DescribeCacheSecurityGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheSecurityGroupName **
The name of the cache security group to return details for.
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
<a name="API_DescribeCacheSecurityGroups_ResponseElements"></a>

The following elements are returned by the service.

 **CacheSecurityGroups.CacheSecurityGroup.N**
A list of cache security groups. Each element in the list contains detailed information about one group.
Type: Array of [CacheSecurityGroup](API_CacheSecurityGroup.md) objects

 ** Marker **
Provides an identifier to allow retrieval of paginated results.
Type: String

## Errors
<a name="API_DescribeCacheSecurityGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CacheSecurityGroupNotFound **
The requested cache security group name does not refer to an existing cache security group.
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
<a name="API_DescribeCacheSecurityGroups_Examples"></a>

### DescribeCacheSecurityGroups
<a name="API_DescribeCacheSecurityGroups_Example_1"></a>

This example illustrates one usage of DescribeCacheSecurityGroups.

#### Sample Request
<a name="API_DescribeCacheSecurityGroups_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=DescribeCacheSecurityGroups
   &MaxRecords=100
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_DescribeCacheSecurityGroups_Example_1_Response"></a>

```
<DescribeCacheSecurityGroupsResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
  <DescribeCacheSecurityGroupsResult>
    <CacheSecurityGroups>
      <CacheSecurityGroup>
        <EC2SecurityGroups/>
        <CacheSecurityGroupName>default</CacheSecurityGroupName>
        <OwnerId>123456789012</OwnerId>
        <Description>default</Description>
      </CacheSecurityGroup>
      <CacheSecurityGroup>
        <EC2SecurityGroups/>
        <CacheSecurityGroupName>mycachesecuritygroup</CacheSecurityGroupName>
        <OwnerId>123456789012</OwnerId>
        <Description>My Security Group</Description>
      </CacheSecurityGroup>
    </CacheSecurityGroups>
  </DescribeCacheSecurityGroupsResult>
  <ResponseMetadata>
    <RequestId>a95360ae-b7fc-11e0-9326-b7275b9d4a6c</RequestId>
  </ResponseMetadata>
</DescribeCacheSecurityGroupsResponse>
```

## See Also
<a name="API_DescribeCacheSecurityGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DescribeCacheSecurityGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DescribeCacheSecurityGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DescribeCacheSecurityGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DescribeCacheSecurityGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DescribeCacheSecurityGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DescribeCacheSecurityGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DescribeCacheSecurityGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DescribeCacheSecurityGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DescribeCacheSecurityGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DescribeCacheSecurityGroups)
