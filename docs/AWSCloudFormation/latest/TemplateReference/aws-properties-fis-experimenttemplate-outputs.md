---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fis-experimenttemplate-outputs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::ExperimentTemplate Outputs
<a name="aws-properties-fis-experimenttemplate-outputs"></a>

Describes the output destinations of the experiment report.

## Syntax
<a name="aws-properties-fis-experimenttemplate-outputs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fis-experimenttemplate-outputs-syntax.json"></a>

```
{
  "[ExperimentReportS3Configuration](#cfn-fis-experimenttemplate-outputs-experimentreports3configuration)" : {{ExperimentReportS3Configuration}}
}
```

### YAML
<a name="aws-properties-fis-experimenttemplate-outputs-syntax.yaml"></a>

```
  [ExperimentReportS3Configuration](#cfn-fis-experimenttemplate-outputs-experimentreports3configuration): {{
    ExperimentReportS3Configuration}}
```

## Properties
<a name="aws-properties-fis-experimenttemplate-outputs-properties"></a>

`ExperimentReportS3Configuration`  <a name="cfn-fis-experimenttemplate-outputs-experimentreports3configuration"></a>
The S3 destination for the experiment report.
*Required*: Yes
*Type*: [ExperimentReportS3Configuration](aws-properties-fis-experimenttemplate-experimentreports3configuration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
