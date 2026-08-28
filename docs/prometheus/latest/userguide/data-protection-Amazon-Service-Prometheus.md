---
source_url: https://docs.aws.amazon.com/prometheus/latest/userguide/data-protection-Amazon-Service-Prometheus.html
---

# Data collected by Amazon Managed Service for Prometheus
<a name="data-protection-Amazon-Service-Prometheus"></a>

Amazon Managed Service for Prometheus collects and stores operational metrics that you configure to be sent from Prometheus servers running in your account to Amazon Managed Service for Prometheus. This data includes the following:
+ Metric values
+ Metric labels (or arbitrary key-value pairs) that help identify and classify data
+ Timestamps for data samples

Unique tenant IDs isolate data from different customers. These IDs limit what customer data is accessible. Customers can't change tenant IDs.

Amazon Managed Service for Prometheus encrypts the data that it stores with AWS Key Management Service (AWS KMS) keys. Amazon Managed Service for Prometheus manages these keys.

**Note**
Amazon Managed Service for Prometheus supports the creation of customer managed keys for encrypting your data. For more information about the keys that Amazon Managed Service for Prometheus uses by default, and how to use your own customer managed keys, see [Encryption at rest](encryption-at-rest-Amazon-Service-Prometheus.md).

Data in transit is encrypted with HTTPS automatically. Amazon Managed Service for Prometheus secures connections between Availability Zones within an AWS Region using HTTPS internally.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
