---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ai-security.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# AWS WAF AI Security rule group

This section explains what the AWS WAF AI Security managed rule group does.

VendorName: `AWS`, Name: `AWSManagedRulesAISecurityRuleSet`, Version: `AWSManagedRulesAISecurityRuleSet-V1-0`, WCU: 400

**Note**
This documentation covers the most recent static version release of this managed rule group. We report version changes in the changelog log at [AWS Managed Rules changelog](aws-managed-rule-groups-changelog.md). For information about other versions, use the API command [DescribeManagedRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_DescribeManagedRuleGroup.html).
The information that we publish for the rules in the AWS Managed Rules rule groups is intended to provide you with what you need to use the rules without giving bad actors what they need to circumvent the rules.
If you need more information than you find here, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/).

This rule group recognizes large language model (LLM), Model Context Protocol (MCP), and Agent2Agent (A2A) traffic. It checks recognized MCP and A2A messages against the rules of their protocol. For assessed operations, it sends the message content to Amazon Bedrock Guardrails to assess it for prompt attacks, harmful content, and sensitive information.

**Important**
This rule group requires a rule group configuration. AWS WAF rejects a managed rule group statement without `ManagedRuleGroupConfigs`. For the configuration shape, see [Configuring AI Security](waf-ai-security-configuring.md). For content assessment, you must also supply an AWS Identity and Access Management (IAM) role. For more information, see [The IAM role for AI Security](waf-ai-security-role.md).

**Note**
You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/). AWS WAF calls Amazon Bedrock with the IAM role that you supply, so Amazon Bedrock charges and service quotas apply to your account.

## Considerations for using this rule group
<a name="aws-managed-rule-groups-ai-security-using"></a>

This page describes Version\_1.0, which is the default and only version of this rule group.

**Resource type support.** This rule group is supported for protection packs (web ACLs) that protect Amazon CloudFront distributions, Application Load Balancers, and Amazon API Gateway REST APIs. AWS WAF rejects a request to associate a protection pack (web ACL) that uses this rule group with any other resource type. These include AWS AppSync GraphQL APIs, Amazon Cognito user pools, AWS App Runner services, Amazon Bedrock AgentCore Gateways, AWS Verified Access instances, Elastic Load Balancing for Envoy proxies, and AWS Amplify apps.

**Body size limits.** The rule group assesses only the part of a body that's within the body inspection size limit. For requests, the default limit is 8 KB for an Application Load Balancer and 16 KB for an Amazon CloudFront distribution or an Amazon API Gateway REST API, and you can increase the limit up to 64 KB in your protection pack (web ACL) configuration. For responses, the limit uses the default for the resource type: 8 KB for an Application Load Balancer and 16 KB for an Amazon CloudFront distribution or an Amazon API Gateway REST API. For details, see [Considerations for managing body inspection in AWS WAF](web-acl-setting-body-inspection-limit.md).

**Firewall Manager.** This rule group isn't currently supported with AWS Firewall Manager or AWS Network Security Manager.

**Region availability.** This rule group is available in the following AWS Regions and for Amazon CloudFront:
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (Oregon)
+ Europe (London)
+ Europe (Stockholm)
+ Asia Pacific (Tokyo)
+ Asia Pacific (Sydney)

These are the Regions where Amazon Bedrock offers the `InvokeGuardrailChecks` API that the content assessment calls.

**Important**
For a protection pack (web ACL) that protects an Amazon CloudFront distribution, AWS WAF sends message text to Amazon Bedrock in one of the Regions where this rule group is available, and you can't choose which. Each CloudFront edge location sends content to the closest of these Regions, so content from one distribution can be assessed in more than one Region, including Regions outside the country of your viewers or your origin. For an Application Load Balancer or an Amazon API Gateway REST API, AWS WAF sends the text to Amazon Bedrock in the Region of the protection pack (web ACL). For information about how Amazon Bedrock handles this content, see [Data protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html) in the *Amazon Bedrock User Guide*.

