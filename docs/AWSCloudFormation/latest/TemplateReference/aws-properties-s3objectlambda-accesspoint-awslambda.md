---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3objectlambda-accesspoint-awslambda.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3ObjectLambda::AccessPoint AwsLambda
<a name="aws-properties-s3objectlambda-accesspoint-awslambda"></a>

<a name="aws-properties-s3objectlambda-accesspoint-awslambda-description"></a>The `AwsLambda` property type specifies Property description not available. for an [AWS::S3ObjectLambda::AccessPoint](aws-resource-s3objectlambda-accesspoint.md).

## Syntax
<a name="aws-properties-s3objectlambda-accesspoint-awslambda-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3objectlambda-accesspoint-awslambda-syntax.json"></a>

```
{
  "[FunctionArn](#cfn-s3objectlambda-accesspoint-awslambda-functionarn)" : {{String}},
  "[FunctionPayload](#cfn-s3objectlambda-accesspoint-awslambda-functionpayload)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3objectlambda-accesspoint-awslambda-syntax.yaml"></a>

```
  [FunctionArn](#cfn-s3objectlambda-accesspoint-awslambda-functionarn): {{String}}
  [FunctionPayload](#cfn-s3objectlambda-accesspoint-awslambda-functionpayload): {{String}}
```

## Properties
<a name="aws-properties-s3objectlambda-accesspoint-awslambda-properties"></a>

`FunctionArn`  <a name="cfn-s3objectlambda-accesspoint-awslambda-functionarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionPayload`  <a name="cfn-s3objectlambda-accesspoint-awslambda-functionpayload"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
