---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-pointintimerecoveryspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable PointInTimeRecoverySpecification
<a name="aws-properties-dynamodb-globaltable-pointintimerecoveryspecification"></a>

Represents the settings used to enable point in time recovery.

## Syntax
<a name="aws-properties-dynamodb-globaltable-pointintimerecoveryspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-pointintimerecoveryspecification-syntax.json"></a>

```
{
  "[PointInTimeRecoveryEnabled](#cfn-dynamodb-globaltable-pointintimerecoveryspecification-pointintimerecoveryenabled)" : {{Boolean}},
  "[RecoveryPeriodInDays](#cfn-dynamodb-globaltable-pointintimerecoveryspecification-recoveryperiodindays)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-pointintimerecoveryspecification-syntax.yaml"></a>

```
  [PointInTimeRecoveryEnabled](#cfn-dynamodb-globaltable-pointintimerecoveryspecification-pointintimerecoveryenabled): {{Boolean}}
  [RecoveryPeriodInDays](#cfn-dynamodb-globaltable-pointintimerecoveryspecification-recoveryperiodindays): {{Integer}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-pointintimerecoveryspecification-properties"></a>

`PointInTimeRecoveryEnabled`  <a name="cfn-dynamodb-globaltable-pointintimerecoveryspecification-pointintimerecoveryenabled"></a>
Indicates whether point in time recovery is enabled (true) or disabled (false) on the table.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecoveryPeriodInDays`  <a name="cfn-dynamodb-globaltable-pointintimerecoveryspecification-recoveryperiodindays"></a>
The number of preceding days for which continuous backups are taken and maintained. Your table data is only recoverable to any point-in-time from within the configured recovery period. This parameter is optional. If no value is provided, the value will default to 35.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `35`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
