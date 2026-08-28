---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/monitoring.html
---

# Monitoring the solution post-deployment
<a name="monitoring"></a>

After deploying the solution, we recommend continuously monitoring the solution’s resources using Amazon CloudWatch alarms and metrics.

## Setting up CloudWatch alarms
<a name="recommended-cloudwatch-alarms"></a>

You can set up [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) to monitor key metrics and receive notifications when thresholds are exceeded. Consider setting up alarms for the following resources:

 **Amazon CloudFront distribution metrics**

Monitor CloudFront distribution performance and errors. For more information, refer to [CloudFront distribution metrics](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/programming-cloudwatch-metrics.html) in the *Amazon CloudFront Developer Guide*.

 **Amazon API Gateway metrics**

Monitor API request rates, latency, and errors. For more information, refer to [Amazon API Gateway dimensions and metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html) in the *Amazon API Gateway Developer Guide*.

 **AWS Lambda function metrics**

Monitor Lambda function invocations, duration, errors, and throttles for the solution’s microservices.

 **Amazon ECS and AWS Fargate metrics**

Monitor task CPU and memory utilization during load tests to ensure adequate resources.

 **Amazon DynamoDB metrics**

Monitor read and write capacity consumption, throttled requests, and latency.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Distributed Load Testing on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
