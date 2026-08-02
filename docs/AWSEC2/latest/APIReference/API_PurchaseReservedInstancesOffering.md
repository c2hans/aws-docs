---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseReservedInstancesOffering.html
---

# PurchaseReservedInstancesOffering
<a name="API_PurchaseReservedInstancesOffering"></a>

Purchases a Reserved Instance for use with your account. With Reserved Instances, you pay a lower hourly rate compared to On-Demand instance pricing.

Use [DescribeReservedInstancesOfferings](API_DescribeReservedInstancesOfferings.md) to get a list of Reserved Instance offerings that match your specifications. After you've purchased a Reserved Instance, you can check for your new Reserved Instance with [DescribeReservedInstances](API_DescribeReservedInstances.md).

To queue a purchase for a future date and time, specify a purchase time. If you do not specify a purchase time, the default is the current time.

For more information, see [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-on-demand-reserved-instances.html) and [Sell in the Reserved Instance Marketplace](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_PurchaseReservedInstancesOffering_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceCount**
The number of Reserved Instances to purchase.
Type: Integer
Required: Yes

 **LimitPrice**
Specified for Reserved Instance Marketplace offerings to limit the total order and ensure that the Reserved Instances are not purchased at unexpected prices.
Type: [ReservedInstanceLimitPrice](API_ReservedInstanceLimitPrice.md) object
Required: No

 **PurchaseTime**
The time at which to purchase the Reserved Instance, in UTC format (for example, *YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z).
Type: Timestamp
Required: No

 **ReservedInstancesOfferingId**
The ID of the Reserved Instance offering to purchase.
Type: String
Required: Yes

## Response Elements
<a name="API_PurchaseReservedInstancesOffering_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **reservedInstancesId**
The IDs of the purchased Reserved Instances. If your purchase crosses into a discounted pricing tier, the final Reserved Instances IDs might change. For more information, see [Crossing pricing tiers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-reserved-instances-application.html#crossing-pricing-tiers) in the *Amazon EC2 User Guide*.
Type: String

## Errors
<a name="API_PurchaseReservedInstancesOffering_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_PurchaseReservedInstancesOffering_Examples"></a>

### Example 1
<a name="API_PurchaseReservedInstancesOffering_Example_1"></a>

This example uses a limit price to limit the total purchase order of Standard Reserved Instances from the Reserved Instance Marketplace.

#### Sample Request
<a name="API_PurchaseReservedInstancesOffering_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=PurchaseReservedInstancesOffering
&ReservedInstancesOfferingId=4b2293b4-5813-4cc8-9ce3-1957fEXAMPLE
&LimitPrice.Amount=200
&InstanceCount=2
&AUTHPARAMS
```

#### Sample Response
<a name="API_PurchaseReservedInstancesOffering_Example_1_Response"></a>

```
<PurchaseReservedInstancesOfferingResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <reservedInstancesId>e5a2ff3b-7d14-494f-90af-0b5d0EXAMPLE</reservedInstancesId>
</PurchaseReservedInstancesOfferingResponse>
```

### Example 2
<a name="API_PurchaseReservedInstancesOffering_Example_2"></a>

This example illustrates a purchase of a Reserved Instances offering.

#### Sample Request
<a name="API_PurchaseReservedInstancesOffering_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=PurchaseReservedInstancesOffering
&ReservedInstancesOfferingId=4b2293b4-5813-4cc8-9ce3-1957fEXAMPLE
&InstanceCount=2
&AUTHPARAMS
```

#### Sample Response
<a name="API_PurchaseReservedInstancesOffering_Example_2_Response"></a>

```
<PurchaseReservedInstancesOfferingResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <reservedInstancesId>e5a2ff3b-7d14-494f-90af-0b5d0EXAMPLE</reservedInstancesId>
</PurchaseReservedInstancesOfferingResponse>
```

## See Also
<a name="API_PurchaseReservedInstancesOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/PurchaseReservedInstancesOffering)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/PurchaseReservedInstancesOffering)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PurchaseReservedInstancesOffering)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/PurchaseReservedInstancesOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PurchaseReservedInstancesOffering)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/PurchaseReservedInstancesOffering)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/PurchaseReservedInstancesOffering)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/PurchaseReservedInstancesOffering)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/PurchaseReservedInstancesOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PurchaseReservedInstancesOffering)
