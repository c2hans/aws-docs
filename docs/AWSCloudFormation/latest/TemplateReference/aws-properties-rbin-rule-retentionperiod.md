---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rbin-rule-retentionperiod.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Rbin::Rule RetentionPeriod
<a name="aws-properties-rbin-rule-retentionperiod"></a>

Information about the retention period for which the retention rule is to retain resources.

## Syntax
<a name="aws-properties-rbin-rule-retentionperiod-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rbin-rule-retentionperiod-syntax.json"></a>

```
{
  "[RetentionPeriodUnit](#cfn-rbin-rule-retentionperiod-retentionperiodunit)" : {{String}},
  "[RetentionPeriodValue](#cfn-rbin-rule-retentionperiod-retentionperiodvalue)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-rbin-rule-retentionperiod-syntax.yaml"></a>

```
  [RetentionPeriodUnit](#cfn-rbin-rule-retentionperiod-retentionperiodunit): {{String}}
  [RetentionPeriodValue](#cfn-rbin-rule-retentionperiod-retentionperiodvalue): {{Integer}}
```

## Properties
<a name="aws-properties-rbin-rule-retentionperiod-properties"></a>

`RetentionPeriodUnit`  <a name="cfn-rbin-rule-retentionperiod-retentionperiodunit"></a>
The unit of time in which the retention period is measured. Currently, only `DAYS` is supported.
*Required*: Yes
*Type*: String
*Allowed values*: `DAYS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetentionPeriodValue`  <a name="cfn-rbin-rule-retentionperiod-retentionperiodvalue"></a>
The period value for which the retention rule is to retain resources, measured in days. The supported retention periods are:
+ EBS volumes: 1 - 7 days
+ EBS snapshots and EBS-backed AMIs: 1 - 365 days
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `3650`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
