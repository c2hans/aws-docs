---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-tableoptimizer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::TableOptimizer
<a name="aws-resource-glue-tableoptimizer"></a>

An AWS Glue resource for enabling table optimizers to improve read performance for open table formats.

## Syntax
<a name="aws-resource-glue-tableoptimizer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-glue-tableoptimizer-syntax.json"></a>

```
{
  "Type" : "AWS::Glue::TableOptimizer",
  "Properties" : {
      "[CatalogId](#cfn-glue-tableoptimizer-catalogid)" : {{String}},
      "[DatabaseName](#cfn-glue-tableoptimizer-databasename)" : {{String}},
      "[TableName](#cfn-glue-tableoptimizer-tablename)" : {{String}},
      "[TableOptimizerConfiguration](#cfn-glue-tableoptimizer-tableoptimizerconfiguration)" : {{TableOptimizerConfiguration}},
      "[Type](#cfn-glue-tableoptimizer-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-glue-tableoptimizer-syntax.yaml"></a>

```
Type: AWS::Glue::TableOptimizer
Properties:
  [CatalogId](#cfn-glue-tableoptimizer-catalogid): {{String}}
  [DatabaseName](#cfn-glue-tableoptimizer-databasename): {{String}}
  [TableName](#cfn-glue-tableoptimizer-tablename): {{String}}
  [TableOptimizerConfiguration](#cfn-glue-tableoptimizer-tableoptimizerconfiguration): {{
    TableOptimizerConfiguration}}
  [Type](#cfn-glue-tableoptimizer-type): {{String}}
```

## Properties
<a name="aws-resource-glue-tableoptimizer-properties"></a>

`CatalogId`  <a name="cfn-glue-tableoptimizer-catalogid"></a>
The catalog ID of the table.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseName`  <a name="cfn-glue-tableoptimizer-databasename"></a>
The name of the database. For Hive compatibility, this is folded to lowercase when it is stored.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableName`  <a name="cfn-glue-tableoptimizer-tablename"></a>
The table name. For Hive compatibility, this must be entirely lowercase.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableOptimizerConfiguration`  <a name="cfn-glue-tableoptimizer-tableoptimizerconfiguration"></a>
Specifies configuration details of a table optimizer.
*Required*: Yes
*Type*: [TableOptimizerConfiguration](aws-properties-glue-tableoptimizer-tableoptimizerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-glue-tableoptimizer-type"></a>
The type of table optimizer. The valid values are:
+ compaction - for managing compaction with a table optimizer.
+ retention - for managing the retention of snapshot with a table optimizer.
+  orphan\_file\_deletion - for managing the deletion of orphan files with a table optimizer.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-glue-tableoptimizer-return-values"></a>

### Ref
<a name="aws-resource-glue-tableoptimizer-return-values-ref"></a>

## Examples
<a name="aws-resource-glue-tableoptimizer--examples"></a>

**Topics**
+ [Compaction table optimizer example](#aws-resource-glue-tableoptimizer--examples--Compaction_table_optimizer_example)
+ [Snapshot retention table optimizer example](#aws-resource-glue-tableoptimizer--examples--Snapshot_retention_table_optimizer_example)
+ [Orphan file deletion table optimizer example](#aws-resource-glue-tableoptimizer--examples--Orphan_file_deletion_table_optimizer_example)

### Compaction table optimizer example
<a name="aws-resource-glue-tableoptimizer--examples--Compaction_table_optimizer_example"></a>

#### JSON
<a name="aws-resource-glue-tableoptimizer--examples--Compaction_table_optimizer_example--json"></a>

```
{
  "GlueTableOptimizer": {
    "Type": "AWS::Glue::TableOptimizer",
    "Properties": {
      "CatalogId": {"Ref": "AWS::AccountId"},
      "DatabaseName": {"Ref": "GlueDatabase"},
      "TableName": {"Ref": "GlueTable"},
      "Type": "compaction",
      "TableOptimizerConfiguration": {
        "RoleArn": {"Fn:: GetAtt": ["CompactionRole", "Arn"]},
        "Enabled": true
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-glue-tableoptimizer--examples--Compaction_table_optimizer_example--yaml"></a>

```
GlueTableOptimizer:
  Type: AWS::Glue::TableOptimizer
  Properties:
    CatalogId: !Ref AWS::AccountId
    DatabaseName: !Ref GlueDatabase
    TableName: !Ref GlueTable
    Type: "compaction"
    TableOptimizerConfiguration:
      RoleArn: !GetAtt CompactionRole.Arn
      Enabled: True
```

### Snapshot retention table optimizer example
<a name="aws-resource-glue-tableoptimizer--examples--Snapshot_retention_table_optimizer_example"></a>

#### JSON
<a name="aws-resource-glue-tableoptimizer--examples--Snapshot_retention_table_optimizer_example--json"></a>

```
{
  "GlueTableOptimizer": {
    "Type": "AWS::Glue::TableOptimizer",
    "Properties": {
      "CatalogId": {"Ref": "AWS::AccountId"},
      "DatabaseName": {"Ref": "GlueDatabase"},
      "TableName": {"Ref": "GlueTable"},
      "Type": "retention",
      "TableOptimizerConfiguration": {
        "RoleArn": {"Fn::GetAtt": ["RetentionRole", "Arn"]},
        "Enabled": true,
        "RetentionConfiguration": {
          "icebergConfiguration": {
            "snapshotRetentionPeriodInDays": 7,
            "numberOfSnapshotsToRetain": 2,
            "cleanExpiredFiles": true
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-glue-tableoptimizer--examples--Snapshot_retention_table_optimizer_example--yaml"></a>

```
GlueTableOptimizer:
    Type: AWS::Glue::TableOptimizer
    Properties:
        CatalogId: !Ref AWS::AccountId
        DatabaseName: !Ref GlueDatabase
        TableName: !Ref GlueTable
        Type: "retention"
        TableOptimizerConfiguration:
            RoleArn: !GetAtt TableOptimizerRole.Arn
            Enabled: False
            RetentionConfiguration:
              IcebergConfiguration:
                SnapshotRetentionPeriodInDays: 7
                NumberOfSnapshotsToRetain: 5
                CleanExpiredFiles: True
```

### Orphan file deletion table optimizer example
<a name="aws-resource-glue-tableoptimizer--examples--Orphan_file_deletion_table_optimizer_example"></a>

#### JSON
<a name="aws-resource-glue-tableoptimizer--examples--Orphan_file_deletion_table_optimizer_example--json"></a>

```
{
  "OrphanFileDeletionOptimizer": {
    "Type": "AWS::Glue::TableOptimizer",
    "Properties": {
      "CatalogId": {"Ref": "AWS::AccountId"},
      "DatabaseName": {"Ref": "GlueDatabase"},
      "TableName": {"Ref": "GlueTable"},
      "Type": "orphan_file_deletion",
      "TableOptimizerConfiguration": {
        "RoleArn": {"Fn::GetAtt": ["OrphanFileDeletionRole", "Arn"]},
        "Enabled": true,
        "OrphanFileDeletionConfiguration": {
          "icebergConfiguration": {
            "orphanFileRetentionPeriodInDays": 5,
            "location": "s3://my-bucket/table-location/"
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-glue-tableoptimizer--examples--Orphan_file_deletion_table_optimizer_example--yaml"></a>

```
GlueTableOptimizer:
    Type: AWS::Glue::TableOptimizer
    Properties:
      CatalogId: !Ref AWS::AccountId
      DatabaseName: !Ref GlueDatabase
      TableName: !Ref GlueTable
      Type: "orphan_file_deletion"
      TableOptimizerConfiguration:
        RoleArn: !GetAtt TableOptimizerRole.Arn
        Enabled: False
        OrphanFileDeletionConfiguration:
          IcebergConfiguration:
            OrphanFileRetentionPeriodInDays: 10
            Location: !Join ['', ['s3://', !ImportValue TestIcebergS3Bucket, '/orphan-files/']]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
