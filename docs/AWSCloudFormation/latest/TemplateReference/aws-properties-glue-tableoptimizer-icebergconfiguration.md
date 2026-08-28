---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-tableoptimizer-icebergconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::TableOptimizer IcebergConfiguration
<a name="aws-properties-glue-tableoptimizer-icebergconfiguration"></a>

 IcebergConfiguration is a property type within the `AWS::Glue::TableOptimizer` resource in AWS CloudFormation. This configuration is used when setting up table optimization for Iceberg tables in AWS Glue.

## Syntax
<a name="aws-properties-glue-tableoptimizer-icebergconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-tableoptimizer-icebergconfiguration-syntax.json"></a>

```
{
  "[Location](#cfn-glue-tableoptimizer-icebergconfiguration-location)" : {{String}},
  "[OrphanFileRetentionPeriodInDays](#cfn-glue-tableoptimizer-icebergconfiguration-orphanfileretentionperiodindays)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-glue-tableoptimizer-icebergconfiguration-syntax.yaml"></a>

```
  [Location](#cfn-glue-tableoptimizer-icebergconfiguration-location): {{String}}
  [OrphanFileRetentionPeriodInDays](#cfn-glue-tableoptimizer-icebergconfiguration-orphanfileretentionperiodindays): {{Integer}}
```

## Properties
<a name="aws-properties-glue-tableoptimizer-icebergconfiguration-properties"></a>

`Location`  <a name="cfn-glue-tableoptimizer-icebergconfiguration-location"></a>
Specifies a directory in which to look for orphan files (defaults to the table's location). You may choose a sub-directory rather than the top-level table location.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrphanFileRetentionPeriodInDays`  <a name="cfn-glue-tableoptimizer-icebergconfiguration-orphanfileretentionperiodindays"></a>
The specific number of days you want to keep the orphan files.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
