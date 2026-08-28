---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running this solution. As of this revision, the estimated cost for running this solution with default settings in the US East (N. Virginia) Region and assuming that you are migrating 200 servers a month with this solution is approximately **$14.31 per month**. The cost for running this solution depends on the amount of data being loaded, requested, stored, processed, and presented as shown in the following table.

| AWS service | Factors | Cost/month [USD] |
| --- | --- | --- |
|  **Core services**  |  |  |
| Amazon API Gateway | 10,000 requests/month x ($3.50/million) | $0.035 |
| AWS Lambda | 10,000 invocations/month<br />(avg 3,000 ms duration and 128 MB memory) | $0.065 |
| Amazon DynamoDB | 20,000 write requests/month x ($1.25/million)<br />40,000 read requests/month x ($0.25/million)<br />Data storage: 1 GB x $0.25 | $0.035 |
| Amazon S3 | Storage (10MB) & 50,000 get requests/month | $0.25 |
| Amazon CloudFront | Regional data transfer out to internet: first 10 TB<br />Regional data transfer out to origin: all data transfer<br />HTTPS requests:<br />50,000 requests/month X ($0.01/10,000 requests) | $0.92 |
| AWS Systems Manager | 10,000 steps/month | $0.00 |
| AWS Secrets Manager | 5 secrets x 30 days duration | $2.00 |
| Amazon Cognito (direct sign-in) | Up to 50,000 monthly active users (MAUs) covered by AWS Free Tier | $0.00 |
| Amazon Athena | 10MB daily x $5.00 per TB of data scanned | $0.0015 |
|  **Optional services**  |  |  |
| AWS Glue (optional migration tracker) | 2 mins daily x Default 10 DPU x $0.44 per DPU-Hour | $4.40 |
| AWS WAF | 2 Web ACLs $5.00 per month (prorated hourly)2 Rules $1.00 per month (prorated hourly)<br />10,000 requests x ($0.60 per 1 million requests) | $6.60 |
| Amazon Cognito (SAML sign-in) | Up to 50 MAUs covered by AWS Free TierAbove 50 MAUs, $0.015/MAU | $0.00 |
|  |  **Total:**  |  **\~$14.31/month**  |

## (Recommended) Deploy an Amazon Elastic Compute Cloud instance to help run automation scripts
<a name="optionalrecommended-deploy-an-amazon-elastic-compute-cloud-instance-to-help-run-automation-scripts"></a>

We recommend deploying an Amazon Elastic Compute Cloud (Amazon EC2) instance to automate the connection to the solution’s APIs and AWS Boto3 APIs with IAM roles. The following cost estimate assumes that the Amazon EC2 instance is located in the `us-east-1` Region and runs eight hours a day, five days a week.

| AWS service | Factors | Cost/month [USD] |
| --- | --- | --- |
| Amazon EC2 | 176 hours a month x $0.1108/per hour (`t3.large`) | $19.50 |
| Amazon Elastic Block Store (Amazon EBS) | 30 GB x $0.08/GB-month (gp3) x (176 hours/720 hours) | $0.59 |
|  |  **Total:**  |  **\~$20.09**  |

Prices are subject to change. For full details, refer to the pricing webpage for each AWS service you will be using in this solution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
