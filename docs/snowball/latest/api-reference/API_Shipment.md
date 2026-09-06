---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_Shipment.html
---

# Shipment
<a name="API_Shipment"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

The `Status` and `TrackingNumber` information for an inbound or outbound shipment.

## Contents
<a name="API_Shipment_Contents"></a>

 ** Status **   <a name="Snowball-Type-Shipment-Status"></a>
Status information for a shipment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** TrackingNumber **   <a name="Snowball-Type-Shipment-TrackingNumber"></a>
The tracking number for this job. Using this tracking number with your region's carrier's website, you can track a Snow device as the carrier transports it.
For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_Shipment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/Shipment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/Shipment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/Shipment)
