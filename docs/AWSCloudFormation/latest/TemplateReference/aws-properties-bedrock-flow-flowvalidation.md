---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-flowvalidation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow FlowValidation
<a name="aws-properties-bedrock-flow-flowvalidation"></a>

Contains information about validation of the flow.

This data type is used in the following API operations:
+  [GetFlow response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetFlow.html#API_agent_GetFlow_ResponseSyntax)
+  [GetFlowVersion response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetFlowVersion.html#API_agent_GetFlowVersion_ResponseSyntax)

## Syntax
<a name="aws-properties-bedrock-flow-flowvalidation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-flowvalidation-syntax.json"></a>

```
{
  "[Message](#cfn-bedrock-flow-flowvalidation-message)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-flowvalidation-syntax.yaml"></a>

```
  [Message](#cfn-bedrock-flow-flowvalidation-message): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-flowvalidation-properties"></a>

`Message`  <a name="cfn-bedrock-flow-flowvalidation-message"></a>
A message describing the validation error.
*Required*: Yes
*Type*: String
*Pattern*: `[\s\S]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
