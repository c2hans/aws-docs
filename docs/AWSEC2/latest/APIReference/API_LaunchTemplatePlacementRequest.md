---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplatePlacementRequest.html
---

# LaunchTemplatePlacementRequest
<a name="API_LaunchTemplatePlacementRequest"></a>

Describes the placement of an instance.

## Contents
<a name="API_LaunchTemplatePlacementRequest_Contents"></a>

 ** Affinity **
The affinity setting for an instance on a Dedicated Host.
Type: String
Required: No

 ** AvailabilityZone **
The Availability Zone for the instance.
Either `AvailabilityZone` or `AvailabilityZoneId` can be specified, but not both
Type: String
Required: No

 ** AvailabilityZoneId **
The ID of the Availability Zone for the instance.
Either `AvailabilityZone` or `AvailabilityZoneId` can be specified, but not both
Type: String
Required: No

 ** GroupId **
The Group Id of a placement group. You must specify the Placement Group **Group Id** to launch an instance in a shared placement group.
Type: String
Required: No

 ** GroupName **
The name of the placement group for the instance.
Type: String
Required: No

 ** HostId **
The ID of the Dedicated Host for the instance.
Type: String
Required: No

 ** HostResourceGroupArn **
The ARN of the host resource group in which to launch the instances. If you specify a host resource group ARN, omit the **Tenancy** parameter or set it to `host`.
Type: String
Required: No

 ** PartitionNumber **
The number of the partition the instance should launch in. Valid only if the placement group strategy is set to `partition`.
Type: Integer
Required: No

 ** SpreadDomain **
Reserved for future use.
Type: String
Required: No

 ** Tenancy **
The tenancy of the instance. An instance with a tenancy of dedicated runs on single-tenant hardware.
Type: String
Valid Values: `default | dedicated | host`
Required: No

## See Also
<a name="API_LaunchTemplatePlacementRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplatePlacementRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplatePlacementRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplatePlacementRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
