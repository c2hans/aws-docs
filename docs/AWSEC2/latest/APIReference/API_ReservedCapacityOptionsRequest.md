---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReservedCapacityOptionsRequest.html
---

# ReservedCapacityOptionsRequest
<a name="API_ReservedCapacityOptionsRequest"></a>

Defines EC2 Fleet preferences for utilizing reserved capacity when DefaultTargetCapacityType is set to `reserved-capacity`.

**Note**
This configuration can only be used if the EC2 Fleet is of type `instant`.

When you specify `ReservedCapacityOptions`, you must also set `DefaultTargetCapacityType` to `reserved-capacity` in the `TargetCapacitySpecification`.

For more information about Interruptible Capacity Reservations, see [Launch instances into an Interruptible Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-launch-instances-interruptible-cr-walkthrough.html) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_ReservedCapacityOptionsRequest_Contents"></a>

 ** ReservationType.N **
The types of Capacity Reservations to use for fulfilling the EC2 Fleet request.
Type: Array of strings
Valid Values: `interruptible-capacity-reservation`
Required: No

## See Also
<a name="API_ReservedCapacityOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReservedCapacityOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReservedCapacityOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReservedCapacityOptionsRequest)
