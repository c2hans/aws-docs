---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-wafconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway WafConfiguration
<a name="aws-properties-bedrockagentcore-gateway-wafconfiguration"></a>

The AWS WAF configuration for the gateway. This configuration controls how the gateway behaves when the associated web ACL cannot be evaluated.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-wafconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-wafconfiguration-syntax.json"></a>

```
{
  "[FailureMode](#cfn-bedrockagentcore-gateway-wafconfiguration-failuremode)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-wafconfiguration-syntax.yaml"></a>

```
  [FailureMode](#cfn-bedrockagentcore-gateway-wafconfiguration-failuremode): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-wafconfiguration-properties"></a>

`FailureMode`  <a name="cfn-bedrockagentcore-gateway-wafconfiguration-failuremode"></a>
The failure mode that determines how the gateway handles requests when AWS WAF is unreachable or times out. Valid values include:
+ `FAIL_CLOSE` - The gateway blocks requests when AWS WAF cannot be evaluated.
+ `FAIL_OPEN` - The gateway allows requests when AWS WAF cannot be evaluated.
*Required*: No
*Type*: String
*Allowed values*: `FAIL_CLOSE | FAIL_OPEN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
