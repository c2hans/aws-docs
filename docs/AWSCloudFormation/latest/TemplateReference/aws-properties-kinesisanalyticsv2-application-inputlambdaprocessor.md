---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application InputLambdaProcessor
<a name="aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor"></a>

An object that contains the Amazon Resource Name (ARN) of the Amazon Lambda function that is used to preprocess records in the stream in a SQL-based Kinesis Data Analytics application.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor-syntax.json"></a>

```
{
  "[ResourceARN](#cfn-kinesisanalyticsv2-application-inputlambdaprocessor-resourcearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor-syntax.yaml"></a>

```
  [ResourceARN](#cfn-kinesisanalyticsv2-application-inputlambdaprocessor-resourcearn): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor-properties"></a>

`ResourceARN`  <a name="cfn-kinesisanalyticsv2-application-inputlambdaprocessor-resourcearn"></a>
The ARN of the Amazon Lambda function that operates on records in the stream.
To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see [Example ARNs: Amazon Lambda](https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda)
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor--seealso"></a>
+ [InputLambdaProcessor](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_InputLambdaProcessor.html) in the *Amazon Kinesis Data Analytics API Reference*
