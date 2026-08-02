---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/cost-component.html
---

# Cost component
<a name="cost-component"></a>

 **Workload Discovery on AWS cost component**

![workload discovery cost component](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/images/workload-discovery-cost-component.png)

You can create an AWS CUR in [AWS Billing and Cost Management and Cost Management](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html). This publishes a [Parquet](https://cwiki.apache.org/confluence/display/Hive/Parquet) formatted file to the `CostAndUsageReportBucket` Amazon S3 bucket. The web UI makes requests to the AWS AppSync endpoint that invokes the Cost Lambda function. The function sends predefined queries to Amazon Athena that return estimated cost information from AWS CUR.

Due to the size of the AWS CUR, the responses from Amazon Athena can be very large. The solution stores the results in the `AthenaResultsBucket` Amazon S3 bucket and paginates the results back to the web UI. The [lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) policy configured on this bucket removes items that are more than seven days old.
