---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/scatter-gather.html
---

# Scatter-gather pattern
<a name="scatter-gather"></a>

## Intent
<a name="scatter-gather-intent"></a>

The scatter-gather pattern is a message routing pattern that involves broadcasting similar or related requests to multiple recipients, and aggregating their responses back into a single message by using a component called an *aggregator*. This pattern helps achieve parallelization, reduces processing latency, and handles asynchronous communication. It's straightforward to implement the scatter-gather pattern by using a synchronous approach, but a more powerful approach involves implementing it as message routing in asynchronous communication, either with or without a messaging service.

## Motivation
<a name="scatter-gather-motivation"></a>

In application processing, a request that might take a long time to process sequentially can be split into multiple requests that are processed in parallel. You can also send requests to multiple external systems through API calls to get a response. The scatter-gather pattern is useful when you need input from multiple sources. Scatter-gather aggregates the results to help you make an informed decision or to select the best response for the request.

The scatter-gather pattern consists of two phases, as its name implies:
+ The *scatter phase* processes the request message and sends it to multiple recipients in parallel. During this phase, the application scatters requests across the network and continues to run without waiting for immediate responses.
+ During the *gather phase*, the application collects the responses from recipients, and filters or combines them into a unified response. When all the responses have been collected, they can either be aggregated into a single response or the best one can be chosen for further processing.

## Applicability
<a name="scatter-gather-applicability"></a>

Use the scatter-gather pattern when:
+ You plan to aggregate and consolidate data from various APIs to create an accurate response. The pattern consolidates information from disparate sources into a cohesive whole. For example, a booking system can make a request to multiple recipients to get quotes from multiple external partners.
+ The same request has to be sent to multiple recipients simultaneously to complete a transaction. For example, you can use this pattern to query inventory data in parallel to check a product's availability.
+ You want to implement a reliable and scalable system where load balancing can be achieved by distributing requests across multiple recipients. If one recipient fails or experiences a high load, other recipients can still process requests.
+ You want to optimize performance when implementing complex queries that involve multiple data sources. You can scatter the query to relevant databases, gather the partial results, and combine them into a comprehensive answer.
+ You are implementing a type of map-reduce processing where the data request is routed to multiple data processing endpoints for sharding and replication. Partial results are filtered and combined to compose the right response.
+ You want to distribute write operations across a partition key space in write-heavy workloads in key-value databases. The aggregator reads the results by querying the data in each shard, and then consolidates them into a single response.

## Issues and considerations
<a name="scatter-gather-issues"></a>
+ **Fault tolerance**: This pattern relies on multiple recipients that work in parallel, so it is essential to handle failures gracefully. To mitigate the impact of recipient failures on the overall system, you can implement strategies such as redundancy, replication, and fault detection.
+ **Scale-out limits**: As the total number of processing nodes increases, the associated network overhead also increases. Every request that involves communication over the network can increase latency and negatively affect the benefits of parallelization.
+ **Response time bottlenecks**: For operations that require all the recipients to be processed before the final processing is done, the performance of the overall system is constrained by the slowest recipient's response time.
+ **Partial responses**: When requests are scattered to multiple recipients, some recipients can time out. In these cases, the implementation should communicate to the client that the response is incomplete. You can also display the response aggregation details by using a UI frontend.
+ **Data consistency**: When you process data across multiple recipients, you must carefully consider data synchronization and conflict resolution techniques, to ensure that the final aggregated results are accurate and consistent.

## Implementation
<a name="scatter-gather-implementation"></a>

### High-level architecture
<a name="high-level-architecture.bff238f5-b571-51c6-b150-6f537d652b53"></a>

The scatter-gather pattern uses a root controller to distribute requests to recipients that will process the requests. During the scatter phase, this pattern can use two mechanisms to send messages to recipients:
+ Scatter by distribution: The application has a known list of recipients that must be called to get the results. The recipients can be different processes that have unique functions or a single process that has been scaled out to distribute the processing load. If any of the processing nodes time out or show delays in responding, the controller can redistribute processing to another node.
+ Scatter by auction: The application broadcasts the message to interested recipients by using a [publish-subscribe pattern](publish-subscribe.md). In this case, recipients can subscribe to the message or withdraw from the subscription at any point.

#### Scatter by distribution
<a name="scatter-by-distribution.1928d902-d02e-5f1f-a48d-d0fada149828"></a>

In the scatter by distribution method, the root controller divides the incoming request into independent tasks and assigns them to available recipients (the *scatter* phase). Each recipient (process, container, or Lambda function) works independently and in parallel on its computation, and produces a portion of the response. When the recipients complete their tasks, they send their responses to an aggregator (the *gather* phase). The aggregator combines the partial responses and returns the final result to the client. The following diagram illustrates this workflow.

![Scatter by distribution method for the scatter-gather pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/c00f559a-a88a-4a4b-ba60-1dd8b2190dc9.png)

The controller (data file processor) orchestrates the entire set of invocations, and is aware of all the booking endpoints to call. It can configure a timeout parameter to ignore responses that take too long. When the requests have been sent, the aggregator waits for the responses back from each endpoint. To implement resilience, each microservice can be deployed with multiple instances for load balancing. The aggregator gets the results, combines them into a single response message, and removes duplicate data before further processing. The responses that time out are ignored. The controller can also act as an aggregator instead of using a separate aggregator service.

