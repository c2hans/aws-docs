---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_select_service_select_for_cost.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST05-BP05 Select components of this workload to optimize cost in line with organization priorities
<a name="cost_select_service_select_for_cost"></a>

 Factor in cost when selecting all components. This includes using application level and managed services, such as Amazon Relational Database Service ([Amazon RDS](https://aws.amazon.com/rds)), [Amazon DynamoDB](https://docs.aws.amazon.com/dynamodb/?id=docs_gateway), Amazon Simple Notification Service ([Amazon SNS](https://docs.aws.amazon.com/sns/?id=docs_gateway)), and Amazon Simple Email Service ([Amazon SES](https://docs.aws.amazon.com/ses/?id=docs_gateway)) to reduce overall organization cost. Use serverless and containers for compute, such as AWS Lambda, Amazon Simple Storage Service ([Amazon S3](https://docs.aws.amazon.com/s3/?id=docs_gateway))for static websites, and Amazon Elastic Container Service ([Amazon ECS](https://docs.aws.amazon.com/ecs/?id=docs_gateway)). Minimize license costs by using open source software, or software that does not have license fees: for example, Amazon Linux for compute workloads or migrate databases to [Amazon Aurora](https://docs.aws.amazon.com/rds/?id=docs_gateway).

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

You can use serverless or application-level services such as [AWS Lambda](https://aws.amazon.com/lambda/), [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/), [Amazon SNS](https://docs.aws.amazon.com/sns/?id=docs_gateway), and [Amazon SES](https://docs.aws.amazon.com/ses/?id=docs_gateway). These services remove the need for you to manage a resource, and provide the function of code execution, queuing services, and message delivery. The other benefit is that they scale in performance and cost in line with usage, allowing efficient cost allocation and attribution.

For more information on Serverless, refer to the [Well-Architected Serverless Application Lens whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html).

** Implementation steps**
+ ** Select each service to optimize cost: **Using your prioritized list and analysis, select each option that provides the best match with your organizational priorities.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Total Cost of Ownership (TCO) Calculator](https://aws.amazon.com/tco-calculator/)
+  [Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/)
+  [Cloud products](https://aws.amazon.com/products/)
