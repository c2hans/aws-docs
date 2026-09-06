---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalytics::Application InputLambdaProcessor
<a name="aws-properties-kinesisanalytics-application-inputlambdaprocessor"></a>

An object that contains the Amazon Resource Name (ARN) of the [AWS Lambda](https://docs.aws.amazon.com/lambda/) function that is used to preprocess records in the stream, and the ARN of the IAM role that is used to access the AWS Lambda function.

## Syntax
<a name="aws-properties-kinesisanalytics-application-inputlambdaprocessor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalytics-application-inputlambdaprocessor-syntax.json"></a>

```
{
  "[ResourceARN](#cfn-kinesisanalytics-application-inputlambdaprocessor-resourcearn)" : {{String}},
  "[RoleARN](#cfn-kinesisanalytics-application-inputlambdaprocessor-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalytics-application-inputlambdaprocessor-syntax.yaml"></a>

```
  [ResourceARN](#cfn-kinesisanalytics-application-inputlambdaprocessor-resourcearn): {{String}}
  [RoleARN](#cfn-kinesisanalytics-application-inputlambdaprocessor-rolearn): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalytics-application-inputlambdaprocessor-properties"></a>

`ResourceARN`  <a name="cfn-kinesisanalytics-application-inputlambdaprocessor-resourcearn"></a>
The ARN of the [AWS Lambda](https://docs.aws.amazon.com/lambda/) function that operates on records in the stream.
To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see [Example ARNs: AWS Lambda](/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda)
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleARN`  <a name="cfn-kinesisanalytics-application-inputlambdaprocessor-rolearn"></a>
The ARN of the IAM role that is used to access the AWS Lambda function.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
