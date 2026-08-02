---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bcmdataexports-export.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BCMDataExports::Export
<a name="aws-resource-bcmdataexports-export"></a>

Creates a data export and specifies the data query, the delivery preference, and any optional resource tags.

A `DataQuery` consists of both a `QueryStatement` and `TableConfigurations`.

The `QueryStatement` is an SQL statement. Data Exports only supports a limited subset of the SQL syntax. For more information on the SQL syntax that is supported, see [Data query](https://docs.aws.amazon.com/cur/latest/userguide/de-data-query.html). To view the available tables and columns, see the [Data Exports table dictionary](https://docs.aws.amazon.com/cur/latest/userguide/de-table-dictionary.html).

The `TableConfigurations` is a collection of specified `TableProperties` for the table being queried in the `QueryStatement`. TableProperties are additional configurations you can provide to change the data and schema of a table. Each table can have different TableProperties. However, tables are not required to have any TableProperties. Each table property has a default value that it assumes if not specified. For more information on table configurations, see [Data query](https://docs.aws.amazon.com/cur/latest/userguide/de-data-query.html). To view the table properties available for each table, see the [Data Exports table dictionary](https://docs.aws.amazon.com/cur/latest/userguide/de-table-dictionary.html) or use the `ListTables` API to get a response of all tables and their available properties.

## Syntax
<a name="aws-resource-bcmdataexports-export-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bcmdataexports-export-syntax.json"></a>

```
{
  "Type" : "AWS::BCMDataExports::Export",
  "Properties" : {
      "[Export](#cfn-bcmdataexports-export-export)" : {{Export}},
      "[Tags](#cfn-bcmdataexports-export-tags)" : {{[ ResourceTag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bcmdataexports-export-syntax.yaml"></a>

```
Type: AWS::BCMDataExports::Export
Properties:
  [Export](#cfn-bcmdataexports-export-export): {{
    Export}}
  [Tags](#cfn-bcmdataexports-export-tags): {{
    - ResourceTag}}
```

## Properties
<a name="aws-resource-bcmdataexports-export-properties"></a>

`Export`  <a name="cfn-bcmdataexports-export-export"></a>
The details that are available for an export.
*Required*: Yes
*Type*: [Export](aws-properties-bcmdataexports-export-export.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bcmdataexports-export-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [ResourceTag](aws-properties-bcmdataexports-export-resourcetag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bcmdataexports-export-return-values"></a>

### Ref
<a name="aws-resource-bcmdataexports-export-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bcmdataexports-export-return-values-fn--getatt"></a>

####
<a name="aws-resource-bcmdataexports-export-return-values-fn--getatt-fn--getatt"></a>

`Export.ExportArn`  <a name="Export.ExportArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for this export.

`ExportArn`  <a name="ExportArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for this export.
