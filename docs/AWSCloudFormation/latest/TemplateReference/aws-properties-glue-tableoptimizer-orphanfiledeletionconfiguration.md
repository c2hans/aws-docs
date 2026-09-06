---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-tableoptimizer-orphanfiledeletionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::TableOptimizer OrphanFileDeletionConfiguration
<a name="aws-properties-glue-tableoptimizer-orphanfiledeletionconfiguration"></a>

Configuration for removing files that are are not tracked by the Iceberg table metadata, and are older than your configured age limit. This configuration helps optimize storage usage and costs by automatically cleaning up files that are no longer needed by the table.

## Syntax
<a name="aws-properties-glue-tableoptimizer-orphanfiledeletionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-tableoptimizer-orphanfiledeletionconfiguration-syntax.json"></a>

```
{
  "[IcebergConfiguration](#cfn-glue-tableoptimizer-orphanfiledeletionconfiguration-icebergconfiguration)" : {{IcebergConfiguration}}
}
```

### YAML
<a name="aws-properties-glue-tableoptimizer-orphanfiledeletionconfiguration-syntax.yaml"></a>

```
  [IcebergConfiguration](#cfn-glue-tableoptimizer-orphanfiledeletionconfiguration-icebergconfiguration): {{
    IcebergConfiguration}}
```

## Properties
<a name="aws-properties-glue-tableoptimizer-orphanfiledeletionconfiguration-properties"></a>

`IcebergConfiguration`  <a name="cfn-glue-tableoptimizer-orphanfiledeletionconfiguration-icebergconfiguration"></a>
The `IcebergConfiguration` property helps optimize your Iceberg tables in AWS Glue by allowing you to specify format-specific settings that control how data is stored, compressed, and managed.
*Required*: No
*Type*: [IcebergConfiguration](aws-properties-glue-tableoptimizer-icebergconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
