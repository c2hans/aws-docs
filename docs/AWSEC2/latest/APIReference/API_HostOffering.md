---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HostOffering.html
---

# HostOffering
<a name="API_HostOffering"></a>

Details about the Dedicated Host Reservation offering.

## Contents
<a name="API_HostOffering_Contents"></a>

 ** currencyCode **
The currency of the offering.
Type: String
Valid Values: `USD`
Required: No

 ** duration **
The duration of the offering (in seconds).
Type: Integer
Required: No

 ** hourlyPrice **
The hourly price of the offering.
Type: String
Required: No

 ** instanceFamily **
The instance family of the offering.
Type: String
Required: No

 ** offeringId **
The ID of the offering.
Type: String
Required: No

 ** paymentOption **
The available payment option.
Type: String
Valid Values: `AllUpfront | PartialUpfront | NoUpfront`
Required: No

 ** upfrontPrice **
The upfront price of the offering. Does not apply to No Upfront offerings.
Type: String
Required: No

## See Also
<a name="API_HostOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/HostOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/HostOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/HostOffering)
