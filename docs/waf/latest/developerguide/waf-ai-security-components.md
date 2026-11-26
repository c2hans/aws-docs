---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-components.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# AWS WAF AI Security components

AI Security processes each message in a fixed order. Any step can end the sequence. The label that the rule group adds shows which step the message reached.

1. **Protocol recognition.** AWS WAF determines whether the message is a large language model (LLM) inference call, a Model Context Protocol (MCP) message, or an Agent2Agent (A2A) message. If the message is none of these, the rule group labels it `traffic:not_recognized` and stops.

1. **Protocol compliance.** For recognized MCP and A2A messages, AWS WAF checks the message against the rules of its protocol.

1. **Text extraction.** For an assessed operation, AWS WAF extracts the readable text from the message. If there is no text to assess, the rule group labels the message as not assessed and stops without calling Amazon Bedrock.

1. **Content assessment.** AWS WAF assumes the AWS Identity and Access Management (IAM) role in your rule group configuration. It then calls Amazon Bedrock Guardrails with the extracted text and the safeguards that apply to this protocol and direction.

1. **Labeling.** AWS WAF assigns each finding from Amazon Bedrock Guardrails to a tier and labels the message.

## Protocol recognition
<a name="waf-ai-security-components-recognition"></a>

AWS WAF recognizes more traffic than it assesses. Recognition adds a `traffic:` label to the message. Only assessed operations continue to text extraction and content assessment.

**MCP.** AWS WAF recognizes MCP traffic at protocol versions `2025-06-18`, `2025-11-25`, and `2026-07-28`. AWS WAF recognizes any MCP method at these versions and assesses only `tools/call`. It doesn't recognize earlier versions, such as `2024-11-05` and `2025-03-26`. To block MCP requests at earlier versions, see [Blocking MCP requests at unsupported protocol versions](waf-ai-security-example-block-unsupported-mcp.md).

**A2A.** AWS WAF recognizes A2A traffic at version 1.0 only. A2A 0.3 traffic, and A2A traffic that declares any other version, isn't recognized. AWS WAF recognizes any A2A 1.0 operation and assesses only `SendMessage` and `SendStreamingMessage` on POST. In the REST binding, these operations are `POST /message:send` and `POST /message:stream`.

**LLM.** AWS WAF recognizes the LLM inference operations in the following table and assesses most of them. Each provider shapes its request and response bodies differently, and AWS WAF uses the operation to locate the text.

**Recognized LLM operations by provider**

| Provider | Operations assessed | Recognized but not assessed |
| --- | --- | --- |
| OpenAI | `openai_chat_completions`, `openai_responses`, `openai_completions`, `openai_images_edits`, `openai_images_generations`, `openai_audio_speech` | embeddings, image variations, audio transcriptions, audio translations |
| Anthropic | `anthropic_messages`, `anthropic_complete` | None |
| Google Gemini | `gemini_generate_content`, `gemini_stream_generate_content` | None |
| Ollama | `ollama_generate`, `ollama_chat` | None |

AWS WAF doesn't send the recognized but not assessed operations to Amazon Bedrock, and the rule group adds no outcome label to them.

AWS WAF classifies a POST to an LLM route as LLM traffic when the body contains fields specific to an LLM inference call.

AWS WAF matches an LLM route by the end of the URI path and by the format of the request body, not by the host. A server that implements one of these APIs, such as a gateway or a self-hosted model with an OpenAI-compatible endpoint, is recognized the same way. Amazon Bedrock's own runtime APIs, such as `Converse` and `InvokeModel`, aren't recognized. A request in their format gets the `traffic:not_recognized` label and no content assessment. Amazon Bedrock Guardrails covers these APIs natively, so the rule group doesn't include them. To protect these calls, specify a guardrail in the request: in the header of an `InvokeModel` or `InvokeModelWithResponseStream` request, or in the `guardrailConfig` field of a `Converse` or `ConverseStream` request. For details, see [Use cases for Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use.html) in the *Amazon Bedrock User Guide*.

An agentic API that AWS WAF doesn't recognize receives no compliance checking and no content assessment.

## Protocol compliance
<a name="waf-ai-security-components-compliance"></a>

AWS WAF checks MCP and A2A messages for protocol compliance. It doesn't check LLM inference calls, because provider inference APIs don't follow a common standard.

Compliance has two levels. Each level has its own rules and its own default action.
+ A **Baseline** violation is a message that is malformed under the protocol. Baseline rules block by default. They are the only rules in this rule group that block without an Amazon Bedrock assessment.
+ A **Strict** violation is a construct that the protocol permits but that is uncommon. Strict rules count by default.

The rule group also publishes a label that names the individual check that failed, alongside the level labels. Each check belongs to the Baseline level or the Strict level. The compliance rules act on the level. To act on one specific check, match its label in your own rule. For the full list, see [AWS WAF AI Security rule group](aws-managed-rule-groups-ai-security.md).

