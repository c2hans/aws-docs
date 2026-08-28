---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf01-bp05.html
---

# ADVPERF01-BP05 Evaluate the choice of open source-based software (self-managed) against using a fully-managed service
<a name="advperf01-bp05"></a>

 Open source-based software is widely used by customers for advertising workloads. Carefully evaluate the factors for adoption of self-managed and managed services.

## Implementation guidance
<a name="implementation-guidance-38"></a>

Adtech customers need to decide between self-managed and fully-managed services for container, databases, and analytics services in their workloads.

 Evaluate the effect of both choices on performance of your workload from operational effort, infrastructure cost, customizability, high availability, and time to market. Create benchmarks for performance using both options if needed, and choose the option that meets your performance requirements.

## Key AWS services
<a name="key-aws-services-22"></a>
+  [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
+  [Amazon Managed Streaming for Apache Kafka (MSK)](https://aws.amazon.com/msk/)
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
+  [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/)
+  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)

## Resources
<a name="resources-33"></a>
+  [Migrating from self-managed Kubernetes to Amazon EKS? Here are some key considerations](https://aws.amazon.com/blogs/containers/migrating-from-self-managed-kubernetes-to-amazon-eks-here-are-some-key-considerations/)
+  [How to choose the right Amazon MSK cluster type for you](https://aws.amazon.com/blogs/big-data/how-to-choose-the-right-amazon-msk-cluster-type-for-you/)
+  [Motivations for migration to Amazon DynamoDB](https://aws.amazon.com/blogs/database/motivations-for-migration-to-amazon-dynamodb/)
+  [Processing large records with Amazon Kinesis Data Streams](https://aws.amazon.com/blogs/big-data/processing-large-records-with-amazon-kinesis-data-streams/)
+  [Build an end-to-end MLOps pipeline using Amazon SageMaker AI Pipelines, GitHub, and GitHub Actions](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/)
+  [Choosing an AWS database service](https://docs.aws.amazon.com/decision-guides/latest/databases-on-aws-how-to-choose/databases-on-aws-how-to-choose.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
