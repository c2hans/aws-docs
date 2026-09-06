---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-catalog-catalogproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Catalog CatalogProperties
<a name="aws-properties-glue-catalog-catalogproperties"></a>

A structure that specifies data lake access properties and other custom properties.

## Syntax
<a name="aws-properties-glue-catalog-catalogproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-catalog-catalogproperties-syntax.json"></a>

```
{
  "[CustomProperties](#cfn-glue-catalog-catalogproperties-customproperties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[DataLakeAccessProperties](#cfn-glue-catalog-catalogproperties-datalakeaccessproperties)" : {{DataLakeAccessProperties}}
}
```

### YAML
<a name="aws-properties-glue-catalog-catalogproperties-syntax.yaml"></a>

```
  [CustomProperties](#cfn-glue-catalog-catalogproperties-customproperties): {{
    {{Key}}: {{Value}}}}
  [DataLakeAccessProperties](#cfn-glue-catalog-catalogproperties-datalakeaccessproperties): {{
    DataLakeAccessProperties}}
```

## Properties
<a name="aws-properties-glue-catalog-catalogproperties-properties"></a>

`CustomProperties`  <a name="cfn-glue-catalog-catalogproperties-customproperties"></a>
Additional key-value properties for the catalog, such as column statistics optimizations.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataLakeAccessProperties`  <a name="cfn-glue-catalog-catalogproperties-datalakeaccessproperties"></a>
A `DataLakeAccessProperties` object that specifies properties to configure data lake access for your catalog resource in the AWS Glue Data Catalog.
*Required*: No
*Type*: [DataLakeAccessProperties](aws-properties-glue-catalog-datalakeaccessproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
