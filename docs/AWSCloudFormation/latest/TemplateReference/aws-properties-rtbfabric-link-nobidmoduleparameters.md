---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-nobidmoduleparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link NoBidModuleParameters
<a name="aws-properties-rtbfabric-link-nobidmoduleparameters"></a>

Describes the parameters of a no bid module.

## Syntax
<a name="aws-properties-rtbfabric-link-nobidmoduleparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-nobidmoduleparameters-syntax.json"></a>

```
{
  "[PassThroughPercentage](#cfn-rtbfabric-link-nobidmoduleparameters-passthroughpercentage)" : {{Number}},
  "[Reason](#cfn-rtbfabric-link-nobidmoduleparameters-reason)" : {{String}},
  "[ReasonCode](#cfn-rtbfabric-link-nobidmoduleparameters-reasoncode)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-nobidmoduleparameters-syntax.yaml"></a>

```
  [PassThroughPercentage](#cfn-rtbfabric-link-nobidmoduleparameters-passthroughpercentage): {{Number}}
  [Reason](#cfn-rtbfabric-link-nobidmoduleparameters-reason): {{String}}
  [ReasonCode](#cfn-rtbfabric-link-nobidmoduleparameters-reasoncode): {{Integer}}
```

## Properties
<a name="aws-properties-rtbfabric-link-nobidmoduleparameters-properties"></a>

`PassThroughPercentage`  <a name="cfn-rtbfabric-link-nobidmoduleparameters-passthroughpercentage"></a>
The pass through percentage.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Reason`  <a name="cfn-rtbfabric-link-nobidmoduleparameters-reason"></a>
The reason description.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReasonCode`  <a name="cfn-rtbfabric-link-nobidmoduleparameters-reasoncode"></a>
The reason code.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
