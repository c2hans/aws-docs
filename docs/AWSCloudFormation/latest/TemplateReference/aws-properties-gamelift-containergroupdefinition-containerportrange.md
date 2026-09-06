---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containergroupdefinition-containerportrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerGroupDefinition ContainerPortRange
<a name="aws-properties-gamelift-containergroupdefinition-containerportrange"></a>

A set of one or more port numbers that can be opened on the container, and the supported network protocol.

 **Part of:** [ContainerPortConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerPortConfiguration.html)

## Syntax
<a name="aws-properties-gamelift-containergroupdefinition-containerportrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containergroupdefinition-containerportrange-syntax.json"></a>

```
{
  "[FromPort](#cfn-gamelift-containergroupdefinition-containerportrange-fromport)" : {{Integer}},
  "[Protocol](#cfn-gamelift-containergroupdefinition-containerportrange-protocol)" : {{String}},
  "[ToPort](#cfn-gamelift-containergroupdefinition-containerportrange-toport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-gamelift-containergroupdefinition-containerportrange-syntax.yaml"></a>

```
  [FromPort](#cfn-gamelift-containergroupdefinition-containerportrange-fromport): {{Integer}}
  [Protocol](#cfn-gamelift-containergroupdefinition-containerportrange-protocol): {{String}}
  [ToPort](#cfn-gamelift-containergroupdefinition-containerportrange-toport): {{Integer}}
```

## Properties
<a name="aws-properties-gamelift-containergroupdefinition-containerportrange-properties"></a>

`FromPort`  <a name="cfn-gamelift-containergroupdefinition-containerportrange-fromport"></a>
A starting value for the range of allowed port numbers.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `60000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-gamelift-containergroupdefinition-containerportrange-protocol"></a>
The network protocol that these ports support.
*Required*: Yes
*Type*: String
*Allowed values*: `TCP | UDP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToPort`  <a name="cfn-gamelift-containergroupdefinition-containerportrange-toport"></a>
An ending value for the range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort`.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `60000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