This rule group isn't available in any other Region, including the AWS GovCloud (US) Regions and the China Regions. In those Regions, a request that adds the rule group fails with `WAFNonexistentItemException`.

This rule group is part of the intelligent threat mitigation protections in AWS WAF. For information, see [Intelligent threat mitigation in AWS WAF](waf-managed-protections.md).

To keep your costs down and to be sure you're managing your web traffic as you want, use this rule group in accordance with the guidance at [Best practices for intelligent threat mitigation in AWS WAF](waf-managed-protections-best-practices.md).

## Rules in this rule group
<a name="aws-managed-rule-groups-ai-security-rules"></a>

The rule group's label namespace is `awswaf:managed:aws:ai-security:`. This page shows each label without that namespace. Add the namespace when you match a label in a rule.

Most rules in this rule group count by default. The following tables list the default action of each rule.

**Protocol recognition rules**

| Rule name | Action | Label | Description |
| --- | --- | --- | --- |
| Recognized\_LLM | Count | traffic:recognized\_llm | The request is a call to a supported LLM inference API. |
| Recognized\_MCP | Count | traffic:recognized\_mcp | The request is an MCP message at a supported protocol version. |
| Recognized\_A2A | Count | traffic:recognized\_a2a | The request is an A2A message that declares version 1.0. |
| Not\_Recognized | Count | traffic:not\_recognized | The request is not a supported LLM, MCP, or A2A message. No safeguard runs on it. |

**Protocol compliance rules**

| Rule name | Action | Label | Description |
| --- | --- | --- | --- |
| Compliance\_BaselineMCP | Block | protocol\_compliance\_level:baseline:mcp | The MCP message violates a baseline protocol rule. Baseline rules catch messages that are clearly malformed. |
| Compliance\_BaselineA2A | Block | protocol\_compliance\_level:baseline:a2a | The A2A message violates a baseline protocol rule. |
| Compliance\_StrictMCP | Count | protocol\_compliance\_level:strict:mcp | The MCP message violates a strict protocol rule. Strict rules catch constructs that are valid but unusual. |
| Compliance\_StrictA2A | Count | protocol\_compliance\_level:strict:a2a | The A2A message violates a strict protocol rule. |

**Prompt attack rules**

| Rule name | Action | Label | Description |
| --- | --- | --- | --- |
| Request\_GuardrailsPromptAttackHighSeverity | Block | request:guardrails:prompt\_attack:severity:high | Amazon Bedrock scored a prompt attack in the request at high severity. |
| Request\_GuardrailsPromptAttackMediumSeverity | Count | request:guardrails:prompt\_attack:severity:medium | Amazon Bedrock scored a prompt attack in the request at medium severity. |
| Request\_GuardrailsPromptAttackLowSeverity | Count | request:guardrails:prompt\_attack:severity:low | Amazon Bedrock scored a prompt attack in the request at low severity. |
| Response\_GuardrailsPromptAttackHighSeverity | Block | response:guardrails:prompt\_attack:severity:high | Amazon Bedrock scored a prompt attack in the response at high severity. AWS WAF assesses MCP tool results and A2A replies for prompt attacks, not LLM responses. |
| Response\_GuardrailsPromptAttackMediumSeverity | Count | response:guardrails:prompt\_attack:severity:medium | Amazon Bedrock scored a prompt attack in the response at medium severity. |
| Response\_GuardrailsPromptAttackLowSeverity | Count | response:guardrails:prompt\_attack:severity:low | Amazon Bedrock scored a prompt attack in the response at low severity. |

**Content filter rules**

| Rule name | Action | Label | Description |
| --- | --- | --- | --- |
| Request\_GuardrailsContentFilterHighSeverity | Count | request:guardrails:content\_filter:severity:high | Amazon Bedrock scored harmful content in the request at high severity. AWS WAF doesn't apply the content filter to MCP requests. |
| Request\_GuardrailsContentFilterMediumSeverity | Count | request:guardrails:content\_filter:severity:medium | Amazon Bedrock scored harmful content in the request at medium severity. |
| Request\_GuardrailsContentFilterLowSeverity | Count | request:guardrails:content\_filter:severity:low | Amazon Bedrock scored harmful content in the request at low severity. |

