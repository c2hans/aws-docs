---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-harnessendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::HarnessEndpoint
<a name="aws-resource-bedrockagentcore-harnessendpoint"></a>

<a name="aws-resource-bedrockagentcore-harnessendpoint-description"></a>The `AWS::BedrockAgentCore::HarnessEndpoint` resource Property description not available. for BedrockAgentCore.

## Syntax
<a name="aws-resource-bedrockagentcore-harnessendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-harnessendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::HarnessEndpoint",
  "Properties" : {
      "[Description](#cfn-bedrockagentcore-harnessendpoint-description)" : {{String}},
      "[EndpointName](#cfn-bedrockagentcore-harnessendpoint-endpointname)" : {{String}},
      "[HarnessId](#cfn-bedrockagentcore-harnessendpoint-harnessid)" : {{String}},
      "[Tags](#cfn-bedrockagentcore-harnessendpoint-tags)" : {{[ Tag, ... ]}},
      "[TargetVersion](#cfn-bedrockagentcore-harnessendpoint-targetversion)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-harnessendpoint-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::HarnessEndpoint
Properties:
  [Description](#cfn-bedrockagentcore-harnessendpoint-description): {{String}}
  [EndpointName](#cfn-bedrockagentcore-harnessendpoint-endpointname): {{String}}
  [HarnessId](#cfn-bedrockagentcore-harnessendpoint-harnessid): {{String}}
  [Tags](#cfn-bedrockagentcore-harnessendpoint-tags): {{
    - Tag}}
  [TargetVersion](#cfn-bedrockagentcore-harnessendpoint-targetversion): {{String}}
```

## Properties
<a name="aws-resource-bedrockagentcore-harnessendpoint-properties"></a>

`Description`  <a name="cfn-bedrockagentcore-harnessendpoint-description"></a>
The description of the endpoint.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointName`  <a name="cfn-bedrockagentcore-harnessendpoint-endpointname"></a>
The name of the endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,47}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HarnessId`  <a name="cfn-bedrockagentcore-harnessendpoint-harnessid"></a>
The ID of the harness that the endpoint belongs to.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrockagentcore-harnessendpoint-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrockagentcore-harnessendpoint-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetVersion`  <a name="cfn-bedrockagentcore-harnessendpoint-targetversion"></a>
The harness version that the endpoint points to. While an update is in progress, this can differ from the live version until the endpoint finishes transitioning.
*Required*: No
*Type*: String
*Pattern*: `^([1-9][0-9]{0,4})$`
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-harnessendpoint-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-harnessendpoint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-harnessendpoint-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrockagentcore-harnessendpoint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the endpoint.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the endpoint was created.

`HarnessName`  <a name="HarnessName-fn::getatt"></a>
The name of the harness that the endpoint belongs to.

`LiveVersion`  <a name="LiveVersion-fn::getatt"></a>
The harness version that the endpoint is currently serving.

`Status`  <a name="Status-fn::getatt"></a>
The status of the endpoint.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the endpoint was last updated.
