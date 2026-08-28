---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-inputvpcrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input InputVpcRequest
<a name="aws-properties-medialive-input-inputvpcrequest"></a>

Settings that apply only if the input is an push input where the source is on Amazon VPC.

The parent of this entity is Input.

## Syntax
<a name="aws-properties-medialive-input-inputvpcrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-inputvpcrequest-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-medialive-input-inputvpcrequest-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-medialive-input-inputvpcrequest-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-medialive-input-inputvpcrequest-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-medialive-input-inputvpcrequest-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-medialive-input-inputvpcrequest-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-medialive-input-inputvpcrequest-properties"></a>

`SecurityGroupIds`  <a name="cfn-medialive-input-inputvpcrequest-securitygroupids"></a>
The list of up to five VPC security group IDs to attach to the input VPC network interfaces. The security groups require subnet IDs. If none are specified, MediaLive uses the VPC default security group.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-medialive-input-inputvpcrequest-subnetids"></a>
The list of two VPC subnet IDs from the same VPC. You must associate subnet IDs to two unique Availability Zones.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
