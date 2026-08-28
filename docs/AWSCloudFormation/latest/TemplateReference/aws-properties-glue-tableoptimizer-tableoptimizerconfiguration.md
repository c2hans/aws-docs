---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-tableoptimizer-tableoptimizerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::TableOptimizer TableOptimizerConfiguration
<a name="aws-properties-glue-tableoptimizer-tableoptimizerconfiguration"></a>

Specifies configuration details of a table optimizer.

## Syntax
<a name="aws-properties-glue-tableoptimizer-tableoptimizerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-tableoptimizer-tableoptimizerconfiguration-syntax.json"></a>

```
{
  "[CompactionConfiguration](#cfn-glue-tableoptimizer-tableoptimizerconfiguration-compactionconfiguration)" : {{CompactionConfiguration}},
  "[Enabled](#cfn-glue-tableoptimizer-tableoptimizerconfiguration-enabled)" : {{Boolean}},
  "[OrphanFileDeletionConfiguration](#cfn-glue-tableoptimizer-tableoptimizerconfiguration-orphanfiledeletionconfiguration)" : {{OrphanFileDeletionConfiguration}},
  "[RetentionConfiguration](#cfn-glue-tableoptimizer-tableoptimizerconfiguration-retentionconfiguration)" : {{RetentionConfiguration}},
  "[RoleArn](#cfn-glue-tableoptimizer-tableoptimizerconfiguration-rolearn)" : {{String}},
  "[VpcConfiguration](#cfn-glue-tableoptimizer-tableoptimizerconfiguration-vpcconfiguration)" : {{VpcConfiguration}}
}
```

### YAML
<a name="aws-properties-glue-tableoptimizer-tableoptimizerconfiguration-syntax.yaml"></a>

```
  [CompactionConfiguration](#cfn-glue-tableoptimizer-tableoptimizerconfiguration-compactionconfiguration): {{
    CompactionConfiguration}}
  [Enabled](#cfn-glue-tableoptimizer-tableoptimizerconfiguration-enabled): {{Boolean}}
  [OrphanFileDeletionConfiguration](#cfn-glue-tableoptimizer-tableoptimizerconfiguration-orphanfiledeletionconfiguration): {{
    OrphanFileDeletionConfiguration}}
  [RetentionConfiguration](#cfn-glue-tableoptimizer-tableoptimizerconfiguration-retentionconfiguration): {{
    RetentionConfiguration}}
  [RoleArn](#cfn-glue-tableoptimizer-tableoptimizerconfiguration-rolearn): {{String}}
  [VpcConfiguration](#cfn-glue-tableoptimizer-tableoptimizerconfiguration-vpcconfiguration): {{
    VpcConfiguration}}
```

## Properties
<a name="aws-properties-glue-tableoptimizer-tableoptimizerconfiguration-properties"></a>

`CompactionConfiguration`  <a name="cfn-glue-tableoptimizer-tableoptimizerconfiguration-compactionconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [CompactionConfiguration](aws-properties-glue-tableoptimizer-compactionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-glue-tableoptimizer-tableoptimizerconfiguration-enabled"></a>
Whether the table optimization is enabled.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrphanFileDeletionConfiguration`  <a name="cfn-glue-tableoptimizer-tableoptimizerconfiguration-orphanfiledeletionconfiguration"></a>
`OrphanFileDeletionConfiguration` is a property that can be included within the TableOptimizer resource. It controls the automatic deletion of orphaned files - files that are not tracked by the table metadata, and older than the configured age limit.
*Required*: No
*Type*: [OrphanFileDeletionConfiguration](aws-properties-glue-tableoptimizer-orphanfiledeletionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetentionConfiguration`  <a name="cfn-glue-tableoptimizer-tableoptimizerconfiguration-retentionconfiguration"></a>
The configuration for a snapshot retention optimizer for Apache Iceberg tables.
*Required*: No
*Type*: [RetentionConfiguration](aws-properties-glue-tableoptimizer-retentionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-glue-tableoptimizer-tableoptimizerconfiguration-rolearn"></a>
A role passed by the caller which gives the service permission to update the resources associated with the optimizer on the caller's behalf.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcConfiguration`  <a name="cfn-glue-tableoptimizer-tableoptimizerconfiguration-vpcconfiguration"></a>
An object that describes the VPC configuration for a table optimizer. This configuration is necessary to perform optimization on tables that are in a customer VPC.
*Required*: No
*Type*: [VpcConfiguration](aws-properties-glue-tableoptimizer-vpcconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
