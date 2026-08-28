---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lakeformation-tagassociation-databaseresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LakeFormation::TagAssociation DatabaseResource
<a name="aws-properties-lakeformation-tagassociation-databaseresource"></a>

A structure for the database object.

## Syntax
<a name="aws-properties-lakeformation-tagassociation-databaseresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lakeformation-tagassociation-databaseresource-syntax.json"></a>

```
{
  "[CatalogId](#cfn-lakeformation-tagassociation-databaseresource-catalogid)" : {{String}},
  "[Name](#cfn-lakeformation-tagassociation-databaseresource-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-lakeformation-tagassociation-databaseresource-syntax.yaml"></a>

```
  [CatalogId](#cfn-lakeformation-tagassociation-databaseresource-catalogid): {{String}}
  [Name](#cfn-lakeformation-tagassociation-databaseresource-name): {{String}}
```

## Properties
<a name="aws-properties-lakeformation-tagassociation-databaseresource-properties"></a>

`CatalogId`  <a name="cfn-lakeformation-tagassociation-databaseresource-catalogid"></a>
The identifier for the Data Catalog. By default, it should be the account ID of the caller.
*Required*: Yes
*Type*: String
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-lakeformation-tagassociation-databaseresource-name"></a>
The name of the database resource. Unique to the Data Catalog.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
