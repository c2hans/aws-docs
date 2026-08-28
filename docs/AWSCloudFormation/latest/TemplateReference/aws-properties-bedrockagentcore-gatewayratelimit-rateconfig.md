---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayratelimit-rateconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRateLimit RateConfig
<a name="aws-properties-bedrockagentcore-gatewayratelimit-rateconfig"></a>

Contains the rate configuration for a rate limit metric, specifying the allowed rate and time period.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayratelimit-rateconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayratelimit-rateconfig-syntax.json"></a>

```
{
  "[Period](#cfn-bedrockagentcore-gatewayratelimit-rateconfig-period)" : {{String}},
  "[Rate](#cfn-bedrockagentcore-gatewayratelimit-rateconfig-rate)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayratelimit-rateconfig-syntax.yaml"></a>

```
  [Period](#cfn-bedrockagentcore-gatewayratelimit-rateconfig-period): {{String}}
  [Rate](#cfn-bedrockagentcore-gatewayratelimit-rateconfig-rate): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayratelimit-rateconfig-properties"></a>

`Period`  <a name="cfn-bedrockagentcore-gatewayratelimit-rateconfig-period"></a>
The time period for the rate limit. Valid values:
+ `second`—Measures the rate limit over a one-second window.
+ `minute`—Measures the rate limit over a one-minute window.
*Required*: Yes
*Type*: String
*Allowed values*: `second | minute`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rate`  <a name="cfn-bedrockagentcore-gatewayratelimit-rateconfig-rate"></a>
The rate value for the limit. For request limits, this is the number of requests allowed per period. For token limits, this is the number of tokens allowed per period. For connection limits, this is the number of concurrent connections allowed.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `10000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