#### Scatter by auction
<a name="scatter-by-auction.da54d17c-e970-5845-b263-10bfb001e3a0"></a>

If the controller isn't aware of the recipients or the recipients are loosely coupled, you can use the scatter by auction method. In this method, the recipients subscribe to a topic and the controller publishes the request to the topic. Recipients publish the results to a response queue. Because the root controller isn't aware of the recipients, the gathering process uses an aggregator (another messaging pattern) to collect the responses and distill them into a single response message. The aggregator uses a unique ID to identify a group of requests.

For example, in the following diagram, the scatter by auction method is used to implement a flight booking service for an airline's website. The website allows users to search and display flights from the airline's own carrier and its partners' carriers, and must display the status of the search in real time. The flight booking service consists of three search microservices: non-stop flights, flights with stops, and partner airlines. The partner airline search calls the partner's API endpoints to get the responses.

![Scatter by auction method for the scatter-gather pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/4e616708-4372-4395-a653-ef927a908379.png)

1. The flight booking service (controller) takes the search criteria as input from the client, and processes and publishes the request to the topic.

1. The controller uses a unique ID to identify each group of requests.

1. The client sends the unique ID to the aggregator for step 6.

1. The booking search microservices that have subscribed to the booking topic receive the request.

1. The microservices process the request and return seat availability for the given search criteria to a response queue.

1. The aggregator collates all the response messages that are stored in a temporary database, groups the flights by unique ID, creates a single unified response, and sends it back to the client.

### Implementation using AWS services
<a name="implementation-using-9999999999999999aws-services-.abdca170-a218-54ec-964b-95fec4dcc396"></a>

#### Scatter by distribution
<a name="scatter-by-distribution.da0135b9-a06e-5e38-b758-9016ea3ac47d"></a>

In the following architecture, the root controller is a data file processor (Amazon ECS) that splits the incoming request data into individual Amazon Simple Storage Service (Amazon S3) buckets and starts an AWS Step Functions workflow. The workflow downloads the data and initiates parallel file processing. The `Parallel` state waits for all the tasks to return a response. An AWS Lambda function aggregates the data and saves it back to Amazon S3.

![Implementing the scatter by distribution method on AWS - architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/8b68cf03-c874-479c-986e-8fddd1413e4c.png)

The following diagram illustrates the Step Functions workflow with the `Parallel` state.

![Implementing the scatter by distribution method on AWS - Step Functions workflow](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/a07fb547-098e-4501-a605-a72609ce98fd.png)

#### Scatter by auction
<a name="scatter-by-auction.a630a35c-038a-5885-89f9-31b48f5acba6"></a>

The following diagram shows an AWS architecture for the scatter by auction method. The root controller **flight booking service **scatters the flight search request to multiple microservices. A publish-subscribe channel is implemented with Amazon Simple Notification Service (Amazon SNS), which is a managed messaging service for communications. Amazon SNS supports messages between decoupled microservice applications or direct communications to users. You can deploy the recipient microservices on Amazon Elastic Kubernetes Service (Amazon EKS) or Amazon Elastic Container Service (Amazon ECS) for better management and scalability. **The flight results service** returns the results to the client. It can be implemented in AWS Lambda or other container orchestration services such as Amazon ECS or Amazon EKS.

![AWS architecture for scatter by auction method](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/de9ade8a-1f31-4bf2-875e-6c9ace06a239.png)

1. The flight booking service (controller) takes the search criteria as input from the client, and processes and publishes the request to the SNS topic.

1. The controller publishes the unique ID to an Amazon Aurora database to identify the request.

1. The client sends the unique ID to the client for step 6.

1. The booking search microservices that have subscribed to the booking topic receive the request.

1. The microservices process the request and return seat availability for the given search criteria to a response queue in Amazon Simple Queue Service (Amazon SQS). The aggregator collates all the response messages and stores them in a temporary database.

1. The flight results service groups the flights by unique ID, creates a single unified response, and sends it back to the client.

If you want to add another airline search to this architecture, you add a microservice that subscribes to the SNS topic and publishes to the SQS queue.

To summarize, the scatter-gather pattern enables distributed systems to achieve efficient parallelization, reduce latency, and seamlessly handle asynchronous communication.

### GitHub repository
<a name="github-repository.a34f9484-5db7-51f0-b156-2f5ebf5ceb00"></a>

For a complete implementation of the sample architecture for this pattern, see the GitHub repository at [https://github.com/aws-samples/asynchronous-messaging-workshop/tree/master/code/lab-3](https://github.com/aws-samples/asynchronous-messaging-workshop/tree/master/code/lab-3).

## Workshop
<a name="scatter-gather-workshop"></a>
+ [Scatter-gather lab](https://catalog.us-east-1.prod.workshops.aws/workshops/e8738cf6-6eb0-4d1d-9e98-ae240d229535/en-US/scatter-gather) in the *Decoupled Microservices* workshop

## Blog references
<a name="scatter-gather-blog"></a>
+ [Application integration patterns for microservices](https://aws.amazon.com/blogs/compute/application-integration-patterns-running-distributed-rfqs/)

## Related content
<a name="scatter-gather-resources"></a>
+ [Publish-subscribe pattern](publish-subscribe.md)