**Sensitive information rules**

| Rule name | Action | Label | Description |
| --- | --- | --- | --- |
| Response\_GuardrailsSensitiveInformationHighConfidence | Count | response:guardrails:sensitive\_information:confidence:high | Amazon Bedrock identified sensitive information in the response at high confidence. |
| Response\_GuardrailsSensitiveInformationMediumConfidence | Count | response:guardrails:sensitive\_information:confidence:medium | Amazon Bedrock identified sensitive information in the response at medium confidence. |
| Response\_GuardrailsSensitiveInformationLowConfidence | Count | response:guardrails:sensitive\_information:confidence:low | Amazon Bedrock identified sensitive information in the response at low confidence. |
| Response\_GuardrailsSensitiveInformationTruncated | Count | response:guardrails:sensitive\_information:truncated | Amazon Bedrock detected more than 1,000 sensitive information entities in the response and returned the first 1,000. The assessment is complete, but the list of findings isn't. |

**Call outcome rules**

| Rule name | Action | Label | Description |
| --- | --- | --- | --- |
| Guardrails\_NotAssessed | Count | guardrails:not\_assessed | AWS WAF found nothing in the message to send to Amazon Bedrock, or couldn't read the body as text. Ordinary traffic produces this label. |
| Guardrails\_CallFailed | Count | guardrails:call\_failed | The call to Amazon Bedrock didn't complete, or AWS WAF didn't make it. The rule counts by default, so the message isn't blocked. |

## Safeguards in each phase
<a name="aws-managed-rule-groups-ai-security-safeguards"></a>

The following table shows the phases in which each safeguard has rules.

**Safeguard phases**

| Safeguard | Runs on | Bands on |
| --- | --- | --- |
| Prompt attack | request and response | severity |
| Content filter | request | severity |
| Sensitive information | response | confidence |

AWS WAF selects the safeguards for each call from the recognized protocol and the direction. As a result, fewer rules can match than the preceding table suggests. The following table shows the safeguards for each assessed operation and direction.

**Safeguards for each assessed operation and direction**

| Traffic | Direction | Prompt attack | Content filter | Sensitive information |
| --- | --- | --- | --- | --- |
| LLM | request | Yes | Yes | No |
| LLM | response | No | No | Yes |
| MCP `tools/call` | request | Yes | No | No |
| MCP `tools/call` | response | Yes | No | Yes |
| A2A `SendMessage` and `SendStreamingMessage` | request | Yes | Yes | No |
| A2A `SendMessage` and `SendStreamingMessage` | response | Yes | No | Yes |

This has the following effects:
+ The response-phase prompt attack rules don't match LLM traffic. AWS WAF doesn't assess a model's completion for prompt attacks.
+ The request-phase content filter rules don't match MCP traffic.

## Categories assessed within each safeguard
<a name="aws-managed-rule-groups-ai-security-categories"></a>

AWS WAF requests a fixed set of categories. You can't add, remove, or reweight categories.

**Categories requested within each safeguard**

| Safeguard | Bands on | Categories requested |
| --- | --- | --- |
| Prompt attack | severity | `jailbreak`, `prompt_injection`, `prompt_leakage` |
| Content filter | severity | `violence`, `hate`, `sexual`, `misconduct`, `insults` |
| Sensitive information | confidence | `aws_access_key`, `aws_secret_key`, `password`, `email`, `credit_debit_card_number`, `us_social_security_number`, `international_bank_account_number`, `us_passport_number`, `us_bank_account_number` |

The sensitive information list covers credential, payment, and identifier types. AWS WAF excludes types whose values resemble ordinary words, such as personal names and place names, to limit findings on normal text. Amazon Bedrock supports more entity types than the nine listed here. AWS WAF requests this subset, and you can't change it.

