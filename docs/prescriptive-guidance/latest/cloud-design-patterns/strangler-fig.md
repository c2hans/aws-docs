---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/strangler-fig.html
---

# Strangler fig pattern
<a name="strangler-fig"></a>

## Intent
<a name="strangler-fig-intent"></a>

The strangler fig pattern helps migrate a monolithic application to a microservices architecture incrementally, with reduced transformation risk and business disruption.

## Motivation
<a name="strangler-fig-motivation"></a>

Monolithic applications are developed to provide most of their functionality within a single process or container. The code is tightly coupled. As a result, application changes require thorough retesting to avoid regression issues. The changes cannot be tested in isolation, which impacts the cycle time. As the application is enriched with more features, high complexity can lead to more time spent on maintenance, increased time to market, and, consequently, slow product innovation.

When the application scales in size, it increases the cognitive load on the team and can cause unclear team ownership boundaries. Scaling individual features based on the load isn't possible―the entire application has to be scaled to support peak load. As the systems age, the technology can become obsolete, which drives up support costs. Monolithic, legacy applications follow best practices that were available at the time of development and weren't designed to be distributed.

When a monolithic application is migrated into a microservices architecture, it can be split into smaller components. These components can scale independently, can be released independently, and can be owned by individual teams. This results in a higher velocity of change, because changes are localized and can be tested and released quickly. Changes have a smaller scope of impact because components are loosely coupled and can be deployed individually.

Replacing a monolith completely with a microservices application by rewriting or refactoring the code is a huge undertaking and a big risk. A big bang migration, where the monolith is migrated in a single operation, introduces transformation risk and business disruption. While the application is being refactored, it is extremely hard or even impossible to add new features.

One way to resolve this issue is to use the strangler fig pattern, which was introduced by Martin Fowler. This pattern involves moving to microservices by gradually extracting features and creating a new application around the existing system. The features in the monolith are replaced by microservices gradually, and application users are able to use the newly migrated features progressively. When all features are moved out to the new system, the monolithic application can be decommissioned safely.

## Accessibility
<a name="strangler-fig-accessibility"></a>

Use the strangler fig pattern when:
+ You want to migrate your monolithic application gradually to a microservices architecture.
+ A big bang migration approach is risky because of the size and complexity of the monolith.
+ The business wants to add new features and cannot wait for the transformation to be complete.
+ End users must be minimally impacted during the transformation.

