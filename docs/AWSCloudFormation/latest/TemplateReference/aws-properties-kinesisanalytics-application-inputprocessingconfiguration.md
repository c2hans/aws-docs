---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalytics::Application InputProcessingConfiguration
<a name="aws-properties-kinesisanalytics-application-inputprocessingconfiguration"></a>

Provides a description of a processor that is used to preprocess the records in the stream before being processed by your application code. Currently, the only input processor available is [AWS Lambda](https://docs.aws.amazon.com/lambda/).

## Syntax
<a name="aws-properties-kinesisanalytics-application-inputprocessingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalytics-application-inputprocessingconfiguration-syntax.json"></a>

```
{
  "[InputLambdaProcessor](#cfn-kinesisanalytics-application-inputprocessingconfiguration-inputlambdaprocessor)" : {{InputLambdaProcessor}}
}
```

### YAML
<a name="aws-properties-kinesisanalytics-application-inputprocessingconfiguration-syntax.yaml"></a>

```
  [InputLambdaProcessor](#cfn-kinesisanalytics-application-inputprocessingconfiguration-inputlambdaprocessor): {{
    InputLambdaProcessor}}
```

## Properties
<a name="aws-properties-kinesisanalytics-application-inputprocessingconfiguration-properties"></a>

`InputLambdaProcessor`  <a name="cfn-kinesisanalytics-application-inputprocessingconfiguration-inputlambdaprocessor"></a>
The [InputLambdaProcessor](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html) that is used to preprocess the records in the stream before being processed by your application code.
*Required*: No
*Type*: [InputLambdaProcessor](aws-properties-kinesisanalytics-application-inputlambdaprocessor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
