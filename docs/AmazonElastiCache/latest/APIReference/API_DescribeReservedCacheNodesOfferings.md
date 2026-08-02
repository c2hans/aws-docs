---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeReservedCacheNodesOfferings.html
---

# DescribeReservedCacheNodesOfferings
<a name="API_DescribeReservedCacheNodesOfferings"></a>

Lists available reserved cache node offerings.

## Request Parameters
<a name="API_DescribeReservedCacheNodesOfferings_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheNodeType **
The cache node type filter value. Use this parameter to show only the available offerings matching the specified cache node type.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.
+ General purpose:
  + Current generation:

     **M7g node types**: `cache.m7g.large`, `cache.m7g.xlarge`, `cache.m7g.2xlarge`, `cache.m7g.4xlarge`, `cache.m7g.8xlarge`, `cache.m7g.12xlarge`, `cache.m7g.16xlarge`
**Note**
For region availability, see [Supported Node Types](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion)

     **M6g node types** (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): `cache.m6g.large`, `cache.m6g.xlarge`, `cache.m6g.2xlarge`, `cache.m6g.4xlarge`, `cache.m6g.8xlarge`, `cache.m6g.12xlarge`, `cache.m6g.16xlarge`

     **M5 node types:** `cache.m5.large`, `cache.m5.xlarge`, `cache.m5.2xlarge`, `cache.m5.4xlarge`, `cache.m5.12xlarge`, `cache.m5.24xlarge`

     **M4 node types:** `cache.m4.large`, `cache.m4.xlarge`, `cache.m4.2xlarge`, `cache.m4.4xlarge`, `cache.m4.10xlarge`

     **T4g node types** (available only for Redis OSS engine version 5.0.6 onward and Memcached engine version 1.5.16 onward): `cache.t4g.micro`, `cache.t4g.small`, `cache.t4g.medium`

     **T3 node types:** `cache.t3.micro`, `cache.t3.small`, `cache.t3.medium`

     **T2 node types:** `cache.t2.micro`, `cache.t2.small`, `cache.t2.medium`
  + Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)

     **T1 node types:** `cache.t1.micro`

     **M1 node types:** `cache.m1.small`, `cache.m1.medium`, `cache.m1.large`, `cache.m1.xlarge`

     **M3 node types:** `cache.m3.medium`, `cache.m3.large`, `cache.m3.xlarge`, `cache.m3.2xlarge`
+ Compute optimized:
  + Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)

     **C1 node types:** `cache.c1.xlarge`
+ Memory optimized:
  + Current generation:

     **R7g node types**: `cache.r7g.large`, `cache.r7g.xlarge`, `cache.r7g.2xlarge`, `cache.r7g.4xlarge`, `cache.r7g.8xlarge`, `cache.r7g.12xlarge`, `cache.r7g.16xlarge`
**Note**
For region availability, see [Supported Node Types](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion)

     **R6g node types** (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): `cache.r6g.large`, `cache.r6g.xlarge`, `cache.r6g.2xlarge`, `cache.r6g.4xlarge`, `cache.r6g.8xlarge`, `cache.r6g.12xlarge`, `cache.r6g.16xlarge`

     **R5 node types:** `cache.r5.large`, `cache.r5.xlarge`, `cache.r5.2xlarge`, `cache.r5.4xlarge`, `cache.r5.12xlarge`, `cache.r5.24xlarge`

     **R4 node types:** `cache.r4.large`, `cache.r4.xlarge`, `cache.r4.2xlarge`, `cache.r4.4xlarge`, `cache.r4.8xlarge`, `cache.r4.16xlarge`
  + Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)

     **M2 node types:** `cache.m2.xlarge`, `cache.m2.2xlarge`, `cache.m2.4xlarge`

     **R3 node types:** `cache.r3.large`, `cache.r3.xlarge`, `cache.r3.2xlarge`, `cache.r3.4xlarge`, `cache.r3.8xlarge`
 **Additional node type info**
