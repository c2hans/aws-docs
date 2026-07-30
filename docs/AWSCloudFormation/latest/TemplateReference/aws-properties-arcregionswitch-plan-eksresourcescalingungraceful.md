---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-eksresourcescalingungraceful.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan EksResourceScalingUngraceful
<a name="aws-properties-arcregionswitch-plan-eksresourcescalingungraceful"></a>

The ungraceful settings for AWS EKS resource scaling.

## Syntax
<a name="aws-properties-arcregionswitch-plan-eksresourcescalingungraceful-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-eksresourcescalingungraceful-syntax.json"></a>

```
{
  "[MinimumSuccessPercentage](#cfn-arcregionswitch-plan-eksresourcescalingungraceful-minimumsuccesspercentage)" : {{Number}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-eksresourcescalingungraceful-syntax.yaml"></a>

```
  [MinimumSuccessPercentage](#cfn-arcregionswitch-plan-eksresourcescalingungraceful-minimumsuccesspercentage): {{Number}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-eksresourcescalingungraceful-properties"></a>

`MinimumSuccessPercentage`  <a name="cfn-arcregionswitch-plan-eksresourcescalingungraceful-minimumsuccesspercentage"></a>
The minimum success percentage for the configuration.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `99`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
