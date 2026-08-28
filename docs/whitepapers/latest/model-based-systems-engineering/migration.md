---
source_url: https://docs.aws.amazon.com/whitepapers/latest/model-based-systems-engineering/migration.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migration
<a name="migration"></a>

 You can *rehost* or *re-platform* MBSE on AWS. This section follows the [6-Rs of migration strategy](https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/) in AWS. We will start with *re-hosting* and then directly move to the other end of "Rs”, *refactoring*. The other 4-Rs in between these two extremes would be a combination of these.

## Rehosting MBSE Application
<a name="rehosting-mbse-application"></a>

 Rehosting MBSE means [lifting and shifting](https://aws.amazon.com/products/storage/lift-and-shift/) your existing MBSE services to the cloud. You can use **AWS Application Migration Service** to migrate your workloads, with a wide selection of chip and cloud storage types available.

 You can still bring flexibility, agility, scalability, and availability without changing your existing setup. You can build your own MBSE **Amazon Machine Image (AMI)** and deploy your applications on **EC2 **instances, Kubernetes with** EKS, **or** **containers with** ECS**. You can also employ **Amazon AppStream 2.0** to virtually deploy a non-persistent desktop and MBSE application virtualization such as IDEs on demand.

 On the other hand, you can also lift & shift your MBSE databases to AWS. You can re-host the databases on **Amazon EBS** and **Amazon FSx for Windows File Server. **You can go slightly beyond simple rehosting and re-platform your databases on** Amazon RDS **to bring a cost-efficient and resizable capacity while automating time-consuming administration.

 Amazon RDS is available on several database instance types - optimized for memory, performance or I/O - and provides you with six familiar database engines to choose from, including Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle Database, and SQL Server. You can use the **AWS Database Migration Service** to migrate easily or replicate your existing MBSE and MBSE-related databases.

 You can use infrastructure automation by providing **Service Catalog for MBSE and Related Services**. Once you have the AMIs and design infrastructure configuration, **AWS** **CloudFormation **templates can be built for desired MBSE stack(s). Then, these stacks can be deployed in a CI/CD pipeline by your IT or through a self-service setting such as using **AWS CodePipeline**. For example, a MDO (Multi-Disciplinary Optimization) or DSE (Design Space Exploration) type of compute-heavy (but parallel processing) jobs can be included as CloudFormation Template that can deploy **ephemeral compute deployments, but with persistent storage**.

 Therefore, the whole process of deploying the lift-and-shift MBSE can be automated where the configuration can be following the best practices (security, cost optimization, etc.). With appropriate **Identity and Access Management** (IAM) using **AWS Identity and Access Management (IAM)**, these configurations are only built/modified by authorized users.

## Refactoring MBSE Application
<a name="refactoring-mbse-application"></a>

 We recommend refactoring towards breaking the monoliths into microservices through APIs and AWS Managed Services. The microservices approach can further bring flexibility to your MBSE workloads as new technologies can be augmented through Restful APIs (**Amazon API Gateway**) and GraphQL APIs (**AWS AppSync**). This chapter is illustrated as *MBSE Backend* diagram further below.

 You can use any of the below recommendations - or adopt them all at once - during the refactoring. You may notice that you can bring **serverless technologies** for cost-effectiveness and to remove infrastructure management tasks altogether.

 You can start refactoring/rearchitecting **your Digital Thread with APIs**. One of the refactoring of MBSE Digital Threads is employing **Amazon API Gateway**, a fully-managed service that allows you to create, publish, maintain, monitor, and secure APIs at scale.

 This is especially the case for [SysMLv2.0](https://www.omgsysml.org/SysML-2.htm), enabling API-based communication for the new MBSE applications. You can also consider using **AWS AppSync** to build APIs with GraphQL since it is easier to develop applications with GraphQL, by giving the ability to query multiple databases, microservices, and APIs with a single GraphQL endpoint.

 The other refactoring is employing **AWS Lambda,** a serverless compute service that lets you run your code with zero administration. You can directly use **CRUD (Create, read, update, delete) **operations to MBSE directly with AWS Lambda functions. These are especially useful for MBSE since the operations are transactional and rather event-based, such as in a CRUD form.

 AWS Lambda can work natively with Amazon API Gateway to bring a serverless business logic to your Digital Thread when triggered by the API Gateway. Therefore, the **millisecond pricing granularity** of AWS Lambda allows you to run your business logic only when needed - and only with the time used (measured in milliseconds).

 You can even perform **low-fidelity MBSE simulations** with AWS Lambda as long as the simulation does not exceed the maximum 15 minutes of runtime duration, which is the limit of AWS Lambda, as of today. AWS Lambda can support 6 vCPus and up to 10 GB of memory, which provides a decent amount of computing power for most low-fidelity simulations.

 AWS Lambda can perform most of the MBSE simulations, not limited to CRUD operations. This can make **MBSE serverless**; therefore, you benefit from having ‘millisecond’ cost granularity, high-scalability, reliability, and zero-administration business logic can be achieved.

 Along with AWS Lambda, **AWS Step Functions** can also help you to create complex business logic with a **State Machine** to perform stateful operations. If you prefer an open-source approach for the workflow, you can consider using **Amazon Managed Workflows with Apache Airflow (AMWAA)**, which a managed service for Apache Airflow on AWS. You can keep temporary and permanent data on **Amazon S3** with virtually unlimited storage space, cost-effective storage with 11 nines of durability (99.999999999%).

 You can keep your costs under control for the stored metadata using **Amazon S3 Lifecycle Management,** which automatically moves colder or cost-effective tier storage as defined by you or determined by an embedded AI.

 If you would like to go with containers and Kubernetes instead of AWS Lambda, you can select **AWS Fargate** to stick to a serverless approach that fits into MBSE operations. Please see [Serverless on AWS](https://aws.amazon.com/serverless/) to learn more about other resources.

 The next refactoring step is for the databases. MBSE typically uses both relational and non-relational databases. **Amazon DynamoDB** can serve as a low-latency key-value and document database for the MBSE. **Amazon DynamoDB** takes the burden of server management from you while providing a highly scalable and reliable key-value and document database required for MBSE.

 Amazon DynamoDB brings virtually unlimited throughput and storage with 11 9’s of durability. Globally shared multi-tenant and multi-region MBSE applications can benefit technologies such as **Global Tables**. In addition, your product development teams benefit from low-latency using the caching on Amazon DynamoDB with **DynamoDB Accelerator (DAX)**.

 MBSE requires relational databases. As mentioned before, you can employ Amazon Aurora for your MySQL or PostgresSQL databases on the top of Amazon RDS. **Amazon Aurora** features a distributed, fault-tolerant, self-healing storage system that auto-scales up to 128TB per database instance. Similar to Global Tables, you can use **Amazon Aurora Global Databases** to employ an easily scalable relational database in MBSE globally read by consumers.

 Global Databases enables fast local reads - typically with less than one second latency - in multiple regions, as well as providing disaster recovery in a region wide outage. These features are especially important for critical applications consumed globally such as MBSE.

 Finally, you can also benefit from serverless technology in your MySQL and PostgresSQL databases with **Amazon** **Aurora Serverless**. Another advantage of Aurora is its direct integration of Amazon Sagemaker for incorporating machine learning (ML) and AI algorithms. With this feature, you can speed up your ML inference by up to x100.

 All of the multi-level relationships in different domains and the same domains require a **graph database for ontology**. Here, you can benefit from using **Amazon Neptune**. The core of **Amazon Neptune **is a purpose-built, high-performance graph database engine optimized for storing billions of relationships and querying the graph with milliseconds latency. Amazon Neptune supports Property Graph and W3C's RDF, and their respective query languages such as Apache TinkerPop Gremlin and SPARQL.

 Amazon Neptune is highly available, with read replicas, point-in-time recovery, **continuous backup to Amazon S3**, and replication across Availability Zones. Neptune is secure with support for HTTPS encrypted client connections and encryption at rest. Neptune is fully managed, so you no longer need to worry about database management tasks and activities.

 Look for the best balance between **open-shared data to better collaboration** and **access controls to ensure** that unintentional data is secure and not shared, mainly in the aerospace and defense industries.

 Using AWS, you can **provide identity and access management tools** that allow you to define granular access controls and guardrails in multiple levels including resources, end-points and users. You can also incorporate solutions to consider data residency while giving minimum privilege, federated access to your MBSE data globally in the way you define. To learn more about identity and access management, please [visit the AWS IAM site.](https://aws.amazon.com/iam/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
