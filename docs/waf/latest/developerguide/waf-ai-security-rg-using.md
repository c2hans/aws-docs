---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-rg-using.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Adding the AI Security managed rule group to your protection pack (web ACL)

This section describes how to add the AI Security managed rule group to a protection pack (web ACL).

This rule group has prerequisites that other AWS Managed Rules rule groups don't have. If you skip one, AWS WAF rejects the request, or the rule group runs without content assessment.

You can add the rule group by using the AWS WAF console or the AWS WAF API. You can't currently use AWS Firewall Manager or AWS Network Security Manager to deploy this rule group. Firewall Manager rejects a rule group that includes it with `WAFInvalidOperationException`.

## Prerequisites
<a name="waf-ai-security-rg-using-prerequisites"></a>

1. **Choose a configuration.** Choose `Disable`, `ProtectRequestOnly`, or `ProtectRequestAndResponse`. You can't add the rule group without a configuration. For what each configuration does, see [Configuring AI Security](waf-ai-security-configuring.md).

1. **Check the Region.** The rule group is available in selected AWS Regions and for Amazon CloudFront. For the list, see [AWS WAF AI Security rule group](aws-managed-rule-groups-ai-security.md). In any other Region, a request that adds the rule group fails with `WAFNonexistentItemException`.

1. **Check the resource type.** You can use the rule group in a protection pack (web ACL) that protects an Amazon CloudFront distribution, an Application Load Balancer, or an Amazon API Gateway REST API. AWS WAF rejects a request to associate a protection pack (web ACL) that uses this rule group with any other resource type.

1. **Create the service role**, unless you chose `Disable`. AWS WAF uses this AWS Identity and Access Management (IAM) role to call Amazon Bedrock. The role must be in the same account and partition as the protection pack (web ACL). AWS WAF rejects a role in another account. See [The IAM role for AI Security](waf-ai-security-role.md).

1. **Get permission to pass the role**, unless you chose `Disable`. The identity that adds the rule group needs `iam:PassRole` permission for the role. AWS WAF checks this permission on `CreateWebACL` and `UpdateWebACL` requests. Without it, the request fails with `AccessDeniedException`, even if the configuration has other errors. A `Disable` configuration names no role, so AWS WAF doesn't check `iam:PassRole` for it.

1. **Check Amazon Bedrock in the Region.** Content assessment calls Amazon Bedrock with your role, so Amazon Bedrock charges and quotas apply to your account. Amazon Bedrock must be available in the Region of your protection pack (web ACL). AWS Security Token Service (AWS STS) must be enabled for your account in that Region. Your Amazon Bedrock quota must accommodate the additional call volume.

1. **Plan your capacity.** The rule group uses 400 WCUs, which count toward the capacity of your protection pack (web ACL). If you add the rule group to a protection pack (web ACL) that already has other rules, check its current capacity first. For capacity limits, see [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md).

## Scope the rule group to your agentic traffic
<a name="waf-ai-security-rg-using-scope"></a>

We recommend that you add a scope-down statement inside the managed rule group statement. Limit evaluation to the paths that serve large language model (LLM), Model Context Protocol (MCP), or Agent2Agent (A2A) traffic. The scope-down statement affects cost and coverage:
+ **Cost.** You pay an additional AWS WAF fee for each request that this rule group evaluates. The `Disable` configuration still incurs this fee. The AI Security and API Security rule groups share the fee, so AWS WAF charges it once for each request, however many of these rule groups evaluate the request. A request that a scope-down statement excludes, or that an earlier rule terminates, isn't evaluated and isn't charged the fee. Content assessment also calls Amazon Bedrock for each assessable message, which adds Amazon Bedrock charges.
+ **Coverage.** The rule group labels traffic that it doesn't recognize with `traffic:not_recognized`, including protocol versions that the rule group doesn't support, such as A2A 0.3. It takes no other action on that traffic. Evaluating non-agentic traffic adds cost and no protection.

Unlike the API Security rule group, this rule group doesn't build a traffic baseline. A scope-down statement doesn't reduce detection quality for the traffic that remains in scope. You can narrow the scope and widen it later without a learning period.

## Order the rule group in your protection pack (web ACL)
<a name="waf-ai-security-rg-using-order"></a>

We recommend that you place the rule group after your IP reputation rules, rate-based rules, and other deterministic rules that cost less to run. AWS WAF then terminates requests that those rules block before they reach a rule group that calls Amazon Bedrock.

Place the rule group before any of your own rules that match its labels. A rule can match only labels that earlier rules added. Your own rules can match request-phase labels only. To act on a response-phase finding, override the rule group's own `Response_` rule.

