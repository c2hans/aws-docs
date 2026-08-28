---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution and a summary of AWS Well-Architected design considerations.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters deploys the following components in your AWS account.

 **Guidance for Deploying a Prebid Server on AWS architectural overview**

![aws solution for prebid server architecture](http://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/images/aws-solution-for-prebid-server-architecture.png)

**Note**
 [AWS CloudFormation](https://aws.amazon.com/cloudformation/) resources are created from AWS Cloud Development Kit (AWS CDK) constructs.

The high-level process flow for the solution, including the components deployed with the AWS CDK template, is as follows:

1. A user browses to a page on a website that hosts ads.

1. The publisher site returns the page source to the browser with resources, and one or more script modules (also called wrappers) that enable real-time bid requests and responses for ads of given dimensions, types, topics, and other criteria.

1. The bid requests are received from the browser at the [Amazon CloudFront](https://aws.amazon.com/cloudfront/) endpoint integrated with [AWS Web Application Firewall](https://aws.amazon.com/waf/) (AWS WAF) for entry into the solution. This step helps validate legitimate traffic from malicious requests, such as penetration or denial-of-service attempts. Traffic can be received here as HTTP or HTTPS.

1. The request is forwarded to [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html) (ALB). ALB determines which container running Prebid Server in the cluster is at a utilization level that can accept more requests. ALB has a network interface on the public internet and one in each private subnet where containers are hosted within [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC).

1. The request arrives at an [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS) container, is parsed and validated, and requests to different bidding services are sent concurrently. The connectivity method depends on the deployment configuration:

   1.  **External bidders**: Requests are sent through the NAT gateway and internet gateway to bidders over the public internet.

   1.  **Bidder simulator with VPC peering**: Requests are sent directly through the VPC peering connection to the bidder simulator in its own VPC.

   1.  **Bidder simulator with RTB Fabric**: Requests are sent through the AWS RTB Fabric requester gateway to the responder gateway in the bidder simulator VPC, utilizing the private RTB Fabric network.

1. The NAT gateway and internet gateway allow containers to initiate outbound requests to the internet and receive responses. These resources are primarily used for Prebid Server containers to request and gather bids for ad auctions from external bidders.

1. Bidders receive one or more bid requests (either over the internet, through VPC peering, or via RTB Fabric) from a Prebid Server container. Bidders respond with zero or more bids for the various requests. The response, including the body of the winning creative(s), is sent back to the browser.

1. For cache operations, Prebid Server containers are configured to use the publicly accessible endpoint (CloudFront domain or external ALB DNS) to store and retrieve cached bid responses. Cache requests from containers flow through the same entry point as client requests, reaching the cache Lambda function via ALB routing rules. This unified cache endpoint ensures both server-side and client-side cache access use the same path.

1. During normal operation, Amazon CloudWatch metrics are collected from various resources involved in handling requests and responses through the solution. As the load changes throughout the cluster, CloudWatch alarms are used to determine when to scale-out or scale-in the container cluster.

1. An ECS service definition (Prebid ECS service) is responsible for tracking the health of the cluster, performing scale-out and scale-in operations, and managing the collection of containers available for ALB. The Prebid ECS service uses [AWS Fargate](https://aws.amazon.com/fargate/) instances.

1. Metrics log files for each container are stored to a shared [Amazon Elastic File System](https://aws.amazon.com/efs/) (Amazon EFS) using NFS protocol. This file system is mounted to each Prebid Server container during start-up. A single metrics log file is written for a limited time and then closed and rotated, so that it can be included in the next stage of processing. EFS is treated as a temporary location as log data is generated and moved to longer-term storage on [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) and into [AWS Glue](https://aws.amazon.com/glue/).

1.  [AWS DataSync](https://aws.amazon.com/datasync/) replicates rotated log files from EFS to S3 on a recurring schedule. DataSync verifies each transferred file and provides a report of the completed work to an [AWS Lambda](https://aws.amazon.com/lambda/) function.

1. The `DataSyncLogsBucket` S3 bucket receives the replicated log files from EFS using the same folder structure. Log files arrive in this bucket as a result of the DataSync process.

1. The `delete_efs_files` Lambda function runs after the DataSync process completes in step 12 and removes transferred and verified log file data from EFS.

1. An AWS Glue job performs an ETL operation on the metrics data in the `DataSyncLogsBucket` S3 bucket. The ETL operation structures the metric data into a single database with several tables, partitions the physical data, and writes it to an S3 bucket.

1. The `MetricsEtlBucket` S3 bucket contains the metric log data transformed and partitioned through ETL. The data in this bucket is made available to AWS Glue clients for queries.

1. Many different types of clients use [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) to access the Prebid Server metric data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
