---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-vpcoutputsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel VpcOutputSettings
<a name="aws-properties-medialive-channel-vpcoutputsettings"></a>

Settings to enable VPC mode in the channel, so that the endpoints for all outputs are in your VPC.

This entity is at the top level in the channel.

## Syntax
<a name="aws-properties-medialive-channel-vpcoutputsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-vpcoutputsettings-syntax.json"></a>

```
{
  "[PublicAddressAllocationIds](#cfn-medialive-channel-vpcoutputsettings-publicaddressallocationids)" : {{[ String, ... ]}},
  "[SecurityGroupIds](#cfn-medialive-channel-vpcoutputsettings-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-medialive-channel-vpcoutputsettings-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-medialive-channel-vpcoutputsettings-syntax.yaml"></a>

```
  [PublicAddressAllocationIds](#cfn-medialive-channel-vpcoutputsettings-publicaddressallocationids): {{
    - String}}
  [SecurityGroupIds](#cfn-medialive-channel-vpcoutputsettings-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-medialive-channel-vpcoutputsettings-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-medialive-channel-vpcoutputsettings-properties"></a>

`PublicAddressAllocationIds`  <a name="cfn-medialive-channel-vpcoutputsettings-publicaddressallocationids"></a>
List of public address allocation IDs to associate with ENIs that will be created in Output VPC. Must specify one for SINGLE\_PIPELINE, two for STANDARD channels
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIds`  <a name="cfn-medialive-channel-vpcoutputsettings-securitygroupids"></a>
A list of up to 5 EC2 VPC security group IDs to attach to the Output VPC network interfaces. If none are specified then the VPC default security group will be used
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-medialive-channel-vpcoutputsettings-subnetids"></a>
A list of VPC subnet IDs from the same VPC. If STANDARD channel, subnet IDs must be mapped to two unique availability zones (AZ).
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
