---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# AWS WAF AI Security

This section explains what AWS WAF AI Security does.

Applications that call large language models (LLMs), invoke tools through the Model Context Protocol (MCP), or exchange messages between agents over the Agent2Agent (A2A) protocol act on instructions in their input. Text in a prompt, in a tool's arguments, or in a tool's result is content that a model reads and might act on. A rule that looks for an exploit signature doesn't match a well-formed request whose text instructs the model to ignore its instructions and reveal its system prompt.

You can monitor and control this type of abuse with the rule group `AWSManagedRulesAISecurityRuleSet`. The rule group recognizes LLM, MCP, and A2A traffic, and it checks recognized MCP and A2A messages against the rules of their protocol. It sends message content to Amazon Bedrock Guardrails for assessment of prompt attacks, harmful content, and sensitive information. It labels requests and responses with what it found and the strength of each finding.

The rule group is available in selected AWS Regions. It's supported for protection packs (web ACLs) that protect Amazon CloudFront distributions, Application Load Balancers, and Amazon API Gateway REST APIs. For the list of Regions, see [AWS WAF AI Security rule group](aws-managed-rule-groups-ai-security.md).

**Note**
This rule group requires configuration. A managed rule group reference statement that doesn't include the `AWSManagedRulesAISecurityRuleSet` rule group configuration is rejected. To have content assessed, you also supply an AWS Identity and Access Management (IAM) role that AWS WAF assumes to call Amazon Bedrock on your behalf. Anyone who creates or updates a protection pack (web ACL) that names this role needs `iam:PassRole` permission for it. This includes updates that don't change the AI Security configuration. For more information, see [Configuring AI Security](waf-ai-security-configuring.md) and [The IAM role for AI Security](waf-ai-security-role.md).

## What the rule group does
<a name="waf-ai-security-what"></a>

AI Security works in two layers: Protocol compliance and Content assessment.

**Protocol recognition and compliance** runs inside AWS WAF. The rule group identifies whether a request is an LLM inference call, an MCP message, or an A2A message, and it labels requests that it doesn't recognize.
+ **MCP** is recognized at protocol versions `2025-06-18`, `2025-11-25`, and `2026-07-28`. Earlier versions, such as `2024-11-05` and `2025-03-26`, aren't recognized.
+ **A2A** is recognized at version 1.0 only. A2A 0.3 traffic, and A2A traffic that declares any other version, isn't recognized.
+ **LLM** traffic is recognized for operations from OpenAI, Anthropic, Google Gemini, and Ollama. Amazon Bedrock's own runtime APIs, such as `Converse` and `InvokeModel`, aren't recognized.

For recognized MCP and A2A messages, the rule group checks the message against its protocol at two levels: Baseline and Strict. **Baseline** violations are malformed messages. Strict violations also include constructs that the protocol permits but that are uncommon. **Strict includes Baseline.** A Baseline check that matches publishes both the baseline and the strict level label for its protocol.

**Content assessment** calls Amazon Bedrock Guardrails. AWS WAF extracts the readable text from a message, sends it to Amazon Bedrock, and converts the findings into labels. The available safeguards are prompt attack, content filter, and sensitive information. AWS WAF sends only some recognized messages for assessment:
+ MCP `tools/call` messages. Other MCP methods are recognized but not assessed.
+ A2A `SendMessage` and `SendStreamingMessage` operations sent with POST, including the REST routes `POST /message:send` and `POST /message:stream`. Other A2A 1.0 operations are recognized but not assessed.
+ Recognized LLM operations, except OpenAI embeddings, image variations, audio transcriptions, and audio translations. These are recognized but not assessed, and they get no outcome label.

**Important**
For a protection pack (web ACL) that protects an Amazon CloudFront distribution, AWS WAF sends message text to Amazon Bedrock in one of the Regions where this rule group is available, and you can't choose which. Each CloudFront edge location sends content to the closest of these Regions, so content from one distribution can be assessed in more than one Region, including Regions outside the country of your viewers or your origin. For an Application Load Balancer or an Amazon API Gateway REST API, AWS WAF sends the text to Amazon Bedrock in the Region of the protection pack (web ACL). For information about how Amazon Bedrock handles this content, see [Data protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html) in the *Amazon Bedrock User Guide*.

