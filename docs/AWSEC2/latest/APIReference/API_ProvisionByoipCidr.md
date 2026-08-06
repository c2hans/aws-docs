---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ProvisionByoipCidr.html
---

# ProvisionByoipCidr
<a name="API_ProvisionByoipCidr"></a>

Provisions an IPv4 or IPv6 address range for use with your AWS resources through bring your own IP addresses (BYOIP) and creates a corresponding address pool. After the address range is provisioned, it is ready to be advertised.

 AWS verifies that you own the address range and are authorized to advertise it. You must ensure that the address range is registered to you and that you created an RPKI ROA to authorize Amazon ASNs 16509 and 14618 to advertise the address range. For the AWS GovCloud (US) Regions, authorize only ASN 8987. For the AWS European Sovereign Cloud, authorize ASNs 16509 and 214101. For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html) in the *Amazon EC2 User Guide*.

Provisioning an address range is an asynchronous operation, so the call returns immediately, but the address range is not ready to use until its status changes from `pending-provision` to `provisioned`. For more information, see [Onboard your address range](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/byoip-onboard.html).

## Request Parameters
<a name="API_ProvisionByoipCidr_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Cidr**
The public IPv4 or IPv6 address range, in CIDR notation. The most specific IPv4 prefix that you can specify is /24. The most specific IPv6 address range that you can bring is /48 for CIDRs that are publicly advertisable and /56 for CIDRs that are not publicly advertisable. The address range cannot overlap with another address range that you've brought to this or another Region.
Type: String
Required: Yes

 **CidrAuthorizationContext**
A signed document that proves that you are authorized to bring the specified IP address range to Amazon using BYOIP.
Type: [CidrAuthorizationContext](API_CidrAuthorizationContext.md) object
Required: No

 **Description**
A description for the address range and the address pool.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **MultiRegion**
Reserved.
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

 **PoolTagSpecification.N**
The tags to apply to the address pool.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **PubliclyAdvertisable**
(IPv6 only) Indicate whether the address range will be publicly advertised to the internet.
Default: true
Type: Boolean
Required: No

## Response Elements
<a name="API_ProvisionByoipCidr_ResponseElements"></a>

The following elements are returned by the service.

 **byoipCidr**
Information about the address range.
Type: [ByoipCidr](API_ByoipCidr.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ProvisionByoipCidr_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ProvisionByoipCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ProvisionByoipCidr)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ProvisionByoipCidr)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ProvisionByoipCidr)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ProvisionByoipCidr)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ProvisionByoipCidr)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ProvisionByoipCidr)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ProvisionByoipCidr)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ProvisionByoipCidr)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ProvisionByoipCidr)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ProvisionByoipCidr)
