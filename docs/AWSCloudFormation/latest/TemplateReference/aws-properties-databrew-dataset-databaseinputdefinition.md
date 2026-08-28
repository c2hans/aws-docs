---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-dataset-databaseinputdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Dataset DatabaseInputDefinition
<a name="aws-properties-databrew-dataset-databaseinputdefinition"></a>

Connection information for dataset input files stored in a database.

## Syntax
<a name="aws-properties-databrew-dataset-databaseinputdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-dataset-databaseinputdefinition-syntax.json"></a>

```
{
  "[DatabaseTableName](#cfn-databrew-dataset-databaseinputdefinition-databasetablename)" : {{String}},
  "[GlueConnectionName](#cfn-databrew-dataset-databaseinputdefinition-glueconnectionname)" : {{String}},
  "[QueryString](#cfn-databrew-dataset-databaseinputdefinition-querystring)" : {{String}},
  "[TempDirectory](#cfn-databrew-dataset-databaseinputdefinition-tempdirectory)" : {{S3Location}}
}
```

### YAML
<a name="aws-properties-databrew-dataset-databaseinputdefinition-syntax.yaml"></a>

```
  [DatabaseTableName](#cfn-databrew-dataset-databaseinputdefinition-databasetablename): {{String}}
  [GlueConnectionName](#cfn-databrew-dataset-databaseinputdefinition-glueconnectionname): {{String}}
  [QueryString](#cfn-databrew-dataset-databaseinputdefinition-querystring): {{
    String}}
  [TempDirectory](#cfn-databrew-dataset-databaseinputdefinition-tempdirectory): {{
    S3Location}}
```

## Properties
<a name="aws-properties-databrew-dataset-databaseinputdefinition-properties"></a>

`DatabaseTableName`  <a name="cfn-databrew-dataset-databaseinputdefinition-databasetablename"></a>
The table within the target database.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlueConnectionName`  <a name="cfn-databrew-dataset-databaseinputdefinition-glueconnectionname"></a>
The AWS Glue Connection that stores the connection information for the target database.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryString`  <a name="cfn-databrew-dataset-databaseinputdefinition-querystring"></a>
Custom SQL to run against the provided AWS Glue connection. This SQL will be used as the input for DataBrew projects and jobs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TempDirectory`  <a name="cfn-databrew-dataset-databaseinputdefinition-tempdirectory"></a>
An Amazon location that AWS Glue Data Catalog can use as a temporary directory.
*Required*: No
*Type*: [S3Location](aws-properties-databrew-dataset-s3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
