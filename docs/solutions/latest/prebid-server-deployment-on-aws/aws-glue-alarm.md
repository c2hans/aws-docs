---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/aws-glue-alarm.html
---

# AWS Glue
<a name="aws-glue-alarm"></a>

## Glue job failure
<a name="glue-job-failure"></a>
+ The alarm changes state if the metrics ETL Glue job reports any errors within a 1-minute period.
+ Check the job run details in the AWS Glue console and the job’s CloudWatch logs to find the cause of the failure.
+ Metric: `glue.error.ALL` > 0
