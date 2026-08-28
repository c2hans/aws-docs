---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-recipe-secondaryinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Recipe SecondaryInput
<a name="aws-properties-databrew-recipe-secondaryinput"></a>

Represents secondary inputs in a UNION transform.

## Syntax
<a name="aws-properties-databrew-recipe-secondaryinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-recipe-secondaryinput-syntax.json"></a>

```
{
  "[DataCatalogInputDefinition](#cfn-databrew-recipe-secondaryinput-datacataloginputdefinition)" : {{DataCatalogInputDefinition}},
  "[S3InputDefinition](#cfn-databrew-recipe-secondaryinput-s3inputdefinition)" : {{S3Location}}
}
```

### YAML
<a name="aws-properties-databrew-recipe-secondaryinput-syntax.yaml"></a>

```
  [DataCatalogInputDefinition](#cfn-databrew-recipe-secondaryinput-datacataloginputdefinition): {{
    DataCatalogInputDefinition}}
  [S3InputDefinition](#cfn-databrew-recipe-secondaryinput-s3inputdefinition): {{
    S3Location}}
```

## Properties
<a name="aws-properties-databrew-recipe-secondaryinput-properties"></a>

`DataCatalogInputDefinition`  <a name="cfn-databrew-recipe-secondaryinput-datacataloginputdefinition"></a>
The AWS Glue Data Catalog parameters for the data.
*Required*: No
*Type*: [DataCatalogInputDefinition](aws-properties-databrew-recipe-datacataloginputdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3InputDefinition`  <a name="cfn-databrew-recipe-secondaryinput-s3inputdefinition"></a>
The Amazon S3 location where the data is stored.
*Required*: No
*Type*: [S3Location](aws-properties-databrew-recipe-s3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
