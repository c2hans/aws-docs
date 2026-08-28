---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::DataQualityJobDefinition StatisticsResource
<a name="aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource"></a>

The statistics resource for a monitoring job.

## Syntax
<a name="aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource-syntax.json"></a>

```
{
  "[S3Uri](#cfn-sagemaker-dataqualityjobdefinition-statisticsresource-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource-syntax.yaml"></a>

```
  [S3Uri](#cfn-sagemaker-dataqualityjobdefinition-statisticsresource-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource-properties"></a>

`S3Uri`  <a name="cfn-sagemaker-dataqualityjobdefinition-statisticsresource-s3uri"></a>
The Amazon S3 URI for the statistics resource.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
