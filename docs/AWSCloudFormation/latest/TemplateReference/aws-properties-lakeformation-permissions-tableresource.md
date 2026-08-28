---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-permissions-tableresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::Permissions TableResource
<a name="aws-properties-lakeformation-permissions-tableresource"></a>

A structure for the table object. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

## Syntax
<a name="aws-properties-lakeformation-permissions-tableresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-permissions-tableresource-syntax.json"></a>

```
{
  "[CatalogId](#cfn-lakeformation-permissions-tableresource-catalogid)" : {{String}},
  "[DatabaseName](#cfn-lakeformation-permissions-tableresource-databasename)" : {{String}},
  "[Name](#cfn-lakeformation-permissions-tableresource-name)" : {{String}},
  "[TableWildcard](#cfn-lakeformation-permissions-tableresource-tablewildcard)" : {{Json}}
}
```

### YAML
<a name="aws-properties-lakeformation-permissions-tableresource-syntax.yaml"></a>

```
  [CatalogId](#cfn-lakeformation-permissions-tableresource-catalogid): {{String}}
  [DatabaseName](#cfn-lakeformation-permissions-tableresource-databasename): {{String}}
  [Name](#cfn-lakeformation-permissions-tableresource-name): {{String}}
  [TableWildcard](#cfn-lakeformation-permissions-tableresource-tablewildcard): {{Json}}
```

## Properties
<a name="aws-properties-lakeformation-permissions-tableresource-properties"></a>

`CatalogId`  <a name="cfn-lakeformation-permissions-tableresource-catalogid"></a>
The identifier for the Data Catalog. By default, it is the account ID of the caller.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseName`  <a name="cfn-lakeformation-permissions-tableresource-databasename"></a>
The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-lakeformation-permissions-tableresource-name"></a>
The name of the table.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableWildcard`  <a name="cfn-lakeformation-permissions-tableresource-tablewildcard"></a>
An empty object representing all tables under a database. If this field is specified instead of the `Name` field, all tables under `DatabaseName` will have permission changes applied.
*Required*: No
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
