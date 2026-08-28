---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-table-retentionproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::Table RetentionProperties
<a name="aws-properties-timestream-table-retentionproperties"></a>

Retention properties contain the duration for which your time-series data must be stored in the magnetic store and the memory store.

## Syntax
<a name="aws-properties-timestream-table-retentionproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-table-retentionproperties-syntax.json"></a>

```
{
  "[MagneticStoreRetentionPeriodInDays](#cfn-timestream-table-retentionproperties-magneticstoreretentionperiodindays)" : {{String}},
  "[MemoryStoreRetentionPeriodInHours](#cfn-timestream-table-retentionproperties-memorystoreretentionperiodinhours)" : {{String}}
}
```

### YAML
<a name="aws-properties-timestream-table-retentionproperties-syntax.yaml"></a>

```
  [MagneticStoreRetentionPeriodInDays](#cfn-timestream-table-retentionproperties-magneticstoreretentionperiodindays): {{String}}
  [MemoryStoreRetentionPeriodInHours](#cfn-timestream-table-retentionproperties-memorystoreretentionperiodinhours): {{String}}
```

## Properties
<a name="aws-properties-timestream-table-retentionproperties-properties"></a>

`MagneticStoreRetentionPeriodInDays`  <a name="cfn-timestream-table-retentionproperties-magneticstoreretentionperiodindays"></a>
The duration for which data must be stored in the magnetic store.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemoryStoreRetentionPeriodInHours`  <a name="cfn-timestream-table-retentionproperties-memorystoreretentionperiodinhours"></a>
The duration for which data must be stored in the memory store.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
