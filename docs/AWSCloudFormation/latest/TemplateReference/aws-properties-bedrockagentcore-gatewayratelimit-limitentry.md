---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayratelimit-limitentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRateLimit LimitEntry
<a name="aws-properties-bedrockagentcore-gatewayratelimit-limitentry"></a>

A single rule entry within a rate limit that maps dimension values to rate configurations. Each entry defines the rate limits for a specific combination of dimension values.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayratelimit-limitentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayratelimit-limitentry-syntax.json"></a>

```
{
  "[Connections](#cfn-bedrockagentcore-gatewayratelimit-limitentry-connections)" : {{[ RateConfig, ... ]}},
  "[Dimensions](#cfn-bedrockagentcore-gatewayratelimit-limitentry-dimensions)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Requests](#cfn-bedrockagentcore-gatewayratelimit-limitentry-requests)" : {{[ RateConfig, ... ]}},
  "[Tokens](#cfn-bedrockagentcore-gatewayratelimit-limitentry-tokens)" : {{[ RateConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayratelimit-limitentry-syntax.yaml"></a>

```
  [Connections](#cfn-bedrockagentcore-gatewayratelimit-limitentry-connections): {{
    - RateConfig}}
  [Dimensions](#cfn-bedrockagentcore-gatewayratelimit-limitentry-dimensions): {{
    {{Key}}: {{Value}}}}
  [Requests](#cfn-bedrockagentcore-gatewayratelimit-limitentry-requests): {{
    - RateConfig}}
  [Tokens](#cfn-bedrockagentcore-gatewayratelimit-limitentry-tokens): {{
    - RateConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayratelimit-limitentry-properties"></a>

`Connections`  <a name="cfn-bedrockagentcore-gatewayratelimit-limitentry-connections"></a>
The connection rate limit configuration. Specifies the maximum number of concurrent connections allowed.
*Required*: No
*Type*: Array of [RateConfig](aws-properties-bedrockagentcore-gatewayratelimit-rateconfig.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dimensions`  <a name="cfn-bedrockagentcore-gatewayratelimit-limitentry-dimensions"></a>
A map of dimension names to dimension values for this rule entry. Keys must match the parent rate limit's dimension keys. Values may use `*` as a wildcard, but only in trailing positions based on the dimension keys ordering.
*Required*: Yes
*Type*: Object of String
*Pattern*: `^(targetName|toolName|qualifiedModelId|\$\.context\.iam\.principal|\$\.context\.iam\.sourceIdentity|\$\.context\.jwt\.[a-zA-Z_][a-zA-Z0-9_\-\.]{0,61}[a-zA-Z0-9_])$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Requests`  <a name="cfn-bedrockagentcore-gatewayratelimit-limitentry-requests"></a>
The request rate limit configuration. Specifies the maximum number of requests allowed per time period.
*Required*: No
*Type*: Array of [RateConfig](aws-properties-bedrockagentcore-gatewayratelimit-rateconfig.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tokens`  <a name="cfn-bedrockagentcore-gatewayratelimit-limitentry-tokens"></a>
The token rate limit configuration. Specifies the maximum number of tokens allowed per time period.
*Required*: No
*Type*: Array of [RateConfig](aws-properties-bedrockagentcore-gatewayratelimit-rateconfig.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
