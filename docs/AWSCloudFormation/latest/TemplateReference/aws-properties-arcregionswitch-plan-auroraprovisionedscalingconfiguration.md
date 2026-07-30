---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-auroraprovisionedscalingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan AuroraProvisionedScalingConfiguration
<a name="aws-properties-arcregionswitch-plan-auroraprovisionedscalingconfiguration"></a>

Configuration for Amazon Aurora provisioned cluster scaling used in a Region switch plan.

## Syntax
<a name="aws-properties-arcregionswitch-plan-auroraprovisionedscalingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-auroraprovisionedscalingconfiguration-syntax.json"></a>

```
{
  "[CrossAccountRole](#cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-crossaccountrole)" : {{String}},
  "[ExternalId](#cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-externalid)" : {{String}},
  "[GlobalClusterIdentifier](#cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-globalclusteridentifier)" : {{String}},
  "[InstanceArns](#cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-instancearns)" : {{{{{Key}}: {{Value}}, ...}}},
  "[RegionDatabaseClusterArns](#cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-regiondatabaseclusterarns)" : {{{{{Key}}: {{Value}}, ...}}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-timeoutminutes)" : {{Number}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-auroraprovisionedscalingconfiguration-syntax.yaml"></a>

```
  [CrossAccountRole](#cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-crossaccountrole): {{String}}
  [ExternalId](#cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-externalid): {{String}}
  [GlobalClusterIdentifier](#cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-globalclusteridentifier): {{String}}
  [InstanceArns](#cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-instancearns): {{
    {{Key}}: {{Value}}}}
  [RegionDatabaseClusterArns](#cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-regiondatabaseclusterarns): {{
    {{Key}}: {{Value}}}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-timeoutminutes): {{Number}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-auroraprovisionedscalingconfiguration-properties"></a>

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-crossaccountrole"></a>
The cross account role for the configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-externalid"></a>
The external ID (secret key) for the configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalClusterIdentifier`  <a name="cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-globalclusteridentifier"></a>
The global cluster identifier for a global database.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][0-9A-Za-z-:._]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArns`  <a name="cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-instancearns"></a>
Per-Region configuration that maps each Region to the Aurora database instance ARN for scaling.
*Required*: Yes
*Type*: Object of String
*Pattern*: `^[a-z]{2}-[a-z-]+-\d+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionDatabaseClusterArns`  <a name="cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-regiondatabaseclusterarns"></a>
Per-Region configuration that maps each Region to the Aurora database cluster ARN for scaling.
*Required*: Yes
*Type*: Object of String
*Pattern*: `^[a-z]{2}-[a-z-]+-\d+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-auroraprovisionedscalingconfiguration-timeoutminutes"></a>
The timeout value specified for the configuration.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
