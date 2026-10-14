---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-rdsungraceful.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan RdsUngraceful
<a name="aws-properties-arcregionswitch-plan-rdsungraceful"></a>

The ungraceful execution settings for an Amazon RDS switchover read replica execution block.

## Syntax
<a name="aws-properties-arcregionswitch-plan-rdsungraceful-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-rdsungraceful-syntax.json"></a>

```
{
  "[Ungraceful](#cfn-arcregionswitch-plan-rdsungraceful-ungraceful)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-rdsungraceful-syntax.yaml"></a>

```
  [Ungraceful](#cfn-arcregionswitch-plan-rdsungraceful-ungraceful): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-rdsungraceful-properties"></a>

`Ungraceful`  <a name="cfn-arcregionswitch-plan-rdsungraceful-ungraceful"></a>
The ungraceful behavior to perform if switching to ungraceful execution.
*Required*: No
*Type*: String
*Allowed values*: `promoteReadReplica`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