## Issues and considerations
<a name="strangler-fig-issues"></a>
+ **Code base access:** To implement the strangler fig pattern, you must have access to the monolith application's code base. As features are migrated out of the monolith, you will need to make minor code changes and implement an anti-corruption layer within the monolith to route calls to new microservices. You cannot intercept calls without code base access. Code base access is also critical for redirecting incoming requests―some code refactoring might be required so that the proxy layer can intercept the calls for migrated features and route them to microservices.
+ **Unclear domain:** The premature decomposition of systems can be costly, especially when the domain isn't clear, and it's possible to get the service boundaries wrong. Domain-driven design (DDD) is a mechanism for understanding the domain, and event storming is a technique for determining domain boundaries.
+ **Identifying microservices:** You can use DDD as a key tool for identifying microservices. To identify microservices, look for the natural divisions between service classes. Many services will own their own data access object and will decouple easily. Services that have related business logic and classes that have no or few dependencies are good candidates for microservices. You can refactor code before breaking down the monolith to prevent tight coupling. You should also consider compliance requirements, the release cadence, the geographical location of the teams, scaling needs, use case-driven technology needs, and the cognitive load of teams.
+ **Anti-corruption layer:** During the migration process, when the features within the monolith have to call the features that were migrated as microservices, you should implement an anti-corruption layer (ACL) that routes each call to the appropriate microservice. In order to decouple and prevent changes to existing callers within the monolith, the ACL works as an adapter or a facade that converts the calls into the newer interface. This is discussed in detail in the [Implementation section](acl.md#acl-implementation) of the ACL pattern earlier in this guide.
+ **Proxy layer failure:** During migration, a proxy layer intercepts the requests that go to the monolithic application and routes them to either the legacy system or the new system. However, this proxy layer can become a single point of failure or a performance bottleneck.
+ **Application complexity:** Large monoliths benefit the most from the strangler fig pattern. For small applications, where the complexity of complete refactoring is low, it might be more efficient to rewrite the application in microservices architecture instead of migrating it.
+ **Service interactions:** Microservices can communicate synchronously or asynchronously. When synchronous communication is required, consider whether the timeouts can cause connection or thread pool consumption, resulting in application performance issues. In such cases, use the [circuit breaker pattern](circuit-breaker.md) to return immediate failure for operations that are likely to fail for extended periods of time. Asynchronous communication can be achieved by using events and messaging queues.
+ **Data aggregation:** In a microservices architecture, data is distributed across databases. When data aggregation is required, you can use [AWS AppSync](https://aws.amazon.com/appsync/) in the front end, or the command query responsibility segregation (CQRS) pattern in the backend.
+ **Data consistency:** The microservices own their data store, and the monolithic application can also potentially use this data. To enable sharing, you can synchronize the new microservices' data store with the monolithic application's database by using a queue and agent. However, this can cause data redundancy and eventual consistency between two data stores, so we recommend that you treat it as a tactical solution until you can establish a long-term solution such as a data lake.

## Implementation
<a name="strangler-fig-implementation"></a>

In the strangler fig pattern, you replace specific functionality with a new service or application, one component at a time. A proxy layer intercepts requests that go to the monolithic application and routes them to either the legacy system or the new system. Because the proxy layer routes users to the correct application, you can add features to the new system while ensuring that the monolith continues to function. The new system eventually replaces all the features of the old system, and you can decommission it.

### High-level architecture
<a name="high-level-architecture.5488c6ec-4ccf-5d48-ade6-669321bc72a6"></a>

In the following diagram, a monolithic application has three services: user service, cart service, and account service. The cart service depends on the user service, and the application uses a monolithic relational database.

![Monolithic application with three services](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/4334547f-fd23-48fc-8dbb-acbca43b1b5b.png)

The first step is to add a proxy layer between the storefront UI and the monolithic application. At the start, the proxy routes all traffic to the monolithic application.

![Adding a proxy to the monolithic application](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/c58461a3-dea5-4252-85d0-fb8d30bfd025.png)

When you want to add new features to your application, you implement them as new microservices instead of adding features to the existing monolith. However, you continue to fix bugs in the monolith to ensure application stability. In the following diagram, the proxy layer routes the calls to the monolith or to the new microservice based on the API URL.

![Proxy routing calls to the monolith or to a new microservice](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/61eba37b-f357-4721-bdc5-efa0bfe8ea46.png)

#### Adding an anti-corruption layer
<a name="adding-an-anti-corruption-layer.fc8517bf-f738-5705-8e7f-e7c322cf0f8e"></a>

In the following architecture, the user service has been migrated to a microservice. The cart service calls the user service, but the implementation is no longer available within the monolith. Also, the interface of the newly migrated service might not match its previous interface inside the monolithic application. To address these changes, you implement an ACL. During the migration process, when the features within the monolith need to call the features that were migrated as microservices, the ACL converts the calls to the new interface and routes them to the appropriate microservice.

![Adding an ACL](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/ae7bfe0a-95de-41a5-966b-25c1075d6dc7.png)

You can implement the ACL inside the monolithic application as a class that's specific to the service that was migrated; for example, `UserServiceFacade` or `UserServiceAdapter`. The ACL must be decommissioned after all dependent services have been migrated into the microservices architecture.

When you use the ACL, the cart service still calls the user service within the monolith, and the user service redirects the call to the microservice through the ACL. The cart service should still call the user service without being aware of the microservice migration. This loose coupling is required to reduce regression and business disruption.

#### Handling data synchronization
<a name="handling-data-synchronization.c9f0b3fa-b897-55ab-93ff-2b30f89bf009"></a>

As a best practice, the microservice should own its data. The user service stores its data in its own data store. It might need to synchronize data with the monolithic database to handle dependencies such as reporting and to support downstream applications that are not yet ready to access the microservices directly. The monolithic application might also require the data for other functions and components that haven't been migrated to microservices yet. So data synchronization is necessary between the new microservice and the monolith. To synchronize the data, you can introduce a synchronizing agent between the user microservice and the monolithic database, as shown in the following diagram. The user microservice sends an event to the queue whenever its database is updated. The synchronizing agent listens to the queue and continuously updates the monolithic database. The data in the monolithic database is eventually consistent for the data that is being synchronized.

![Adding a synchronizing agent](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/85c5df50-c23d-4270-8202-e6329dd3ea3a.png)

#### Migrating additional services
<a name="migrating-additional-services.267af776-273e-5086-967f-356a12f1de5c"></a>

When the cart service is migrated out of the monolithic application, its code is revised to call the new service directly, so the ACL no longer routes those calls. The following diagram illustrates this architecture.

![Migrating additional services](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/83ee091a-ac3a-4171-a105-bb213ee5d651.png)

The following diagram shows the final strangled state where all services have been migrated out of the monolith and only the skeleton of the monolith remains. Historical data can be migrated to data stores owned by individual services. The ACL can be removed, and the monolith is ready to be decommissioned at this stage.

![Final strangled state](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/5e904fe6-5028-43c4-b6d5-99c835bd887d.png)

The following diagram shows the final architecture after the monolithic application has been decommissioned. You can host the individual microservices through a resource-based URL (such as `http://www.storefront.com/user`) or through their own domain (for example, `http://user.storefront.com`) based on your application's requirements. For more information about the major methods for exposing HTTP APIs to upstream consumers by using hostnames and paths, see the [API routing patterns](api-routing.md) section.

![Final architecture after decommissioning monolith](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/a9c3e90f-3c56-46bf-b4f1-d82052d3d005.png)

### Implementation using AWS services
<a name="implementation-using-aws-services.92d08836-e44d-5e5c-8720-66fac40afb87"></a>

#### Using API Gateway as the application proxy
<a name="using-api-gateway-as-the-application-proxy.c98680e3-667c-5b01-919a-455f18c6c836"></a>

The following diagram shows the initial state of the monolithic application. Let's assume that it was migrated to AWS by using a lift-and-shift strategy, so it's running on an [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) instance and uses an [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) database. For simplicity, the architecture uses a single virtual private cloud (VPC) with one private and one public subnet, and let's assume that the microservices will initially be deployed within the same AWS account. (The best practice in production environments is to use a multi-account architecture to ensure deployment independence.) The EC2 instance resides in a single Availability Zone in the public subnet, and the RDS instance resides in a single Availability Zone in the private subnet. [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) stores static assets such as the JavaScript, CSS, and React files for the website.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/b0dfd95f-f48d-4dd2-abae-ea4b6ea9bc8c.png)

In the following architecture, [AWS Migration Hub Refactor Spaces](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/what-is-mhub-refactor-spaces.html) deploys [Amazon API Gateway](https://aws.amazon.com/api-gateway/) in front of the monolithic application. Refactor Spaces creates a refactoring infrastructure inside your account, and API Gateway acts as the proxy layer for routing calls to the monolith. Initially, all calls are routed to the monolithic application through the proxy layer. As discussed earlier, proxy layers can become a single point of failure. However, using API Gateway as the proxy mitigates the risk because it is a serverless, Multi-AZ service.

**Note**
AWS Migration Hub Refactor Spaces is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform).

![Implementing the strangler fig pattern with API Gateway](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/636e0c78-75b4-431c-94fe-b82016a8ea26.png)

The user service is migrated into a Lambda function, and an [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) database stores its data. A Lambda service endpoint and default route are added to Refactor Spaces, and API Gateway is automatically configured to route the calls to the Lambda function. For implementation details, see Module 2 in the [Iterative App Modernization Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/f2c0706c-7192-495f-853c-fd3341db265a/en-US/refactor-spaces).

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/d2fc0639-be3f-449b-88e6-678e176b5bb8.png)

In the following diagram, the cart service has also been migrated out of the monolith and into a Lambda function. An additional route and service endpoint are added to Refactor Spaces, and traffic automatically cuts over to the Cart Lambda function. The data store for the Lambda function is managed by [Amazon ElastiCache](https://aws.amazon.com/elasticache/). The monolithic application still remains in the EC2 instance along with the Amazon RDS database.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/84c9ccf4-73b5-4e38-9120-d27cd51f9cc8.png)

In the next diagram, the last service (account) is migrated out of the monolith into a Lambda function. It continues to use the original Amazon RDS database. The new architecture now has three microservices with separate databases. Each service uses a different type of database. This concept of using purpose-built databases to meet the specific needs of microservices is called *polyglot persistence*. The Lambda functions can also be implemented in different programming languages, as determined by the use case. During refactoring, Refactor Spaces automates the cutover and routing of traffic to Lambda. This saves your builders the time needed to architect, deploy, and configure the routing infrastructure.

![Moving all services out of the monolith with the strangler fig pattern](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/9416bff7-e2e7-4662-bdda-46085fecfe8b.png)

#### Using multiple AWS accounts
<a name="using-multiple-aws-accounts.8967f304-9b30-5c6c-a566-49606edc89ca"></a>

In the previous implementation, we used a single VPC with a private and a public subnet for the monolithic application, and we deployed the microservices within the same AWS account for the sake of simplicity. However, this is rarely the case in real-world scenarios where microservices are often deployed in multiple AWS accounts for deployment independence. In a multi-account structure, you need to configure routing traffic from the monolith to the new services in different accounts.

[Refactor Spaces](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/what-is-mhub-refactor-spaces.html) helps you create and configure the AWS infrastructure for routing API calls away from the monolithic application. Refactor Spaces orchestrates API Gateway, Network Load Balancer, and resource-based AWS Identity and Access Management (IAM) policies inside your AWS accounts as part of its application resource. You can transparently add new services in a single AWS account or across multiple accounts to an external HTTP endpoint. All of these resources are orchestrated inside your AWS account and can be customized and configured after deployment.

Let's assume that the user and cart services are deployed to two different accounts, as shown in the following diagram. When you use Refactor Spaces, you only need to configure the service endpoint and the route. Refactor Spaces automates the [API Gateway-Lambda integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html) and the creation of Lambda resource policies, so you can focus on safely refactoring services off the monolith.

![Implementing the strangler fig pattern with Migration Hub Refactor Spaces](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/eb8395a2-e884-43f6-bf7b-a4c3c2c9f48d.png)

For a video tutorial on using Refactor Spaces, see [Refactor Apps Incrementally with AWS Migration Hub Refactor Spaces](https://www.youtube.com/watch?v=2KAyPNEi9aw).

## Workshop
<a name="strangler-fig-workshop"></a>
+ [Iterative app modernization workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/f2c0706c-7192-495f-853c-fd3341db265a/en-US)

## Blog references
<a name="strangler-fig-blog"></a>
+ [AWS Migration Hub Refactor Spaces](https://aws.amazon.com/blogs/aws/new-aws-migration-hub-refactor-spaces-helps-to-incrementally-refactor-your-applications/)
+ [Deep Dive on an AWS Migration Hub Refactor Spaces Environment](https://aws.amazon.com/blogs/mt/deep-dive-on-an-aws-migration-hub-refactor-spaces-environment/)
+ [Deployment Pipelines Reference Architecture and Reference Implementations](https://aws.amazon.com/blogs/aws/new_deployment_pipelines_reference_architecture_and_-reference_implementations/)

## Related content
<a name="strangler-fig-resources"></a>
+ [API routing patterns](api-routing.md)
+ [Migration Hub Refactor Spaces documentation](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/what-is-mhub-refactor-spaces.html)
