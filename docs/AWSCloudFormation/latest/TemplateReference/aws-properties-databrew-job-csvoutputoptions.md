---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-job-csvoutputoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Job CsvOutputOptions
<a name="aws-properties-databrew-job-csvoutputoptions"></a>

Represents a set of options that define how DataBrew will write a comma-separated value (CSV) file.

## Syntax
<a name="aws-properties-databrew-job-csvoutputoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-job-csvoutputoptions-syntax.json"></a>

```
{
  "[Delimiter](#cfn-databrew-job-csvoutputoptions-delimiter)" : {{String}}
}
```

### YAML
<a name="aws-properties-databrew-job-csvoutputoptions-syntax.yaml"></a>

```
  [Delimiter](#cfn-databrew-job-csvoutputoptions-delimiter): {{String}}
```

## Properties
<a name="aws-properties-databrew-job-csvoutputoptions-properties"></a>

`Delimiter`  <a name="cfn-databrew-job-csvoutputoptions-delimiter"></a>
A single character that specifies the delimiter used to create CSV job output.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
