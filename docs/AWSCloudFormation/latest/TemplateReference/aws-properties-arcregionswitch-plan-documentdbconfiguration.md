---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-documentdbconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan DocumentDbConfiguration
<a name="aws-properties-arcregionswitch-plan-documentdbconfiguration"></a>

Configuration for Amazon DocumentDB global clusters used in a Region switch plan.

## Syntax
<a name="aws-properties-arcregionswitch-plan-documentdbconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-documentdbconfiguration-syntax.json"></a>

```
{
  "[Behavior](#cfn-arcregionswitch-plan-documentdbconfiguration-behavior)" : {{}},
  "[CrossAccountRole](#cfn-arcregionswitch-plan-documentdbconfiguration-crossaccountrole)" : {{String}},
  "[DatabaseClusterArns](#cfn-arcregionswitch-plan-documentdbconfiguration-databaseclusterarns)" : {{[ String, ... ]}},
  "[ExternalId](#cfn-arcregionswitch-plan-documentdbconfiguration-externalid)" : {{String}},
  "[GlobalClusterIdentifier](#cfn-arcregionswitch-plan-documentdbconfiguration-globalclusteridentifier)" : {{String}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-documentdbconfiguration-timeoutminutes)" : {{Number}},
  "[Ungraceful](#cfn-arcregionswitch-plan-documentdbconfiguration-ungraceful)" : {{DocumentDbUngraceful}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-documentdbconfiguration-syntax.yaml"></a>

```
  [Behavior](#cfn-arcregionswitch-plan-documentdbconfiguration-behavior): {{
    }}
  [CrossAccountRole](#cfn-arcregionswitch-plan-documentdbconfiguration-crossaccountrole): {{String}}
  [DatabaseClusterArns](#cfn-arcregionswitch-plan-documentdbconfiguration-databaseclusterarns): {{
    - String}}
  [ExternalId](#cfn-arcregionswitch-plan-documentdbconfiguration-externalid): {{String}}
  [GlobalClusterIdentifier](#cfn-arcregionswitch-plan-documentdbconfiguration-globalclusteridentifier): {{String}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-documentdbconfiguration-timeoutminutes): {{Number}}
  [Ungraceful](#cfn-arcregionswitch-plan-documentdbconfiguration-ungraceful): {{
    DocumentDbUngraceful}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-documentdbconfiguration-properties"></a>

`Behavior`  <a name="cfn-arcregionswitch-plan-documentdbconfiguration-behavior"></a>
The behavior for a global cluster, that is, only allow switchover or also allow failover.
*Required*: Yes
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-documentdbconfiguration-crossaccountrole"></a>
The cross account role for the configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseClusterArns`  <a name="cfn-arcregionswitch-plan-documentdbconfiguration-databaseclusterarns"></a>
The database cluster Amazon Resource Names (ARNs) for a DocumentDB global cluster.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-documentdbconfiguration-externalid"></a>
The external ID (secret key) for the configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalClusterIdentifier`  <a name="cfn-arcregionswitch-plan-documentdbconfiguration-globalclusteridentifier"></a>
The global cluster identifier for a DocumentDB global cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][0-9A-Za-z-:._]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-documentdbconfiguration-timeoutminutes"></a>
The timeout value specified for the configuration.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ungraceful`  <a name="cfn-arcregionswitch-plan-documentdbconfiguration-ungraceful"></a>
The settings for ungraceful execution.
*Required*: No
*Type*: [DocumentDbUngraceful](aws-properties-arcregionswitch-plan-documentdbungraceful.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
