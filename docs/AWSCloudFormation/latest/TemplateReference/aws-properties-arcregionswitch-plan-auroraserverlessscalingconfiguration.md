---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-auroraserverlessscalingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan AuroraServerlessScalingConfiguration
<a name="aws-properties-arcregionswitch-plan-auroraserverlessscalingconfiguration"></a>

Configuration for Amazon Aurora Serverless scaling used in a Region switch plan.

## Syntax
<a name="aws-properties-arcregionswitch-plan-auroraserverlessscalingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-auroraserverlessscalingconfiguration-syntax.json"></a>

```
{
  "[CrossAccountRole](#cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-crossaccountrole)" : {{String}},
  "[ExternalId](#cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-externalid)" : {{String}},
  "[GlobalClusterIdentifier](#cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-globalclusteridentifier)" : {{String}},
  "[RegionDatabaseClusterArns](#cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-regiondatabaseclusterarns)" : {{{{{Key}}: {{Value}}, ...}}},
  "[TargetPercent](#cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-targetpercent)" : {{Number}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-timeoutminutes)" : {{Number}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-auroraserverlessscalingconfiguration-syntax.yaml"></a>

```
  [CrossAccountRole](#cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-crossaccountrole): {{String}}
  [ExternalId](#cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-externalid): {{String}}
  [GlobalClusterIdentifier](#cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-globalclusteridentifier): {{String}}
  [RegionDatabaseClusterArns](#cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-regiondatabaseclusterarns): {{
    {{Key}}: {{Value}}}}
  [TargetPercent](#cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-targetpercent): {{Number}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-timeoutminutes): {{Number}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-auroraserverlessscalingconfiguration-properties"></a>

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-crossaccountrole"></a>
The cross account role for the configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-externalid"></a>
The external ID (secret key) for the configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalClusterIdentifier`  <a name="cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-globalclusteridentifier"></a>
The global cluster identifier for a global database.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][0-9A-Za-z-:._]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionDatabaseClusterArns`  <a name="cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-regiondatabaseclusterarns"></a>
Per-Region configuration that maps each Region to the Aurora database cluster ARN for scaling.
*Required*: Yes
*Type*: Object of String
*Pattern*: `^[a-z]{2}-[a-z-]+-\d+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetPercent`  <a name="cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-targetpercent"></a>
The target capacity percentage for Aurora Serverless scaling.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-auroraserverlessscalingconfiguration-timeoutminutes"></a>
The timeout value specified for the configuration.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
