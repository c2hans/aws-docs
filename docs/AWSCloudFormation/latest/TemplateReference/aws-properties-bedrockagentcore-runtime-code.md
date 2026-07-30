---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-code.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime Code
<a name="aws-properties-bedrockagentcore-runtime-code"></a>

The source code configuration that specifies the location and details of the code to be executed.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-code-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-code-syntax.json"></a>

```
{
  "[S3](#cfn-bedrockagentcore-runtime-code-s3)" : {{S3Location}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-code-syntax.yaml"></a>

```
  [S3](#cfn-bedrockagentcore-runtime-code-s3): {{
    S3Location}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-code-properties"></a>

`S3`  <a name="cfn-bedrockagentcore-runtime-code-s3"></a>
The Amazon Amazon S3 object that contains the source code for the agent runtime.
*Required*: No
*Type*: [S3Location](aws-properties-bedrockagentcore-runtime-s3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
