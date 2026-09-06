---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-matchprincipalentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule MatchPrincipalEntry
<a name="aws-properties-bedrockagentcore-gatewayrule-matchprincipalentry"></a>

<a name="aws-properties-bedrockagentcore-gatewayrule-matchprincipalentry-description"></a>The `MatchPrincipalEntry` property type specifies Property description not available. for an [AWS::BedrockAgentCore::GatewayRule](aws-resource-bedrockagentcore-gatewayrule.md).

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-matchprincipalentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-matchprincipalentry-syntax.json"></a>

```
{
  "[IamPrincipal](#cfn-bedrockagentcore-gatewayrule-matchprincipalentry-iamprincipal)" : {{IamPrincipal}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-matchprincipalentry-syntax.yaml"></a>

```
  [IamPrincipal](#cfn-bedrockagentcore-gatewayrule-matchprincipalentry-iamprincipal): {{
    IamPrincipal}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-matchprincipalentry-properties"></a>

`IamPrincipal`  <a name="cfn-bedrockagentcore-gatewayrule-matchprincipalentry-iamprincipal"></a>
An IAM principal to match against, specified by ARN.
*Required*: Yes
*Type*: [IamPrincipal](aws-properties-bedrockagentcore-gatewayrule-iamprincipal.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
