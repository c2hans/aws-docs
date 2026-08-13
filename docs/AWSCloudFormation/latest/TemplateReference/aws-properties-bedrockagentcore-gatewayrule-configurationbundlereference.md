---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-configurationbundlereference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule ConfigurationBundleReference
<a name="aws-properties-bedrockagentcore-gatewayrule-configurationbundlereference"></a>

A reference to a specific version of a configuration bundle.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-configurationbundlereference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-configurationbundlereference-syntax.json"></a>

```
{
  "[BundleArn](#cfn-bedrockagentcore-gatewayrule-configurationbundlereference-bundlearn)" : {{String}},
  "[BundleVersion](#cfn-bedrockagentcore-gatewayrule-configurationbundlereference-bundleversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-configurationbundlereference-syntax.yaml"></a>

```
  [BundleArn](#cfn-bedrockagentcore-gatewayrule-configurationbundlereference-bundlearn): {{String}}
  [BundleVersion](#cfn-bedrockagentcore-gatewayrule-configurationbundlereference-bundleversion): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-configurationbundlereference-properties"></a>

`BundleArn`  <a name="cfn-bedrockagentcore-gatewayrule-configurationbundlereference-bundlearn"></a>
The Amazon Resource Name (ARN) of the configuration bundle.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BundleVersion`  <a name="cfn-bedrockagentcore-gatewayrule-configurationbundlereference-bundleversion"></a>
The version of the configuration bundle.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
