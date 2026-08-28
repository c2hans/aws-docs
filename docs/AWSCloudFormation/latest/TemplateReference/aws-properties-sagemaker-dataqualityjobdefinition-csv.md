---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-dataqualityjobdefinition-csv.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::DataQualityJobDefinition Csv
<a name="aws-properties-sagemaker-dataqualityjobdefinition-csv"></a>

The CSV dataset format configuration.

## Syntax
<a name="aws-properties-sagemaker-dataqualityjobdefinition-csv-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-dataqualityjobdefinition-csv-syntax.json"></a>

```
{
  "[Header](#cfn-sagemaker-dataqualityjobdefinition-csv-header)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-sagemaker-dataqualityjobdefinition-csv-syntax.yaml"></a>

```
  [Header](#cfn-sagemaker-dataqualityjobdefinition-csv-header): {{Boolean}}
```

## Properties
<a name="aws-properties-sagemaker-dataqualityjobdefinition-csv-properties"></a>

`Header`  <a name="cfn-sagemaker-dataqualityjobdefinition-csv-header"></a>
Indicates whether the CSV data has a header row.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
