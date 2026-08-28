---
source_url: https://docs.aws.amazon.com/frauddetector/latest/ug/uploading-event-data-to-an-s3-bucket.html
---

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Store your event data externally with Amazon S3
<a name="uploading-event-data-to-an-s3-bucket"></a>

If you are training an Online Fraud Insights model, you can choose to store your event data externally with Amazon S3. To store your event data in Amazon S3 you must first create a text file in CSV format, add your event data, and then upload the CSV file to an Amazon S3 bucket.

**Note**
The **Transaction Fraud Insights** and **Account Takeover Insights** model types do not support datasets stored externally with Amazon S3

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