**Strict includes Baseline.** A Baseline finding publishes both level labels, so it matches the Strict rule as well as the Baseline rule. As a result, Strict rule match counts include all Baseline matches.

## Text that AWS WAF sends to Amazon Bedrock
<a name="waf-ai-security-components-text"></a>

AWS WAF sends only the text of a message to Amazon Bedrock. It omits the rest of the body.

AWS WAF reads text from the members of the message that carry words. It selects these members from the protocol schema and ignores the content type that the sender declares.

For a member that the schema defines as bytes, such as an MCP resource `blob` or the `raw` data of an A2A part, AWS WAF decodes the base64 data. The decoded bytes determine whether there is text to send. Without decoding, base64 image data might score as a prompt attack, and base64 encoding might hide a credential from the sensitive information check.

AWS WAF drops entire files, including their URI and file name. AWS WAF doesn't fetch any URL in a message.

AWS WAF passes free-form members through as they are. A free-form member is one whose schema is defined by the tool rather than the protocol, such as MCP `arguments`, an A2A `data` part, or a content block's `input`. The schema doesn't identify which key in such a member holds bytes.

## Messages that AWS WAF doesn't assess
<a name="waf-ai-security-components-not-assessed"></a>

If text extraction finds nothing to send, the rule group adds the `guardrails:not_assessed` label and makes no Amazon Bedrock call. A not-assessed message isn't a failure. The `Guardrails_NotAssessed` rule counts by default.

A message isn't assessed in these cases:
+ It holds no words, such as a `tools/call` whose arguments carry no text. This is ordinary traffic.
+ Its content is only in a form that AWS WAF doesn't read as text, such as an image-only prompt, an audio upload, or a part that contains only a file.
+ The body isn't text, such as a compressed or binary body.
+ In the response phase, the inspection size limit cut the body before its first whole character.

In every case except the first, the message contained content that passed without being checked.

The published label doesn't include the reason. As a result, the label doesn't distinguish a message that held no words from a message whose words were in a form that AWS WAF doesn't read.

Some responses get no AI Security label at all, not even `guardrails:not_assessed`:
+ An empty response body
+ A streaming response whose body hasn't arrived
+ Any response, when the protection pack (web ACL) captures no response body
+ A response with a status other than 2xx, a custom error page, or a response that the front door produces

These responses look the same as a response that AWS WAF assessed and found no issues.

## Failed Amazon Bedrock calls
<a name="waf-ai-security-components-call-failed"></a>

If the Amazon Bedrock call doesn't complete, the rule group adds the `guardrails:call_failed` label. It also adds a second label, `guardrails:call_failed:<reason>`, that names the reason. By default, the `Guardrails_CallFailed` rule counts the message, and the message passes without assessment. To block messages that AWS WAF couldn't assess, override `Guardrails_CallFailed` to Block. The override applies in both phases.

**Reasons for a failed Amazon Bedrock call**

| Reason label | What it means | What to do |
| --- | --- | --- |
| `access_denied` | AWS WAF couldn't assume your role, your role doesn't allow the Amazon Bedrock call, or AWS STS isn't enabled for your account in the Region. | Fix the role, or turn on AWS STS in the Region. |
| `throttling` | Amazon Bedrock throttled the call against your account's quota. | Request a quota increase. |
| `service_unavailable` | Any other failure in AWS WAF or a dependency, and calls that AWS WAF holds back. | See the following paragraphs. |

The `service_unavailable` reason also covers calls that AWS WAF holds back. AWS WAF limits the rate of Amazon Bedrock calls for each protection pack (web ACL). It also pauses calls for a protection pack (web ACL) after repeated failures, including failures that your role or your Amazon Bedrock quota causes. A pause lasts up to a minute. AWS WAF doesn't send calls that exceed the limit or that arrive during a pause. It labels those messages `guardrails:call_failed` with the reason `service_unavailable`, and those calls don't count against your Amazon Bedrock quota. As a result, a broken role or an exhausted quota can appear mostly as `service_unavailable`.

If `service_unavailable` follows `access_denied` or `throttling`, fix the role or the quota first. If a sustained `service_unavailable` rate doesn't follow either reason, contact AWS Support.

