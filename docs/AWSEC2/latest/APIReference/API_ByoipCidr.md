---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ByoipCidr.html
---

# ByoipCidr
<a name="API_ByoipCidr"></a>

Information about an address range that is provisioned for use with your AWS resources through bring your own IP addresses (BYOIP).

## Contents
<a name="API_ByoipCidr_Contents"></a>

 ** advertisementType **
Specifies the advertisement method for the BYOIP CIDR. Valid values are:
+  `unicast`: IP is advertised from a single location (regional services like EC2)
+  `anycast`: IP is advertised from multiple global locations simultaneously (global services like CloudFront)
For more information, see [Bring your own IP to CloudFront using IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-cloudfront.html) in the *Amazon VPC IPAM User Guide*.
Type: String
Required: No

 ** AsnAssociationSet.N **
The BYOIP CIDR associations with ASNs.
Type: Array of [AsnAssociation](API_AsnAssociation.md) objects
Required: No

 ** cidr **
The address range, in CIDR notation.
Type: String
Required: No

 ** description **
The description of the address range.
Type: String
Required: No

 ** ipamPoolId **
The ID of the IPAM pool associated with the CIDR.
Type: String
Required: No

 ** networkBorderGroup **
If you have [Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/how-local-zones-work.html) enabled, you can choose a network border group for Local Zones when you provision and advertise a BYOIPv4 CIDR. Choose the network border group carefully as the EIP and the AWS resource it is associated with must reside in the same network border group.
You can provision BYOIP address ranges to and advertise them in the following Local Zone network border groups:
+ us-east-1-dfw-2
+ us-west-2-lax-1
+ us-west-2-phx-2
You cannot provision or advertise BYOIPv6 address ranges in Local Zones at this time.
Type: String
Required: No

 ** poolId **
The ID of the address pool associated with the CIDR.
Type: String
Required: No

 ** state **
The state of the address range.
+  `advertised`: The address range is being advertised to the internet by AWS.
+  `deprovisioned`: The address range is deprovisioned.
+  `failed-deprovision`: The request to deprovision the address range was unsuccessful. Ensure that all EIPs from the range have been deallocated and try again.
+  `failed-provision`: The request to provision the address range was unsuccessful.
+  `pending-deprovision`: You’ve submitted a request to deprovision an address range and it's pending.
+  `pending-provision`: You’ve submitted a request to provision an address range and it's pending.
+  `provisioned`: The address range is provisioned and can be advertised. The range is not currently advertised.
+  `provisioned-not-publicly-advertisable`: The address range is provisioned and cannot be advertised.
Type: String
Valid Values: `advertised | deprovisioned | failed-deprovision | failed-provision | pending-advertising | pending-deprovision | pending-provision | pending-withdrawal | provisioned | provisioned-not-publicly-advertisable`
Required: No

 ** statusMessage **
Upon success, contains the ID of the address pool. Otherwise, contains an error message.
Type: String
Required: No

## See Also
<a name="API_ByoipCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ByoipCidr)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ByoipCidr)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ByoipCidr)
