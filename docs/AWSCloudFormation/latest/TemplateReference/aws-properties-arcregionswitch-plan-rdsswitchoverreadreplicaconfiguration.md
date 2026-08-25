---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan RdsSwitchoverReadReplicaConfiguration
<a name="aws-properties-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration"></a>

<a name="aws-properties-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-description"></a>The `RdsSwitchoverReadReplicaConfiguration` property type specifies Property description not available. for an [AWS::ARCRegionSwitch::Plan](aws-resource-arcregionswitch-plan.md).

## Syntax
<a name="aws-properties-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-syntax.json"></a>

```
{
  "[CrossAccountRole](#cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-crossaccountrole)" : {{String}},
  "[DbInstanceArnMap](#cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-dbinstancearnmap)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ExternalId](#cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-externalid)" : {{String}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-timeoutminutes)" : {{Number}},
  "[Ungraceful](#cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-ungraceful)" : {{RdsUngraceful}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-syntax.yaml"></a>

```
  [CrossAccountRole](#cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-crossaccountrole): {{String}}
  [DbInstanceArnMap](#cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-dbinstancearnmap): {{
    {{Key}}: {{Value}}}}
  [ExternalId](#cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-externalid): {{String}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-timeoutminutes): {{Number}}
  [Ungraceful](#cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-ungraceful): {{
    RdsUngraceful}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-properties"></a>

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-crossaccountrole"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DbInstanceArnMap`  <a name="cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-dbinstancearnmap"></a>
Property description not available.
*Required*: Yes
*Type*: Object of String
*Pattern*: `^[a-z]{2}-[a-z-]+-\d+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-externalid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-timeoutminutes"></a>
Property description not available.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ungraceful`  <a name="cfn-arcregionswitch-plan-rdsswitchoverreadreplicaconfiguration-ungraceful"></a>
Property description not available.
*Required*: No
*Type*: [RdsUngraceful](aws-properties-arcregionswitch-plan-rdsungraceful.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