A call to Amazon Bedrock can fail when your role or your Amazon Bedrock quota doesn't permit it. For how the calls are charged, see [Managing the cost of AI Security](#waf-ai-security-cost).

## Safeguards by protocol and direction
<a name="waf-ai-security-safeguards"></a>

For each call, AWS WAF requests a set of safeguards from Amazon Bedrock Guardrails. The set depends on the recognized protocol and the direction of the message. The following table shows which safeguards apply to each type of traffic.

**Safeguards by protocol and direction**

| Traffic | Direction | Prompt attack | Content filter | Sensitive information |
| --- | --- | --- | --- | --- |
| LLM | request | Yes | Yes | No |
| LLM | response | No | No | Yes |
| MCP `tools/call` | request | Yes | No | No |
| MCP `tools/call` | response | Yes | No | Yes |
| A2A `SendMessage` and `SendStreamingMessage` | request | Yes | Yes | No |
| A2A `SendMessage` and `SendStreamingMessage` | response | Yes | No | Yes |

Prompt attack isn't assessed on LLM responses, so a model's own completion isn't checked for prompt attack constructs. AWS WAF does assess prompt attack on MCP tool results and A2A replies. Those responses carry third-party content that your agent reads and might act on. This covers indirect prompt injection, where a tool returns text that instructs the model and the model follows it. When an agent sends a tool result back to the model in an LLM request, the request phase also assesses that text for prompt attack.

Sensitive information is assessed only on responses, and content filter is assessed only on requests.

## How AWS WAF scores findings
<a name="waf-ai-security-scoring"></a>

Amazon Bedrock returns a score for each category that AWS WAF requests. AWS WAF assigns each score to a tier and labels the message with the tier. The cut points between tiers are fixed, and you can't change them through any setting.

**Finding tiers and default handling**

| Tier | Score | Default handling |
| --- | --- | --- |
| High | 0.8 and above | Blocks for prompt attack; counts for content filter and sensitive information |
| Medium | 0.6 and above, below 0.8 | Counts |
| Low | above 0, below 0.6 | Counts |
| No finding | 0 | No label. The category was assessed and scored clean |

A score of zero means no finding. Amazon Bedrock returns a result for every category that AWS WAF requests, so a clean message still has a result for each category. Those results carry no label.

