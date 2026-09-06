---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-mitigationaction-addthingstothinggroupparams.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::MitigationAction AddThingsToThingGroupParams
<a name="aws-properties-iot-mitigationaction-addthingstothinggroupparams"></a>

Parameters used when defining a mitigation action that move a set of things to a thing group.

## Syntax
<a name="aws-properties-iot-mitigationaction-addthingstothinggroupparams-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-mitigationaction-addthingstothinggroupparams-syntax.json"></a>

```
{
  "[OverrideDynamicGroups](#cfn-iot-mitigationaction-addthingstothinggroupparams-overridedynamicgroups)" : {{Boolean}},
  "[ThingGroupNames](#cfn-iot-mitigationaction-addthingstothinggroupparams-thinggroupnames)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-iot-mitigationaction-addthingstothinggroupparams-syntax.yaml"></a>

```
  [OverrideDynamicGroups](#cfn-iot-mitigationaction-addthingstothinggroupparams-overridedynamicgroups): {{Boolean}}
  [ThingGroupNames](#cfn-iot-mitigationaction-addthingstothinggroupparams-thinggroupnames): {{
    - String}}
```

## Properties
<a name="aws-properties-iot-mitigationaction-addthingstothinggroupparams-properties"></a>

`OverrideDynamicGroups`  <a name="cfn-iot-mitigationaction-addthingstothinggroupparams-overridedynamicgroups"></a>
Specifies if this mitigation action can move the things that triggered the mitigation action even if they are part of one or more dynamic thing groups.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThingGroupNames`  <a name="cfn-iot-mitigationaction-addthingstothinggroupparams-thinggroupnames"></a>
The list of groups to which you want to add the things that triggered the mitigation action. You can add a thing to a maximum of 10 groups, but you can't add a thing to more than one group in the same hierarchy.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `128 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
