---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/amazon-cloudwatch-metrics-cost.html
---

# Amazon CloudWatch metrics cost
<a name="amazon-cloudwatch-metrics-cost"></a>

Amazon CloudWatch charges $0.30 per metric per month for the first 10,000 metrics. This solution uses 11 metrics, so the cost for an hour-long stream can be determined by:

11 (number of metrics) \* 1 (hours of streaming) / 720 (hours per month) \* $0.30 = $0.005

For more information about metrics, refer to [Amazon CloudWatch metrics](amazon-cloudwatch-metrics.md).

We recommend creating a [budget](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, refer to the pricing webpages for each AWS service used in this solution.
