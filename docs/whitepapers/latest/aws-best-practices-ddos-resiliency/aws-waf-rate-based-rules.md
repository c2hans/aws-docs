---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-waf-rate-based-rules.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS WAF – Rate-based rules
<a name="aws-waf-rate-based-rules"></a>

 AWS strongly recommends protecting against HTTP request floods by using the rate-based rules in AWS WAF to automatically block IP addresses of bad actors when the number of requests received in a 5-minute sliding window exceed a threshold that you define. Offending client IP addresses will receive a 403 forbidden response (or configured block error response) and remain blocked until request rates drop below the threshold.

 It’s recommended to layer rate-based rules to provide enhanced protection so that you have:
+  A blanket rate-based rule to protect your application from large HTTP floods.
+  One or more rate-based rules to protect specific URIs at more restrictive rates than the blanket rate-based rule.

 For instance you may choose a blanket rate-based rule (no scope-down statement) with a limit of 500 requests within a 5-minute period, and then create one or more of the following rate-based rules with lower limits than 500 (as low as 100 requests in a 5-minute period) using scope-down statements:
+  Protect your **web pages** with a scope-down statement like "`if NOT uri_path contains '.'`" so that requests for resources without a file extension are further protected. This also protects your homepage (`/`) which is a frequently targeted URI path.
+  Protect **dynamic endpoints** with a scope-down statement like "`if method exactly matches 'post' (convert lowercase)`"
+  Protect **heavy requests** that reach your database or invoke a one-time password (OTP) with a scope-down like "`if uri_path starts_with '/login' OR uri_path starts_with '/signup' OR uri_path starts_with '/forgotpassword'`"

 Rate-based in "Block" mode are the cornerstone of your defense-in-depth WAF configuration to protect against request floods and are a requirement for AWS Shield Advanced cost protection requests to be approved. We’ll examine additional defense-in-depth WAF configurations in the following sections.
