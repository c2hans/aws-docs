---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-prerequisites.html
---

# Prerequisites
<a name="pb-es68-prerequisites"></a>

Before you begin, confirm the following.

 **Source**
+ A reachable self-managed Elasticsearch 6.8 cluster.
+ Administrative access to the source cluster so you can install a plugin, attach an IAM role to its nodes, and register a snapshot repository.
+ Network connectivity from the source cluster to [Amazon Simple Storage Service](https://aws.amazon.com/s3) (Amazon S3) so the source can write a snapshot.

 **Target**
+ An Amazon OpenSearch Service domain running OpenSearch 3.x, deployed in or reachable from the same VPC you will use for Migration Assistant.
+ If the domain has fine-grained access control (FGAC) enabled, plan to map the migration IAM role as a domain user so the workflow can write metadata and documents.

 **Infrastructure**
+ An existing VPC with at least two subnets in different Availability Zones for the Amazon EKS cluster.
+ The AWS CLI and `kubectl` configured with credentials that can deploy AWS CloudFormation stacks and access Amazon EKS.
+ Permission to create an Amazon S3 bucket (or use the solution’s default bucket) for snapshot storage.
