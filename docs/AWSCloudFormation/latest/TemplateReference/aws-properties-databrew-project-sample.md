---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-project-sample.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Project Sample
<a name="aws-properties-databrew-project-sample"></a>

Represents the sample size and sampling type for DataBrew to use for interactive data analysis.

## Syntax
<a name="aws-properties-databrew-project-sample-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-project-sample-syntax.json"></a>

```
{
  "[Size](#cfn-databrew-project-sample-size)" : {{Integer}},
  "[Type](#cfn-databrew-project-sample-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-databrew-project-sample-syntax.yaml"></a>

```
  [Size](#cfn-databrew-project-sample-size): {{Integer}}
  [Type](#cfn-databrew-project-sample-type): {{String}}
```

## Properties
<a name="aws-properties-databrew-project-sample-properties"></a>

`Size`  <a name="cfn-databrew-project-sample-size"></a>
The number of rows in the sample.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-databrew-project-sample-type"></a>
The way in which DataBrew obtains rows from a dataset.
*Required*: Yes
*Type*: String
*Allowed values*: `FIRST_N | LAST_N | RANDOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
