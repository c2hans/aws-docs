---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan RdsCreateCrossRegionReplicaConfiguration
<a name="aws-properties-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration"></a>

Configuration for creating an Amazon RDS cross-Region read replica during post-recovery in a Region switch.

## Syntax
<a name="aws-properties-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-syntax.json"></a>

```
{
  "[CrossAccountRole](#cfn-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-crossaccountrole)" : {{String}},
  "[DbInstanceArnMap](#cfn-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-dbinstancearnmap)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ExternalId](#cfn-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-externalid)" : {{String}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-timeoutminutes)" : {{Number}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-syntax.yaml"></a>

```
  [CrossAccountRole](#cfn-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-crossaccountrole): {{String}}
  [DbInstanceArnMap](#cfn-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-dbinstancearnmap): {{
    {{Key}}: {{Value}}}}
  [ExternalId](#cfn-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-externalid): {{String}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-timeoutminutes): {{Number}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-properties"></a>

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-crossaccountrole"></a>
The cross-account role for the configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DbInstanceArnMap`  <a name="cfn-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-dbinstancearnmap"></a>
A map of database instance ARNs for each Region in the plan.
*Required*: Yes
*Type*: Object of String
*Pattern*: `^[a-z]{2}-[a-z-]+-\d+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-externalid"></a>
The external ID (secret key) for the configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-rdscreatecrossregionreplicaconfiguration-timeoutminutes"></a>
The timeout value specified for the configuration.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
