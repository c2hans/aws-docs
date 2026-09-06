---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_PurchaseReservedCacheNodesOffering.html
---

# PurchaseReservedCacheNodesOffering
<a name="API_PurchaseReservedCacheNodesOffering"></a>

Allows you to purchase a reserved cache node offering. Reserved nodes are not eligible for cancellation and are non-refundable. For more information, see [Managing Costs with Reserved Nodes](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/reserved-nodes.html).

## Request Parameters
<a name="API_PurchaseReservedCacheNodesOffering_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ReservedCacheNodesOfferingId **
The ID of the reserved cache node offering to purchase.
Example: `438012d3-4052-4cc7-b2e3-8d3372e0e706`
Type: String
Required: Yes

 ** CacheNodeCount **
The number of cache node instances to reserve.
Default: `1`
Type: Integer
Required: No

 ** ReservedCacheNodeId **
A customer-specified identifier to track this reservation.
The Reserved Cache Node ID is an unique customer-specified identifier to track this reservation. If this parameter is not specified, ElastiCache automatically generates an identifier for the reservation.
Example: myreservationID
Type: String
Required: No

 **Tags.Tag.N**
A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Elements
<a name="API_PurchaseReservedCacheNodesOffering_ResponseElements"></a>

The following element is returned by the service.

 ** ReservedCacheNode **
Represents the output of a `PurchaseReservedCacheNodesOffering` operation.
Type: [ReservedCacheNode](API_ReservedCacheNode.md) object

## Errors
<a name="API_PurchaseReservedCacheNodesOffering_Errors"></a>

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

 ** ReservedCacheNodeAlreadyExists **
You already have a reservation with the given identifier.
HTTP Status Code: 404

 ** ReservedCacheNodeQuotaExceeded **
The request cannot be processed because it would exceed the user's cache node quota.
HTTP Status Code: 400

 ** ReservedCacheNodesOfferingNotFound **
The requested cache node offering does not exist.
HTTP Status Code: 404

 ** TagQuotaPerResourceExceeded **
The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.
HTTP Status Code: 400

## Examples
<a name="API_PurchaseReservedCacheNodesOffering_Examples"></a>

### PurchaseReservedCacheNodesOffering
<a name="API_PurchaseReservedCacheNodesOffering_Example_1"></a>

This example illustrates one usage of PurchaseReservedCacheNodesOffering.

#### Sample Request
<a name="API_PurchaseReservedCacheNodesOffering_Example_1_Request"></a>

```
https://elasticache.amazonaws.com/
   ?Action=PurchaseReservedCacheNodesOffering
   &ReservedCacheNodeId=myreservationID
   &ReservedCacheNodesOfferingId=438012d3-4052-4cc7-b2e3-8d3372e0e706
   &CacheNodeCount=1
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

#### Sample Response
<a name="API_PurchaseReservedCacheNodesOffering_Example_1_Response"></a>

```
<PurchaseReservedCacheNodesOfferingResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
  <PurchaseReservedCacheNodesOfferingResult>
    <ReservedCacheNode>
      <OfferingType>Medium Utilization</OfferingType>
      <RecurringCharges/>
      <ProductDescription>memcached</ProductDescription>
      <ReservedCacheNodesOfferingId> 438012d3-4052-4cc7-b2e3-8d3372e0e706</ReservedCacheNodesOfferingId>
      <State>payment-pending</State>
      <ReservedCacheNodeId>myreservationID</ReservedCacheNodeId>
      <CacheNodeCount>10</CacheNodeCount>
      <StartTime>2015-02-02T23:24:56.577Z</StartTime>
      <Duration>31536000</Duration>
      <FixedPrice>123.0</FixedPrice>
      <UsagePrice>0.123</UsagePrice>
      <CacheNodeType>cache.m1.small</CacheNodeType>
    </ReservedCacheNode>
  </PurchaseReservedCacheNodesOfferingResult>
  <ResponseMetadata>
    <RequestId>7f099901-29cf-11e1-bd06-6fe008f046c3</RequestId>
  </ResponseMetadata>
</PurchaseReservedCacheNodesOfferingResponse>
```

## See Also
<a name="API_PurchaseReservedCacheNodesOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/PurchaseReservedCacheNodesOffering)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/PurchaseReservedCacheNodesOffering)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/PurchaseReservedCacheNodesOffering)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/PurchaseReservedCacheNodesOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/PurchaseReservedCacheNodesOffering)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/PurchaseReservedCacheNodesOffering)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/PurchaseReservedCacheNodesOffering)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/PurchaseReservedCacheNodesOffering)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/PurchaseReservedCacheNodesOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/PurchaseReservedCacheNodesOffering)
