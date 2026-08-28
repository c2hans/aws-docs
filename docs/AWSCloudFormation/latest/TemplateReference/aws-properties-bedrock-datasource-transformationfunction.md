---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-transformationfunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource TransformationFunction
<a name="aws-properties-bedrock-datasource-transformationfunction"></a>

A Lambda function that processes documents.

## Syntax
<a name="aws-properties-bedrock-datasource-transformationfunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-transformationfunction-syntax.json"></a>

```
{
  "[TransformationLambdaConfiguration](#cfn-bedrock-datasource-transformationfunction-transformationlambdaconfiguration)" : {{TransformationLambdaConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-transformationfunction-syntax.yaml"></a>

```
  [TransformationLambdaConfiguration](#cfn-bedrock-datasource-transformationfunction-transformationlambdaconfiguration): {{
    TransformationLambdaConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-datasource-transformationfunction-properties"></a>

`TransformationLambdaConfiguration`  <a name="cfn-bedrock-datasource-transformationfunction-transformationlambdaconfiguration"></a>
The Lambda function.
*Required*: Yes
*Type*: [TransformationLambdaConfiguration](aws-properties-bedrock-datasource-transformationlambdaconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
