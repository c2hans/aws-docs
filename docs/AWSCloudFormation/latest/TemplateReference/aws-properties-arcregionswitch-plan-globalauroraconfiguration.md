---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-globalauroraconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan GlobalAuroraConfiguration
<a name="aws-properties-arcregionswitch-plan-globalauroraconfiguration"></a>

Configuration for Amazon Aurora global databases used in a Region switch plan.

## Syntax
<a name="aws-properties-arcregionswitch-plan-globalauroraconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-globalauroraconfiguration-syntax.json"></a>

```
{
  "[Behavior](#cfn-arcregionswitch-plan-globalauroraconfiguration-behavior)" : {{}},
  "[CrossAccountRole](#cfn-arcregionswitch-plan-globalauroraconfiguration-crossaccountrole)" : {{String}},
  "[DatabaseClusterArns](#cfn-arcregionswitch-plan-globalauroraconfiguration-databaseclusterarns)" : {{[ String, ... ]}},
  "[ExternalId](#cfn-arcregionswitch-plan-globalauroraconfiguration-externalid)" : {{String}},
  "[GlobalClusterIdentifier](#cfn-arcregionswitch-plan-globalauroraconfiguration-globalclusteridentifier)" : {{String}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-globalauroraconfiguration-timeoutminutes)" : {{Number}},
  "[Ungraceful](#cfn-arcregionswitch-plan-globalauroraconfiguration-ungraceful)" : {{GlobalAuroraUngraceful}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-globalauroraconfiguration-syntax.yaml"></a>

```
  [Behavior](#cfn-arcregionswitch-plan-globalauroraconfiguration-behavior): {{
    }}
  [CrossAccountRole](#cfn-arcregionswitch-plan-globalauroraconfiguration-crossaccountrole): {{String}}
  [DatabaseClusterArns](#cfn-arcregionswitch-plan-globalauroraconfiguration-databaseclusterarns): {{
    - String}}
  [ExternalId](#cfn-arcregionswitch-plan-globalauroraconfiguration-externalid): {{String}}
  [GlobalClusterIdentifier](#cfn-arcregionswitch-plan-globalauroraconfiguration-globalclusteridentifier): {{String}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-globalauroraconfiguration-timeoutminutes): {{Number}}
  [Ungraceful](#cfn-arcregionswitch-plan-globalauroraconfiguration-ungraceful): {{
    GlobalAuroraUngraceful}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-globalauroraconfiguration-properties"></a>

`Behavior`  <a name="cfn-arcregionswitch-plan-globalauroraconfiguration-behavior"></a>
The behavior for a global database, that is, only allow switchover or also allow failover.
*Required*: Yes
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-globalauroraconfiguration-crossaccountrole"></a>
The cross account role for the configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseClusterArns`  <a name="cfn-arcregionswitch-plan-globalauroraconfiguration-databaseclusterarns"></a>
The database cluster Amazon Resource Names (ARNs) for a global database.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-globalauroraconfiguration-externalid"></a>
The external ID (secret key) for the configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalClusterIdentifier`  <a name="cfn-arcregionswitch-plan-globalauroraconfiguration-globalclusteridentifier"></a>
The global cluster identifier for a global database.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-globalauroraconfiguration-timeoutminutes"></a>
The timeout value specified for the configuration.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ungraceful`  <a name="cfn-arcregionswitch-plan-globalauroraconfiguration-ungraceful"></a>
The settings for ungraceful execution.
*Required*: No
*Type*: [GlobalAuroraUngraceful](aws-properties-arcregionswitch-plan-globalauroraungraceful.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
