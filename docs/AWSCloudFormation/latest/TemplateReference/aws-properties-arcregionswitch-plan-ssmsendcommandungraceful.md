---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-ssmsendcommandungraceful.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan SsmSendCommandUngraceful
<a name="aws-properties-arcregionswitch-plan-ssmsendcommandungraceful"></a>

The ungraceful execution settings for an AWS Systems Manager `SendCommand` execution block.

## Syntax
<a name="aws-properties-arcregionswitch-plan-ssmsendcommandungraceful-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-ssmsendcommandungraceful-syntax.json"></a>

```
{
  "[Behavior](#cfn-arcregionswitch-plan-ssmsendcommandungraceful-behavior)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-ssmsendcommandungraceful-syntax.yaml"></a>

```
  [Behavior](#cfn-arcregionswitch-plan-ssmsendcommandungraceful-behavior): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-ssmsendcommandungraceful-properties"></a>

`Behavior`  <a name="cfn-arcregionswitch-plan-ssmsendcommandungraceful-behavior"></a>
Specifies whether to skip running this command during an ungraceful execution. Set to `skip` to skip the command.
*Required*: No
*Type*: String
*Allowed values*: `skip`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
