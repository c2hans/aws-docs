---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-volume-autocommitperiod.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::Volume AutocommitPeriod
<a name="aws-properties-fsx-volume-autocommitperiod"></a>

Sets the autocommit period of files in an FSx for ONTAP SnapLock volume, which determines how long the files must remain unmodified before they're automatically transitioned to the write once, read many (WORM) state.

For more information, see [Autocommit](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/worm-state.html#worm-state-autocommit).

## Syntax
<a name="aws-properties-fsx-volume-autocommitperiod-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-volume-autocommitperiod-syntax.json"></a>

```
{
  "[Type](#cfn-fsx-volume-autocommitperiod-type)" : {{String}},
  "[Value](#cfn-fsx-volume-autocommitperiod-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-fsx-volume-autocommitperiod-syntax.yaml"></a>

```
  [Type](#cfn-fsx-volume-autocommitperiod-type): {{String}}
  [Value](#cfn-fsx-volume-autocommitperiod-value): {{Integer}}
```

## Properties
<a name="aws-properties-fsx-volume-autocommitperiod-properties"></a>

`Type`  <a name="cfn-fsx-volume-autocommitperiod-type"></a>
Defines the type of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. Setting this value to `NONE` disables autocommit. The default value is `NONE`.
*Required*: Yes
*Type*: String
*Allowed values*: `MINUTES | HOURS | DAYS | MONTHS | YEARS | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-fsx-volume-autocommitperiod-value"></a>
Defines the amount of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. The following ranges are valid:
+ `Minutes`: 5 - 65,535
+ `Hours`: 1 - 65,535
+ `Days`: 1 - 3,650
+ `Months`: 1 - 120
+ `Years`: 1 - 10
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
