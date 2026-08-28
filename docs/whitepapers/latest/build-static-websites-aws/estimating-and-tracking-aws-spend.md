---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/estimating-and-tracking-aws-spend.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Estimating and tracking AWS spend
<a name="estimating-and-tracking-aws-spend"></a>

 With AWS, there is no upper limit to the amount of Amazon S3 storage or network bandwidth you can consume. You pay as you go and only pay for actual usage.

 Because you’re not using web servers in this architecture, you have no licensing costs or concern for server scalability or utilization.

## Estimating AWS spend
<a name="estimating-aws-spend"></a>

 To estimate your monthly costs, you can use the [AWS Simple Monthly Calculator](https://calculator.s3.amazonaws.com/index.html). Pricing sheets for Amazon Route 53, Amazon S3, and Amazon CloudFront are available [online](https://aws.amazon.com/pricing/). (Any pricing information included in this document is provided only as an estimate of usage charges for AWS services based on the prices effective at the time of this writing. Monthly charges will be based on your actual use of AWS services, and may vary from the estimates provided.)

 AWS pricing is Region specific. See the following links for the most recent pricing information: [Amazon Route 53](https://aws.amazon.com/route53/pricing/), [Amazon CloudFront](https://aws.amazon.com/cloudfront/pricing/), [Amazon S3](https://aws.amazon.com/s3/pricing/).

## Tracking AWS spend
<a name="tracking-aws-spend"></a>

 The [AWS Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-explorer-what-is.html) can help you track cost trends by service type. It’s integrated in the AWS Billing and Cost Management console and runs in your browser. The Monthly Cost by Service chart allows you to see a detailed breakdown by service. The Daily Cost report helps you track your spending as it happens. If you configured tags for your Amazon S3 bucket, you can filter your reports against specific tags for [cost allocation](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketBilling.html) purposes. See [Using the Default Cost Explorer Reports](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-default-reports.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
