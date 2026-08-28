---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-tagassociation-tableresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::TagAssociation TableResource
<a name="aws-properties-lakeformation-tagassociation-tableresource"></a>

A structure for the table object. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

## Syntax
<a name="aws-properties-lakeformation-tagassociation-tableresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-tagassociation-tableresource-syntax.json"></a>

```
{
  "[CatalogId](#cfn-lakeformation-tagassociation-tableresource-catalogid)" : {{String}},
  "[DatabaseName](#cfn-lakeformation-tagassociation-tableresource-databasename)" : {{String}},
  "[Name](#cfn-lakeformation-tagassociation-tableresource-name)" : {{String}},
  "[TableWildcard](#cfn-lakeformation-tagassociation-tableresource-tablewildcard)" : {{Json}}
}
```

### YAML
<a name="aws-properties-lakeformation-tagassociation-tableresource-syntax.yaml"></a>

```
  [CatalogId](#cfn-lakeformation-tagassociation-tableresource-catalogid): {{String}}
  [DatabaseName](#cfn-lakeformation-tagassociation-tableresource-databasename): {{String}}
  [Name](#cfn-lakeformation-tagassociation-tableresource-name): {{String}}
  [TableWildcard](#cfn-lakeformation-tagassociation-tableresource-tablewildcard): {{Json}}
```

## Properties
<a name="aws-properties-lakeformation-tagassociation-tableresource-properties"></a>

`CatalogId`  <a name="cfn-lakeformation-tagassociation-tableresource-catalogid"></a>
The identifier for the Data Catalog. By default, it is the account ID of the caller.
*Required*: Yes
*Type*: String
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseName`  <a name="cfn-lakeformation-tagassociation-tableresource-databasename"></a>
The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-lakeformation-tagassociation-tableresource-name"></a>
The name of the table.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableWildcard`  <a name="cfn-lakeformation-tagassociation-tableresource-tablewildcard"></a>
A wildcard object representing every table under a database.This is an object with no properties that effectively behaves as a true or false depending on whether not it is passed as a parameter. The valid inputs for a property with this type in either yaml or json is null or {}.
At least one of `TableResource$Name` or `TableResource$TableWildcard` is required.
*Required*: No
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
