---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotPlacement.html
---

# SpotPlacement
<a name="API_SpotPlacement"></a>

Describes Spot Instance placement.

## Contents
<a name="API_SpotPlacement_Contents"></a>

 ** AvailabilityZone ** (request), ** availabilityZone ** (response)
The Availability Zone. For example, `us-east-2a`.
[Spot Fleet only] To specify multiple Availability Zones, separate them using commas; for example, "`us-east-2a`, `us-east-2b`".
Either `AvailabilityZone` or `AvailabilityZoneId` must be specified in the request, but not both.
Type: String
Required: No

 ** AvailabilityZoneId ** (request), ** availabilityZoneId ** (response)
The ID of the Availability Zone. For example, `use2-az1`.
[Spot Fleet only] To specify multiple Availability Zones, separate them using commas; for example, "`use2-az1`, `use2-bz1`".
Either `AvailabilityZone` or `AvailabilityZoneId` must be specified in the request, but not both.
Type: String
Required: No

 ** GroupName ** (request), ** groupName ** (response)
The name of the placement group.
Type: String
Required: No

 ** Tenancy ** (request), ** tenancy ** (response)
The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of `dedicated` runs on single-tenant hardware. The `host` tenancy is not supported for Spot Instances.
Type: String
Valid Values: `default | dedicated | host`
Required: No

## See Also
<a name="API_SpotPlacement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SpotPlacement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SpotPlacement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SpotPlacement)
