---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_ShippingDetails.html
---

# ShippingDetails
<a name="API_ShippingDetails"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

A job's shipping information, including inbound and outbound tracking numbers and shipping speed options.

## Contents
<a name="API_ShippingDetails_Contents"></a>

 ** InboundShipment **   <a name="Snowball-Type-ShippingDetails-InboundShipment"></a>
The `Status` and `TrackingNumber` values for a Snow device being returned to AWS for a particular job.
Type: [Shipment](API_Shipment.md) object
Required: No

 ** OutboundShipment **   <a name="Snowball-Type-ShippingDetails-OutboundShipment"></a>
The `Status` and `TrackingNumber` values for a Snow device being delivered to the address that you specified for a particular job.
Type: [Shipment](API_Shipment.md) object
Required: No

 ** ShippingOption **   <a name="Snowball-Type-ShippingDetails-ShippingOption"></a>
The shipping speed for a particular job. This speed doesn't dictate how soon you'll get the Snow device from the job's creation date. This speed represents how quickly it moves to its destination while in transit. Regional shipping speeds are as follows:
+ In Australia, you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day.
+ In the European Union (EU), you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.
+ In India, Snow devices are delivered in one to seven days.
+ In the United States of America (US), you have access to one-day shipping and two-day shipping.
Type: String
Valid Values: `SECOND_DAY | NEXT_DAY | EXPRESS | STANDARD`
Required: No

## See Also
<a name="API_ShippingDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/ShippingDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/ShippingDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/ShippingDetails)