**Truncated sensitive information results.** Amazon Bedrock returns at most 1,000 sensitive information entities for a response. When a response reaches this cap, the rule group adds the `response:guardrails:sensitive_information:truncated` label, and the assessment still counts as complete. The band and category labels describe only the returned entities. An entity that Amazon Bedrock left out might be in a different category or have a higher confidence. We recommend that you treat the truncated label as at least as serious as the findings beside it. For more information, see [Example configurations, results, and scores](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-invoke-guardrail-checks-examples.html) in the *Amazon Bedrock User Guide*.

Amazon Bedrock documents what each category and entity type covers. That documentation is the authoritative description, and it changes as Amazon Bedrock updates each safeguard:
+ Prompt attack categories: [Detect prompt attacks with Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prompt-attack.html)
+ Content filter categories: [Block harmful words and conversations with content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html)
+ Sensitive information entity types: [Remove PII from conversations by using sensitive information filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html), and the full set of valid values in the [API reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_GuardrailChecksSensitiveInformationEntityConfig.html)

## How AWS WAF assigns scores to tiers
<a name="aws-managed-rule-groups-ai-security-tiers"></a>

**How AWS WAF assigns scores to tiers**

| Tier | Score | Default handling |
| --- | --- | --- |
| High | 0.8 and above | Blocks for prompt attack; counts for content filter and sensitive information |
| Medium | 0.6 and above, below 0.8 | Counts |
| Low | above 0, below 0.6 | Counts |
| No finding | 0 | No label. The category was assessed and scored clean |

**AWS WAF defines the tiers.** Amazon Bedrock returns a numeric severity score for prompt attack and content filter results, and a numeric confidence score for sensitive information results. AWS WAF assigns each score to one of the tiers in the preceding table. The cut points are fixed, and no setting changes them. For what the underlying scores mean, see [Example configurations, results, and scores](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-invoke-guardrail-checks-examples.html) in the *Amazon Bedrock User Guide*.

Each tier covers a range of scores. Amazon Bedrock currently returns prompt attack and content filter severities as one of a few discrete values. Sensitive information confidence is continuous. Don't assume that a score is one of a known set of values.

A score of 0 produces no label. Amazon Bedrock returns a result for every requested category, so a label for a zero score would label every category of every message.

## Recognized protocols and operations
<a name="waf-ai-security-supported"></a>

AWS WAF recognizes more traffic than it assesses. Recognition adds a `traffic:` label to the message. AWS WAF sends content to Amazon Bedrock only for assessed operations.

**LLM.** AWS WAF recognizes the LLM inference operations in the following table and assesses most of them.

**Recognized LLM inference operations**

| Provider | Operations assessed | Recognized but not assessed |
| --- | --- | --- |
| OpenAI | `openai_chat_completions`, `openai_responses`, `openai_completions`, `openai_images_edits`, `openai_images_generations`, `openai_audio_speech` | embeddings, image variations, audio transcriptions, audio translations |
| Anthropic | `anthropic_messages`, `anthropic_complete` | None |
| Google Gemini | `gemini_generate_content`, `gemini_stream_generate_content` | None |
| Ollama | `ollama_generate`, `ollama_chat` | None |

AWS WAF doesn't send the recognized but not assessed operations to Amazon Bedrock, and the rule group adds no outcome label to them.

AWS WAF classifies a POST to an LLM route as LLM traffic when the body contains fields specific to an LLM inference call.

AWS WAF matches an LLM route by the end of the URI path and by the format of the request body, not by the host. A server that implements one of these APIs, such as a gateway or a self-hosted model with an OpenAI-compatible endpoint, is recognized the same way. Amazon Bedrock's own runtime APIs, such as `Converse` and `InvokeModel`, aren't recognized. A request in their format gets the `traffic:not_recognized` label and no content assessment. Amazon Bedrock Guardrails covers these APIs natively, so the rule group doesn't include them. To protect these calls, specify a guardrail in the request: in the header of an `InvokeModel` or `InvokeModelWithResponseStream` request, or in the `guardrailConfig` field of a `Converse` or `ConverseStream` request. For details, see [Use cases for Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use.html) in the *Amazon Bedrock User Guide*.

