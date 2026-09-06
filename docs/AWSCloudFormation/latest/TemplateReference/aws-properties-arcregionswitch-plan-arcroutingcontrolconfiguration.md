---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-arcroutingcontrolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan ArcRoutingControlConfiguration
<a name="aws-properties-arcregionswitch-plan-arcroutingcontrolconfiguration"></a>

Configuration for ARC routing controls used in a Region switch plan. Routing controls are simple on/off switches that you can use to shift traffic away from an impaired Region.

## Syntax
<a name="aws-properties-arcregionswitch-plan-arcroutingcontrolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-arcroutingcontrolconfiguration-syntax.json"></a>

```
{
  "[CrossAccountRole](#cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-crossaccountrole)" : {{String}},
  "[ExternalId](#cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-externalid)" : {{String}},
  "[RegionAndRoutingControls](#cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-regionandroutingcontrols)" : {{{{{Key}}: {{Value}}, ...}}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-timeoutminutes)" : {{Number}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-arcroutingcontrolconfiguration-syntax.yaml"></a>

```
  [CrossAccountRole](#cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-crossaccountrole): {{String}}
  [ExternalId](#cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-externalid): {{String}}
  [RegionAndRoutingControls](#cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-regionandroutingcontrols): {{
    {{Key}}: {{Value}}}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-timeoutminutes): {{Number}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-arcroutingcontrolconfiguration-properties"></a>

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-crossaccountrole"></a>
The cross account role for the configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-externalid"></a>
The external ID (secret key) for the configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionAndRoutingControls`  <a name="cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-regionandroutingcontrols"></a>
The Region and ARC routing controls for the configuration.
*Required*: Yes
*Type*: Object of Array
*Pattern*: `.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-timeoutminutes"></a>
The timeout value specified for the configuration.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
