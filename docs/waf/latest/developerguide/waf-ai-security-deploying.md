---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-deploying.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Testing and deploying AWS WAF AI Security

This section explains how to test the AI Security managed rule group on your own traffic and how to move it into enforcement.

The rule group has no learning period. Nothing in the rule group learns from traffic, so the rule group applies the same assessment from the first request. Testing determines whether the rule group's findings on your traffic are ones that you want to act on.

**To test and deploy the AI Security managed rule group**

1.

**Step 1: Deploy with every blocking rule overridden to Count**

   On the first deployment, override all blocking rules to Count, whatever actions you plan to use later:

**Blocking rules to override to Count**

<table>
<thead>
  <tr><th>Rule name</th><th>Label, after the namespace</th></tr>
</thead>
<tbody>
  <tr><td><code>Compliance_BaselineMCP</code></td><td><code>protocol_compliance_level:baseline:mcp</code></td></tr>
  <tr><td><code>Compliance_BaselineA2A</code></td><td><code>protocol_compliance_level:baseline:a2a</code></td></tr>
  <tr><td><code>Request_GuardrailsPromptAttackHighSeverity</code></td><td><code>request:guardrails:prompt_attack:severity:high</code></td></tr>
  <tr><td><code>Response_GuardrailsPromptAttackHighSeverity</code></td><td><code>response:guardrails:prompt_attack:severity:high</code></td></tr>
</tbody>
</table>

   To do this, use rule action overrides on the individual rules. Setting the rule group's override action to Count also makes every rule count. However, you then can't enforce one rule at a time without removing the rule group override. With rule action overrides, you can enforce the rules one at a time.

1.

**Step 2: Confirm that the rule group assesses your traffic**

   Before you review findings, confirm that the rule group produces them. Complete the following checks in order, because each check depends on the one before it.

   1. Confirm that AWS WAF recognizes your traffic. Look for the `traffic:recognized_llm`, `traffic:recognized_mcp`, and `traffic:recognized_a2a` labels on the endpoints that you expect to carry large language model (LLM), Model Context Protocol (MCP), and Agent2Agent (A2A) traffic. AWS WAF doesn't check or assess traffic that it labels `traffic:not_recognized`. Common causes are a provider or operation that the rule group doesn't recognize and a gateway that changes the request before AWS WAF inspects it. For MCP, AWS WAF recognizes only protocol versions `2025-06-18`, `2025-11-25`, and `2026-07-28`. To block MCP requests at earlier versions, see [Blocking MCP requests at unsupported protocol versions](waf-ai-security-example-block-unsupported-mcp.md). For A2A, AWS WAF recognizes version 1.0 only. For details, see [AWS WAF AI Security components](waf-ai-security-components.md).

   1. Confirm that Amazon Bedrock calls complete. Look for the `guardrails:call_failed` label and its reason label, `guardrails:call_failed:<reason>`. The reason is `access_denied`, `throttling`, or `service_unavailable`. AWS WAF limits the rate of Amazon Bedrock calls for each protection pack (web ACL). It also pauses calls for a protection pack (web ACL) after repeated failures, including failures that your role or your Amazon Bedrock quota causes. A pause lasts up to a minute. AWS WAF doesn't send calls that exceed the limit or that arrive during a pause. It labels those messages with the reason `service_unavailable`, and those calls don't count against your Amazon Bedrock quota. As a result, a broken role or an exhausted quota can appear mostly as `service_unavailable`. If `service_unavailable` follows `access_denied` or `throttling`, fix the role or the quota first. If a sustained `service_unavailable` rate doesn't follow either reason, contact AWS Support. While calls fail, messages pass without assessment, so an absence of findings doesn't show that your traffic is clean. To investigate a call, check the `externalServiceCalls` field of the request's log record for the Amazon Bedrock request ID. Resolve call failures before you continue.

   1. Confirm that your messages contain text to assess. Compare the number of `guardrails:not_assessed` labels with the number of recognized messages. A message with no words in it is ordinary traffic, so some not-assessed volume is expected. Image-only prompts and audio uploads are also not assessed. If almost no recognized traffic is assessed, the text that AWS WAF reads might not be the text that carries your content.

   Some responses get no AI Security label at all. These include responses with an empty body, streaming responses whose body hasn't arrived, and every response when the protection pack (web ACL) captures no response body. They also include responses with a status other than 2xx, custom error pages, and responses that the front door produces. In metrics, these responses look the same as responses that were assessed and had no findings.
**Create an alarm for call failures**
We recommend that you create an Amazon CloudWatch alarm on the `guardrails:call_failed` label metric. By default, a message whose Amazon Bedrock call fails passes without assessment. A misconfigured AWS Identity and Access Management (IAM) role or an exhausted Amazon Bedrock quota therefore doesn't change how your application responds, and AWS WAF assesses no messages until you fix it. For an example alarm, see [Alarming on failed Amazon Bedrock calls](waf-ai-security-example-call-failed-alarm.md).

1.

