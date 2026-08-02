---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/logging.html
---

# Logging
<a name="logging"></a>

The Log Archive account serves as a centralized repository for aggregating logs of API activities (by using AWS CloudTrail) and resource configurations (by using AWS Config) across all accounts within the landing zone. Furthermore, you can centralize other logs from across your organization, such as Amazon CloudWatch, Amazon S3 access logs, and VPC Flow Logs, in this account. The Log Archive account seamlessly integrates with AWS Control Tower to automatically capture and record actions and events. This includes actions initiated from both the management account and member accounts. For comprehensive guidance, see [Logging and monitoring in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/logging-and-monitoring.html) in the AWS Control Tower documentation.

Centralized logging in AWS Control Tower provides numerous benefits, including:
+ Integration of security services to audit the logs and automate alerts and remediations
+ Adherence to compliance and regulatory standards that require you to keep a record of all activities in your environment
+ Centralized visibility into all activities across accounts to enable rapid troubleshooting and aid in forensic analysis during security incidents
+ Support for growing log volumes and cost-effective, long-term storage solutions

**Note**
To further enhance your centralized logging solution, you can use AWS solutions such as [Centralized Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/), which provides capabilities to ingest, process, and visualize both application logs and AWS service logs.

The following table provides an overview of the logs that you can set up for your landing zone, as an example of a table that you can use in your landing zone design document. You can extend this table with additional log solutions according to your landing zone requirements. For more guidance about the security logs to include in the Log Archive account, see the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html).

|
|
| Logging service | Description | Build approach | Location |
| --- |--- |--- |--- |
| AWS CloudTrail** **and AWS Config | AWS Config logs configuration activity  in the resources it supports. CloudTrail logs API calls, console access, and logins. Logs from all accounts are aggregated in the Log Archive account. | Automatically enabled and set up by AWS Control Tower for all accounts in the landing zone. | S3 bucket in the Log Archive account. |
| Amazon CloudWatch | CloudWatch monitors resources and applications in the environment in real time. CloudWatch collects and tracks metrics for resources and applications. | We recommend that you set up CloudWatch for all required AWS resources. | S3 bucket configuration details are provided with the workloads. |
| Amazon S3 access logs | Amazon S3 access logging provides detailed records for requests made to an S3 bucket. AWS Control Tower automatically sets up Amazon S3 access logging in the S3 bucket for CloudTrail and AWS Config.<br />For information about Amazon S3 access logging, see [Logging requests using server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html) in the Amazon S3 documentation. | Automatically enabled and set up by AWS Control Tower in the S3 bucket for CloudTrail and AWS Config. | S3 bucket in the Log Archive account. |
| Elastic Load Balancing (ELB) access logs | ELB access logs capture detailed information about requests sent to your load balancer. These logs can be collected in all member accounts that have load balancers and centralized in the Log Archive bucket.<br />For more information about ELB access logging, see [Access logs for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-access-logs.html) and [Access logs for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html) in the ELB documentation. | We recommend that you set up access logs for all ELB resources. | S3 bucket in the Log Archive account. |
| VPC Flow Logs | VPC Flow Logs captures information about IP traffic going to and from network interfaces in the VPC. These logs are locally stored in each member account and can be used for troubleshooting and analysis.<br />For more information about this feature, see [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) in the Amazon VPC documentation. | We recommend that you use an CloudFormation script to enable VPC Flow Logs when you set up a VPC in each account. | Locally sent to CloudWatch in each account. The retention period for these logs should be three days. |
