---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-state.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance State
<a name="aws-properties-ec2-instance-state"></a>

Describes the current state of an instance.

## Syntax
<a name="aws-properties-ec2-instance-state-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-state-syntax.json"></a>

```
{
  "[Code](#cfn-ec2-instance-state-code)" : {{String}},
  "[Name](#cfn-ec2-instance-state-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-instance-state-syntax.yaml"></a>

```
  [Code](#cfn-ec2-instance-state-code): {{String}}
  [Name](#cfn-ec2-instance-state-name): {{String}}
```

## Properties
<a name="aws-properties-ec2-instance-state-properties"></a>

`Code`  <a name="cfn-ec2-instance-state-code"></a>
The state of the instance as a 16-bit unsigned integer.
The high byte is all of the bits between 2^8 and (2^16)-1, which equals decimal values between 256 and 65,535. These numerical values are used for internal purposes and should be ignored.
The low byte is all of the bits between 2^0 and (2^8)-1, which equals decimal values between 0 and 255.
The valid values for instance-state-code will all be in the range of the low byte and they are:
+ `0` : `pending`
+ `16` : `running`
+ `32` : `shutting-down`
+ `48` : `terminated`
+ `64` : `stopping`
+ `80` : `stopped`
You can ignore the high byte value by zeroing out all of the bits above 2^8 or 256 in decimal.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ec2-instance-state-name"></a>
The current state of the instance.
*Required*: No
*Type*: String
*Allowed values*: `pending | running | shutting-down | terminated | stopping | stopped`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
