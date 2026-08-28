---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-well-architected-pillars.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-pillars"></a>

This solution was designed with best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

 **Operational excellence**

This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).
+ The solution pushes metrics, logs, and traces to Amazon CloudWatch at various stages to provide observability into the infrastructure, Elastic Load Balancing, Amazon ECS cluster, Lambda functions, Step Function workflow, and the rest of the solution components. This solution also creates the CloudWatch dashboards for each pipeline monitoring.

 **Security**

This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).
+ The web console users are authenticated and authorized with Amazon Cognito or OpenID Connect.
+ All inter-service communications use AWS IAM roles.
+ All roles used by the solution follow least privilege access. That is, it only contains the minimum permissions required so the service can function properly.

 **Reliability**

This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).
+ Using AWS serverless services wherever possible (for example, AWS AppSync, Amazon DynamoDB, AWS Lambda, AWS Step Functions, Amazon S3, and Amazon SQS) for high availability and recovery from service failure.
+ Configuration management content of the solution is stored in Amazon DynamoDB, all of your data is stored on solid-state disks (SSDs) and is automatically replicated across multiple Availability Zones in an AWS Region, providing built-in high availability and data durability.

 **Performance efficiency**

This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).
+ The ability to launch this solution in any Region that supports AWS services in this solution such as: Amazon S3, Amazon ECS, and Elastic Load Balancing.
+ Using serverless architecture removes the need for you to run and maintain physical servers for traditional compute activities.
+ Automatically testing and deploying this solution daily. Reviewing this solution by solutions architects and subject matter experts for areas to experiment and improve.

 **Cost optimization**

This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).
+ Using Auto Scaling groups so that the compute costs are only related to how much data is ingested and processed.
+ Using serverless services such as Amazon S3, Amazon DynamoDB, and AWS Lambda so that customers only get charged for what they use.

 **Sustainability**

This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).
+ The solution’s serverless design (using Amazon Kinesis Data Streams, Amazon S3, AWS Lambda) and the use of managed services (such as Amazon ECS) are aimed at reducing carbon footprint compared to the footprint of continually operating on-premises servers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Logging with OpenSearch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
