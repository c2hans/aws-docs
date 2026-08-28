---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-table-compaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::Table Compaction
<a name="aws-properties-s3tables-table-compaction"></a>

Contains details about the compaction settings for an Iceberg table.

## Syntax
<a name="aws-properties-s3tables-table-compaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-table-compaction-syntax.json"></a>

```
{
  "[Status](#cfn-s3tables-table-compaction-status)" : {{String}},
  "[TargetFileSizeMB](#cfn-s3tables-table-compaction-targetfilesizemb)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-s3tables-table-compaction-syntax.yaml"></a>

```
  [Status](#cfn-s3tables-table-compaction-status): {{String}}
  [TargetFileSizeMB](#cfn-s3tables-table-compaction-targetfilesizemb): {{Integer}}
```

## Properties
<a name="aws-properties-s3tables-table-compaction-properties"></a>

`Status`  <a name="cfn-s3tables-table-compaction-status"></a>
The status of the maintenance configuration.
*Required*: No
*Type*: String
*Allowed values*: `enabled | disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetFileSizeMB`  <a name="cfn-s3tables-table-compaction-targetfilesizemb"></a>
The target file size for the table in MB.
*Required*: No
*Type*: Integer
*Minimum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
