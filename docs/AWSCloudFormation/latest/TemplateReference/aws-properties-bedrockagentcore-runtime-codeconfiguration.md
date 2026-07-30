---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-codeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime CodeConfiguration
<a name="aws-properties-bedrockagentcore-runtime-codeconfiguration"></a>

The configuration for the source code that defines how the agent runtime code should be executed, including the code location, runtime environment, and entry point.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-codeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-codeconfiguration-syntax.json"></a>

```
{
  "[Code](#cfn-bedrockagentcore-runtime-codeconfiguration-code)" : {{Code}},
  "[EntryPoint](#cfn-bedrockagentcore-runtime-codeconfiguration-entrypoint)" : {{[ String, ... ]}},
  "[Runtime](#cfn-bedrockagentcore-runtime-codeconfiguration-runtime)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-codeconfiguration-syntax.yaml"></a>

```
  [Code](#cfn-bedrockagentcore-runtime-codeconfiguration-code): {{
    Code}}
  [EntryPoint](#cfn-bedrockagentcore-runtime-codeconfiguration-entrypoint): {{
    - String}}
  [Runtime](#cfn-bedrockagentcore-runtime-codeconfiguration-runtime): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-codeconfiguration-properties"></a>

`Code`  <a name="cfn-bedrockagentcore-runtime-codeconfiguration-code"></a>
The source code location and configuration details.
*Required*: Yes
*Type*: [Code](aws-properties-bedrockagentcore-runtime-code.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EntryPoint`  <a name="cfn-bedrockagentcore-runtime-codeconfiguration-entrypoint"></a>
The entry point for the code execution, specifying the function or method that should be invoked when the code runs.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Runtime`  <a name="cfn-bedrockagentcore-runtime-codeconfiguration-runtime"></a>
The runtime environment for executing the agent code. Specify the programming language and version to use for the agent runtime. For valid values, see the list of supported runtimes.
*Required*: Yes
*Type*: String
*Allowed values*: `PYTHON_3_10 | PYTHON_3_11 | PYTHON_3_12 | PYTHON_3_13 | PYTHON_3_14 | NODE_22`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
