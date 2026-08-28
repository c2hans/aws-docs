---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-trainingdataset-gluedatasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::TrainingDataset GlueDataSource
<a name="aws-properties-cleanroomsml-trainingdataset-gluedatasource"></a>

Defines the Glue data source that contains the training data.

## Syntax
<a name="aws-properties-cleanroomsml-trainingdataset-gluedatasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-trainingdataset-gluedatasource-syntax.json"></a>

```
{
  "[CatalogId](#cfn-cleanroomsml-trainingdataset-gluedatasource-catalogid)" : {{String}},
  "[DatabaseName](#cfn-cleanroomsml-trainingdataset-gluedatasource-databasename)" : {{String}},
  "[TableName](#cfn-cleanroomsml-trainingdataset-gluedatasource-tablename)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-trainingdataset-gluedatasource-syntax.yaml"></a>

```
  [CatalogId](#cfn-cleanroomsml-trainingdataset-gluedatasource-catalogid): {{String}}
  [DatabaseName](#cfn-cleanroomsml-trainingdataset-gluedatasource-databasename): {{String}}
  [TableName](#cfn-cleanroomsml-trainingdataset-gluedatasource-tablename): {{String}}
```

## Properties
<a name="aws-properties-cleanroomsml-trainingdataset-gluedatasource-properties"></a>

`CatalogId`  <a name="cfn-cleanroomsml-trainingdataset-gluedatasource-catalogid"></a>
The Glue catalog that contains the training data.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseName`  <a name="cfn-cleanroomsml-trainingdataset-gluedatasource-databasename"></a>
The Glue database that contains the training data.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_](([a-zA-Z0-9_]+-)*([a-zA-Z0-9_]+))?$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableName`  <a name="cfn-cleanroomsml-trainingdataset-gluedatasource-tablename"></a>
The Glue table that contains the training data.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
