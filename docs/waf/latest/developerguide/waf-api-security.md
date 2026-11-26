---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# AWS WAF API Security

This section explains what the API Security managed rule group does.

The API Security managed rule group protects your APIs against attacks that use legitimate, well-formed API calls rather than known exploit signatures. Many API attacks carry no signature at all: an authenticated caller requesting object identifiers that belong to someone else, a caller cycling through stolen credentials until one works, or a caller adding parameters an endpoint never advertised to find a hidden feature. A rule that inspects a single request for a malicious pattern cannot distinguish these from normal use.

The rule group combines two types of detection:
+ **Deterministic rules** inspect the contents of a single request and take effect immediately, with no learning period. They identify JWT attack techniques in the Authorization header, including unsigned tokens, empty signatures, embedded keys or certificate chains, remote key URLs, and path traversal or injection in a key identifier.
+ **Behavioral detections** group a client's requests and score its activity across your endpoints over time. They cover object level authorization abuse, enumeration, credential stuffing, and route and parameter fuzzing.

The rule group labels each request with the detection type, the stage of the activity it observed, and a confidence level.

## Scope and limitations
<a name="waf-api-security-scope"></a>

Keep the following scope and limitations in mind when you use this rule group:
+ **Token structure only** – The rule group identifies attack techniques in a token's structure. It does not verify token signatures. Signature validation remains with your application.
+ **Authorization header only** – The credential stuffing detection reads credentials from the Authorization header only. For credentials submitted in a request body, use AWS WAF Fraud Control account takeover prevention (ATP). For more information, see [AWS WAF Fraud Control account takeover prevention (ATP) rule group](aws-managed-rule-groups-atp.md).
+ **Request inspection only** – The rule group evaluates incoming requests. It does not inspect the content of your application's responses, and it does not detect sensitive data in a response body.
+ **Cross-request behavioral detection** – The behavioral detections judge a client's activity across many requests. A single request for a record the caller does not own is not detected on its own. Checking ownership on each individual request remains with your application.

## Understanding behavioral detections
<a name="waf-api-security-behavioral"></a>

Behavioral detections are risk indicators, not confirmed attacks. A behavioral detection means that a client's activity deviated from the established pattern for the endpoints it accessed, in a combination that the rule group could not explain through normal use. It does not mean that an attack has been confirmed. Use a detection as evidence to investigate or to act on according to your own risk tolerance.

The behavioral detections score traffic against a baseline that AWS WAF establishes for each protected resource. Plan for approximately one day of typical traffic before the first baseline is available. Expect the behavioral detections to become more accurate over the first one to two weeks.

A client that AWS WAF can identify only by IP address is never reported at high confidence, so the behavioral rules count rather than block such clients by default.

We recommend that you validate the rule group against your own traffic before you enforce. For guidance, see [Testing and deploying AWS WAF API Security](waf-api-security-deploying.md).

## How behavioral detections work
<a name="waf-api-security-behavioral-how"></a>

Behavioral detections depend on a baseline that the rule group establishes for each protected resource. The rule group learns the normal pattern of activity for each API pattern it observes, then raises a detection when a client's activity deviates from that pattern in a way that cannot be explained by normal use.

## Confidence levels
<a name="waf-api-security-confidence"></a>

A detection requires several independent kinds of evidence to agree, not a single measurement. The confidence level reflects how much benign activity the combination of evidence ruled out, rather than how closely the traffic resembles a known attack.
+ **High** – Rules out the known benign explanations. Defaults to Block.
+ **Medium** – Leaves at least one benign explanation that fits. Defaults to Count.
+ **Low** – Rules out none of the benign explanations. Defaults to Count.

## Client identification
<a name="waf-api-security-client-id"></a>

High confidence also requires that AWS WAF can identify the caller beyond its IP address alone.

AWS WAF identifies a client by its source IP address together with a hash of the request's authentication header. When a request carries no credential that can be hashed, AWS WAF falls back to the source IP address alone. A finding that would otherwise qualify as high confidence is reported as medium for a client identified only by IP address, so the behavioral rules never block requests from clients that do not authenticate.

## Baseline learning period
<a name="waf-api-security-baseline"></a>

AWS WAF establishes the baseline for each protected resource and refreshes it automatically as traffic arrives. Plan for approximately one day of typical traffic before the first baseline is available. Expect the behavioral detections to become more accurate over the first one to two weeks. The deterministic JWT rules don't require a baseline and take effect immediately, so they provide protection from the first day.