**MCP** is recognized at protocol versions `2025-06-18`, `2025-11-25`, and `2026-07-28`. Earlier versions, such as `2024-11-05` and `2025-03-26`, aren't recognized. To block MCP requests at earlier versions, see [Blocking MCP requests at unsupported protocol versions](waf-ai-security-example-block-unsupported-mcp.md).

**A2A** is recognized at version 1.0 only. A2A 0.3 traffic, and A2A traffic that declares any other version, isn't recognized. The rule group labels it `traffic:not_recognized`, and AWS WAF doesn't check its compliance or assess it.

## Labels added by this rule group
<a name="aws-managed-rule-groups-ai-security-labels"></a>

Only request-phase labels reach your own rules and your AWS WAF logs. In the response phase, AWS WAF evaluates only this rule group's own `Response_` rules and the `Guardrails_NotAssessed` and `Guardrails_CallFailed` rules. Response-phase labels appear in Amazon CloudWatch label metrics, such as `BlockedResponses`. This applies to all sensitive information labels and to the response prompt attack labels. To act on a response-phase finding, override the rule group's own `Response_` rule for that finding.

**Labels published by this rule group**

| Labels | Count | Notes |
| --- | --- | --- |
| Matched by a rule in this group | 23 | One per rule. A rule action applies. |
| Informational, no rule | 67 | No rule in this group acts on them. You can match the request-phase labels in your own rules. |
| **Total published** | **90** |  |

All labels begin with the namespace `awswaf:managed:aws:ai-security:`. After the namespace, the labels that the rules match take the following forms:

```text
traffic     traffic:<recognized_llm|recognized_mcp|recognized_a2a|not_recognized>
compliance  protocol_compliance_level:<baseline|strict>:<mcp|a2a>
guardrails  <request|response>:guardrails:<safeguard>:<severity|confidence>:<tier>
outcome     guardrails:<not_assessed|call_failed>
```

The label of the `Response_GuardrailsSensitiveInformationTruncated` rule, `response:guardrails:sensitive_information:truncated`, has no tier.

