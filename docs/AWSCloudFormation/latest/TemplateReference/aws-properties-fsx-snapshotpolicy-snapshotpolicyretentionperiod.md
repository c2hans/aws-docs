---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-snapshotpolicy-snapshotpolicyretentionperiod.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::SnapshotPolicy SnapshotPolicyRetentionPeriod

The length of time that snapshots created by this schedule are locked. This setting applies only to volumes that have snapshot locking enabled.

## Syntax
<a name="aws-properties-fsx-snapshotpolicy-snapshotpolicyretentionperiod-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-snapshotpolicy-snapshotpolicyretentionperiod-syntax.json"></a>

```json
{
  "[Type](#cfn-fsx-snapshotpolicy-snapshotpolicyretentionperiod-type)" : {{String}},
  "[Value](#cfn-fsx-snapshotpolicy-snapshotpolicyretentionperiod-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-fsx-snapshotpolicy-snapshotpolicyretentionperiod-syntax.yaml"></a>

```yaml
  [Type](#cfn-fsx-snapshotpolicy-snapshotpolicyretentionperiod-type): {{String}}
  [Value](#cfn-fsx-snapshotpolicy-snapshotpolicyretentionperiod-value): {{Integer}}
```

## Properties
<a name="aws-properties-fsx-snapshotpolicy-snapshotpolicyretentionperiod-properties"></a>

`Type`  <a name="cfn-fsx-snapshotpolicy-snapshotpolicyretentionperiod-type"></a>
The unit of time for the retention period. If you set it to `INFINITE`, the snapshots are retained forever.
*Required*: Yes
*Type*: String
*Allowed values*: `SECONDS | MINUTES | HOURS | DAYS | MONTHS | YEARS | INFINITE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-fsx-snapshotpolicy-snapshotpolicyretentionperiod-value"></a>
Defines the amount of time for the retention period. You can't set a value for `INFINITE`.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
