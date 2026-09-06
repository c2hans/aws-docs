---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-oracleparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource OracleParameters
<a name="aws-properties-quicksight-datasource-oracleparameters"></a>

Oracle parameters.

## Syntax
<a name="aws-properties-quicksight-datasource-oracleparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-oracleparameters-syntax.json"></a>

```
{
  "[Database](#cfn-quicksight-datasource-oracleparameters-database)" : {{String}},
  "[Host](#cfn-quicksight-datasource-oracleparameters-host)" : {{String}},
  "[Port](#cfn-quicksight-datasource-oracleparameters-port)" : {{Number}},
  "[UseServiceName](#cfn-quicksight-datasource-oracleparameters-useservicename)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-oracleparameters-syntax.yaml"></a>

```
  [Database](#cfn-quicksight-datasource-oracleparameters-database): {{String}}
  [Host](#cfn-quicksight-datasource-oracleparameters-host): {{String}}
  [Port](#cfn-quicksight-datasource-oracleparameters-port): {{Number}}
  [UseServiceName](#cfn-quicksight-datasource-oracleparameters-useservicename): {{Boolean}}
```

## Properties
<a name="aws-properties-quicksight-datasource-oracleparameters-properties"></a>

`Database`  <a name="cfn-quicksight-datasource-oracleparameters-database"></a>
Database.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Host`  <a name="cfn-quicksight-datasource-oracleparameters-host"></a>
Host.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-quicksight-datasource-oracleparameters-port"></a>
Port.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseServiceName`  <a name="cfn-quicksight-datasource-oracleparameters-useservicename"></a>
A Boolean value that indicates whether the `Database` uses a service name or an SID. If this value is left blank, the default value is `SID`. If this value is set to `false`, the value is `SID`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
