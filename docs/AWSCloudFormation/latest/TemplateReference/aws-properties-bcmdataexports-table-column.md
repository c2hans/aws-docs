---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bcmdataexports-table-column.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BCMDataExports::Table Column
<a name="aws-properties-bcmdataexports-table-column"></a>

Includes basic information for a data column such as its description, name, and type.

## Syntax
<a name="aws-properties-bcmdataexports-table-column-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bcmdataexports-table-column-syntax.json"></a>

```
{
  "[Description](#cfn-bcmdataexports-table-column-description)" : {{String}},
  "[Name](#cfn-bcmdataexports-table-column-name)" : {{String}},
  "[Type](#cfn-bcmdataexports-table-column-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bcmdataexports-table-column-syntax.yaml"></a>

```
  [Description](#cfn-bcmdataexports-table-column-description): {{String}}
  [Name](#cfn-bcmdataexports-table-column-name): {{String}}
  [Type](#cfn-bcmdataexports-table-column-type): {{String}}
```

## Properties
<a name="aws-properties-bcmdataexports-table-column-properties"></a>

`Description`  <a name="cfn-bcmdataexports-table-column-description"></a>
The description for a column.
*Required*: No
*Type*: String
*Pattern*: `^[\S\s]*$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bcmdataexports-table-column-name"></a>
The column name.
*Required*: No
*Type*: String
*Pattern*: `^[\S\s]*$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bcmdataexports-table-column-type"></a>
The kind of data a column stores.
*Required*: No
*Type*: String
*Pattern*: `^[\S\s]*$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
