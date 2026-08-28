---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AvailabilityZone.html
---

# AvailabilityZone
<a name="API_AvailabilityZone"></a>

Describes Availability Zones, Local Zones, and Wavelength Zones.

## Contents
<a name="API_AvailabilityZone_Contents"></a>

 ** GeographySet.N **
The geography information for the Availability Zone or Local Zone. The geography is returned as a list.
Type: Array of [AvailabilityZoneGeography](API_AvailabilityZoneGeography.md) objects
Required: No

 ** groupLongName **
The long name of the Availability Zone group, Local Zone group, or Wavelength Zone group.
Type: String
Required: No

 ** groupName **
The name of the zone group. For example:
+ Availability Zones - `us-east-1-zg-1`
+ Local Zones - `us-west-2-lax-1`
+ Wavelength Zones - `us-east-1-wl1-bos-wlz-1`
Type: String
Required: No

 ** MessageSet.N **
Any messages about the Availability Zone, Local Zone, or Wavelength Zone.
Type: Array of [AvailabilityZoneMessage](API_AvailabilityZoneMessage.md) objects
Required: No

 ** networkBorderGroup **
The name of the network border group.
Type: String
Required: No

 ** optInStatus **
For Availability Zones, this parameter always has the value of `opt-in-not-required`.
For Local Zones and Wavelength Zones, this parameter is the opt-in status. The possible values are `opted-in` and `not-opted-in`.
Type: String
Valid Values: `opt-in-not-required | opted-in | not-opted-in`
Required: No

 ** parentZoneId **
The ID of the zone that handles some of the Local Zone or Wavelength Zone control plane operations, such as API calls.
Type: String
Required: No

 ** parentZoneName **
The name of the zone that handles some of the Local Zone or Wavelength Zone control plane operations, such as API calls.
Type: String
Required: No

 ** regionName **
The name of the Region.
Type: String
Required: No

 ** SubGeographySet.N **
The sub-geography information for the Availability Zone or Local Zone. The sub-geography is returned as a list.
Type: Array of [AvailabilityZoneSubGeography](API_AvailabilityZoneSubGeography.md) objects
Required: No

 ** zoneId **
The ID of the Availability Zone, Local Zone, or Wavelength Zone.
Type: String
Required: No

 ** zoneName **
The name of the Availability Zone, Local Zone, or Wavelength Zone.
Type: String
Required: No

 ** zoneState **
The state of the Availability Zone, Local Zone, or Wavelength Zone. The possible values are `available`, `unavailable`, and `constrained`.
Type: String
Valid Values: `available | information | impaired | unavailable | constrained`
Required: No

 ** zoneType **
The type of zone.
Valid values: `availability-zone` \| `local-zone` \| `wavelength-zone`
Type: String
Required: No

## See Also
<a name="API_AvailabilityZone_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AvailabilityZone)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AvailabilityZone)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AvailabilityZone)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
