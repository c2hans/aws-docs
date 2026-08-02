---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/run-bluage-modernized-mainframes/solution-architecture.html
---

# Solution architecture
<a name="solution-architecture"></a>

The solution runs the modernized application inside a [Docker](https://aws.amazon.com/docker/) container that is orchestrated by [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html). The wrapper shell script running within the container image manages the modernized Java application, such as the collection of inputs, the operation of the Java code, and the processing and delivery of outputs.

The Java application code inside the container is out of scope for this guide. At a high level, the wrapper shell script acts as the entry point to the container, and it orchestrates various tasks. At runtime, the ECS [task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html) supplies the environmental metadata, such as Amazon Simple Storage Service (Amazon S3) buckets, by using native integrations with [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) and [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), a capability of AWS Systems Manager.

The following architecture is designed to run modernized mainframe workloads by using serverless AWS services, eliminating the need to manage and maintain on-premises infrastructure.

![Architecture diagram of a modernized mainframe application running on AWS serverless infrastructure.](http://docs.aws.amazon.com/prescriptive-guidance/latest/run-bluage-modernized-mainframes/images/guide-img/8df97f4b-4eac-4953-975c-83ed512be5b7/images/07cd22fc-e59a-4722-9ea7-eb5a3c5495d0.png)

The diagram shows the following process:

1. Create and store the container image in [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html). The Amazon ECS task definition references the image by using the image tag.

1. Use one of the following types of Elastic Load Balancing resources to provide an entry point for requests:
   + For HTTP-based services, use an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html). This enables the use of TLS certificates to provide encryption in transit and application health checks.
   + For other services, such as IBM CICS, use a [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html). This transparently creates proxy TCP connections (Layer 4) to the containers in the Amazon ECS cluster.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/run-bluage-modernized-mainframes/solution-architecture.html)

1. Store environmental configurations, such as database endpoints and credentials, in Secrets Manager or Parameter Store. With Secrets Manager, you pay based on the number of secrets stored and API calls made. This service is best suited for any sensitive data, such as database credentials. With Parameter Store, there is no additional charge for standard parameters and standard throughput of API interactions. This service is best suited for other, non-sensitive data, such as Java logging parameters.

1. Use [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) to store task inputs and outputs. The [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) inside the bash wrapper handles the integration of the container with Amazon S3. Amazon S3 events, such as `PutObject` requests, can be used to trigger workflows, such as running the Amazon ECS task for a batch job or delivering outputs to downstream consumers.

1. Use [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) as a replacement for the mainframe database engine, such as IBM Db2 or IBM IMS. Connection details, such as endpoints and credentials, are supplied at runtime to the task. One of the most challenging aspects when modernizing mainframe workloads is ensuring that the inputs match between the mainframe and modernized versions of the application. There are few real-time, change data capture (CDC) solutions that can replicate data from a mainframe to a modern database engine such as PostgreSQL. Ensure that you have a good understanding of the data the modernized application needs and how it will be made available.

1. The task definition for real-time services includes details about the container image, which TCP/IP ports should be presented to the load balancing resources, and the number of containers that are required at any given time. The built-in [Amazon ECS deployment circuit breaker](https://aws.amazon.com/blogs/containers/announcing-amazon-ecs-deployment-circuit-breaker/) (AWS blog post) provides a managed, rolling-update deployment mechanism that eliminates the operational overhead of managing service deployments.

1. The task definition for batch jobs includes details about the container image and any environment variables that are required for configuration. These can include the available resources (such as CPU, RAM, or ephemeral storage), inputs, outputs, and other settings.

1. Use [Amazon S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html) or [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to initiate workflows. These services can start an AWS Step Functions workflow or process objects based upon events in Amazon S3, such as when a job writes an output object to a bucket.

1. Use [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) to wrap the operation of batch jobs in Amazon ECS. The workflow can start a batch task, monitor its progress, and handle any errors.

With mainframe workloads, it's likely that a degree of customization will be required. This architecture is intended to be compatible with common use cases, and you can extend it to support many requirements.
