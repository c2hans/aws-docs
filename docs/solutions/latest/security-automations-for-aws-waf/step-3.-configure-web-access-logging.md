---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/step-3.-configure-web-access-logging.html
---

# Step 3. Configure web access logging
<a name="step-3.-configure-web-access-logging"></a>

Configure CloudFront or your ALB to send web access logs to the appropriate Amazon S3 bucket so that this data is available for the Log Parser Lambda function.

## Store web access logs from a CloudFront distribution
<a name="store-web-access-logs-from-a-cloudfront-distribution"></a>

1. Sign in to the [Amazon CloudFront console](https://console.aws.amazon.com/cloudfront/).

1. Select your web application’s distribution, and choose **Distribution Settings.**

1. On the **General** tab, choose **Edit**.

1. For **AWS WAF Web ACL**, choose the web ACL solution created (the **Stack name** parameter).

1. For **Logging**, choose **On**.

1. For **Bucket for Logs**, choose the S3 bucket that you want to use for storing web access logs. This can be a new or existing S3 bucket that is used in the main stack and has permission for CloudFront to write logs. The drop-down list enumerates the buckets associated with the current AWS account. For more information, see [Getting started with a basic CloudFront distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.SimpleDistribution.html) in the *Amazon CloudFront Developer Guide*.

1. Set the log prefix to the prefix used for deploying the solution. You can find the prefix in the main stack, **Parameters** tab, **AppAccessLogBucketPrefixParam** (default `AWSLogs/`).

1. Choose **Yes, edit** to save your changes.

For more information, refer to [Configuring and using standard logs (access logs)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) in the *Amazon CloudFront Developer Guide*.

## Store web access logs from an Application Load Balancer
<a name="store-web-access-logs-from-an-application-load-balancer"></a>

1. Sign in to the [Amazon Elastic Compute Cloud (Amazon EC2) console](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Load Balancers**.

1. Select your web application’s ALB.

1. On the **Description** tab, choose **Edit attributes**.

1. Choose **Enable access logs**.

1. For **S3 location**, type the name of the S3 bucket that you want to use for storing web access logs. This can be a new or existing S3 bucket that is used in the main stack and has permission for Application Load Balancer to write logs.

1. Set the log prefix to the prefix used for deploying the solution. You can find the prefix in the main stack, **Parameters** tab, **AppAccessLogBucketPrefixParam** (default `AWSLogs/`).

1. Choose **Save**.

For more information, refer to [Access Logs for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html) in the *Elastic Load Balancing User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Automations for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
