---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/examples.html
---

# Infrastructure examples on AWS
<a name="examples"></a>

This section provides examples for designing an infrastructure for your application on AWS that you can use to implement a hexagonal architecture. We recommend that you start with a simple architecture for building a minimum viable product (MVP). Most microservices need a single entry point to handle client requests, a compute layer to run the code, and a persistence layer to store data. The following AWS services are great candidates for use as clients, primary adapters, and secondary adapters in hexagonal architecture:
+ **Clients:** Amazon API Gateway, Amazon Simple Queue Service (Amazon SQS), Elastic Load Balancing, Amazon EventBridge
+ **Primary adapters:** AWS Lambda, Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), Amazon Elastic Compute Cloud (Amazon EC2)
+ **Secondary adapters:** Amazon DynamoDB, Amazon Relational Database Service (Amazon RDS), Amazon Aurora, API Gateway, Amazon SQS, Elastic Load Balancing, EventBridge, Amazon Simple Notification Service (Amazon SNS)

The following sections discuss these services in the context of hexagonal architecture in more detail.

## Start simple
<a name="start-simple"></a>

We recommend that you start simple when you architect an application by using hexagonal architecture. In this example, API Gateway is used as the client (REST API), Lambda is used as the primary adapter (compute), and DynamoDB is used as the secondary adapter (persistence). The gateway client calls the entry point, which, in this case, is a Lambda handler.

![Simple hexagonal architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/images/guide-img/b67c0cd8-adc6-4a04-a6b7-ed44f0888b3f/images/2819dd9e-9423-4e53-9148-0b34f414465d.png)

This architecture is fully serverless and gives the architect a good starting point. We recommend that you use the command pattern in the domain because it makes the code easier to maintain, and it adapts to new business and non-functional requirements. This architecture could be sufficient for building simple microservices with a few operations.

## Apply the CQRS pattern
<a name="apply-cqrs"></a>

We recommend that you switch to the CQRS pattern if the number of operations on the domain is going to scale. You can apply the CQRS pattern as a fully serverless architecture in AWS by using the following example.

![Applying the CQRS pattern in hexagonal architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/images/guide-img/b67c0cd8-adc6-4a04-a6b7-ed44f0888b3f/images/76e4a8ff-2d97-48bb-ae4f-71897002c736.png)

This example uses two Lambda handlers, one for queries and one for commands. Queries are run synchronously by using an API gateway as the client. Commands are run asynchronously by using Amazon SQS as the client.

This architecture includes multiple clients (API Gateway and Amazon SQS) and multiple primary adapters (Lambda), which are called by their corresponding entry points (Lambda handlers). All components belong to the same bounded context, so they are within the same domain.

## Evolve the architecture by adding containers, a relational database, and an external API
<a name="evolve"></a>

Containers are a good option for long-running tasks. You might also want to use a relational database if you have a predefined data schema and want to benefit from the power of the SQL language. In addition, the domain would have to communicate with external APIs. You can evolve the architecture example to support these requirements as shown in the following diagram.

![Evolving the hexagonal architecture by adding containers, a relational database, and an external API](http://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/images/guide-img/b67c0cd8-adc6-4a04-a6b7-ed44f0888b3f/images/e081652e-99ab-4fc3-86d1-87fed9681e41.png)

This example uses Amazon ECS as the primary adapter for launching long-running tasks in the domain. Amazon EventBridge (client) initiates an Amazon ECS task (entry point) when a specific event happens. The architecture includes Amazon RDS as another secondary adapter for storing relational data. It also adds another API gateway as a secondary adapter for invoking an external API call. As a result, the architecture uses multiple primary and secondary adapters that rely on different underlying compute layers in one business domain.

The domain is always loosely coupled with all primary and secondary adapters through abstractions called *ports*. The domain defines what it requires from the outside world by using ports. Because it is the adapter's responsibility to implement the port, switching from one adapter to another doesn't affect the domain. For example, you can switch from Amazon DynamoDB to Amazon RDS by writing a new adapter, without affecting the domain.

## Add more domains (zoom out)
<a name="zoom"></a>

Hexagonal architecture aligns well with the principles of a microservices architecture. The architecture examples shown so far contained a single domain (or bounded context). Applications typically include multiple domains, which need to communicate through primary and secondary adapters. Each domain represents a microservice and is loosely coupled with other domains.

![Adding domains to your hexagonal architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/images/guide-img/b67c0cd8-adc6-4a04-a6b7-ed44f0888b3f/images/28cf0573-056b-4e91-9191-c1e99153b760.png)

In this architecture, each domain uses a different set of compute environment(s). (Each domain might also have multiple compute environments, as in the previous example.) Each domain defines its required interfaces to communicate with other domains through ports. Ports are implemented by using primary and secondary adapters. This way, the domain is unaffected if there is a change in the adapter. In addition, domains are decoupled from one another.

In the architecture example shown in the previous diagram, Lambda, Amazon EC2, Amazon ECS, and AWS Fargate are used as primary adapters. API Gateway, Elastic Load Balancing, EventBridge, and Amazon SQS are used as secondary adapters.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
