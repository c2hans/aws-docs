---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-policy-multiregiontargets.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Policy MultiRegionTargets
<a name="aws-properties-resiliencehubv2-policy-multiregiontargets"></a>

Defines the multi-Region disaster recovery targets for a resilience policy.

## Syntax
<a name="aws-properties-resiliencehubv2-policy-multiregiontargets-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-policy-multiregiontargets-syntax.json"></a>

```
{
  "[DisasterRecoveryApproach](#cfn-resiliencehubv2-policy-multiregiontargets-disasterrecoveryapproach)" : {{String}},
  "[RpoInMinutes](#cfn-resiliencehubv2-policy-multiregiontargets-rpoinminutes)" : {{Integer}},
  "[RtoInMinutes](#cfn-resiliencehubv2-policy-multiregiontargets-rtoinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-policy-multiregiontargets-syntax.yaml"></a>

```
  [DisasterRecoveryApproach](#cfn-resiliencehubv2-policy-multiregiontargets-disasterrecoveryapproach): {{String}}
  [RpoInMinutes](#cfn-resiliencehubv2-policy-multiregiontargets-rpoinminutes): {{Integer}}
  [RtoInMinutes](#cfn-resiliencehubv2-policy-multiregiontargets-rtoinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-resiliencehubv2-policy-multiregiontargets-properties"></a>

`DisasterRecoveryApproach`  <a name="cfn-resiliencehubv2-policy-multiregiontargets-disasterrecoveryapproach"></a>
The disaster recovery approach for multi-Region.
*Required*: No
*Type*: String
*Allowed values*: `ACTIVE_ACTIVE | HOT_STANDBY | WARM_STANDBY | PILOT_LIGHT | BACKUP_AND_RESTORE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RpoInMinutes`  <a name="cfn-resiliencehubv2-policy-multiregiontargets-rpoinminutes"></a>
The recovery point objective (RPO) target for multi-Region, in minutes.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RtoInMinutes`  <a name="cfn-resiliencehubv2-policy-multiregiontargets-rtoinminutes"></a>
The recovery time objective (RTO) target for multi-Region, in minutes.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
