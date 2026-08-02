---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/identity-monitoring-violations.html
---

# Monitoring violations
<a name="identity-monitoring-violations"></a>

## Control objective
<a name="control-objective.fa4d9191-4823-5aa4-af69-dd804d25a253"></a>

***Identity perimeter**** – Only trusted identities can access my resources*

Set up Amazon CloudWatch alarms and EventBridge rules to detect identity perimeter violations by creating an EventBridge rule that monitors AWS CloudTrail events for failed Amazon Bedrock API calls:

```
# Create EventBridge rule to detect unauthorized Bedrock access attempts
aws events put-rule \
  --name BedrockUnauthorizedAccess \
  --description "Alert on unauthorized Bedrock access attempts" \
  --event-pattern '{
    "source": ["aws.bedrock"],
    "detail-type": ["AWS API Call via CloudTrail"],
    "detail": {
      "eventName": ["InvokeModel", "InvokeModelWithResponseStream"],
      "errorCode": ["AccessDenied", "UnauthorizedOperation"]
    }
  }'

# Configure SNS target for security alerts
aws events put-targets \
  --rule BedrockUnauthorizedAccess \
  --targets '[{"Id":"1","Arn":"arn:aws:sns:us-east-1:123456789012:security-alerts"}]'
```

**Event pattern (for reference):**

```
{
  "source": ["aws.bedrock"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventName": ["InvokeModel", "InvokeModelWithResponseStream"],
    "errorCode": ["AccessDenied", "UnauthorizedOperation"]
  }
}
```

**Policy explanation:**
+ **Event pattern** – Detects failed Amazon Bedrock API calls that indicate potential identity perimeter violations, triggering alerts when unauthorized access attempts occur.
