---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/quotas.html
---

# Quotas
<a name="quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Quotas for AWS services in this solution
<a name="quotas-for-aws-services-in-this-solution"></a>

Make sure you have sufficient quota for each of the [services implemented in this solution](architecture-details.md#aws-services-in-this-solution). For more information, refer to [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

Use the following links to go to the page for that service. To view the Service Quotas for all AWS services in the documentation without switching pages, view the information in the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information) page in the PDF instead.

## AWS CloudFormation quotas
<a name="aws-cloudformation-quotas"></a>

Your AWS account has AWS CloudFormation quotas that you should be aware of when [launching the stack](deployment.md#step-2) in this solution. By understanding these quotas, you can avoid limitation errors that would prevent you from deploying this solution successfully. For more information, see [AWS CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the *AWS CloudFormation User Guide*.

## Amazon CloudWatch quotas
<a name="aws-cloudwatch-quotas"></a>

Your AWS account has Amazon CloudWatch quotas tied to CloudWatch Resource Policies, which allow only 10 resource policies per Region per account and cannot be increased. For more information, see [Amazon CloudWatch Logs Quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.html) in the *Amazon CloudWatch User Guide*. Before your deployment, check your current usage to ensure you won’t cross this threshold when deploying the solution.

## AWS Organizations
<a name="aws-org-quotas"></a>

The solution’s Lambda functions make calls to the [AWS Organizations API](https://docs.aws.amazon.com/organizations/latest/APIReference/Welcome.html) in order to fetch the alias of the current account to include in messages published to the solution’s SNS topic. This enables human-readable account names to be visible in the solution’s notifications for debugging and tracking purposes.

AWS Organizations imposes limits on how often customers can invoke their API endpoints. If you find that the solution is exceeding the limits set for your account, you can disable the feature that fetches and displays the account alias.

To do this, **navigate to the Lambda function** named `SO0111-ASR-sendNotifications` located in the region and account where you deployed the Admin stack. Then, **locate the environment variable** named `DISABLE_ACCOUNT_ALIAS_LOOKUP` and change the value from "False" to **"True"**. The account alias field in the solution’s notifications will now be *"Unknown"* however this will not impact the functionality of the solution.

## Solution limits and defaults
<a name="solution-limits-and-defaults"></a>

In addition to the AWS service quotas described above, the solution applies its own default limits that are set in the AWS CDK configuration. These are configurable and sit well below the underlying AWS service quotas. They exist as safety floors to contain unexpected load or runaway loops, not as tight per-user quotas. The tables below list the values that differ from the corresponding AWS service default.

| Limit | Solution default | AWS service default |
| --- | --- | --- |
| Amazon API Gateway stage throttle (account-wide) | 500 requests/second steady, 1,000 burst | 10,000 requests/second, 5,000 burst |
| AWS WAF per-user rate limit (60-second window) | 1,000 requests | No default rule |
| AWS WAF per-IP rate limit (60-second window) | 2,000 requests | No default rule |
| AWS WAF sensitive-write rate limit (60-second window) | 300 requests | No default rule |

**Note**
The per-user rate limits aggregate on the caller’s access token; requests without one are covered by the per-IP rule. Requests that exceed an AWS WAF rate-based rule are blocked and receive an HTTP 429 (Too Many Requests) response with a JSON body.

The solution also configures the following CloudWatch alarm thresholds for observability. These alarms notify operators; they do not block requests.

| Alarm | Threshold |
| --- | --- |
| Control state changes | 5 per minute |
| Sensitive writes | 20 per minute |

The following compute and processing defaults apply:

| Limit | Solution default | AWS service default |
| --- | --- | --- |
| Orchestrator (AWS Step Functions) execution timeout | 23 hours | 1 year (maximum) |
| Notification dispatcher Lambda function memory | 256 MB | 128 MB |
| Notification dispatcher Lambda function reserved concurrency | 10 | None (unreserved) |
| Notification dispatcher Lambda function timeout | 30 seconds (60 seconds for webhook delivery) | 3 seconds |
| Amazon SQS message retention | 14 days | 4 days |
| AWS KMS data key reuse period | 60 minutes | 5 minutes |

The solution sets the following data retention (Amazon DynamoDB TTL and Amazon S3) and export limits:

| Item | Solution default |
| --- | --- |
| Findings retention | 8 days |
| Remediation History retention | 365 days |
| Export file retention | 30 days |
| Pre-signed URL validity | 1 day |
| Maximum export time per request | 26,000 milliseconds |
| Maximum records per export | 50,000 |
