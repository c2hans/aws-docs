---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/communication-mechanisms.html
---

# Communication mechanisms
<a name="communication-mechanisms"></a>

 In the microservices paradigm, various components of an application must communicate over a network. Common approaches for this include REST-based, GraphQL-based, gRPC-based, and asynchronous messaging.

## REST-based communication
<a name="rest-based-communication"></a>

 The HTTP/S protocol, used broadly for synchronous communication between microservices, often operates through RESTful APIs. API Gateway offers a streamlined way to build an API that serves as a centralized access point to backend services, handling tasks like traffic management, authorization, monitoring, and version control.

## GraphQL-based communication
<a name="graphql-based-communication"></a>

 Similarly, GraphQL is a widespread method for synchronous communication, using the same protocols as REST but limiting exposure to a single endpoint. With AWS AppSync, you can create and publish GraphQL applications that interact with AWS services and datastores directly, or incorporate Lambda functions for business logic.

## gRPC-based communication
<a name="grpc-based-communication"></a>

 gRPC is a synchronous, lightweight, high performance, open-source RPC communication protocol. gRPC improves upon its underlying protocols by using HTTP/2 and enabling more features such as compression and stream prioritization. It uses Protobuf Interface Definition Language (IDL) which is binary-encoded and thus takes advantage of HTTP/2 binary framing.

## Asynchronous messaging and event passing
<a name="asynchronous-messaging-and-event-passing"></a>

Asynchronous messaging allows services to communicate by sending and receiving messages through a queue. This enables services to remain loosely coupled and promote service discovery.

Messaging can be defined of the following three types:
+  **Message Queues:** A message queue acts as a buffer that decouples senders (producers) and receivers (consumers) of messages. Producers enqueue messages into the queue, and consumers dequeue and process them. This pattern is useful for asynchronous communication, load leveling, and handling bursts of traffic.
+  **Publish-Subscribe:** In the publish-subscribe pattern, a message is published to a topic, and multiple interested subscribers receive the message. This pattern enables broadcasting events or messages to multiple consumers asynchronously.
+  **Event-Driven Messaging:** Event-driven messaging involves capturing and reacting to events that occur in the system. Events are published to a message broker, and interested services subscribe to specific event types. This pattern enables loose coupling and allows services to react to events without direct dependencies.

 To implement each of these message types, AWS offers various managed services such as Amazon SQS, Amazon SNS, Amazon EventBridge, Amazon MQ, and Amazon MSK. These services have unique features tailored to specific needs:
+  **Amazon Simple Queue Service (Amazon SQS) and Amazon Simple Notification Service (Amazon SNS):** As you can see in Figure 8, these two services complement each other, with Amazon SQS providing a space for storing messages and Amazon SNS enabling delivery of messages to multiple subscribers. They are effective when the same message needs to be delivered to multiple destinations.
![Diagram showing Message bus pattern on AWS](http://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/images/message-bus-pattern.png)
+  **Amazon EventBridge:** a serverless service that uses events to connect application components together, making it easier for you to build scalable event-driven applications. Use it to route events from sources such as home-grown applications, AWS services, and third- party software to consumer applications across your organization. EventBridge provides a simple and consistent way to ingest, filter, transform, and deliver events so you can build new applications quickly. EventBridge event buses are well suited for many-to-many routing of events between event-driven services.
+  **Amazon MQ:** a good choice if you have a pre-existing messaging system that uses standard protocols like JMS, AMQP, or similar. This managed service provides a replacement for your system without disrupting operations.
+  **Amazon MSK (Managed Kafka): **a messaging system for storing and reading messages, useful for cases where messages must be processed multiple times. It also supports real-time message streaming.
+  **Amazon Kinesis:** real-time processing and analyzing of streaming data. This allows for the development of real-time applications and provides seamless integration with the AWS ecosystem.

 Remember, the best service for you depends on your specific needs, so it's important to understand what each one offers and how they align with your requirements.

## Orchestration and state management
<a name="orchestration-and-state-management"></a>

 Microservices orchestration refers to a centralized approach, where a central component, known as the orchestrator, is responsible for managing and coordinating the interactions between microservices. Orchestrating workflows across multiple microservices can be challenging. Embedding orchestration code directly into services is discouraged, as it introduces tighter coupling and hinders replacing individual services.

 Step Functions provides a workflow engine to manage service orchestration complexities, such as error handling and serialization. This allows you to scale and change applications quickly without adding coordination code. Step Functions is part of the AWS serverless platform and supports Lambda functions, Amazon EC2, Amazon EKS, Amazon ECS, SageMaker AI, AWS Glue, and more.

![Diagram of a microservices workflow invoked by AWS Step Functions](http://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/images/microservices-workflow-with-steps.png)

[Amazon Managed Workflows for Apache Airflow](https://aws.amazon.com/managed-workflows-for-apache-airflow/) (Amazon MWAA) is an alternative to Step Functions. You should use Amazon MWAA if you prioritize open source and portability. Airflow has a large and active open-source community that contributes new functionality and integrations regularly.
