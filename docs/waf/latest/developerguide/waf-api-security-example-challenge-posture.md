---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-security-example-challenge-posture.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Challenging clients that produced posture warnings

Posture rules count by default because they describe a weak configuration rather than an attacker, and blocking them would block your own integrations. For human-driven browser traffic, if you want a response stronger than Count but weaker than Block, a Challenge is the middle ground: a real client completes it transparently and an automated client usually doesn't.

This rule challenges browser page requests that carry any posture warning, without touching the attack and reconnaissance stages.

AWS WAF can run a Challenge only in response to a `GET` request that accepts `text/html`. For any other request, such as a `POST` from an SDK, a service, or a script, AWS WAF returns HTTP 202 instead, and a client that isn't a browser can't complete the challenge, so its call fails. The rule therefore also requires the `GET` method and an `Accept` header that contains `text/html`. For more information, see [Best practices for using the CAPTCHA and Challenge actions](waf-captcha-and-challenge-best-practices.md).

If posture warnings come from your own API clients, keep the posture rules at Count and fix the token configuration that causes them.

```json
{
  "Name": "challenge-api-security-posture-warnings",
  "Priority": 113,
  "Statement": {
    "AndStatement": {
      "Statements": [
        {
          "LabelMatchStatement": {
            "Scope": "NAMESPACE",
            "Key": "awswaf:managed:aws:api-security:warning:"
          }
        },
        {
          "ByteMatchStatement": {
            "SearchString": "GET",
            "FieldToMatch": {
              "Method": {}
            },
            "TextTransformations": [
              {
                "Priority": 0,
                "Type": "NONE"
              }
            ],
            "PositionalConstraint": "EXACTLY"
          }
        },
        {
          "ByteMatchStatement": {
            "SearchString": "text/html",
            "FieldToMatch": {
              "SingleHeader": {
                "Name": "accept"
              }
            },
            "TextTransformations": [
              {
                "Priority": 0,
                "Type": "LOWERCASE"
              }
            ],
            "PositionalConstraint": "CONTAINS"
          }
        }
      ]
    }
  },
  "Action": {
    "Challenge": {}
  },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "challenge-api-security-posture-warnings"
  }
}
```
