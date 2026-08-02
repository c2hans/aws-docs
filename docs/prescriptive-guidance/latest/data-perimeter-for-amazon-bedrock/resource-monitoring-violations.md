---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/resource-monitoring-violations.html
---

# Monitoring violations
<a name="resource-monitoring-violations"></a>

## Control objective
<a name="control-objective.ff1f83dc-a00a-5fa1-b373-3505c4ae537a"></a>

***Resource perimeter**** – My identities can access only trusted resources*

Continuous monitoring detects unauthorized access attempts and policy violations. Use CloudWatch alarms to alert on access denials that indicate attempts to bypass organizational boundaries or access restricted resources.

**Monitor unauthorized API calls:**

```
{
  "CloudWatchAlarms": [
    {
      "AlarmName": "UnauthorizedS3Access",
      "MetricName": "UnauthorizedAPICallsCount",
      "Threshold": 1,
      "ComparisonOperator": "GreaterThanOrEqualToThreshold",
      "AlarmActions": [
        "arn:aws:sns:us-east-1:123456789012:security-alerts"
      ]
    }
  ]
}
```

**Policy explanation:**
+ **UnauthorizedS3Access alarm** – Triggers immediate alerts when unauthorized API calls are detected, enabling rapid response to potential resource perimeter violations or data exfiltration attempts

**Key events to monitor:**
+ *Access denied* errors with `PrincipalOrgID` or `ResourceOrgID `conditions (organizational boundary violations)
+ AWS KMS decrypt failures (encryption perimeter violations)
+ Amazon S3 `PutObject/GetObject` denials (data exfiltration attempts)
+ Resource policy changes (potential weakening of perimeter controls)
