---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicruledestination-vpcdestinationproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRuleDestination VpcDestinationProperties
<a name="aws-properties-iot-topicruledestination-vpcdestinationproperties"></a>

The properties of a virtual private cloud (VPC) destination.

## Syntax
<a name="aws-properties-iot-topicruledestination-vpcdestinationproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicruledestination-vpcdestinationproperties-syntax.json"></a>

```
{
  "[RoleArn](#cfn-iot-topicruledestination-vpcdestinationproperties-rolearn)" : {{String}},
  "[SecurityGroups](#cfn-iot-topicruledestination-vpcdestinationproperties-securitygroups)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-iot-topicruledestination-vpcdestinationproperties-subnetids)" : {{[ String, ... ]}},
  "[VpcId](#cfn-iot-topicruledestination-vpcdestinationproperties-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicruledestination-vpcdestinationproperties-syntax.yaml"></a>

```
  [RoleArn](#cfn-iot-topicruledestination-vpcdestinationproperties-rolearn): {{String}}
  [SecurityGroups](#cfn-iot-topicruledestination-vpcdestinationproperties-securitygroups): {{
    - String}}
  [SubnetIds](#cfn-iot-topicruledestination-vpcdestinationproperties-subnetids): {{
    - String}}
  [VpcId](#cfn-iot-topicruledestination-vpcdestinationproperties-vpcid): {{String}}
```

## Properties
<a name="aws-properties-iot-topicruledestination-vpcdestinationproperties-properties"></a>

`RoleArn`  <a name="cfn-iot-topicruledestination-vpcdestinationproperties-rolearn"></a>
The ARN of a role that has permission to create and attach to elastic network interfaces (ENIs).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroups`  <a name="cfn-iot-topicruledestination-vpcdestinationproperties-securitygroups"></a>
The security groups of the VPC destination.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-iot-topicruledestination-vpcdestinationproperties-subnetids"></a>
The subnet IDs of the VPC destination.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-iot-topicruledestination-vpcdestinationproperties-vpcid"></a>
The ID of the VPC.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
