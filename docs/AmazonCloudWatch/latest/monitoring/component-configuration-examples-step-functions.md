---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-step-functions.html
---

# AWS Step Functions
<a name="component-configuration-examples-step-functions"></a>

The following example shows a component configurations in JSON format for AWS Step Functions.

```
{
  "alarmMetrics": [
    {
      "alarmMetricName": "ExecutionsFailed",
      "monitor": true
    },
    {
      "alarmMetricName": "LambdaFunctionsFailed",
      "monitor": true
    },
    {
      "alarmMetricName": "ProvisionedRefillRate",
      "monitor": true
    }
  ],
  "logs": [
    {
     "logGroupName": "/aws/states/HelloWorld-Logs",
      "logType": "STEP_FUNCTION",
      "monitor": true,
    }
  ]
}
```
