---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-partition-schemareference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Partition SchemaReference
<a name="aws-properties-glue-partition-schemareference"></a>

An object that references a schema stored in the AWS Glue Schema Registry.

## Syntax
<a name="aws-properties-glue-partition-schemareference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-partition-schemareference-syntax.json"></a>

```
{
  "[SchemaId](#cfn-glue-partition-schemareference-schemaid)" : {{SchemaId}},
  "[SchemaVersionId](#cfn-glue-partition-schemareference-schemaversionid)" : {{String}},
  "[SchemaVersionNumber](#cfn-glue-partition-schemareference-schemaversionnumber)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-glue-partition-schemareference-syntax.yaml"></a>

```
  [SchemaId](#cfn-glue-partition-schemareference-schemaid): {{
    SchemaId}}
  [SchemaVersionId](#cfn-glue-partition-schemareference-schemaversionid): {{String}}
  [SchemaVersionNumber](#cfn-glue-partition-schemareference-schemaversionnumber): {{Integer}}
```

## Properties
<a name="aws-properties-glue-partition-schemareference-properties"></a>

`SchemaId`  <a name="cfn-glue-partition-schemareference-schemaid"></a>
A structure that contains schema identity fields. Either this or the `SchemaVersionId` has to be provided.
*Required*: No
*Type*: [SchemaId](aws-properties-glue-partition-schemaid.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaVersionId`  <a name="cfn-glue-partition-schemareference-schemaversionid"></a>
The unique ID assigned to a version of the schema. Either this or the `SchemaId` has to be provided.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaVersionNumber`  <a name="cfn-glue-partition-schemareference-schemaversionnumber"></a>
The version number of the schema.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
