---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-waf-rate-based-rules.html
---

# AWS WAF – Rate-based rules
<a name="aws-waf-rate-based-rules"></a>

 AWS strongly recommends protecting against HTTP request floods by using rate-based rules in AWS WAF to automatically block or challenge requests matching a specific [aggregation key](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-aggregation-options.html) (which is by IP address), when the number of requests received in a configurable sliding window exceed a threshold that you define. Client IP addresses that match the aggregation key will receive an HTTP 403 forbidden response (or custom configured block error response code or body) and remain blocked until request rates drop below the threshold.

 It's recommended to layer rate-based rules to provide enhanced protection so that you have:
+  A blanket rate-based rule to protect your application from large HTTP floods.
+  A rule with a [custom aggregation key](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-aggregation-options.html)—for example Header (Host) \+ URI \+ query string \+ IP—at more restrictive rates than the blanket rate-based rule. This is particularly effective against DDoS because DDoS botnets usually target the same URL repeatedly.
+  A rate-based rule with JA3 or JA4 as an aggregation key to monitor request based on client TLS fingerprints.
+  One or more rate-based rules to protect specific URIs—such as those that are unable to be cached—at more restrictive rates than the blanket rate-based rule.

   For instance, you can choose a blanket rate-based rule (no scope-down statement) with a limit of 500 requests within a 5-minute period, and then create one or more of the following rate-based rules with lower limits than 500 (as low as 10 requests in a 10-minute period) using scope-down statements:
  +  Protect your **web pages** with a scope-down statement such as `if NOT uri_path contains '.'` so that requests for resources without a file extension are further protected. This also protects your homepage (`/`) which is a frequently targeted URI path.
  +  Protect **dynamic endpoints** with a scope-down statement such as `if method exactly matches 'post' (convert lowercase)`.
  +  Protect **heavy requests** that reach your database or invoke a one-time password (OTP) with a scope-down such as `if uri_path starts_with '/login', uri_path starts_with '/signup' or uri_path starts_with '/forgotpassword'`.
  +  Use lower limits for country codes that aren't your target demographic

 Rate-based rules with JA3 and JA4 headers are supported in CloudFront and ALB. Customers have asked for SSL/TLS inspection capabilities and JA3 and JA4 fingerprints to help them analyze unique TLS handshake characteristics in the form of 32 (JA3)- or 36 (JA4)-character hash fingerprint of the TLS Client Hello packet of incoming requests. By using both JA4 and JA3 fingerprinting capabilities, you can implement robust protection against automated threats while maintaining legitimate [traffic flow](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-flow.html) to your applications.

 Also, you can use autonomous system number (ASN)-based rate-limits to control incoming traffic from well-known ASN lists or network vendors from countries where you aren't actively operating.

 Together with IP Reputation rule groups (discussed in the following section), rate-based rules in Block mode are the cornerstone of a defense-in-depth AWS WAF configuration to protect against request floods and are a requirement for [AWS Shield Advanced cost protection](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-request-service-credit.html) requests to be approved.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
