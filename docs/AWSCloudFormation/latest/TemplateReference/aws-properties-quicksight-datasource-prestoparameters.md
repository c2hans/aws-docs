---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-prestoparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource PrestoParameters
<a name="aws-properties-quicksight-datasource-prestoparameters"></a>

The parameters for Presto.

## Syntax
<a name="aws-properties-quicksight-datasource-prestoparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-prestoparameters-syntax.json"></a>

```
{
  "[Catalog](#cfn-quicksight-datasource-prestoparameters-catalog)" : {{String}},
  "[Host](#cfn-quicksight-datasource-prestoparameters-host)" : {{String}},
  "[Port](#cfn-quicksight-datasource-prestoparameters-port)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-prestoparameters-syntax.yaml"></a>

```
  [Catalog](#cfn-quicksight-datasource-prestoparameters-catalog): {{String}}
  [Host](#cfn-quicksight-datasource-prestoparameters-host): {{String}}
  [Port](#cfn-quicksight-datasource-prestoparameters-port): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-datasource-prestoparameters-properties"></a>

`Catalog`  <a name="cfn-quicksight-datasource-prestoparameters-catalog"></a>
Catalog.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Host`  <a name="cfn-quicksight-datasource-prestoparameters-host"></a>
Host.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-quicksight-datasource-prestoparameters-port"></a>
Port.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
