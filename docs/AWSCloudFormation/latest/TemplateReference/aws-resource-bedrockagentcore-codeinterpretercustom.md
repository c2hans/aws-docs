---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-codeinterpretercustom.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CodeInterpreterCustom
<a name="aws-resource-bedrockagentcore-codeinterpretercustom"></a>

The AgentCore Code Interpreter tool enables agents to securely execute code in isolated sandbox environments. It offers advanced configuration support and seamless integration with popular frameworks.

For more information about using the custom code interpreter, see [Execute code and analyze data using Amazon Bedrock AgentCore Code Interpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-codeinterpretercustom-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-codeinterpretercustom-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::CodeInterpreterCustom",
  "Properties" : {
      "[Certificates](#cfn-bedrockagentcore-codeinterpretercustom-certificates)" : {{[ Certificate, ... ]}},
      "[Description](#cfn-bedrockagentcore-codeinterpretercustom-description)" : {{String}},
      "[ExecutionRoleArn](#cfn-bedrockagentcore-codeinterpretercustom-executionrolearn)" : {{String}},
      "[Name](#cfn-bedrockagentcore-codeinterpretercustom-name)" : {{String}},
      "[NetworkConfiguration](#cfn-bedrockagentcore-codeinterpretercustom-networkconfiguration)" : {{CodeInterpreterNetworkConfiguration}},
      "[Tags](#cfn-bedrockagentcore-codeinterpretercustom-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-codeinterpretercustom-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::CodeInterpreterCustom
Properties:
  [Certificates](#cfn-bedrockagentcore-codeinterpretercustom-certificates): {{
    - Certificate}}
  [Description](#cfn-bedrockagentcore-codeinterpretercustom-description): {{String}}
  [ExecutionRoleArn](#cfn-bedrockagentcore-codeinterpretercustom-executionrolearn): {{String}}
  [Name](#cfn-bedrockagentcore-codeinterpretercustom-name): {{String}}
  [NetworkConfiguration](#cfn-bedrockagentcore-codeinterpretercustom-networkconfiguration): {{
    CodeInterpreterNetworkConfiguration}}
  [Tags](#cfn-bedrockagentcore-codeinterpretercustom-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-bedrockagentcore-codeinterpretercustom-properties"></a>

`Certificates`  <a name="cfn-bedrockagentcore-codeinterpretercustom-certificates"></a>
A list of certificates to install in the code interpreter.
*Required*: No
*Type*: Array of [Certificate](aws-properties-bedrockagentcore-codeinterpretercustom-certificate.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-bedrockagentcore-codeinterpretercustom-description"></a>
The description of the code interpreter.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExecutionRoleArn`  <a name="cfn-bedrockagentcore-codeinterpretercustom-executionrolearn"></a>
The IAM role ARN that provides permissions for the code interpreter.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws(?:-cn|-us-gov|-iso(?:-[bef])?)?):iam::[0-9]{12}:role/.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-bedrockagentcore-codeinterpretercustom-name"></a>
The name of the code interpreter.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkConfiguration`  <a name="cfn-bedrockagentcore-codeinterpretercustom-networkconfiguration"></a>
The network configuration for a code interpreter. This structure defines how the code interpreter connects to the network.
*Required*: Yes
*Type*: [CodeInterpreterNetworkConfiguration](aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrockagentcore-codeinterpretercustom-tags"></a>
A map of tag keys and values to assign to the browser. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-codeinterpretercustom-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-codeinterpretercustom-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the custom code interpreter. For example:

 `arn:aws:bedrock-agentcore:us-east-1:123456789012:code-interpreter-custom/MyCodeInterpreter-a1b2c3d4e5`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-codeinterpretercustom-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-codeinterpretercustom-return-values-fn--getatt-fn--getatt"></a>

`CodeInterpreterArn`  <a name="CodeInterpreterArn-fn::getatt"></a>
The code interpreter Amazon Resource Name (ARN).

`CodeInterpreterId`  <a name="CodeInterpreterId-fn::getatt"></a>
The unique identifier of the created code interpreter.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the code interpreter was created.

`FailureReason`  <a name="FailureReason-fn::getatt"></a>
The reason for failure if the code interpreter is in a failed state.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The time at which the code interpreter was last updated.

`Status`  <a name="Status-fn::getatt"></a>
The status of the custom code interpreter.