In a content assessment label, the direction comes before the safeguard. API Security labels use the opposite order. For the API Security label shapes, see [Labels added by this rule group](aws-managed-rule-groups-api-security.md#aws-managed-rule-groups-api-security-labels).

**Informational labels.** In addition to the labels that its rules match, the rule group publishes informational labels. No rule in this rule group acts on them. Request-phase informational labels appear in your AWS WAF logs and in CloudWatch label metrics, and you can match them in your own rules. Response-phase informational labels appear only in CloudWatch metrics.

**Informational labels**

| Family | Labels | Form, after the namespace | What it tells you |
| --- | --- | --- | --- |
| Per-check protocol compliance | 13 | `protocol_compliance_check:<check>` | Which individual compliance check failed. The compliance rules act on the level, not the individual check. |
| Finding category | 51 | `guardrails:<safeguard>:<category>:<severity\|confidence>:<tier>` | The specific Amazon Bedrock category behind a finding, such as a jailbreak or an email address. |
| Call failure reason | 3 | `guardrails:call_failed:<reason>` | Why the Amazon Bedrock call did not complete: `access_denied`, `throttling`, `service_unavailable`. |

## Finding category labels
<a name="aws-managed-rule-groups-ai-security-category-labels"></a>

A category label names the specific Amazon Bedrock category or entity type behind a finding. You can use it to act on one category instead of a whole safeguard. The rule group publishes a category label for every category that AWS WAF requests at every tier:

```text
guardrails:<safeguard>:<category>:<severity|confidence>:<tier>
```

**Finding category label counts**

| Safeguard | Categories | Tiers | Labels |
| --- | --- | --- | --- |
| Prompt attack | 3 | 3 | 9 |
| Content filter | 5 | 3 | 15 |
| Sensitive information | 9 | 3 | 27 |
| **Total** | **17** |  | **51** |

To form a category label, take the lowercase category name from the table in [Categories assessed within each safeguard](#aws-managed-rule-groups-ai-security-categories). Then use the band key for the safeguard: `severity` for prompt attack and content filter, and `confidence` for sensitive information. For example:

```text
guardrails:prompt_attack:jailbreak:severity:high
guardrails:content_filter:violence:severity:medium
guardrails:sensitive_information:email:confidence:low
```

**A category label carries no direction.** Rule labels begin with `request:` or `response:`. A category label is the same in both phases. Only request-phase labels reach your own rules and your AWS WAF logs, as described in [Labels added by this rule group](#aws-managed-rule-groups-ai-security-labels). As a result, a category label in your rules or your logs comes from the request phase. To count response-phase category findings, use the response-phase CloudWatch metrics.

## Protocol compliance checks
<a name="aws-managed-rule-groups-ai-security-compliance-checks"></a>

AWS WAF runs the protocol compliance checks in the following tables on MCP and A2A messages. Each check that matches publishes its own label under `protocol_compliance_check:`. It also publishes the level labels that the compliance rules act on.

**MCP**

**MCP protocol compliance checks**

| Check label, after `protocol_compliance_check:` | Level | What it detects |
| --- | --- | --- |
| mcp\_non\_object\_root | Baseline | The body root is not a JSON object. |
| mcp\_mirrored\_header\_unvalidated\_version | Baseline | A mirrored header on a protocol revision that does not require the server to check it. |
| mcp\_method\_mismatch | Baseline | The `Mcp-Method` header differs from the body's `method`. |
| mcp\_protocol\_version\_mismatch | Baseline | The header version differs from the `_meta` version, or that member is absent. |
| mcp\_method\_not\_string | Baseline | `method` is present and is not a string. |
| mcp\_invalid\_json\_rpc\_version | Strict | `jsonrpc` is present and is not `2.0`. |
| mcp\_missing\_method | Strict | No `method` in an object root. |
| mcp\_missing\_method\_header | Strict | `Mcp-Method` is absent on protocol revision 2026-07-28. |
| mcp\_missing\_name\_header | Strict | `Mcp-Name` is absent on a method that names a target. |
| mcp\_tool\_call\_missing\_name | Strict | A `tools/call` with no usable `params.name`. |

**A2A**

**A2A protocol compliance checks**

| Check label, after `protocol_compliance_check:` | Level | What it detects |
| --- | --- | --- |
| a2a\_invalid\_role | Baseline | `role` is present and is neither `ROLE_USER` nor `ROLE_AGENT`. |
| a2a\_missing\_required\_field | Strict | The message is missing `messageId`, `role`, or a non-empty `parts`. |
| a2a\_missing\_task\_id | Strict | A task operation with no `params.id`. |

**A conforming request gets no compliance label.** The rule group has no label that means "checked and passed". The absence of a compliance label doesn't show that the checks ran. A request that the checks don't apply to, such as recognized LLM traffic, also gets no compliance label.

The checks are stateless and read only the request. They need no history and take effect from the first request.

## How the compliance level labels relate
<a name="aws-managed-rule-groups-ai-security-compliance-levels"></a>

**Important**
**Strict includes Baseline.** A Baseline check that matches publishes both the baseline **and** the strict level label for its protocol. The request matches both `Compliance_Baseline<protocol>` and `Compliance_Strict<protocol>`. A Strict check publishes only the strict label.

**Compliance level labels and matching rules**

| Finding | Level labels emitted | Which rules match |
| --- | --- | --- |
| A **Baseline** check matched | `protocol_compliance_level:baseline:<protocol>` **and** `protocol_compliance_level:strict:<protocol>` | Both the Baseline rule and the Strict rule for that protocol match |
| A **Strict** check matched | `protocol_compliance_level:strict:<protocol>` only | Only the Strict rule for that protocol matches |
| Nothing matched, or the request is out of scope | no label | No compliance rule matches. There is no label for a conforming request |

This has the following effects:
+ **Strict rule match counts include Baseline matches.** `Compliance_StrictMCP` counts every MCP compliance finding, including Baseline findings. To count Strict findings alone, subtract the Baseline rule's matches, or match the individual check labels.
+ **An override on one level rule doesn't change the other.** Overriding the Strict rule doesn't exempt Baseline findings from the Baseline rule. Overriding the Baseline rule to Count still leaves the Strict rule counting the same request.

## Call outcomes
<a name="aws-managed-rule-groups-ai-security-call-outcomes"></a>

For an assessed operation, the rule group adds an outcome label when AWS WAF sends nothing to Amazon Bedrock or when the call doesn't complete. In both cases, the message passes without assessment. Both outcome rules count by default.

`guardrails:not_assessed` means that AWS WAF found no text in the message to send to Amazon Bedrock. Ordinary traffic produces this label, for example a tool call with no words in its arguments, an image-only prompt, or a body that isn't text. The published label doesn't distinguish between these cases.

In the response phase, some responses get no AI Security label at all, not even `guardrails:not_assessed`. These responses look the same as a response that AWS WAF assessed and found no issues. For the list, see [AWS WAF AI Security components](waf-ai-security-components.md).

`guardrails:call_failed` means that the Amazon Bedrock call didn't complete, or that AWS WAF didn't make the call. The rule group also adds a reason label. Role failures publish as `access_denied`, and throttling of your Amazon Bedrock quota publishes as `throttling`. Any other failure publishes as `service_unavailable`.

The `service_unavailable` reason also covers calls that AWS WAF holds back, because of its rate limit or a pause after repeated failures. As a result, a broken role or an exhausted quota can appear mostly as `service_unavailable`. For how to respond to each reason, see [Failed Amazon Bedrock calls](waf-ai-security-components.md#waf-ai-security-components-call-failed).

To block messages that AWS WAF couldn't assess, override `Guardrails_CallFailed` to Block. The override applies in both phases.

## Amazon CloudWatch metrics
<a name="aws-managed-rule-groups-ai-security-metrics"></a>

The rule group's metrics appear in the standard AWS WAF metrics namespace, `AWS/WAFV2`. AI Security has no separate namespace.

**Amazon CloudWatch metrics**

| Metric | Phase | What it is |
| --- | --- | --- |
| `AllowedRequests`, `BlockedRequests` | Request phase | Label metrics. One count for each request that carries the label, under the metric for the request's final action, with the `LabelNamespace` and `LabelName` dimensions. If another rule ends the request with a CAPTCHA or Challenge action, the count is in `CaptchaRequests` or `ChallengeRequests`. |
| `AllowedResponses`, `BlockedResponses`, `CountedResponses` | Response phase | Label metrics for responses that carry an AI Security label, under the metric for the response's final action. They are separate metrics, not a dimension on the request-phase ones. No metric counts all inspected responses. |
| `AllowedRequests`, `BlockedRequests`, `CountedRequests`, `Requests` | Request phase | Rule metrics, published under the rule group metric name `AWSManagedRulesAISecurityRuleSet`. |
| `AllowedResponses`, `BlockedResponses`, `CountedResponses` | Response phase | The response-phase equivalents of the rule metrics. |

AWS WAF doesn't publish rule match metrics, such as `CountRuleMatch` and `CountResponseRuleMatch`, for AI Security labels. Those metrics count labels that a rule adds. The rules in this rule group match labels but don't add any.

`Requests` counts only the request phase. As a result, a response-phase label metric divided by `Requests` understates the match rate on inspected responses. `AllowedResponses`, `BlockedResponses`, and `CountedResponses` count only responses that carry an AI Security label.

No metric counts distinct clients or sessions.
