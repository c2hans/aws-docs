---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-documentdbungraceful.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan DocumentDbUngraceful
<a name="aws-properties-arcregionswitch-plan-documentdbungraceful"></a>

Configuration for handling failures when performing operations on DocumentDB global clusters.

## Syntax
<a name="aws-properties-arcregionswitch-plan-documentdbungraceful-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-documentdbungraceful-syntax.json"></a>

```
{
  "[Ungraceful](#cfn-arcregionswitch-plan-documentdbungraceful-ungraceful)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-documentdbungraceful-syntax.yaml"></a>

```
  [Ungraceful](#cfn-arcregionswitch-plan-documentdbungraceful-ungraceful): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-documentdbungraceful-properties"></a>

`Ungraceful`  <a name="cfn-arcregionswitch-plan-documentdbungraceful-ungraceful"></a>
The settings for ungraceful execution.
*Required*: No
*Type*: String
*Allowed values*: `failover`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
