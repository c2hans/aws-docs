---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-gatewaytarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget
<a name="aws-resource-bedrockagentcore-gatewaytarget"></a>

After creating a gateway, you can add targets, which define the tools that your gateway will host.

For more information about adding gateway targets, see [Add targets to an existing gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building-adding-targets.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-gatewaytarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-gatewaytarget-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::GatewayTarget",
  "Properties" : {
      "[CredentialProviderConfigurations](#cfn-bedrockagentcore-gatewaytarget-credentialproviderconfigurations)" : {{[ CredentialProviderConfiguration, ... ]}},
      "[Description](#cfn-bedrockagentcore-gatewaytarget-description)" : {{String}},
      "[GatewayIdentifier](#cfn-bedrockagentcore-gatewaytarget-gatewayidentifier)" : {{String}},
      "[MetadataConfiguration](#cfn-bedrockagentcore-gatewaytarget-metadataconfiguration)" : {{MetadataConfiguration}},
      "[Name](#cfn-bedrockagentcore-gatewaytarget-name)" : {{String}},
      "[PrivateEndpoint](#cfn-bedrockagentcore-gatewaytarget-privateendpoint)" : {{PrivateEndpoint}},
      "[TargetConfiguration](#cfn-bedrockagentcore-gatewaytarget-targetconfiguration)" : {{TargetConfiguration}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-gatewaytarget-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::GatewayTarget
Properties:
  [CredentialProviderConfigurations](#cfn-bedrockagentcore-gatewaytarget-credentialproviderconfigurations): {{
    - CredentialProviderConfiguration}}
  [Description](#cfn-bedrockagentcore-gatewaytarget-description): {{String}}
  [GatewayIdentifier](#cfn-bedrockagentcore-gatewaytarget-gatewayidentifier): {{String}}
  [MetadataConfiguration](#cfn-bedrockagentcore-gatewaytarget-metadataconfiguration): {{
    MetadataConfiguration}}
  [Name](#cfn-bedrockagentcore-gatewaytarget-name): {{String}}
  [PrivateEndpoint](#cfn-bedrockagentcore-gatewaytarget-privateendpoint): {{
    PrivateEndpoint}}
  [TargetConfiguration](#cfn-bedrockagentcore-gatewaytarget-targetconfiguration): {{
    TargetConfiguration}}
```

## Properties
<a name="aws-resource-bedrockagentcore-gatewaytarget-properties"></a>

`CredentialProviderConfigurations`  <a name="cfn-bedrockagentcore-gatewaytarget-credentialproviderconfigurations"></a>
The credential provider configurations.
*Required*: No
*Type*: Array of [CredentialProviderConfiguration](aws-properties-bedrockagentcore-gatewaytarget-credentialproviderconfiguration.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrockagentcore-gatewaytarget-description"></a>
The description for the gateway target.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GatewayIdentifier`  <a name="cfn-bedrockagentcore-gatewaytarget-gatewayidentifier"></a>
The gateway ID for the gateway target.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-z][-]?){1,100}-[0-9a-z]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetadataConfiguration`  <a name="cfn-bedrockagentcore-gatewaytarget-metadataconfiguration"></a>
The metadata configuration for HTTP header and query parameter propagation to and from this gateway target.
*Required*: No
*Type*: [MetadataConfiguration](aws-properties-bedrockagentcore-gatewaytarget-metadataconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-gatewaytarget-name"></a>
The name of the gateway target.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-zA-Z][-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateEndpoint`  <a name="cfn-bedrockagentcore-gatewaytarget-privateendpoint"></a>
The private endpoint configuration for a gateway target. Defines how the gateway connects to private resources in your VPC.
*Required*: No
*Type*: [PrivateEndpoint](aws-properties-bedrockagentcore-gatewaytarget-privateendpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetConfiguration`  <a name="cfn-bedrockagentcore-gatewaytarget-targetconfiguration"></a>
The configuration for a gateway target. This structure defines how the gateway connects to and interacts with the target endpoint.
*Required*: Yes
*Type*: [TargetConfiguration](aws-properties-bedrockagentcore-gatewaytarget-targetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-gatewaytarget-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-gatewaytarget-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the gateway identifier and target ID. For example:

 `my-gateway-a1b2c3d4e5|a1B2c3D4e5`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-gatewaytarget-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-gatewaytarget-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time at which the target was created.

`GatewayArn`  <a name="GatewayArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the gateway target.

`LastSynchronizedAt`  <a name="LastSynchronizedAt-fn::getatt"></a>
The timestamp when the target was last synchronized.

`PrivateEndpointManagedResources`  <a name="PrivateEndpointManagedResources-fn::getatt"></a>
A list of managed resources created by the gateway for private endpoint connectivity.

`ProtocolType`  <a name="ProtocolType-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
The status of the gateway target.

`StatusReasons`  <a name="StatusReasons-fn::getatt"></a>
The status reasons for the target status.

`TargetId`  <a name="TargetId-fn::getatt"></a>
The target ID.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time at which the target was updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
