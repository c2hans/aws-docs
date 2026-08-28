---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used to run the Automated Forensics Orchestrator for Amazon EC2 and EKS Guidance. As of the recent revision, the monthly cost for running this Guidance with the default settings in the US East (N. Virginia) AWS Region is approximately **$235 assuming an average of one forensic instance is 50% utilized for performing forensic analysis** with 512GB of volume attached to the instance. Prices are subject to change. For full details, refer to the pricing page for each AWS service used in this Guidance.

The total cost to run this Guidance depends on the following factors:
+ The number of forensic incidents reported
+ The frequency of forensic orchestration
+ The Guidance assumes a forensic instance runs 12 hours a day

This Guidance uses the following AWS components, which incur a cost based on your configuration.

| Service | Usage estimate | Monthly cost (USD) |
| --- | --- | --- |
|  **AWS Step Functions**  | Workflow requests (10 per day), State transitions per workflow (20) | $1 |
|  **Amazon CloudWatch**  | Number of Metrics (includes detailed and custom metrics) (20)<br />Number of Custom/Cross-account events (100,000) Number of Dashboards (1)<br />Number of Standard Resolution Alarm Metrics (20)<br />Number of High-Resolution Alarm Metrics (20)<br />Number of Canary runs (5)<br />Number of Lambda functions (10)<br />Number of requests per function (5 per day)<br />Number of Contributor Insights rules for DynamoDB (5) Total number of events for DynamoDB (1 million events per month)<br />Total number of matched log events for CloudWatch (1 million matched log events per month)<br />Number of Contributor Insights rules for CloudWatch (5) Standard Logs: Data Ingested (1 GB)<br />Logs Delivered to S3: Data Ingested (1 GB) | $47 |
|  **Amazon DynamoDB**  | Average item size (all attributes) (20 KB)<br />Data storage size (0.5 GB) | $26 |
|  **Amazon Simple Notification Service (SNS)**  | DT Inbound: Not selected (0 TB per month)<br />DT Outbound: Not selected (0 TB per month)<br />Requests (100,000 per month)<br />HTTP/HTTPS Notifications (100,000 per month) EMAIL/EMAIL-JSON Notifications (100,000 per month) SQS Notifications (100,000 per month)<br />AWS Lambda (1 million per month) | $2 |
|  **Amazon EC2**  | Operating system (Linux)<br />Quantity (1)<br />Pricing strategy (On-Demand Instances)<br />Storage amount (100 GB)<br />Instance type (`M5.2Xlarge`) - OnDemand based on the forensic analysis performed - Currently we are leveraging Ubuntu Server 20.04 LTS (HVM) SSD Volume Type | $142 |
|  **AWS Lambda**  | 10,000 requests, 60 seconds per lambda function, 512MB of Memory | $10 |
|  **AWS KMS Key**  | 1 KMS key, 1,990,000 requests (2,010,000 total requests - 20,000 free tier requests) x $0.03 / 10,000 requests | $7 |
|  |  **Total**  |  **\~$235 USD/ month**  |

\*average usage cost of Amazon EC2

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Forensics Orchestrator for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
