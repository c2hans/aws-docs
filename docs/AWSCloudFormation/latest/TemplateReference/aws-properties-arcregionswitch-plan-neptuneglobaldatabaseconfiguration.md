---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-neptuneglobaldatabaseconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan NeptuneGlobalDatabaseConfiguration
<a name="aws-properties-arcregionswitch-plan-neptuneglobaldatabaseconfiguration"></a>

Configuration for Amazon Neptune global databases used in a Region switch plan.

## Syntax
<a name="aws-properties-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-syntax.json"></a>

```
{
  "[Behavior](#cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-behavior)" : {{}},
  "[CrossAccountRole](#cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-crossaccountrole)" : {{String}},
  "[ExternalId](#cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-externalid)" : {{String}},
  "[GlobalClusterIdentifier](#cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-globalclusteridentifier)" : {{String}},
  "[RegionDatabaseClusterArns](#cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-regiondatabaseclusterarns)" : {{{{{Key}}: {{Value}}, ...}}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-timeoutminutes)" : {{Number}},
  "[Ungraceful](#cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-ungraceful)" : {{NeptuneUngraceful}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-syntax.yaml"></a>

```
  [Behavior](#cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-behavior): {{
    }}
  [CrossAccountRole](#cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-crossaccountrole): {{String}}
  [ExternalId](#cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-externalid): {{String}}
  [GlobalClusterIdentifier](#cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-globalclusteridentifier): {{String}}
  [RegionDatabaseClusterArns](#cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-regiondatabaseclusterarns): {{
    {{Key}}: {{Value}}}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-timeoutminutes): {{Number}}
  [Ungraceful](#cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-ungraceful): {{
    NeptuneUngraceful}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-properties"></a>

`Behavior`  <a name="cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-behavior"></a>
The behavior for a global database, that is, only allow switchover or also allow failover.
*Required*: Yes
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-crossaccountrole"></a>
The cross account role for the configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-externalid"></a>
The external ID (secret key) for the configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalClusterIdentifier`  <a name="cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-globalclusteridentifier"></a>
The global cluster identifier for a Neptune global database.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][0-9A-Za-z-]*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionDatabaseClusterArns`  <a name="cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-regiondatabaseclusterarns"></a>
The database cluster Amazon Resource Names (ARNs) for a Neptune global database.
*Required*: Yes
*Type*: Object of String
*Pattern*: `^[a-z]{2}-[a-z-]+-\d+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-timeoutminutes"></a>
The timeout value specified for the configuration.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ungraceful`  <a name="cfn-arcregionswitch-plan-neptuneglobaldatabaseconfiguration-ungraceful"></a>
The settings for ungraceful execution.
*Required*: No
*Type*: [NeptuneUngraceful](aws-properties-arcregionswitch-plan-neptuneungraceful.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
