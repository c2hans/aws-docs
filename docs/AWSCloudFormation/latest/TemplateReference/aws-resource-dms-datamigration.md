---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-datamigration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::DataMigration
<a name="aws-resource-dms-datamigration"></a>

This object provides information about a AWS DMS data migration.

## Syntax
<a name="aws-resource-dms-datamigration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-dms-datamigration-syntax.json"></a>

```
{
  "Type" : "AWS::DMS::DataMigration",
  "Properties" : {
      "[DataMigrationIdentifier](#cfn-dms-datamigration-datamigrationidentifier)" : {{String}},
      "[DataMigrationName](#cfn-dms-datamigration-datamigrationname)" : {{String}},
      "[DataMigrationSettings](#cfn-dms-datamigration-datamigrationsettings)" : {{DataMigrationSettings}},
      "[DataMigrationType](#cfn-dms-datamigration-datamigrationtype)" : {{String}},
      "[MigrationProjectIdentifier](#cfn-dms-datamigration-migrationprojectidentifier)" : {{String}},
      "[ServiceAccessRoleArn](#cfn-dms-datamigration-serviceaccessrolearn)" : {{String}},
      "[SourceDataSettings](#cfn-dms-datamigration-sourcedatasettings)" : {{[ SourceDataSettings, ... ]}},
      "[Tags](#cfn-dms-datamigration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-dms-datamigration-syntax.yaml"></a>

```
Type: AWS::DMS::DataMigration
Properties:
  [DataMigrationIdentifier](#cfn-dms-datamigration-datamigrationidentifier): {{String}}
  [DataMigrationName](#cfn-dms-datamigration-datamigrationname): {{String}}
  [DataMigrationSettings](#cfn-dms-datamigration-datamigrationsettings): {{
    DataMigrationSettings}}
  [DataMigrationType](#cfn-dms-datamigration-datamigrationtype): {{String}}
  [MigrationProjectIdentifier](#cfn-dms-datamigration-migrationprojectidentifier): {{String}}
  [ServiceAccessRoleArn](#cfn-dms-datamigration-serviceaccessrolearn): {{String}}
  [SourceDataSettings](#cfn-dms-datamigration-sourcedatasettings): {{
    - SourceDataSettings}}
  [Tags](#cfn-dms-datamigration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-dms-datamigration-properties"></a>

`DataMigrationIdentifier`  <a name="cfn-dms-datamigration-datamigrationidentifier"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataMigrationName`  <a name="cfn-dms-datamigration-datamigrationname"></a>
The user-friendly name for the data migration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataMigrationSettings`  <a name="cfn-dms-datamigration-datamigrationsettings"></a>
Specifies CloudWatch settings and selection rules for the data migration.
*Required*: No
*Type*: [DataMigrationSettings](aws-properties-dms-datamigration-datamigrationsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataMigrationType`  <a name="cfn-dms-datamigration-datamigrationtype"></a>
Specifies whether the data migration is full-load only, change data capture (CDC) only, or full-load and CDC.
*Required*: Yes
*Type*: String
*Allowed values*: `full-load | cdc | full-load-and-cdc`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MigrationProjectIdentifier`  <a name="cfn-dms-datamigration-migrationprojectidentifier"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceAccessRoleArn`  <a name="cfn-dms-datamigration-serviceaccessrolearn"></a>
The IAM role that the data migration uses to access AWS resources.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceDataSettings`  <a name="cfn-dms-datamigration-sourcedatasettings"></a>
Specifies information about the data migration's source data provider.
*Required*: No
*Type*: [Array](aws-properties-dms-datamigration-sourcedatasettings.md) of [SourceDataSettings](aws-properties-dms-datamigration-sourcedatasettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-dms-datamigration-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-dms-datamigration-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-dms-datamigration-return-values"></a>

### Ref
<a name="aws-resource-dms-datamigration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-dms-datamigration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-dms-datamigration-return-values-fn--getatt-fn--getatt"></a>

`DataMigrationArn`  <a name="DataMigrationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) that identifies this replication.

`DataMigrationCreateTime`  <a name="DataMigrationCreateTime-fn::getatt"></a>
The UTC time when DMS created the data migration.
