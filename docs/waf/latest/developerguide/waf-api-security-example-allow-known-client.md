---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-example-allow-known-client.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Treating a known client more leniently than an unknown one

An identity label indicates that the rule group has already concluded something about this client, which lets you separate a client you recognize from one you don't. In this example, requests from a partner's known IP addresses are allowed ahead of the rule group, so the partner is never blocked by an identity label earned elsewhere.

Identify the partner by something that a client can't set, such as its source IP addresses in an IP set. Don't use a header such as `User-Agent`, because any client can send the same value and skip the rule group.

Place this rule before the API Security rule group, and after any rules that should still apply to the partner, such as rate-based rules. An Allow action ends evaluation of the protection pack (web ACL), so matching requests skip every rule after this one. Requests that this rule allows are also absent from the behavioral baseline.

```json
{
  "Name": "allow-known-partner-before-api-security",
  "Priority": 90,
  "Statement": {
    "IPSetReferenceStatement": {
      "ARN": "arn:aws:wafv2:us-east-1:111111111111:regional/ipset/partner-addresses/33333333-4444-5555-6666-777777777777"
    }
  },
  "Action": {
    "Allow": {}
  },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "allow-known-partner-before-api-security"
  }
}
```
