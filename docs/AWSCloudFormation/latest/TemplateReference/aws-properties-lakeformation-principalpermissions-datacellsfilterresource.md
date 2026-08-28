---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::PrincipalPermissions DataCellsFilterResource
<a name="aws-properties-lakeformation-principalpermissions-datacellsfilterresource"></a>

A structure that describes certain columns on certain rows.

## Syntax
<a name="aws-properties-lakeformation-principalpermissions-datacellsfilterresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-principalpermissions-datacellsfilterresource-syntax.json"></a>

```
{
  "[DatabaseName](#cfn-lakeformation-principalpermissions-datacellsfilterresource-databasename)" : {{String}},
  "[Name](#cfn-lakeformation-principalpermissions-datacellsfilterresource-name)" : {{String}},
  "[TableCatalogId](#cfn-lakeformation-principalpermissions-datacellsfilterresource-tablecatalogid)" : {{String}},
  "[TableName](#cfn-lakeformation-principalpermissions-datacellsfilterresource-tablename)" : {{String}}
}
```

### YAML
<a name="aws-properties-lakeformation-principalpermissions-datacellsfilterresource-syntax.yaml"></a>

```
  [DatabaseName](#cfn-lakeformation-principalpermissions-datacellsfilterresource-databasename): {{String}}
  [Name](#cfn-lakeformation-principalpermissions-datacellsfilterresource-name): {{String}}
  [TableCatalogId](#cfn-lakeformation-principalpermissions-datacellsfilterresource-tablecatalogid): {{String}}
  [TableName](#cfn-lakeformation-principalpermissions-datacellsfilterresource-tablename): {{String}}
```

## Properties
<a name="aws-properties-lakeformation-principalpermissions-datacellsfilterresource-properties"></a>

`DatabaseName`  <a name="cfn-lakeformation-principalpermissions-datacellsfilterresource-databasename"></a>
A database in the Data Catalog.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-lakeformation-principalpermissions-datacellsfilterresource-name"></a>
The name given by the user to the data filter cell.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableCatalogId`  <a name="cfn-lakeformation-principalpermissions-datacellsfilterresource-tablecatalogid"></a>
The ID of the catalog to which the table belongs.
*Required*: Yes
*Type*: String
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableName`  <a name="cfn-lakeformation-principalpermissions-datacellsfilterresource-tablename"></a>
The name of the table.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
