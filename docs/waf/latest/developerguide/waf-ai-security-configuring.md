---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-configuring.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Configuring AI Security

This section explains how to configure the AI Security managed rule group.

Most AWS Managed Rules rule groups work as soon as you add them to a protection pack (web ACL). The AI Security rule group requires a rule group configuration. The configuration determines whether AWS WAF calls Amazon Bedrock and which of the rule group's rules can match.

## The configuration object
<a name="waf-ai-security-configuring-object"></a>

You provide the configuration as a `ManagedRuleGroupConfig` element in the `ManagedRuleGroupConfigs` list of the managed rule group statement. The element has the following structure:

```text
ManagedRuleGroupConfig
  └── AWSManagedRulesAISecurityRuleSet        (required)
        └── BedrockGuardrails                 (required)
              ├── Disable                     (empty)
              ├── ProtectRequestOnly          (RoleArn, required)
              └── ProtectRequestAndResponse   (RoleArn, required)
```

`BedrockGuardrails` takes exactly one of three members.

**BedrockGuardrails members**

| Member | Carries | What it does |
| --- | --- | --- |
| `Disable` | nothing | The Guardrails integration is off. The protocol classification and compliance rules still run, because they are deterministic and local to AWS WAF. |
| `ProtectRequestOnly` | `RoleArn` | Guardrails assesses requests. Only the request-phase rules can fire. |
| `ProtectRequestAndResponse` | `RoleArn` | Guardrails assesses requests and responses. Every rule can fire. |

AWS WAF enforces the following constraints on the configuration:
+ `ManagedRuleGroupConfigs` takes exactly one `AWSManagedRulesAISecurityRuleSet` element. AWS WAF rejects a second element as a duplicate.
+ AWS WAF rejects the `AWSManagedRulesAISecurityRuleSet` element in a statement for any other rule group.
+ AWS WAF rejects a statement for this rule group that has no configuration.
+ `BedrockGuardrails` takes exactly one member. If you set two members, or none, AWS WAF returns `WAFInvalidParameterException` with the `Field` value `BEDROCK_GUARDRAILS` and the following reason: "You have used none or multiple values for a field that requires exactly one value."

## How AI Security uses Amazon Bedrock Guardrails
<a name="waf-ai-security-configuring-guardrails"></a>

When you use Amazon Bedrock Guardrails directly, you create a guardrail resource, configure its filters, publish a version, and refer to the guardrail by its identifier. AI Security doesn't use a guardrail resource, so none of these steps apply.

AWS WAF calls the Amazon Bedrock [`InvokeGuardrailChecks`](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeGuardrailChecks.html) operation. This operation doesn't act on a resource. The request carries the content to assess and the list of checks to run, and it contains no guardrail identifier, version, or ARN. AWS WAF chooses the checks, and the categories within each check, based on the protocol and direction of the message. You can't change this selection.

For more information about the operation, see [Use the InvokeGuardrailChecks API in your application](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-invoke-guardrail-checks.html) in the *Amazon Bedrock User Guide*.

As a result, the following apply:
+ There is no guardrail in your account for this feature.
+ You can't add, remove, or reweight categories. The category sets are fixed.
+ The only resource you supply is an AWS Identity and Access Management (IAM) role. For details, see [The IAM role for AI Security](waf-ai-security-role.md).
+ The role needs permission for `InvokeGuardrailChecks`. AWS WAF doesn't call `ApplyGuardrail`, so that permission isn't used.

## Permissions for setting the configuration
<a name="waf-ai-security-configuring-permissions"></a>

When you call `CreateWebACL` or `UpdateWebACL`, AWS WAF checks that you have `iam:PassRole` permission for every role ARN in the AI Security configuration. The following requirements also apply to the role:
+ The role must be in the same account as the protection pack (web ACL). AWS WAF rejects a role in another account with the message "Cross-account pass role is not allowed".
+ The role must be in the same partition as the protection pack (web ACL).

AWS WAF checks `iam:PassRole` before it validates the configuration. A caller who doesn't have this permission receives `AccessDeniedException`, even when the configuration is malformed.

`Disable` carries no role, so AWS WAF doesn't check `iam:PassRole` for it.

## Choose among the three members
<a name="waf-ai-security-configuring-members"></a>

`Disable` turns off content assessment. Protocol recognition and compliance still run. The rule group still adds the traffic labels and the compliance labels, and the baseline compliance rules still block. AWS WAF makes no Amazon Bedrock calls, so you don't need an IAM role, and no Amazon Bedrock charges apply. You still pay the additional AWS WAF fee for each request that the rule group evaluates. You can use `Disable` to apply the protocol checks before you set up the IAM role.

`ProtectRequestOnly` assesses inbound messages. Use it when the content that you want to assess arrives in requests from your users.

`ProtectRequestAndResponse` assesses inbound and outbound messages. Use it when you also want to assess responses, for example, to detect sensitive information in a response or a tool result that contains instructions for your model.

