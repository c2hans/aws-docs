---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-database-databaseidentifier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Database DatabaseIdentifier
<a name="aws-properties-glue-database-databaseidentifier"></a>

A structure that describes a target database for resource linking.

## Syntax
<a name="aws-properties-glue-database-databaseidentifier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-database-databaseidentifier-syntax.json"></a>

```
{
  "[CatalogId](#cfn-glue-database-databaseidentifier-catalogid)" : {{String}},
  "[DatabaseName](#cfn-glue-database-databaseidentifier-databasename)" : {{String}},
  "[Region](#cfn-glue-database-databaseidentifier-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-database-databaseidentifier-syntax.yaml"></a>

```
  [CatalogId](#cfn-glue-database-databaseidentifier-catalogid): {{String}}
  [DatabaseName](#cfn-glue-database-databaseidentifier-databasename): {{String}}
  [Region](#cfn-glue-database-databaseidentifier-region): {{String}}
```

## Properties
<a name="aws-properties-glue-database-databaseidentifier-properties"></a>

`CatalogId`  <a name="cfn-glue-database-databaseidentifier-catalogid"></a>
The ID of the Data Catalog in which the database resides.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-glue-database-databaseidentifier-databasename"></a>
The name of the catalog database.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-glue-database-databaseidentifier-region"></a>
The Region of the database.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
