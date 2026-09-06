---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-globalauroraungraceful.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan GlobalAuroraUngraceful
<a name="aws-properties-arcregionswitch-plan-globalauroraungraceful"></a>

Configuration for handling failures when performing operations on Aurora global databases.

## Syntax
<a name="aws-properties-arcregionswitch-plan-globalauroraungraceful-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-globalauroraungraceful-syntax.json"></a>

```
{
  "[Ungraceful](#cfn-arcregionswitch-plan-globalauroraungraceful-ungraceful)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-globalauroraungraceful-syntax.yaml"></a>

```
  [Ungraceful](#cfn-arcregionswitch-plan-globalauroraungraceful-ungraceful): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-globalauroraungraceful-properties"></a>

`Ungraceful`  <a name="cfn-arcregionswitch-plan-globalauroraungraceful-ungraceful"></a>
The settings for ungraceful execution.
*Required*: No
*Type*: String
*Allowed values*: `failover`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
