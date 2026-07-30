---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-inlinecodeflownodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion InlineCodeFlowNodeConfiguration
<a name="aws-properties-bedrock-flowversion-inlinecodeflownodeconfiguration"></a>

Contains configurations for an inline code node in your flow. Inline code nodes let you write and execute code directly within your flow, enabling data transformations, custom logic, and integrations without needing an external Lambda function.

## Syntax
<a name="aws-properties-bedrock-flowversion-inlinecodeflownodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-inlinecodeflownodeconfiguration-syntax.json"></a>

```
{
  "[Code](#cfn-bedrock-flowversion-inlinecodeflownodeconfiguration-code)" : {{String}},
  "[Language](#cfn-bedrock-flowversion-inlinecodeflownodeconfiguration-language)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-inlinecodeflownodeconfiguration-syntax.yaml"></a>

```
  [Code](#cfn-bedrock-flowversion-inlinecodeflownodeconfiguration-code): {{String}}
  [Language](#cfn-bedrock-flowversion-inlinecodeflownodeconfiguration-language): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-inlinecodeflownodeconfiguration-properties"></a>

`Code`  <a name="cfn-bedrock-flowversion-inlinecodeflownodeconfiguration-code"></a>
The code that's executed in your inline code node. The code can access input data from previous nodes in the flow, perform operations on that data, and produce output that can be used by other nodes in your flow.
The code must be valid in the programming `language` that you specify.
*Required*: Yes
*Type*: String
*Maximum*: `5000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Language`  <a name="cfn-bedrock-flowversion-inlinecodeflownodeconfiguration-language"></a>
The programming language used by your inline code node.
The code must be valid in the programming `language` that you specify. Currently, only Python 3 (`Python_3`) is supported.
*Required*: Yes
*Type*: String
*Allowed values*: `Python_3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
