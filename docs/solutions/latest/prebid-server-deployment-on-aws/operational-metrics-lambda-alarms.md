---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/operational-metrics-lambda-alarms.html
---

# Operational metrics Lambda function

## Errors and throttles
<a name="operational-metrics-lambda-errors"></a>
+ The solution creates two alarms for the custom resource Lambda function that manages anonymized operational metrics collection. One alarm changes state if the function reports errors, and the other changes state if the function is throttled, within a 1-minute period.
+ Check the function’s CloudWatch logs to find the cause of the errors.
+ Metric: `Errors` >= 1, `Throttles` >= 1
