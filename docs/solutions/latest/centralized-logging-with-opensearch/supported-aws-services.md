---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/supported-aws-services.html
---

# Supported AWS services
<a name="supported-aws-services"></a>

Most of the supported AWS services output logs to Amazon CloudWatch Logs, Amazon S3, Amazon Kinesis Data Streams, or Amazon Kinesis DataFirehose. The log outputs must be in the same AWS Region as the Centralized Logging with OpenSearch solution.

The following table lists the supported AWS services and the supported log analytics engines.

| AWS Service | Log Type | OpenSearch Engine Support | Light Engine Support |
| --- | --- | --- | --- |
| AWS CloudTrail | N/A | Yes | Yes |
| Amazon S3 |  [Access logs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html)  | Yes | No |
| Amazon RDS/Aurora |  [MySQL Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.LogFileSize.html)  | Yes | Yes |
| Amazon CloudFront |  [Standard access logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html)  | Yes | Yes |
| Application Load Balancer |  [Access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html)  | Yes | Yes |
| AWS WAF |  [Web ACL logs](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html)  | Yes | Yes |
| AWS Lambda | N/A | Yes | No |
| Amazon VPC |  [Flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)  | Yes | Yes |
| AWS Config | N/A | Yes | No |

The solution supports detects the log location of the resource automatically, reads the logs, and then ingests them into the log analytics engines. The solution also provides dashboard templates for all supported AWS service. It automatically ingests logs into the log analytics engine. You can go to the OpenSearch Dashboards or Grafana to view the dashboards after the pipeline being provisioned.

In this chapter, you will learn how to create log ingestion and dashboards for the following AWS services:
+  [AWS CloudTrail](aws-cloudtrail-logs.md)
+  [Amazon S3](amazon-s3-logs.md)
+  [Amazon RDS/Aurora](amazon-rdsaurora-logs.md)
+  [Amazon CloudFront](amazon-cloudfront-logs.md)
+  [AWS Lambda](aws-lambda-logs.md)
+  [Application Load Balancer](application-load-balancer-application-load-balancer-logs.md)
+  [AWS WAF](aws-waf-logs.md)
+  [Amazon VPC](vpc-flow-logs.md)
+  [AWS Config](aws-config-logs.md)
