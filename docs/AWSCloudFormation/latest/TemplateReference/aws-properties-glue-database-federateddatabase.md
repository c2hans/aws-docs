---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-database-federateddatabase.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Database FederatedDatabase
<a name="aws-properties-glue-database-federateddatabase"></a>

A `FederatedDatabase` structure that references an entity outside the AWS Glue Data Catalog.

## Syntax
<a name="aws-properties-glue-database-federateddatabase-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-database-federateddatabase-syntax.json"></a>

```
{
  "[ConnectionName](#cfn-glue-database-federateddatabase-connectionname)" : {{String}},
  "[Identifier](#cfn-glue-database-federateddatabase-identifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-database-federateddatabase-syntax.yaml"></a>

```
  [ConnectionName](#cfn-glue-database-federateddatabase-connectionname): {{String}}
  [Identifier](#cfn-glue-database-federateddatabase-identifier): {{String}}
```

## Properties
<a name="aws-properties-glue-database-federateddatabase-properties"></a>

`ConnectionName`  <a name="cfn-glue-database-federateddatabase-connectionname"></a>
The name of the connection to the external metastore.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Identifier`  <a name="cfn-glue-database-federateddatabase-identifier"></a>
A unique identifier for the federated database.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
