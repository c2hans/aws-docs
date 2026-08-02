---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AdvertiseByoipCidr.html
---

# AdvertiseByoipCidr
<a name="API_AdvertiseByoipCidr"></a>

Advertises an IPv4 or IPv6 address range that is provisioned for use with your AWS resources through bring your own IP addresses (BYOIP).

You can perform this operation at most once every 10 seconds, even if you specify different address ranges each time.

We recommend that you stop advertising the BYOIP CIDR from other locations when you advertise it from AWS. To minimize down time, you can configure your AWS resources to use an address from a BYOIP CIDR before it is advertised, and then simultaneously stop advertising it from the current location and start advertising it through AWS.

It can take a few minutes before traffic to the specified addresses starts routing to AWS because of BGP propagation delays.

To stop advertising the BYOIP CIDR, use [WithdrawByoipCidr](API_WithdrawByoipCidr.md).

## Request Parameters
<a name="API_AdvertiseByoipCidr_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Asn**
The public 2-byte or 4-byte ASN that you want to advertise.
Type: String
Required: No

 **Cidr**
The address range, in CIDR notation. This must be the exact range that you provisioned. You can't advertise only a portion of the provisioned range.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **NetworkBorderGroup**
If you have [Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/how-local-zones-work.html) enabled, you can choose a network border group for Local Zones when you provision and advertise a BYOIPv4 CIDR. Choose the network border group carefully as the EIP and the AWS resource it is associated with must reside in the same network border group.
You can provision BYOIP address ranges to and advertise them in the following Local Zone network border groups:
+ us-east-1-dfw-2
+ us-west-2-lax-1
+ us-west-2-phx-2
You cannot provision or advertise BYOIPv6 address ranges in Local Zones at this time.
Type: String
Required: No

## Response Elements
<a name="API_AdvertiseByoipCidr_ResponseElements"></a>

The following elements are returned by the service.

 **byoipCidr**
Information about the address range.
Type: [ByoipCidr](API_ByoipCidr.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_AdvertiseByoipCidr_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_AdvertiseByoipCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AdvertiseByoipCidr)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AdvertiseByoipCidr)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AdvertiseByoipCidr)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AdvertiseByoipCidr)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AdvertiseByoipCidr)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AdvertiseByoipCidr)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AdvertiseByoipCidr)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AdvertiseByoipCidr)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AdvertiseByoipCidr)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AdvertiseByoipCidr)