Plan for this ramp-up period. Add the rule group with its behavioral detections set to count, let the baseline establish on your own traffic, review what the rule group detected, and then decide what to enforce. For guidance, see [Testing and deploying AWS WAF API Security](waf-api-security-deploying.md).

## Supported resources and protocols
<a name="waf-api-security-supported"></a>

AWS WAF API Security is available in all AWS Regions where AWS WAF is available, except the AWS GovCloud (US) Regions, the China Regions, and the AWS European Sovereign Cloud.

API Security is available for protection packs (web ACLs) that protect the following resource types:
+ Amazon CloudFront distributions
+ Application Load Balancers
+ Amazon API Gateway REST APIs

The rule group doesn't support the other resource types that AWS WAF protects. It is not available for AWS AppSync GraphQL APIs, Amazon Cognito user pools, AWS App Runner services, Amazon Bedrock AgentCore Gateways, AWS Verified Access instances, Elastic Load Balancing for Envoy proxies, or AWS Amplify apps.

The rule group only supports REST APIs. It does not support other API types such as WebSockets or stream mode.

If you add this rule group to a protection pack (web ACL) and then try to associate the protection pack (web ACL) with an unsupported resource type, AWS WAF rejects the association.

For the resource types that AWS WAF supports generally, see [Resources that you can protect with AWS WAF](how-aws-waf-works-resources.md).

## Managing the cost of API Security
<a name="waf-api-security-cost"></a>

You are charged an additional fee for the requests that this rule group evaluates. Use a scope-down statement inside the managed rule group statement to limit evaluation to the paths and methods that serve your APIs. This reduces both the cost of the rule group and the volume of traffic it analyzes.

Narrowing the scope involves a trade-off. A scope-down statement also reduces what the rule group can baseline, because traffic you exclude is excluded from behavioral analysis as well as from billing. Scope to the endpoints you want to protect, rather than to a sample of them.

**Note**
You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).

**Note**
API Security isn't available for every resource type that AWS WAF protects. For the list, see [Supported resources and protocols](#waf-api-security-supported).

**Important**
API Security uses multiple detection techniques, including behavioral analysis and statistical comparison against learned baselines, to identify and categorize API activity. These methods are designed to produce high-confidence detections, but they are probabilistic and might not correctly identify or categorize all API abuse in all cases. We continuously test and update our analysis methods to increase accuracy. We recommend running the behavioral detections in count mode to validate that they produce the results you expect on your own traffic before you enforce them.

## Labels and metrics
<a name="waf-api-security-labels-metrics"></a>

When AWS WAF evaluates a web request against the API Security managed rule group, it labels requests where it detects API abuse. Labels carry the stage of the activity and, for a detection, its type and confidence level. The rule group also labels the client itself once it has detected an issue, so your own rules can act on that client's later requests to any of your endpoints. You can match against these labels in your own AWS WAF rules to customize handling.

The labels that the API Security managed rule group generates are included in Amazon CloudWatch metrics and in your protection pack (web ACL) logs.

## AWS Firewall Manager support
<a name="waf-api-security-fms"></a>

AWS Firewall Manager AWS WAF policies don't support the API Security managed rule group. You can use AWS Network Security Manager or add the rule group to each protection pack (web ACL) directly.

For more information about the API Security managed rule group, see [AWS WAF API Security rule group](aws-managed-rule-groups-api-security.md).

**Topics**
+ [Scope and limitations](#waf-api-security-scope)
+ [Understanding behavioral detections](#waf-api-security-behavioral)
+ [How behavioral detections work](#waf-api-security-behavioral-how)
+ [Confidence levels](#waf-api-security-confidence)
+ [Client identification](#waf-api-security-client-id)
+ [Baseline learning period](#waf-api-security-baseline)
+ [Supported resources and protocols](#waf-api-security-supported)
+ [Managing the cost of API Security](#waf-api-security-cost)
+ [Labels and metrics](#waf-api-security-labels-metrics)
+ [AWS Firewall Manager support](#waf-api-security-fms)
+ [AWS WAF API Security components](waf-api-security-components.md)
+ [Adding the API Security managed rule group to your protection pack (web ACL)](waf-api-security-rg-using.md)
+ [Testing and deploying AWS WAF API Security](waf-api-security-deploying.md)
+ [Monitoring and investigating AWS WAF API Security detections](waf-api-security-monitoring.md)
+ [Example scenarios of false positives with AWS WAF API Security](waf-api-security-false-positives.md)
+ [AWS WAF API Security examples](waf-api-security-examples.md)
