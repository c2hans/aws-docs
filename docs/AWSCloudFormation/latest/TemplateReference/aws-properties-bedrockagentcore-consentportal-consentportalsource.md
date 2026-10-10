---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-consentportal-consentportalsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::ConsentPortal ConsentPortalSource
<a name="aws-properties-bedrockagentcore-consentportal-consentportalsource"></a>

A resource served by the consent portal.

## Syntax
<a name="aws-properties-bedrockagentcore-consentportal-consentportalsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-consentportal-consentportalsource-syntax.json"></a>

```
{
  "[Identifier](#cfn-bedrockagentcore-consentportal-consentportalsource-identifier)" : {{String}},
  "[Type](#cfn-bedrockagentcore-consentportal-consentportalsource-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-consentportal-consentportalsource-syntax.yaml"></a>

```
  [Identifier](#cfn-bedrockagentcore-consentportal-consentportalsource-identifier): {{String}}
  [Type](#cfn-bedrockagentcore-consentportal-consentportalsource-type): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-consentportal-consentportalsource-properties"></a>

`Identifier`  <a name="cfn-bedrockagentcore-consentportal-consentportalsource-identifier"></a>
The identifier of the source resource. For an `agentcore-gateway` source, this is the gateway ID or its Amazon Resource Name (ARN).
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-z][-]?){1,100}-[0-9a-z]{10}$|^arn:aws(-[a-z-]+)?:bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-bedrockagentcore-consentportal-consentportalsource-type"></a>
The type of the source resource.
*Required*: Yes
*Type*: String
*Allowed values*: `agentcore-gateway`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
