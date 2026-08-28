---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-tableoptimizer-retentionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::TableOptimizer RetentionConfiguration
<a name="aws-properties-glue-tableoptimizer-retentionconfiguration"></a>

The configuration for a snapshot retention optimizer for Apache Iceberg tables.

## Syntax
<a name="aws-properties-glue-tableoptimizer-retentionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-tableoptimizer-retentionconfiguration-syntax.json"></a>

```
{
  "[IcebergConfiguration](#cfn-glue-tableoptimizer-retentionconfiguration-icebergconfiguration)" : {{IcebergRetentionConfiguration}}
}
```

### YAML
<a name="aws-properties-glue-tableoptimizer-retentionconfiguration-syntax.yaml"></a>

```
  [IcebergConfiguration](#cfn-glue-tableoptimizer-retentionconfiguration-icebergconfiguration): {{
    IcebergRetentionConfiguration}}
```

## Properties
<a name="aws-properties-glue-tableoptimizer-retentionconfiguration-properties"></a>

`IcebergConfiguration`  <a name="cfn-glue-tableoptimizer-retentionconfiguration-icebergconfiguration"></a>
The configuration for an Iceberg snapshot retention optimizer.
*Required*: No
*Type*: [IcebergRetentionConfiguration](aws-properties-glue-tableoptimizer-icebergretentionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
