---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/cost_select_service_select_for_cost.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST05-BP05 Select components of this workload to optimize cost in line with organization priorities
<a name="cost_select_service_select_for_cost"></a>

Factor in cost when selecting all components for your workload. This includes using application level and managed services or serverless, containers, or event-driven architecture to reduce overall cost. Minimize license costs by using open-source software, software that does not have license fees, or alternatives to reduce the cost.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Consider the cost of services and options when selecting all components. This includes using application level and managed services, such as [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/), [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/), and [Amazon Simple Email Service (Amazon SES)](https://aws.amazon.com/ses/) to reduce overall organization cost. Use serverless and containers for compute, such as [AWS Lambda](https://aws.amazon.com/lambda/) and [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) for static websites. Containerize your application if possible and use AWS Managed Container Services such as [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/) or [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/). Minimize license costs by using open-source software, or software that does not have license fees (for example, Amazon Linux for compute workloads or migrate databases to Amazon Aurora).

You can use serverless or application-level services such as [AWS Lambda](https://aws.amazon.com/lambda/), [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/), [Amazon SNS](https://docs.aws.amazon.com/sns/?id=docs_gateway), and [Amazon SES](https://docs.aws.amazon.com/ses/?id=docs_gateway). These services remove the need for you to manage a resource, and provide the function of running code, queuing services, and message delivery. The other benefit is that they scale in performance and cost in line with usage, allowing efficient cost allocation and attribution.

 Using [event-driven architecture (EDA)](https://aws.amazon.com/what-is/eda/) is also possible with serverless services. Event-driven architectures are push-based, so everything happens on demand as the event presents itself in the router. This way, you’re not paying for continuous polling to check for an event. This means less network bandwidth consumption, less CPU utilization, less idle fleet capacity, and fewer SSL/TLS handshakes.

For more information on Serverless, refer to the [Well-Architected Serverless Application Lens whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html).

** Implementation steps**
+ ** Select each service to optimize cost: **Using your prioritized list and analysis, select each option that provides the best match with your organizational priorities. Instead of increasing the capacity to meet the demand, consider other options which may give you better performance with lower cost. For example, you need to review expected traffic for your databases on AWS and consider either increasing the instance size or using Amazon ElastiCache services (Redis or Memcached) to provide cached mechanisms for your databases.
+  **Evaluate event-driven architecture:** Using serverless architecture also allows you to build event-driven architecture for distributed microservice-based applications, which helps you build scalable, resilient, agile and cost-effective solutions.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Total Cost of Ownership (TCO) Calculator](https://aws.amazon.com/tco-calculator/)
+ [AWS Serverless ](https://aws.amazon.com/serverless/)
+ [ What is Event-Driven Architecture ](https://aws.amazon.com/what-is/eda/)
+  [Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/)
+  [Cloud products](https://aws.amazon.com/products/)
+ [ Amazon ElastiCache (Redis OSS) ](https://aws.amazon.com/elasticache/redis/)

 **Related examples:**
+ [ Getting started with event-driven architecture ](https://aws.amazon.com/blogs/compute/getting-started-with-event-driven-architecture/)
+ [What is an Event-Driven Architecture?](https://aws.amazon.com/event-driven-architecture/)
+ [ How Statsig runs 100x more cost-effectively using Amazon ElastiCache (Redis OSS) ](https://aws.amazon.com/blogs/database/how-statsig-runs-100x-more-cost-effectively-using-amazon-elasticache-for-redis/)
+ [ Best practices for working with AWS Lambda functions ](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
