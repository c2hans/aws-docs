---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/wave-based-refactoring/wave-based-implementation-phase.html
---

# Phase 3: Wave-based implementation
<a name="wave-based-implementation-phase"></a>

The wave-based implementation phase focuses on selecting AWS microservices to replace specific functionalities of the legacy system, and then implementing those services in waves. The following recommendations can help you prioritize which capabilities to modernize first, and then roll out the changes to production incrementally.

**Important**
Make sure that you consult and get approval from key stakeholders before implementing any of the following wave groups. It's recommended to use an iterative approach when creating these groups, rather than relying solely on the capability matrix's scoring criteria.

**Key focus areas**
+ Using a series of prioritization criteria to categorize capabilities into three implementation waves based on their number of dependencies, business priority, and level of complexity
+ Selecting cloud-native AWS microservices that can provide the same capabilities as the legacy IT system
+ Configuring the foundational AWS infrastructure required to set up the selected AWS microservices
+ Rolling changes out to production incrementally in waves

## Step 1: Organize capabilities based on their number of dependencies, business priority, and level of complexity
<a name="organize-capabilities"></a>

Using input from key stakeholders along with the weighted scores from the capability matrix, organize the legacy system's capabilities into the following three main groups:

**Note**
Most implementations also require the use of many subwave groups. This guide outlines the three main wave groups for example purposes only.

**Wave 1 capabilities**

|  |
| --- |
| Number of dependencies | None or very low |
| --- |--- |
| **Business priority** | Low |
| **Complexity** | Low |

** **

**Wave 2 capabilities**

|  |
| --- |
| Number of dependencies | Low to medium |
| --- |--- |
| **Business priority** | Low to medium |
| **Complexity** | Medium |

**Wave 3 capabilities**

|  |
| --- |
| Number of dependencies | High |
| --- |--- |
| **Business priority** | Medium to high |
| **Complexity** | Medium to high |

## Step 2: Select AWS microservices to replace the legacy IT system's capabilities
<a name="select-aws-services"></a>

In coordination with key stakeholders, use an iterative process of reviewing and finalizing the sequence of capabilities that you want to modernize. Then, select AWS microservices to replace the legacy IT system's capabilities.

The following are some example AWS microservices that can often be used to replace capabilities that fall within each wave group:

**Wave 1 AWS microservice examples**
+ AWS Lambda
+ Amazon Simple Queue Service (Amazon SQS)
+ Amazon Simple Notification Service (Amazon SNS)
+ Amazon API Gateway

**Note**
Wave 1 capabilities can be integrated with minimal AWS foundational services by using a strangler migration pattern. For more information, see [Seamlessly migrate on-premises legacy workloads using a strangler pattern](https://aws.amazon.com/blogs/architecture/seamlessly-migrate-on-premises-legacy-workloads-using-a-strangler-pattern/) on the AWS Blog.

**Wave 2 AWS microservice examples**
+ AWS Step Functions based workflow
+ Database fit for purpose (migration to Aurora PostgreSQL)
+ AWS SaaS factory

**Note**
Wave 2 capabilities typically involve some level of database modernization, such as migrating to a PostgreSQL-compatible database. To maintain a hybrid cloud solution, synchronizing legacy databases with new, cloud-native databases is also usually required.

**Wave 3 AWS microservice examples**
+ AWS Fargate
+ Real-time recommendation engines, such as Amazon Textract, Amazon Comprehend, Amazon Rekognition, and Amazon SageMaker models
+ Scalable data lakes, such as Amazon Simple Storage Service (Amazon S3) and AWS Lake Formation
+ Purpose-built Amazon analytics services, such as Amazon Athena, Amazon EMR, Amazon OpenSearch Service, Amazon Kinesis, and Amazon Redshift
+ Seamless data movement services, such as AWS Glue and AWS App Mesh

**Important**
End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect).

**Note**
Wave 3 capabilities typically have a high number of dependencies and usually need to integrate with other microservices. These attributes make wave 3 capabilities good candidates to be replaced by container-based microservices.

## Step 3: Configure the foundational AWS infrastructure required to set up the selected AWS microservices
<a name="configure-foundational-aws-infrastructure"></a>

After reviewing and finalizing the target cloud-based architecture with key stakeholders, configure the AWS infrastructure required to set up the AWS microservices that you selected.

**Example foundational AWS infrastructure resources**
+ [AWS Control Tower](https://aws.amazon.com/controltower/) and landing zone
+ [AWS Organizations](https://aws.amazon.com/organizations/) organizational units and service control policies (SCPs)
+ [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) policies
+ [Amazon API Gateway](https://aws.amazon.com/api-gateway/) APIs
+ [AWS Lambda](https://aws.amazon.com/lambda/) functions
+ AWS database services, such as [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/)
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) dashboards and alarms
+ [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) queues
+ [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/) topics and subscriptions
+ [Amazon Cognito](https://aws.amazon.com/cognito/) and user pools

## Step 4: Implement the changes in waves
<a name="implement-the-changes-in-waves"></a>

Sequentially implement each wave group in a test environment. As each wave group becomes ready for production, test the system's functionality and debug any issues in the test environment. Then, cut over the changes to your production environment incrementally.

The following are high-level descriptions of the types of tasks that are usually associated with implementing each wave group:

**Wave 1 implementation**
+ Create serverless Lambda functions
+ Integrate the Lambda functions with the API Gateway service
+ Configure authentication and authorization systems by using tools such as Amazon Cognito, IAM, Okta, and Ping Identity
+ For hybrid cloud architectures, set up a proxy layer by using a service mesh, such as [AWS App Mesh](https://aws.amazon.com/app-mesh/).

**Wave 2 implementation**
+ Configure AWS App Mesh, including your service mesh, virtual services, nodes, routes, and proxies
+ Set up containers in AWS Fargate or Amazon Elastic Kubernetes Service (Amazon EKS)
+ Integrate the proxy layer with the frontend system

**Wave 3 implementation**
+ Complete complex data migrations and integrations
+ Implement your most complex workflows that involve multiple microservices
