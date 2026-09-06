---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/solution-quotas.html
---

# Quotas
<a name="solution-quotas"></a>

## Scaling limitations
<a name="scaling-limitations"></a>

Instance Scheduler scales on two primary axes to manage large enterprise deployments:

### Vertical scaling (resources per target)
<a name="vertical-scaling-resources-per-target"></a>

Vertical scaling is bounded by the number of resources that a single Scheduling Request Lambda function can efficiently process within a single scheduling target (account/region/service combination).

Instance Scheduler is designed to be able to handle 1000s of EC2s, 100s of ASGs, and 100s of RDS dbs/clusters in a single [scheduling targets](cost.md#calculating-scheduling-targets) but may be limited by cross-region latency.

To ensure optimal performance, we recommend monitoring the execution time of the Scheduling Request Lambda (see [Operational insights dashboard](monitor-the-solution.md#operational-insights-dashboard)). We recommend keeping average runtime below 90 seconds with a maximum peak time no greater than 4 minutes.

### Horizontal scaling (number of targets)
<a name="horizontal-scaling-number-of-targets"></a>

Horizontal scaling is limited by the number of [active scheduling targets](cost.md#calculating-scheduling-targets) being managed. An active target is an account/region/service combination with at least one actively tagged resource. Instance Scheduler can be deployed to many more accounts and regions, but only targets with actively tagged resources affect performance.

With the default Lambda concurrency quota of 1000, you can run 1000 active targets simultaneously. Lambda queues additional executions automatically, allowing you to scale beyond this limit. We recommend keeping cumulative delay below 3 minutes for optimal performance.

For example, with a 15-second average runtime and lambda concurrency limit of 1000, you can manage up to 12000 active targets while keeping cumulative delay under 3 minutes (3 minutes ÷ 15 seconds × 1000 = 12000 targets).

For larger deployments, you can request a Lambda concurrency quota increase from AWS Support.

## Additional Considerations
<a name="additional-considerations"></a>

 **AWS resource tags**: AWS resources typically have a limit of 50 tags per resource. Instance Scheduler requires 6 informational and control tags for operating the solution. Ensure your resources have sufficient tag capacity to accommodate both Instance Scheduler tags and your existing tagging strategy.

 **Lambda execution limits**: Each Scheduling Request Handler Lambda function has a 5-minute execution timeout.

 **DynamoDB scaling**: The solution uses on-demand scaling for its [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) tables, automatically adjusting capacity based on your workload.

 **API rate limits**: AWS service API throttling may occur with very large deployments. The solution includes retry logic to handle temporary throttling, but excessive throttling may reduce the upper scaling limits of the solution.

## AWS Service Quotas
<a name="aws-service-quotas"></a>

### Service quotas for AWS services
<a name="service-quotas-for-aws-services"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. Make sure you have sufficient quota for each of the services implemented in this solution. For more information, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

### AWS CloudFormation quotas
<a name="aws-cloudformation-quotas"></a>

Your AWS account has AWS CloudFormation quotas that you should be aware of when launching the stack in this solution. By understanding these quotas, you can avoid limitation errors that would prevent you from deploying this solution successfully. For more information, see [AWS CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the *AWS CloudFormation User’s Guide*.

#### AWS Lambda quotas
<a name="aws-lambda-quotas"></a>

Your account has a default AWS Lambda Concurrent Execution quota of 1000. For larger deployments, we recommend deploying Instance Scheduler to a dedicated account to avoid competing with other workloads for Lambda concurrency. This value is adjustable. For more information, refer to [AWS Lambda Getting started guide](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).
