---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/integration.html
---

# Determining the integration approach for microservices in MES
<a name="integration"></a>

In a microservice-based MES, service-to-service communication is essential to exchange data, share information, and ensure seamless operations. MES microservices can exchange data on specific events or at regular intervals. For example, a user might provide the production quantity during a production confirmation transaction. Such a transaction can initiate several transactions in the background, such as sending the information to ERP, capturing the running hours of the machine, capturing quality information about products, and reporting labor hours. Different microservices could be responsible for these tasks, yet a single event initiates all of them through one microservice.

Furthermore, an MES also integrates with external systems to optimize manufacturing operations, connect end-to-end digital threads, and process automation. When you build a microservice-based MES, you must decide on the strategy for handling integration with internal and external services.

The following functional patterns provide guidelines on selecting the right technology based on the type of communications required.

## Synchronous communications
<a name="synchronous-communications.571b7c3c-22f2-5860-9f44-2d3f865d2c65"></a>

In a synchronous communications pattern, the calling service is blocked until it receives a response from the endpoint. The endpoint can typically call other services for additional processing. MES requires synchronous communications for latency-sensitive transactions. For example, consider a continuous production line where one user completes an operation on an order. The next user would expect to see that order immediately arrive for the next operation. Any delay in such transactions could negatively impact the product's cycle time and plant performance KPIs, and could cause additional wait time and under-utilization of resources.

![Synchronous communications in MES](http://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/images/guide-img/093538ca-c7c9-4311-a0e9-8a876ae66d65/images/f65d09de-3792-4aa2-8665-bc47e7b42253.png)

## Asynchronous communications
<a name="asynchronous-communications.593489f4-7d75-5224-bdc8-d7b063c72ebc"></a>

In this communication pattern, the caller doesn't wait for a response from the endpoint or from another service. MES adopts this pattern when it can tolerate latency without negatively affecting the business transaction. For example, when a user completes an operation by using a machine, you might want to report the run hours of that machine to the maintenance microservice. This communication can be asynchronous, because updating run hours doesn't immediately initiate an event or affect the operation's completion.

![Asynchronous communications in MES](http://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/images/guide-img/093538ca-c7c9-4311-a0e9-8a876ae66d65/images/7166a2e8-70a5-448e-b4bb-4ef416802d6f.png)

## Pub/sub pattern
<a name="pub-sub-pattern.a918a812-c10b-50e6-b912-b90a04fba402"></a>

The publish/subscribe (pub/sub) pattern further extends asynchronous communications. Managing interdependent communications can become challenging as the MES matures and the number of microservices grows. You might not want to change a caller service every time you add a new service that has to listen to it. The pub/sub pattern solves this by enabling asynchronous communications among multiple microservices without tight coupling. In this pattern, a microservice publishes event messages to a channel that subscriber microservices can listen to. Therefore, when you add a new service, you subscribe to the channel without changing the publishing service. For example, a production report or operation-complete transaction might update several log and transaction history records. Instead of modifying these transactions whenever you add new logging services for machines, labor, inventory, external systems, and so on, you can subscribe each new service to the original transaction's message and handle it separately.

![Pub/sub communications in MES](http://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/images/guide-img/093538ca-c7c9-4311-a0e9-8a876ae66d65/images/355bb00e-ce3a-4c9c-a8ba-2d698dedb7ce.png)

## Hybrid communications
<a name="hybrid-communications.d2f2604e-fadf-57a9-a2cc-5dc49953f831"></a>

Hybrid communication patterns combine synchronous and asynchronous communication patterns.

AWS offers multiple [serverless services](https://aws.amazon.com/serverless/) that can be combined in different ways to produce the desired communication pattern. The following table lists some of the prominent AWS services and their key features.

|
|
| AWS service | Description | Supports pattern |
| --- |--- |--- |
| **Synchronous** | **Asynchronous** | **Pub/sub** |
| [Amazon API Gateway](https://aws.amazon.com/api-gateway/) | Enables microservices to access data, business logic, or functionality from other microservices.  API Gateway accepts and processes concurrent API calls for all three communication patterns. |  |  |  |
| [AWS Lambda](https://aws.amazon.com/lambda/) | Provides serverless, event-driven compute functionality to run code without managing servers. Businesses can use Lambda to decouple, process, and pass data between other AWS services such as databases and storage services. |  |  |  |
| [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/) | Supports application-to-application (A2A) and application-to-person (A2P) messaging. A2A provides high-throughput, push-based messaging between distributed systems, microservices, and serverless applications. A2P functionality lets you send messages to people with SMS texts, push notifications, and email. |   |  |  |
| [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) | Lets you send, store, and receive messages between software components at any volume without losing messages or requiring other services to be available. |   |  |  |
| [Amazon EventBridge](https://aws.amazon.com/eventbridge/) | Provides real-time access to events caused by changes in data in a microservice or an AWS service within a microservice without writing code. You can then receive, filter, transform, route, and deliver this event to the target. |   |  |  |
| [Amazon MQ](https://aws.amazon.com/amazon-mq/) | Managed message broker service that streamlines the setup, operation, and management of message brokers on AWS. Message brokers allow software systems, which often use different programming languages on various platforms, to communicate and exchange information. |   |   |  |

For more information, see [Integrating microservices by using AWS serverless services](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/welcome.html) on the AWS Prescriptive Guidance website.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
