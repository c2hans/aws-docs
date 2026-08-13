---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-workloadidentity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::WorkloadIdentity
<a name="aws-resource-bedrockagentcore-workloadidentity"></a>

Creates a workload identity for Amazon Bedrock AgentCore. A workload identity provides OAuth2-based authentication for resources associated with agent runtimes.

For more information about using workload identities in Amazon Bedrock AgentCore, see [Managing workload identities](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/workload-identity.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-workloadidentity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-workloadidentity-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::WorkloadIdentity",
  "Properties" : {
      "[AllowedResourceOauth2ReturnUrls](#cfn-bedrockagentcore-workloadidentity-allowedresourceoauth2returnurls)" : {{[ String, ... ]}},
      "[Name](#cfn-bedrockagentcore-workloadidentity-name)" : {{String}},
      "[Tags](#cfn-bedrockagentcore-workloadidentity-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-workloadidentity-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::WorkloadIdentity
Properties:
  [AllowedResourceOauth2ReturnUrls](#cfn-bedrockagentcore-workloadidentity-allowedresourceoauth2returnurls): {{
    - String}}
  [Name](#cfn-bedrockagentcore-workloadidentity-name): {{String}}
  [Tags](#cfn-bedrockagentcore-workloadidentity-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrockagentcore-workloadidentity-properties"></a>

`AllowedResourceOauth2ReturnUrls`  <a name="cfn-bedrockagentcore-workloadidentity-allowedresourceoauth2returnurls"></a>
The list of allowed OAuth2 return URLs for resources associated with this workload identity.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-workloadidentity-name"></a>
The name of the workload identity. The name must be unique within your account.
*Required*: Yes
*Type*: String
*Pattern*: `[A-Za-z0-9_.-]+`
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrockagentcore-workloadidentity-tags"></a>
The tags for the workload identity.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrockagentcore-workloadidentity-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-workloadidentity-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-workloadidentity-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the workload identity name.

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-workloadidentity-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-workloadidentity-return-values-fn--getatt-fn--getatt"></a>

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The timestamp when the workload identity was created.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The timestamp when the workload identity was last updated.

`WorkloadIdentityArn`  <a name="WorkloadIdentityArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the workload identity.
