---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-policy-multiaztargets.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Policy MultiAzTargets
<a name="aws-properties-resiliencehubv2-policy-multiaztargets"></a>

Defines the multi-AZ disaster recovery targets for a resilience policy.

## Syntax
<a name="aws-properties-resiliencehubv2-policy-multiaztargets-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-policy-multiaztargets-syntax.json"></a>

```
{
  "[DisasterRecoveryApproach](#cfn-resiliencehubv2-policy-multiaztargets-disasterrecoveryapproach)" : {{String}},
  "[RpoInMinutes](#cfn-resiliencehubv2-policy-multiaztargets-rpoinminutes)" : {{Integer}},
  "[RtoInMinutes](#cfn-resiliencehubv2-policy-multiaztargets-rtoinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-policy-multiaztargets-syntax.yaml"></a>

```
  [DisasterRecoveryApproach](#cfn-resiliencehubv2-policy-multiaztargets-disasterrecoveryapproach): {{String}}
  [RpoInMinutes](#cfn-resiliencehubv2-policy-multiaztargets-rpoinminutes): {{Integer}}
  [RtoInMinutes](#cfn-resiliencehubv2-policy-multiaztargets-rtoinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-resiliencehubv2-policy-multiaztargets-properties"></a>

`DisasterRecoveryApproach`  <a name="cfn-resiliencehubv2-policy-multiaztargets-disasterrecoveryapproach"></a>
The disaster recovery approach for multi-AZ.
*Required*: No
*Type*: String
*Allowed values*: `ACTIVE_ACTIVE | HOT_STANDBY | WARM_STANDBY | PILOT_LIGHT | BACKUP_AND_RESTORE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RpoInMinutes`  <a name="cfn-resiliencehubv2-policy-multiaztargets-rpoinminutes"></a>
The recovery point objective (RPO) target for multi-AZ, in minutes.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RtoInMinutes`  <a name="cfn-resiliencehubv2-policy-multiaztargets-rtoinminutes"></a>
The recovery time objective (RTO) target for multi-AZ, in minutes.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