+ All current generation instance types are created in Amazon VPC by default.
+ Valkey or Redis OSS append-only files (AOF) are not supported for T1 or T2 instances.
+ Valkey or Redis OSS Multi-AZ with automatic failover is not supported on T1 instances.
+ The configuration variables `appendonly` and `appendfsync` are not supported on Valkey, or on Redis OSS version 2.8.22 and later.
Type: String
Required: No

 ** Duration **
Duration filter value, specified in years or seconds. Use this parameter to show only reservations for a given duration.
Valid Values: `1 | 3 | 31536000 | 94608000`
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

 ** OfferingType **
The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.
Valid Values: `"Light Utilization"|"Medium Utilization"|"Heavy Utilization" |"All Upfront"|"Partial Upfront"| "No Upfront"`
Type: String
Required: No

 ** ProductDescription **
The product description filter value. Use this parameter to show only the available offerings matching the specified product description.
Type: String
Required: No

 ** ReservedCacheNodesOfferingId **
The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.
Example: `438012d3-4052-4cc7-b2e3-8d3372e0e706`
Type: String
Required: No

## Response Elements
<a name="API_DescribeReservedCacheNodesOfferings_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **
Provides an identifier to allow retrieval of paginated results.
Type: String

 **ReservedCacheNodesOfferings.ReservedCacheNodesOffering.N**
A list of reserved cache node offerings. Each element in the list contains detailed information about one offering.
Type: Array of [ReservedCacheNodesOffering](API_ReservedCacheNodesOffering.md) objects

## Errors
<a name="API_DescribeReservedCacheNodesOfferings_Errors"></a>

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

 ** ReservedCacheNodesOfferingNotFound **
The requested cache node offering does not exist.
HTTP Status Code: 404

## Examples
<a name="API_DescribeReservedCacheNodesOfferings_Examples"></a>

### DescribeReservedCacheNodesOfferings
<a name="API_DescribeReservedCacheNodesOfferings_Example_1"></a>

This example illustrates one usage of DescribeReservedCacheNodesOfferings.

#### Sample Request
<a name="API_DescribeReservedCacheNodesOfferings_Example_1_Request"></a>

```
https://elasticache.amazonaws.com/
   ?Action=DescribeReservedCacheNodesOfferings
   &ReservedCacheNodesOfferingId=438012d3-4052-4cc7-b2e3-8d3372e0e706
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_DescribeReservedCacheNodesOfferings_Example_1_Response"></a>

```
<DescribeReservedCacheNodesOfferingsResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
  <DescribeReservedCacheNodesOfferingsResult>
    <ReservedCacheNodesOfferings>
      <ReservedCacheNodesOffering>
        <Duration>31536000</Duration>
        <OfferingType>Heavy Utilization</OfferingType>
        <RecurringCharges>
          <RecurringCharge>
            <RecurringChargeFrequency>Hourly</RecurringChargeFrequency>
            <RecurringChargeAmount>0.123</RecurringChargeAmount>
          </RecurringCharge>
        </RecurringCharges>
        <FixedPrice>162.0</FixedPrice>
        <ProductDescription>memcached</ProductDescription>
        <UsagePrice>0.0</UsagePrice>
        <ReservedCacheNodesOfferingId>SampleOfferingId</ReservedCacheNodesOfferingId>
        <CacheNodeType>cache.m1.small</CacheNodeType>
      </ReservedCacheNodesOffering>
    </ReservedCacheNodesOfferings>
  </DescribeReservedCacheNodesOfferingsResult>
  <ResponseMetadata>
    <RequestId>521b420a-2961-11e1-bd06-6fe008f046c3</RequestId>
  </ResponseMetadata>
</DescribeReservedCacheNodesOfferingsResponse>
```

## See Also
<a name="API_DescribeReservedCacheNodesOfferings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings)
