---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/pipeline-management.html
---

# Pipeline management
<a name="pipeline-management"></a>

 Data pipeline is the core functionality of this guidance. In the Clickstream Analytics on AWS guidance, we define a data pipeline as a sequence of integrated AWS services that ingest, process, and model the clickstream data into a destination data warehouse for analytics and visualization. It is also designed to efficiently and reliably collect data from your websites and apps to a S3-based data lake, where it can be further processed, analyzed, and utilized for additional use cases (such as real-time monitoring, and recommendation).

To get a basic understanding of the pipeline, you can refer to [terms and concepts](terms-and-concepts.md) for more information.

## Prerequisites
<a name="prerequisites-4"></a>

 You can configure the pipeline in all AWS Regions. For opt-in regions, you need to [enable them](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) first.

 Before you start to configure the pipeline in a specific region, make sure you have the following in the target region:
+  At least one Amazon VPC.
+  At least two public subnets across two AZs in the VPC.
+  At least two private (with NAT gateways or instances) subnets across two AZs, or at least two isolated subnets across two AZs in the VPC. If you want to deploy the guidance resources in the isolated subnets, you have to create [VPC endpoints](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.html) for below AWS services,
  +  s3, logs, ecr.api, ecr.dkr, ecs, ecs-agent, ecs-telemetry.
  +  kinesis-streams if you use KDS as sink buffer in ingestion module.
  +  emr-serverless, glue if you enable data processing module.
  +  redshift-data, sts, dynamodb, states and lambda if you enable Redshift as analytics engine in data modeling module.
+  An Amazon S3 bucket located in the same region.
+  If you need to enable Redshift Serverless as analytics engine in data modeling module, you need have subnets across at least three AZs.
+  QuickSight Enterprise edition subscription is required if the reporting is enabled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
