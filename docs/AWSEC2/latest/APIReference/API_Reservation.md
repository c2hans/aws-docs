---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Reservation.html
---

# Reservation
<a name="API_Reservation"></a>

Describes a launch request for one or more instances, and includes owner, requester, and security group information that applies to all instances in the launch request.

## Contents
<a name="API_Reservation_Contents"></a>

 ** GroupSet.N **
Not supported.
Type: Array of [GroupIdentifier](API_GroupIdentifier.md) objects
Required: No

 ** InstancesSet.N **
The instances.
Type: Array of [Instance](API_Instance.md) objects
Required: No

 ** ownerId **
The ID of the AWS account that owns the reservation.
Type: String
Required: No

 ** requesterId **
The ID of the requester that launched the instances on your behalf (for example, AWS Management Console or Auto Scaling).
Type: String
Required: No

 ** reservationId **
The ID of the reservation.
Type: String
Required: No

## See Also
<a name="API_Reservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Reservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Reservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Reservation)
