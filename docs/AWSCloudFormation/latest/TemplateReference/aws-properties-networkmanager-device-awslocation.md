---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-device-awslocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::Device AWSLocation
<a name="aws-properties-networkmanager-device-awslocation"></a>

Specifies a location in AWS.

## Syntax
<a name="aws-properties-networkmanager-device-awslocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-device-awslocation-syntax.json"></a>

```
{
  "[SubnetArn](#cfn-networkmanager-device-awslocation-subnetarn)" : {{String}},
  "[Zone](#cfn-networkmanager-device-awslocation-zone)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkmanager-device-awslocation-syntax.yaml"></a>

```
  [SubnetArn](#cfn-networkmanager-device-awslocation-subnetarn): {{String}}
  [Zone](#cfn-networkmanager-device-awslocation-zone): {{String}}
```

## Properties
<a name="aws-properties-networkmanager-device-awslocation-properties"></a>

`SubnetArn`  <a name="cfn-networkmanager-device-awslocation-subnetarn"></a>
The Amazon Resource Name (ARN) of the subnet that the device is located in.
*Required*: No
*Type*: String
*Pattern*: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:subnet\/subnet-[0-9a-f]{8,17}$|^$`
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Zone`  <a name="cfn-networkmanager-device-awslocation-zone"></a>
The Zone that the device is located in. Specify the ID of an Availability Zone, Local Zone, Wavelength Zone, or an Outpost.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
