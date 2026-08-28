---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-job-allowedstatistics.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Job AllowedStatistics
<a name="aws-properties-databrew-job-allowedstatistics"></a>

Configuration of statistics that are allowed to be run on columns that contain detected entities. When undefined, no statistics will be computed on columns that contain detected entities.

## Syntax
<a name="aws-properties-databrew-job-allowedstatistics-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-job-allowedstatistics-syntax.json"></a>

```
{
  "[Statistics](#cfn-databrew-job-allowedstatistics-statistics)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-databrew-job-allowedstatistics-syntax.yaml"></a>

```
  [Statistics](#cfn-databrew-job-allowedstatistics-statistics): {{
    - String}}
```

## Properties
<a name="aws-properties-databrew-job-allowedstatistics-properties"></a>

`Statistics`  <a name="cfn-databrew-job-allowedstatistics-statistics"></a>
One or more column statistics to allow for columns that contain detected entities.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