**Step 3: Rank findings with metrics**

   AWS WAF publishes label metrics in the `AWS/WAFV2` namespace with the `LabelNamespace` and `LabelName` dimensions. Use metrics to find which findings occur and how often. Use logs to judge individual findings, as described in Step 4.

   Each label metric is named for the final action on the request or response. A request that carries a label is counted in `AllowedRequests` if AWS WAF allows it and in `BlockedRequests` if AWS WAF blocks it. AWS WAF doesn't publish rule match metrics, such as `CountRuleMatch`, for AI Security labels.

   Response-phase matches have separate metrics. Labels added in the response phase appear only in `AllowedResponses`, `BlockedResponses`, and `CountedResponses`. A dashboard that tracks both phases needs the request-phase and the response-phase label metrics.

   Calculate each finding's match rate with metric math. Add the label metrics for each phase. `FILL` replaces a missing data point with 0, so the sum has a value when only one of the metrics is published:

   ```text
   request_match_rate  = (FILL(AllowedRequests, 0) + FILL(BlockedRequests, 0)) / Requests
   response_match_rate = (FILL(AllowedResponses, 0) + FILL(BlockedResponses, 0)
                          + FILL(CountedResponses, 0)) / Requests
   ```

   `Requests` counts only the request phase, and no metric counts inspected responses. As a result, the response-phase rate understates the rate on inspected responses. `Requests` also counts requests whose responses AWS WAF doesn't inspect. These include responses with a status other than 2xx, and every response when the rule group uses `ProtectRequestOnly`. `AllowedResponses`, `BlockedResponses`, and `CountedResponses` count only responses that carry an AI Security label.

   Review each rate together with its pattern over time:
   + A finding that matches a steady share of requests, in proportion to traffic, usually comes from your own clients. It describes your application rather than an attack on it. For example, a content filter category that matches a fixed share of all prompts usually reflects the topics that your users discuss.
   + A finding that stays near zero and then rises sharply for a short period is consistent with an attack, because attacks are limited in time.
   + A finding that never matches doesn't show that enforcing its rule is safe.

   For each safeguard, compare the high, medium, and low tiers. The number of matches usually decreases as the tier rises. If the high tier matches about as often as the low tier, the tiers don't separate your traffic. In that case, we recommend that you don't enforce that safeguard's rules yet.

1.

**Step 4: Review findings in the logs**

   Metrics show which findings occur and how often. They don't show which clients produce the findings, because no metric counts distinct clients or sessions. Only your logs attribute findings to clients. Many findings from a few clients suggest a targeted campaign. One finding each from many clients usually reflects your own application's traffic.

   Request-phase findings appear in the following AWS WAF log fields:
   + `labels` lists each full label name, up to 100 for each request.
   + The rule group's entry in `ruleGroupList` contains `terminatingRule`, `nonTerminatingMatchingRules`, and `excludedRules`.
   + `httpRequest` identifies the client.
   + `externalServiceCalls` contains the Amazon Bedrock request ID when AWS WAF called Amazon Bedrock Guardrails for the request and Amazon Bedrock returned an ID. The entry has `serviceName` set to `bedrock` and the ID in `requestId`. Use the ID when you troubleshoot a call with AWS Support.

   Response-phase labels don't appear in logs, and neither does the Amazon Bedrock request ID for a response-phase call. To review response-phase findings, use the response-phase metrics. Raw Amazon Bedrock scores don't appear in labels, logs, or metrics. The tier is the finest measure of a finding that AWS WAF provides.

   For a content assessment finding, review the category label as well as the safeguard. The `prompt_attack` safeguard alone doesn't identify what to change. A `jailbreak` category label that matches your support chatbot's "ignore the previous instruction" phrasing identifies a specific pattern.

1.

**Step 5: Adjust rule behavior, then enforce**

   The rule group has no sensitivity settings. You can't change which Amazon Bedrock categories are assessed or change their weight. The tier cut points are fixed, and no setting changes them. To control how AWS WAF acts on findings, use the following AWS WAF features:
   + **Rule action overrides.** Change the action of a rule in the rule group. Use overrides to enforce one finding and not another. To act on a response-phase finding, override the rule group's own `Response_` rule. In the response phase, a Block action returns HTTP 403 and ignores any custom response. AWS WAF rejects some overrides for `Response_` rules. For the list, see [Configuring AI Security](waf-ai-security-configuring.md).
   + **Scope-down statements.** Exclude traffic from evaluation. Use a scope-down statement when an endpoint produces findings that correctly describe the content but don't indicate risk. An example is an internal tool that exists to discuss credentials.
   + **Your own rules that match labels.** Combine a finding with other information about the request. For example, your rule can block a request with a prompt attack label only when the request comes from an unauthenticated client on a new session. Because the rule group also adds a label for each category, your rule can act on one category without acting on the whole safeguard. Your own rules see only request-phase labels.

   We recommend that you enforce one rule at a time. Start with rules that have a low match rate and whose matches come in short, concentrated periods. After each change, monitor the rule's metric and your application's error rate.

## How AWS WAF handles messages that it can't assess
<a name="waf-ai-security-deploying-cantassess"></a>

AWS WAF handles a failed Amazon Bedrock call and a failure of the response inspection path differently. To troubleshoot a call, find the Amazon Bedrock request ID in the `externalServiceCalls` field of your AWS WAF logs.

**The Amazon Bedrock call fails.** AWS WAF labels the message `guardrails:call_failed`, and by default the message passes without assessment. For why a call fails and how to respond, see [Failed Amazon Bedrock calls](waf-ai-security-components.md#waf-ai-security-components-call-failed).

If you override `Guardrails_CallFailed` to Block, AWS WAF blocks messages for as long as calls fail. Call failures include throttling of your Amazon Bedrock quota, Amazon Bedrock unavailability, and pauses of up to a minute after repeated failures. If you use the override, we recommend that you keep your Amazon Bedrock quota above your peak traffic and set the alarm described in Step 2.

`Guardrails_NotAssessed` works the same way. A message with nothing to assess is ordinary traffic, so overriding `Guardrails_NotAssessed` to Block also blocks legitimate messages.

**The response inspection path fails.** If an internal error prevents AWS WAF from evaluating the rule group's response rules, the client receives an error response instead of your application's response. Rule action overrides don't change this. When you enable response inspection, a failure in the response inspection path therefore affects the responses that your clients receive.
