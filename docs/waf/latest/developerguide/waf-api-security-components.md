---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-components.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# AWS WAF API Security components

The main components of an API Security implementation are the following:
+ **`AWSManagedRulesAPISecurityRuleSet`** – The API Security managed rule group, whose rules detect, label, and handle abuse of your APIs. The rule group adds labels to the web requests that it evaluates.
**Note**
You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).

  The rule group detects API abuse in two ways:
  + **Deterministic rules** – Identify JSON Web Token (JWT) attack techniques from the contents of a single request, such as an unsigned token or an injected key identifier. These rules don't require traffic history and take effect from the first request.
  + **Behavioral detections** – Score a client's activity across your endpoints against a learned baseline, and label a request when that activity can't be explained by the baseline. These detections require a baseline window before they produce meaningful results, and they report a confidence level rather than a confirmed attack.

  For details about the rule group's rules and the labels it adds, see [AWS WAF API Security rule group](aws-managed-rule-groups-api-security.md).

  You include this rule group in your protection pack (web ACL) using a managed rule group reference statement. The rule group doesn't have a configuration of its own, so you don't set an inspection level or enable individual detections. For information about adding this managed rule group to your protection pack (web ACL), see [Adding the API Security managed rule group to your protection pack (web ACL)](waf-api-security-rg-using.md).
+ **Client identity** – The identifier that behavioral detections use to track activity. AWS WAF resolves it from the source IP address together with a hash of the request's authentication header. When the request carries no credential that can be hashed, AWS WAF falls back to the source IP address alone. You don't configure this. For information about how client identity affects detection confidence, see [AWS WAF API Security rule group](aws-managed-rule-groups-api-security.md).
+ **Protection pack (Web ACL) dashboard** – The dashboard for your protection pack (web ACL), built on the Amazon CloudWatch metrics that AWS WAF publishes. Use it to see which detections are firing and how often. Because these metrics count requests and matches rather than clients, use your logs to determine how many clients are behind a given count. For more information, see [Monitoring and investigating AWS WAF API Security detections](waf-api-security-monitoring.md).
+ **Events** – A correlated, deduplicated record of security-relevant activity against a protected resource. An event represents related activity, not a single rule match. The rule group labels every match and promotes a subset to an event. Events are available through the AWS WAF API, and they are the primary surface for per-client investigation. For more information, see [Monitoring and investigating AWS WAF API Security detections](waf-api-security-monitoring.md).
+ **Logging and metrics** – You can monitor your API traffic and understand how the API Security managed rule group evaluates and handles it by studying the data that your protection pack (web ACL) collects through AWS WAF logs, Amazon Security Lake, and Amazon CloudWatch. The labels that the rule group adds to your web requests are included in this data. For information about these options, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md), [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md), and [What is Amazon Security Lake?](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html)

## Customization options
<a name="waf-api-security-components-customization"></a>

Depending on your needs and the traffic that you see, you might want to customize your API Security implementation. The following are some of the most commonly used options.
+ **Scope-down statements** – You can exclude traffic from the web requests that the API Security managed rule group evaluates by adding a scope-down statement inside the managed rule group reference statement. A scope-down statement can be any nestable rule statement. When a request doesn't match the scope-down statement, AWS WAF evaluates it as not matching the rule group reference statement without evaluating it against the rule group. For more information about scope-down statements, see [Using scope-down statements in AWS WAF](waf-rule-scope-down-statements.md).

  Your costs for using the API Security managed rule group increase with the number of web requests that AWS WAF evaluates with it. You can help reduce these costs by using a scope-down statement to limit the requests that the rule group evaluates. For example, you might scope evaluation to the path prefix that serves your APIs, so that requests for static content and your web front end aren't evaluated.

  A scope-down statement has an additional effect for this rule group. Because the behavioral detections learn from the traffic they evaluate, traffic you exclude is excluded from behavioral analysis as well as from billing. Scope evaluation to the endpoints you want to protect, rather than to a sample of them.
+ **Labels and label matching rules** – You can customize how the API Security rule group handles the activity that it identifies by using the AWS WAF label match rule statement. The rule group adds labels to your web requests, all beginning with `awswaf:managed:aws:api-security:`. You can add label matching rules after the rule group that match on these labels and apply the handling that you need.

  A namespace match is a raw string prefix match rather than a whole-segment match, so the value you write determines what you catch. The rule group reference page documents the shapes, the full label list, and the cases where a partial namespace value matches more broadly than you might intend. For more information, see [AWS WAF API Security rule group](aws-managed-rule-groups-api-security.md), [Label match rule statement](waf-rule-statement-type-label-match.md), and [Web request labeling in AWS WAF](waf-labels.md).
+ **Custom requests and responses** – You can add custom headers to requests that you allow and send custom responses for requests that you block by pairing label matching with the AWS WAF custom request and response features. With dynamic label interpolation, you can use `${namespace:}` syntax to resolve API Security label values at evaluation time. A single rule can then forward an entire label namespace as a header value instead of requiring one rule for each label. This is a convenient way to pass the detection stage and confidence to your application for logging. For more information about customizing requests and responses, see [Customized web requests and responses in AWS WAF](waf-custom-request-response.md). For information about dynamic interpolation, see [Dynamic label interpolation](waf-dynamic-label-interpolation.md).
