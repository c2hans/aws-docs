---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-job-outputformatoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Job OutputFormatOptions
<a name="aws-properties-databrew-job-outputformatoptions"></a>

Represents a set of options that define the structure of comma-separated (CSV) job output.

## Syntax
<a name="aws-properties-databrew-job-outputformatoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-job-outputformatoptions-syntax.json"></a>

```
{
  "[Csv](#cfn-databrew-job-outputformatoptions-csv)" : {{CsvOutputOptions}}
}
```

### YAML
<a name="aws-properties-databrew-job-outputformatoptions-syntax.yaml"></a>

```
  [Csv](#cfn-databrew-job-outputformatoptions-csv): {{
    CsvOutputOptions}}
```

## Properties
<a name="aws-properties-databrew-job-outputformatoptions-properties"></a>

`Csv`  <a name="cfn-databrew-job-outputformatoptions-csv"></a>
Represents a set of options that define the structure of comma-separated value (CSV) job output.
*Required*: No
*Type*: [CsvOutputOptions](aws-properties-databrew-job-csvoutputoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
