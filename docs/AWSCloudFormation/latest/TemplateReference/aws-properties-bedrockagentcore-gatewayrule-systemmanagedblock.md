---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-systemmanagedblock.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule SystemManagedBlock
<a name="aws-properties-bedrockagentcore-gatewayrule-systemmanagedblock"></a>

System-managed metadata for rules created by automated processes such as A/B tests.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-systemmanagedblock-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-systemmanagedblock-syntax.json"></a>

```
{
  "[ManagedBy](#cfn-bedrockagentcore-gatewayrule-systemmanagedblock-managedby)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-systemmanagedblock-syntax.yaml"></a>

```
  [ManagedBy](#cfn-bedrockagentcore-gatewayrule-systemmanagedblock-managedby): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-systemmanagedblock-properties"></a>

`ManagedBy`  <a name="cfn-bedrockagentcore-gatewayrule-systemmanagedblock-managedby"></a>
The identifier of the system or process that manages this rule.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