**Important**
With `ProtectRequestAndResponse`, a failure in the response inspection path affects the responses that your clients receive. If an internal error prevents AWS WAF from evaluating the rule group's response rules, the client receives an error response instead of your application's response. Rule action overrides don't change this, so you can't configure the rule group to let responses through when this happens. For details, see [How AWS WAF handles messages that it can't assess](waf-ai-security-deploying.md#waf-ai-security-deploying-cantassess).

**Important**
With `ProtectRequestOnly`, the response-phase rules can't match: the response-phase prompt attack rules and the sensitive information rules. One of these, `Response_GuardrailsPromptAttackHighSeverity`, blocks by default, so this choice changes what the rule group blocks. These rules show no matches because of the configuration, whatever your traffic contains.

Indirect prompt injection, where a tool returns text that your model then acts on, can reach the rule group in two places. An MCP tool result or an A2A reply arrives in a response, so only the response phase assesses it, and `ProtectRequestOnly` doesn't detect it there. An LLM request carries earlier tool results back to the model, for example an OpenAI `tool` message or an Anthropic `tool_result` block. The request phase assesses that text, so `ProtectRequestOnly` detects indirect prompt injection in a tool result that reaches your model through an LLM endpoint that the protection pack (web ACL) protects.

## How AWS WAF handles failures and response-phase actions
<a name="waf-ai-security-configuring-failures"></a>

By default, when an Amazon Bedrock call fails, the `Guardrails_CallFailed` rule counts the message, and the message passes without assessment. To block these messages, override `Guardrails_CallFailed` to Block. For details, see [Failed Amazon Bedrock calls](waf-ai-security-components.md#waf-ai-security-components-call-failed).

Response inspection has a separate failure behavior, and rule action overrides don't change it. For details, see [How AWS WAF handles messages that it can't assess](waf-ai-security-deploying.md#waf-ai-security-deploying-cantassess). Response inspection also adds Amazon Bedrock calls. We recommend that you size your Amazon Bedrock quota for your peak traffic rather than your average traffic.

In the response phase, a Block action returns HTTP 403 and ignores any custom response. AWS WAF rejects the following action overrides for a `Response_` rule, and the error names the rule:
+ Captcha or Challenge
+ Block with a custom response
+ Count or Allow with custom request handling

Rules in your protection pack (web ACL) don't see response-phase labels. To act on a response-phase finding, override the action of the rule group's `Response_` rule.

## Change protocol compliance actions
<a name="waf-ai-security-configuring-compliance"></a>

The configuration object has no compliance setting. The baseline and strict levels are separate rules with different default actions. `Compliance_BaselineMCP` and `Compliance_BaselineA2A` block, and `Compliance_StrictMCP` and `Compliance_StrictA2A` count. To change how AWS WAF handles a level, override the action of its rule, as you do for any managed rule group rule.

A request that violates the baseline level also matches the strict rule for its protocol. To review strict violations without blocking them, keep the strict rules at Count and review their labels.

## Set the configuration in the console
<a name="waf-ai-security-configuring-console"></a>

In the console, you set the configuration in the **AI Security configuration** pane.

**To set the AI Security configuration in the console**

1. To use content assessment, turn on **Send inspected traffic to Amazon Bedrock Guardrails**. A newly added rule group starts with this toggle off. With the toggle off, the console saves `Disable`.

1. For **Service role**, choose a role or enter its ARN. To review the selected role, choose **View role details in IAM**.
   + **Create role** opens the create-role page in the IAM console. The console doesn't create the role for you. For the permissions, trust policy, and condition keys to add, see [The IAM role for AI Security](waf-ai-security-role.md).

1. To assess responses as well as requests, select **Inspect responses**. The console saves `ProtectRequestAndResponse`. With the toggle on and **Inspect responses** cleared, the console saves `ProtectRequestOnly`. Before you inspect responses, review how a response inspection failure affects your clients, described in [How AWS WAF handles messages that it can't assess](waf-ai-security-deploying.md#waf-ai-security-deploying-cantassess).

## Example: enable request and response assessment
<a name="waf-ai-security-configuring-example-enable"></a>

The following rule adds the AI Security rule group with request and response assessment.

```json
{
  "Name": "AI-Security",
  "Priority": 100,
  "Statement": {
    "ManagedRuleGroupStatement": {
      "VendorName": "AWS",
      "Name": "AWSManagedRulesAISecurityRuleSet",
      "ManagedRuleGroupConfigs": [
        {
          "AWSManagedRulesAISecurityRuleSet": {
            "BedrockGuardrails": {
              "ProtectRequestAndResponse": {
                "RoleArn": "arn:aws:iam::111122223333:role/AWSWAFAISecurityRole"
              }
            }
          }
        }
      ]
    }
  },
  "OverrideAction": { "None": {} },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "AI-Security"
  }
}
```

## Example: turn off content assessment
<a name="waf-ai-security-configuring-example-disable"></a>

The following `ManagedRuleGroupConfigs` element turns off content assessment. Protocol recognition and compliance still run.

```json
{
  "AWSManagedRulesAISecurityRuleSet": {
    "BedrockGuardrails": {
      "Disable": {}
    }
  }
}
```
