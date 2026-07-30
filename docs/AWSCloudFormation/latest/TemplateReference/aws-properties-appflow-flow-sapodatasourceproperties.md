---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-sapodatasourceproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow SAPODataSourceProperties
<a name="aws-properties-appflow-flow-sapodatasourceproperties"></a>

 The properties that are applied when using SAPOData as a flow source.

## Syntax
<a name="aws-properties-appflow-flow-sapodatasourceproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-sapodatasourceproperties-syntax.json"></a>

```
{
  "[ObjectPath](#cfn-appflow-flow-sapodatasourceproperties-objectpath)" : {{String}},
  "[paginationConfig](#cfn-appflow-flow-sapodatasourceproperties-paginationconfig)" : {{SAPODataPaginationConfig}},
  "[parallelismConfig](#cfn-appflow-flow-sapodatasourceproperties-parallelismconfig)" : {{SAPODataParallelismConfig}}
}
```

### YAML
<a name="aws-properties-appflow-flow-sapodatasourceproperties-syntax.yaml"></a>

```
  [ObjectPath](#cfn-appflow-flow-sapodatasourceproperties-objectpath): {{String}}
  [paginationConfig](#cfn-appflow-flow-sapodatasourceproperties-paginationconfig): {{
    SAPODataPaginationConfig}}
  [parallelismConfig](#cfn-appflow-flow-sapodatasourceproperties-parallelismconfig): {{
    SAPODataParallelismConfig}}
```

## Properties
<a name="aws-properties-appflow-flow-sapodatasourceproperties-properties"></a>

`ObjectPath`  <a name="cfn-appflow-flow-sapodatasourceproperties-objectpath"></a>
 The object path specified in the SAPOData flow source.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`paginationConfig`  <a name="cfn-appflow-flow-sapodatasourceproperties-paginationconfig"></a>
Sets the page size for each concurrent process that transfers OData records from your SAP instance.
*Required*: No
*Type*: [SAPODataPaginationConfig](aws-properties-appflow-flow-sapodatapaginationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`parallelismConfig`  <a name="cfn-appflow-flow-sapodatasourceproperties-parallelismconfig"></a>
Sets the number of concurrent processes that transfers OData records from your SAP instance.
*Required*: No
*Type*: [SAPODataParallelismConfig](aws-properties-appflow-flow-sapodataparallelismconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