## Using the rule group more than once
<a name="waf-ai-security-rg-using-multiple"></a>

You can add the rule group to one protection pack (web ACL) more than once, for example with different scope-down statements and rule action overrides. Each instance applies its own scope-down statement and overrides.

AWS WAF assesses content once in each phase. In the request phase, it uses the role of the first instance that evaluates the request. In the response phase, it uses the role of the first instance that inspects responses.

AWS WAF charges the rule group fee once for each request, however many instances evaluate it. Each instance adds its own WCUs to the capacity of the protection pack (web ACL).

## Add the rule group
<a name="waf-ai-security-rg-using-adding"></a>

For the first deployment, both procedures override the rule group's blocking rules to Count: `Compliance_BaselineMCP`, `Compliance_BaselineA2A`, `Request_GuardrailsPromptAttackHighSeverity`, and `Response_GuardrailsPromptAttackHighSeverity`. Do this whatever actions you plan to use later.

**To add the rule group by using the console**

1. Open the AWS WAF console.

1. Choose your protection pack (web ACL).

1. Add the `AWSManagedRulesAISecurityRuleSet` managed rule group from vendor `AWS`.

1. In the **AI Security configuration** pane, turn on **Send inspected traffic to Amazon Bedrock Guardrails**. A newly added rule group starts with this toggle off, which saves the `Disable` configuration. With the toggle on, the console saves `ProtectRequestOnly`. If you chose `Disable`, leave the toggle off and go to step 7.

1. For **Service role**, choose your role or enter its ARN. If you haven't created the role, **Create role** opens the create-role page of the IAM console. The console doesn't create the role for you. For the policies that the role needs, see [The IAM role for AI Security](waf-ai-security-role.md).

1. (Optional) To inspect responses, select **Inspect responses**. This saves the `ProtectRequestAndResponse` configuration. A failure of the response inspection path then returns an error response to your clients. For details, see [How AWS WAF handles messages that it can't assess](waf-ai-security-deploying.md#waf-ai-security-deploying-cantassess).

1. Add a scope-down statement that limits evaluation to your agentic paths.

1. Override the blocking rules to Count.

1. Save the protection pack (web ACL).

**To add the rule group by using the API**

1. In a `CreateWebACL` or `UpdateWebACL` request, add a managed rule group statement for `AWSManagedRulesAISecurityRuleSet` from vendor `AWS`.

1. In `ManagedRuleGroupConfigs`, add one `AWSManagedRulesAISecurityRuleSet` element.

1. In that element, add a `BedrockGuardrails` member and set exactly one of its members: `Disable`, `ProtectRequestOnly`, or `ProtectRequestAndResponse`. If you set none or more than one, the request fails with `WAFInvalidParameterException`.

1. For `ProtectRequestOnly` or `ProtectRequestAndResponse`, set `RoleArn` to the ARN of your role. For details, see [Configuring AI Security](waf-ai-security-configuring.md).

1. Add a scope-down statement that limits evaluation to your agentic paths.

1. Override the blocking rules to Count.

1. Send the request.

## Confirm the configuration took effect
<a name="waf-ai-security-rg-using-confirm"></a>

**To confirm the configuration**

1. Send a representative request to each of your agentic endpoints.

1. In your AWS WAF logs, check that each request has a protocol recognition label.

1. Check that no request has the `guardrails:call_failed` label.

1. Review what the rule group finds over a period that covers your normal traffic patterns.

1. Remove the Count overrides selectively. See [Testing and deploying AWS WAF AI Security](waf-ai-security-deploying.md).

AWS WAF logs show request-phase labels only. For the response phase, use the Amazon CloudWatch response-phase label metrics, such as `BlockedResponses`.

Most configuration mistakes in this rule group don't return an error. If the results aren't what you expect, check the following.

**Content assessment.** If every assessable message is labeled `guardrails:not_assessed` or `guardrails:call_failed`, either AWS WAF isn't reaching Amazon Bedrock or your messages have no content to assess. A `call_failed` label points to your role or your Amazon Bedrock quota. If the reason `service_unavailable` follows `access_denied` or `throttling`, fix the role or the quota first. If you chose `Disable`, you see neither label and no content assessment labels, which is expected.

**Protocol recognition.** If your agentic endpoints produce `traffic:not_recognized`, the rule group doesn't check compliance or assess content for that traffic. Both depend on recognition. MCP traffic is recognized only at protocol versions `2025-06-18`, `2025-11-25`, and `2026-07-28`. A2A traffic is recognized at version 1.0 only.
