---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-trinoparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource TrinoParameters
<a name="aws-properties-quicksight-datasource-trinoparameters"></a>

The parameters that are required to connect to a Trino data source.

## Syntax
<a name="aws-properties-quicksight-datasource-trinoparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-trinoparameters-syntax.json"></a>

```
{
  "[Catalog](#cfn-quicksight-datasource-trinoparameters-catalog)" : {{String}},
  "[Host](#cfn-quicksight-datasource-trinoparameters-host)" : {{String}},
  "[Port](#cfn-quicksight-datasource-trinoparameters-port)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-trinoparameters-syntax.yaml"></a>

```
  [Catalog](#cfn-quicksight-datasource-trinoparameters-catalog): {{String}}
  [Host](#cfn-quicksight-datasource-trinoparameters-host): {{String}}
  [Port](#cfn-quicksight-datasource-trinoparameters-port): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-datasource-trinoparameters-properties"></a>

`Catalog`  <a name="cfn-quicksight-datasource-trinoparameters-catalog"></a>
The catalog name for the Trino data source.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Host`  <a name="cfn-quicksight-datasource-trinoparameters-host"></a>
The host name of the Trino data source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-quicksight-datasource-trinoparameters-port"></a>
The port for the Trino data source.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
