---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-domainoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway DomainOverride

The public domain names for a gateway that clients reach through your own proxy or custom domain. When you configure a domain override, the gateway advertises these domains instead of the inbound Host header in the URLs that it returns for OAuth discovery, such as the protected resource metadata and the `WWW-Authenticate` challenge.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-domainoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-domainoverride-syntax.json"></a>

```json
{
  "[AlternateDomains](#cfn-bedrockagentcore-gateway-domainoverride-alternatedomains)" : {{[ String, ... ]}},
  "[DefaultDomain](#cfn-bedrockagentcore-gateway-domainoverride-defaultdomain)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-domainoverride-syntax.yaml"></a>

```yaml
  [AlternateDomains](#cfn-bedrockagentcore-gateway-domainoverride-alternatedomains): {{
    - String}}
  [DefaultDomain](#cfn-bedrockagentcore-gateway-domainoverride-defaultdomain): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-domainoverride-properties"></a>

`AlternateDomains`  <a name="cfn-bedrockagentcore-gateway-domainoverride-alternatedomains"></a>
Additional public domain names for the gateway, up to 10. Don't repeat the default domain or list a domain more than once. A request can select one of these domains, or the default domain, with the `x-amzn-bedrock-agentcore-gateway-domain` header. The gateway rejects a request that selects a domain that isn't configured.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `253 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultDomain`  <a name="cfn-bedrockagentcore-gateway-domainoverride-defaultdomain"></a>
The default public domain name for the gateway. The gateway advertises this domain when a request doesn't select a specific domain.
*Required*: Yes
*Type*: String
*Pattern*: `^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)(?:\.(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?))+$`
*Minimum*: `1`
*Maximum*: `253`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
