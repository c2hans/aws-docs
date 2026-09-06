---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-neptuneungraceful.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan NeptuneUngraceful
<a name="aws-properties-arcregionswitch-plan-neptuneungraceful"></a>

Configuration for handling failures when performing operations on Neptune global databases.

## Syntax
<a name="aws-properties-arcregionswitch-plan-neptuneungraceful-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-neptuneungraceful-syntax.json"></a>

```
{
  "[Ungraceful](#cfn-arcregionswitch-plan-neptuneungraceful-ungraceful)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-neptuneungraceful-syntax.yaml"></a>

```
  [Ungraceful](#cfn-arcregionswitch-plan-neptuneungraceful-ungraceful): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-neptuneungraceful-properties"></a>

`Ungraceful`  <a name="cfn-arcregionswitch-plan-neptuneungraceful-ungraceful"></a>
The settings for ungraceful execution.
*Required*: No
*Type*: String
*Allowed values*: `failover`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
