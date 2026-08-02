---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-browser.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Browser
<a name="aws-resource-bedrockagentcore-browser"></a>

Returns information about an AWS managed Browser (aws.browser.v1) browser for Amazon Bedrock AgentCore.

## Syntax
<a name="aws-resource-bedrockagentcore-browser-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-browser-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::Browser"
}
```

### YAML
<a name="aws-resource-bedrockagentcore-browser-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::Browser
```

## Return values
<a name="aws-resource-bedrockagentcore-browser-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-browser-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-browser-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-browser-return-values-fn--getatt-fn--getatt"></a>

`BrowserArn`  <a name="BrowserArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the browser.

`BrowserId`  <a name="BrowserId-fn::getatt"></a>
The unique identifier of the browser.

`Name`  <a name="Name-fn::getatt"></a>
The name of the browser.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the browser.