**Important**
This section describes a failed Amazon Bedrock call. A failure of the response inspection path behaves differently, and rule action overrides don't change it. For details, see [How AWS WAF handles messages that it can't assess](waf-ai-security-deploying.md#waf-ai-security-deploying-cantassess).

## Labels
<a name="waf-ai-security-components-labels"></a>

Some of the rule group's labels have a matching rule in the group. The rest are informational, and no rule in the group acts on them.

Only request-phase labels reach your own rules and your AWS WAF logs. In the response phase, AWS WAF evaluates only this rule group's own `Response_` rules and the `Guardrails_NotAssessed` and `Guardrails_CallFailed` rules. Response-phase labels appear in Amazon CloudWatch label metrics, such as `BlockedResponses`. This applies to all sensitive information labels and to the response prompt attack labels. To act on a response-phase finding, override the rule group's own `Response_` rule for that finding.

**Published labels**

| Labels | Count | Notes |
| --- | --- | --- |
| Matched by a rule in this group | 23 | One per rule. A rule action applies. |
| Informational, no rule | 67 | No rule in this group acts on them. You can match the request-phase labels in your own rules. |
| **Total published** | **90** |  |

All labels begin with the namespace `awswaf:managed:aws:ai-security:`. The rest of the label takes one of four forms:

```text
traffic     traffic:<recognized_llm|recognized_mcp|recognized_a2a|not_recognized>
compliance  protocol_compliance_level:<baseline|strict>:<mcp|a2a>
guardrails  <request|response>:guardrails:<safeguard>:<severity|confidence>:<tier>
outcome     guardrails:<not_assessed|call_failed>
```

In a content assessment label, the direction comes before the safeguard. API Security labels use the opposite order. For the API Security label shapes, see [Labels added by this rule group](aws-managed-rule-groups-api-security.md#aws-managed-rule-groups-api-security-labels).

For the full list, see [AWS WAF AI Security rule group](aws-managed-rule-groups-ai-security.md).

AWS WAF determines which checks run and how scores map to tiers. Amazon Bedrock Guardrails defines each category and entity type, and what a score represents. For those definitions, see [Use the InvokeGuardrailChecks API in your application](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-invoke-guardrail-checks.html) in the *Amazon Bedrock User Guide*.

## Amazon CloudWatch metrics
<a name="waf-ai-security-components-metrics"></a>

The rule group's metrics appear in the standard AWS WAF metrics namespace, `AWS/WAFV2`. AI Security has no separate namespace.

A label metric counts matches of one label. It gives you a count for a single finding rather than for the whole rule group.

**AI Security Amazon CloudWatch metrics**

| Metric | Phase | What it is |
| --- | --- | --- |
| `AllowedRequests`, `BlockedRequests` | Request phase | Label metrics. One count for each request that carries the label, under the metric for the request's final action, with the `LabelNamespace` and `LabelName` dimensions. If another rule ends the request with a CAPTCHA or Challenge action, the count is in `CaptchaRequests` or `ChallengeRequests`. |
| `AllowedResponses`, `BlockedResponses`, `CountedResponses` | Response phase | Label metrics for responses that carry an AI Security label, under the metric for the response's final action. They are separate metrics, not a dimension on the request-phase ones. No metric counts all inspected responses. |
| `AllowedRequests`, `BlockedRequests`, `CountedRequests`, `Requests` | Request phase | Rule metrics, published under the rule group metric name `AWSManagedRulesAISecurityRuleSet`. |
| `AllowedResponses`, `BlockedResponses`, `CountedResponses` | Response phase | The response-phase equivalents of the rule metrics. |

AWS WAF doesn't publish rule match metrics, such as `CountRuleMatch` and `CountResponseRuleMatch`, for AI Security labels. Those metrics count labels that a rule adds. The rules in this rule group match labels but don't add any.

AWS WAF splits a label at its last colon to form the label metric dimensions. The last element is `LabelName`. Everything before the last colon is `LabelNamespace`, without a trailing colon. For example, for `awswaf:managed:aws:ai-security:guardrails:call_failed`, `LabelName` is `call_failed`. `LabelNamespace` is the rest of the label, which ends in `ai-security:guardrails` with no trailing colon. protection pack (web ACL) label metrics also carry the `WebACL` and `Region` dimensions. Omit `Region` for Amazon CloudFront. An alarm must name every dimension.

The rules whose names start with `Response_` run in the response phase. Their matches and labels appear only in the response-phase metrics, such as `BlockedResponses`. A dashboard built only on request-phase metrics doesn't show them.

`Requests` counts only the request phase. As a result, a response-phase label metric divided by `Requests` understates the match rate on inspected responses. `AllowedResponses`, `BlockedResponses`, and `CountedResponses` count only responses that carry an AI Security label.

No metric counts distinct clients or sessions. Every metric is a request counter or a match counter.

## AWS WAF logs
<a name="waf-ai-security-components-logs"></a>

Request-phase findings appear in the following AWS WAF log fields:
+ `labels` lists each full label name, up to 100 for each request.
+ The rule group's entry in `ruleGroupList` contains `terminatingRule`, `nonTerminatingMatchingRules`, and `excludedRules`.
+ `httpRequest` identifies the client.
+ `externalServiceCalls` contains the Amazon Bedrock request ID when AWS WAF called Amazon Bedrock Guardrails for the request and Amazon Bedrock returned an ID. The entry has `serviceName` set to `bedrock` and the ID in `requestId`. Use the ID when you troubleshoot a call with AWS Support.

Response-phase labels don't appear in logs, as described in [Labels](#waf-ai-security-components-labels). The Amazon Bedrock request ID for a response-phase call doesn't appear in logs either. Raw Amazon Bedrock scores don't appear in labels, logs, or metrics.

We recommend that you use metrics to find which findings occur and how often. Then use logs to review individual request-phase findings before you change a rule action.
