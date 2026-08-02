---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::PrincipalPermissions TableWithColumnsResource
<a name="aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource"></a>

A structure for a table with columns object. This object is only used when granting a SELECT permission.

This object must take a value for at least one of `ColumnsNames`, `ColumnsIndexes`, or `ColumnsWildcard`.

## Syntax
<a name="aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource-syntax.json"></a>

```
{
  "[CatalogId](#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-catalogid)" : {{String}},
  "[ColumnNames](#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-columnnames)" : {{[ String, ... ]}},
  "[ColumnWildcard](#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-columnwildcard)" : {{ColumnWildcard}},
  "[DatabaseName](#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-databasename)" : {{String}},
  "[Name](#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource-syntax.yaml"></a>

```
  [CatalogId](#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-catalogid): {{String}}
  [ColumnNames](#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-columnnames): {{
    - String}}
  [ColumnWildcard](#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-columnwildcard): {{
    ColumnWildcard}}
  [DatabaseName](#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-databasename): {{String}}
  [Name](#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-name): {{String}}
```

## Properties
<a name="aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource-properties"></a>

`CatalogId`  <a name="cfn-lakeformation-principalpermissions-tablewithcolumnsresource-catalogid"></a>
The identifier for the Data Catalog where the location is registered with AWS Lake Formation.
*Required*: Yes
*Type*: String
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ColumnNames`  <a name="cfn-lakeformation-principalpermissions-tablewithcolumnsresource-columnnames"></a>
The list of column names for the table. At least one of `ColumnNames` or `ColumnWildcard` is required.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ColumnWildcard`  <a name="cfn-lakeformation-principalpermissions-tablewithcolumnsresource-columnwildcard"></a>
A wildcard specified by a `ColumnWildcard` object. At least one of `ColumnNames` or `ColumnWildcard` is required.
*Required*: No
*Type*: [ColumnWildcard](aws-properties-lakeformation-principalpermissions-columnwildcard.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseName`  <a name="cfn-lakeformation-principalpermissions-tablewithcolumnsresource-databasename"></a>
The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-lakeformation-principalpermissions-tablewithcolumnsresource-name"></a>
The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
