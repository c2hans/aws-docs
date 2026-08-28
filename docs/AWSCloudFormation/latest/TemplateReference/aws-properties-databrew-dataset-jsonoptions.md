---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-dataset-jsonoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Dataset JsonOptions
<a name="aws-properties-databrew-dataset-jsonoptions"></a>

Represents the JSON-specific options that define how input is to be interpreted by AWS Glue DataBrew.

## Syntax
<a name="aws-properties-databrew-dataset-jsonoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-dataset-jsonoptions-syntax.json"></a>

```
{
  "[MultiLine](#cfn-databrew-dataset-jsonoptions-multiline)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-databrew-dataset-jsonoptions-syntax.yaml"></a>

```
  [MultiLine](#cfn-databrew-dataset-jsonoptions-multiline): {{Boolean}}
```

## Properties
<a name="aws-properties-databrew-dataset-jsonoptions-properties"></a>

`MultiLine`  <a name="cfn-databrew-dataset-jsonoptions-multiline"></a>
A value that specifies whether JSON input contains embedded new line characters.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
