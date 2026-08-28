---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-transformationlambdaconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource TransformationLambdaConfiguration
<a name="aws-properties-bedrock-datasource-transformationlambdaconfiguration"></a>

A Lambda function that processes documents.

## Syntax
<a name="aws-properties-bedrock-datasource-transformationlambdaconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-transformationlambdaconfiguration-syntax.json"></a>

```
{
  "[LambdaArn](#cfn-bedrock-datasource-transformationlambdaconfiguration-lambdaarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-transformationlambdaconfiguration-syntax.yaml"></a>

```
  [LambdaArn](#cfn-bedrock-datasource-transformationlambdaconfiguration-lambdaarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-transformationlambdaconfiguration-properties"></a>

`LambdaArn`  <a name="cfn-bedrock-datasource-transformationlambdaconfiguration-lambdaarn"></a>
The function's ARN identifier.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
