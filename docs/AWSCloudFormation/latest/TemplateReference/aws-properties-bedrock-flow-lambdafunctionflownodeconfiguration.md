---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-lambdafunctionflownodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow LambdaFunctionFlowNodeConfiguration
<a name="aws-properties-bedrock-flow-lambdafunctionflownodeconfiguration"></a>

Contains configurations for a Lambda function node in the flow. You specify the Lambda function to invoke and the inputs into the function. The output is the response that is defined in the Lambda function. For more information, see [Node types in a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-flow-lambdafunctionflownodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-lambdafunctionflownodeconfiguration-syntax.json"></a>

```
{
  "[LambdaArn](#cfn-bedrock-flow-lambdafunctionflownodeconfiguration-lambdaarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-lambdafunctionflownodeconfiguration-syntax.yaml"></a>

```
  [LambdaArn](#cfn-bedrock-flow-lambdafunctionflownodeconfiguration-lambdaarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-lambdafunctionflownodeconfiguration-properties"></a>

`LambdaArn`  <a name="cfn-bedrock-flow-lambdafunctionflownodeconfiguration-lambdaarn"></a>
The Amazon Resource Name (ARN) of the Lambda function to invoke.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
