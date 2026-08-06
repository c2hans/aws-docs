---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-harnessversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::HarnessVersion
<a name="aws-resource-bedrockagentcore-harnessversion"></a>

<a name="aws-resource-bedrockagentcore-harnessversion-description"></a>The `AWS::BedrockAgentCore::HarnessVersion` resource Property description not available. for BedrockAgentCore.

## Syntax
<a name="aws-resource-bedrockagentcore-harnessversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-harnessversion-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::HarnessVersion",
  "Properties" : {
      "[HarnessId](#cfn-bedrockagentcore-harnessversion-harnessid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-harnessversion-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::HarnessVersion
Properties:
  [HarnessId](#cfn-bedrockagentcore-harnessversion-harnessid): {{String}}
```

## Properties
<a name="aws-resource-bedrockagentcore-harnessversion-properties"></a>

`HarnessId`  <a name="cfn-bedrockagentcore-harnessversion-harnessid"></a>
The ID of the harness.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bedrockagentcore-harnessversion-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-harnessversion-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-harnessversion-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrockagentcore-harnessversion-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when this harness version was created.

`HarnessArn`  <a name="HarnessArn-fn::getatt"></a>
Property description not available.

`HarnessName`  <a name="HarnessName-fn::getatt"></a>
The name of the harness.

`HarnessVersion`  <a name="HarnessVersion-fn::getatt"></a>
The version of the harness that this summary describes.

`Status`  <a name="Status-fn::getatt"></a>
The status of this harness version.

`Tags`  <a name="Tags-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when this harness version was last updated.
