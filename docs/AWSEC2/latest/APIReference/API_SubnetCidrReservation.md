---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SubnetCidrReservation.html
---

# SubnetCidrReservation
<a name="API_SubnetCidrReservation"></a>

Describes a subnet CIDR reservation.

## Contents
<a name="API_SubnetCidrReservation_Contents"></a>

 ** cidr **
The CIDR that has been reserved.
Type: String
Required: No

 ** description **
The description assigned to the subnet CIDR reservation.
Type: String
Required: No

 ** ownerId **
The ID of the account that owns the subnet CIDR reservation.
Type: String
Required: No

 ** reservationType **
The type of reservation.
Type: String
Valid Values: `prefix | explicit`
Required: No

 ** subnetCidrReservationId **
The ID of the subnet CIDR reservation.
Type: String
Required: No

 ** subnetId **
The ID of the subnet.
Type: String
Required: No

 ** TagSet.N **
The tags assigned to the subnet CIDR reservation.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_SubnetCidrReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SubnetCidrReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SubnetCidrReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SubnetCidrReservation)