**There is no learning period.** Neither layer builds a baseline from your traffic or learns from it, so the rule group assesses traffic the same way from the first request. API Security differs here: its behavioral detections need a baseline window before they can detect anything. For more information, see [Baseline learning period](waf-api-security.md#waf-api-security-baseline).

## What the rule group blocks by default
<a name="waf-ai-security-blocks"></a>

By default, the rules in the following table block. All other rules in the rule group count.

**Rules that block by default**

| Rule name | Label, after the namespace |
| --- | --- |
| `Compliance_BaselineMCP` | `protocol_compliance_level:baseline:mcp` |
| `Compliance_BaselineA2A` | `protocol_compliance_level:baseline:a2a` |
| `Request_GuardrailsPromptAttackHighSeverity` | `request:guardrails:prompt_attack:severity:high` |
| `Response_GuardrailsPromptAttackHighSeverity` | `response:guardrails:prompt_attack:severity:high` |

A failed Amazon Bedrock call doesn't block by default. The rule group labels the message `guardrails:call_failed`, the `Guardrails_CallFailed` rule counts it, and the message passes without assessment. If your role stops working or your Amazon Bedrock quota is exhausted, traffic continues without assessment. To block these messages instead, override `Guardrails_CallFailed` to Block. For why a call fails and how to respond, see [Failed Amazon Bedrock calls](waf-ai-security-components.md#waf-ai-security-components-call-failed).

Response inspection failures are handled separately. If an internal error prevents AWS WAF from evaluating the rule group's response rules, the client receives an error response, and rule action overrides don't change this. For details, see [How AWS WAF handles messages that it can't assess](waf-ai-security-deploying.md#waf-ai-security-deploying-cantassess).

## Managing the cost of AI Security
<a name="waf-ai-security-cost"></a>

You pay an additional AWS WAF fee for each request that this rule group evaluates. AI Security and API Security share this fee. AWS WAF charges it once for a request, however many AI Security and API Security rule groups evaluate that request. A request that a scope-down statement excludes, or that an earlier rule terminates, isn't evaluated and isn't charged this fee. For rates, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).

The content assessment layer calls Amazon Bedrock with the IAM role that you supply. Amazon Bedrock charges and service quotas for those calls apply to your account. Amazon Bedrock reports usage per check, and AWS WAF requests up to three checks for one message. One assessed message can therefore account for more than one check. For the applicable quota, see [Amazon Bedrock endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.html).

Calls that AWS WAF holds back, because of its rate limit or a pause after repeated failures, don't count against your Amazon Bedrock quota. AWS WAF labels those messages `guardrails:call_failed` with the reason `service_unavailable`. For details, see [Failed Amazon Bedrock calls](waf-ai-security-components.md#waf-ai-security-components-call-failed).

To limit evaluation to the paths that serve your agentic traffic, use a scope-down statement inside the managed rule group statement. Narrowing the scope doesn't change how the rule group assesses the requests that remain in scope.

To run protocol recognition and compliance without Amazon Bedrock calls, set the rule group configuration to `Disable`. AWS WAF makes no Amazon Bedrock call, so you incur no Amazon Bedrock charge. You still pay the AWS WAF fee for each request that the rule group evaluates.

**Important**
AI Security uses Amazon Bedrock Guardrails to assess message content. These assessments are probabilistic. They might not identify or categorize all abuse correctly, and they might identify content that isn't abusive. We recommend that you override the blocking rules to Count and confirm that the rule group produces the results you expect on your own traffic before you enforce them.

## Labels
<a name="waf-ai-security-labels"></a>

When AWS WAF evaluates a web request against the AI Security managed rule group, it labels requests and responses with what it recognized and what it found. Labels that the rule group adds in the request phase are available to your own AWS WAF rules. They appear in your protection pack (web ACL) logs and in Amazon CloudWatch metrics.

Labels that the rule group adds in the response phase appear only in CloudWatch label metrics, such as `BlockedResponses`. Your own rules can't match them, and they don't appear in AWS WAF logs. This applies to all sensitive information labels and to the response prompt attack labels. To act on a response-phase finding, override the action of the rule group's own `Response_` rule.

You can't currently deploy this rule group through AWS Firewall Manager or AWS Network Security Manager. Firewall Manager rejects it with `WAFInvalidOperationException`.

For more information about the AI Security managed rule group, see [AWS WAF AI Security rule group](aws-managed-rule-groups-ai-security.md).

**Topics**
+ [What the rule group does](#waf-ai-security-what)
+ [Safeguards by protocol and direction](#waf-ai-security-safeguards)
+ [How AWS WAF scores findings](#waf-ai-security-scoring)
+ [What the rule group blocks by default](#waf-ai-security-blocks)
+ [Managing the cost of AI Security](#waf-ai-security-cost)
+ [Labels](#waf-ai-security-labels)
+ [AWS WAF AI Security components](waf-ai-security-components.md)
+ [Configuring AI Security](waf-ai-security-configuring.md)
+ [The IAM role for AI Security](waf-ai-security-role.md)
+ [Adding the AI Security managed rule group to your protection pack (web ACL)](waf-ai-security-rg-using.md)
+ [Testing and deploying AWS WAF AI Security](waf-ai-security-deploying.md)
+ [AWS WAF AI Security examples](waf-ai-security-examples.md)
