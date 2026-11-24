---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-example-call-failed-alarm.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Alarming on failed Amazon Bedrock calls

By default, a failed call to Amazon Bedrock doesn't change how AWS WAF handles the message. The following Amazon CloudWatch alarm reports these failures, for example when the AWS Identity and Access Management (IAM) role lacks a permission.

```json
{
  "AlarmName": "AISecurity-GuardrailsCallFailed",
  "Metrics": [
    {
      "Id": "allowed",
      "ReturnData": false,
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/WAFV2",
          "MetricName": "AllowedRequests",
          "Dimensions": [
            { "Name": "WebACL", "Value": "my-protection-pack" },
            { "Name": "Region", "Value": "us-east-1" },
            { "Name": "LabelNamespace", "Value": "awswaf:managed:aws:ai-security:guardrails" },
            { "Name": "LabelName", "Value": "call_failed" }
          ]
        },
        "Period": 300,
        "Stat": "Sum"
      }
    },
    {
      "Id": "blocked",
      "ReturnData": false,
      "MetricStat": {
        "Metric": {
          "Namespace": "AWS/WAFV2",
          "MetricName": "BlockedRequests",
          "Dimensions": [
            { "Name": "WebACL", "Value": "my-protection-pack" },
            { "Name": "Region", "Value": "us-east-1" },
            { "Name": "LabelNamespace", "Value": "awswaf:managed:aws:ai-security:guardrails" },
            { "Name": "LabelName", "Value": "call_failed" }
          ]
        },
        "Period": 300,
        "Stat": "Sum"
      }
    },
    {
      "Id": "callfailed",
      "Expression": "FILL(allowed, 0) + FILL(blocked, 0)",
      "Label": "Requests with guardrails:call_failed",
      "ReturnData": true
    }
  ],
  "EvaluationPeriods": 2,
  "Threshold": 1,
  "ComparisonOperator": "GreaterThanOrEqualToThreshold",
  "TreatMissingData": "notBreaching"
}
```

The alarm enters the `ALARM` state when the `guardrails:call_failed` label is added in each of two consecutive 5-minute periods.

The alarm adds two label metrics because AWS WAF counts a label under the metric for the final action on the request: `AllowedRequests` when AWS WAF allows the request and `BlockedRequests` when it blocks it. If other rules in your protection pack (web ACL) use a CAPTCHA or Challenge action, also add `CaptchaRequests` and `ChallengeRequests`. The alarm doesn't use `CountRuleMatch`. AWS WAF doesn't publish rule match metrics for AI Security labels.

AWS WAF splits a label at its last colon to form the metric dimensions. The part before the last colon, without a trailing colon, is `LabelNamespace`. The last element is `LabelName`. An alarm must name every dimension of the metric.

Replace `my-protection-pack` with the name of your protection pack (web ACL). For a protection pack (web ACL) that protects an Amazon CloudFront distribution, omit the `Region` dimension.

This alarm covers request-phase call failures. Response-phase call failures are published under `AllowedResponses`, `BlockedResponses`, and `CountedResponses`. To alarm on them, create the same alarm with these three metrics in place of `AllowedRequests` and `BlockedRequests`, and add all three in the expression.
