---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application InputProcessingConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration"></a>

For an SQL-based Amazon Kinesis Data Analytics application, describes a processor that is used to preprocess the records in the stream before being processed by your application code. Currently, the only input processor available is [Amazon Lambda](https://docs.aws.amazon.com/lambda/).

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration-syntax.json"></a>

```
{
  "[InputLambdaProcessor](#cfn-kinesisanalyticsv2-application-inputprocessingconfiguration-inputlambdaprocessor)" : {{InputLambdaProcessor}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration-syntax.yaml"></a>

```
  [InputLambdaProcessor](#cfn-kinesisanalyticsv2-application-inputprocessingconfiguration-inputlambdaprocessor): {{
    InputLambdaProcessor}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration-properties"></a>

`InputLambdaProcessor`  <a name="cfn-kinesisanalyticsv2-application-inputprocessingconfiguration-inputlambdaprocessor"></a>
The [InputLambdaProcessor](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_InputLambdaProcessor.html) that is used to preprocess the records in the stream before being processed by your application code.
*Required*: No
*Type*: [InputLambdaProcessor](aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration--seealso"></a>
+ [InputProcessingConfiguration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_InputProcessingConfiguration.html) in the *Amazon Kinesis Data Analytics API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
