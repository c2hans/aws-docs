---
source_url: https://docs.aws.amazon.com/whitepapers/latest/reactive-systems-on-aws/characteristics-of-reactive-systems.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Characteristics of reactive systems
<a name="characteristics-of-reactive-systems"></a>

 The following sections outline the essential characteristics of reactive systems.

## Responsive
<a name="responsive"></a>

 Responsiveness means that systems respond in a timely manner. It is crucial to reduce latency between request and response. Latency is an important factor that can, under certain circumstances, be decisive for the success or failure of a service. It directly influences the behavior of the consumer of the website or webservice. Imagine, you want to check out your shopping cart on an e-commerce website and processing of the payment takes a significant amount of time or even crashes. This results in an overall bad user experience. Latency is often correlated with conversion rate. Responding in a timely manner ensures these systems deliver a consistent behavior and quality of service.

## Resilient
<a name="resilient"></a>

 A resilient system stays responsive in the face of failure. A resilient workload has the capability to recover when stressed by load, attacks, and failure of any component in the workload's components. If a failure occurs in one component, this must be contained in the source of the failure by isolating it from others. As a result, this prevents a small failure from causing a major outage of the complete system.

## Elastic
<a name="elastic"></a>

 A reactive architecture remains responsive under varying workload. This elasticity requires you to be able to scale a system dynamically and add or remove resources to react to changes which leads to the avoidance of bottlenecks. These systems support predictive as well as reactive scaling based on metrics which leads to an efficient use of resources.

## Message driven
<a name="message-driven"></a>

In order to establish boundaries between services, reactive systems rely on asynchronous message-passing. This helps ensure loose coupling, isolation, and location transparency. Location transparency can be achieved by using a message queue or a similar system to access data without the explicit knowledge of the location. This can be achieved using network resources like DNS. The main advantage of this approach is that it’s not important where exactly the resource is located. This is key for resiliency and elasticity, because a failover mechanism can be implemented that abstracts the actual resource behind a network name. In reactive systems, asynchronous message-passing is also used to distribute information of failures or other errors as messages. By using this pattern, the system enables better load management by monitoring the message queues and implementing a mechanism for [backpressure](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/). This allows non-blocking communication which leads to less system overhead. One of the biggest challenges to effectively scale large systems is the bottleneck that is introduced by shared resources. This communication pattern helps minimizing concurrent access.

 But what’s the difference between message-driven and event-driven? According to K. Mani Chandy, Professor of Computer Science at the California Institute of Technology, events can be defined as [https://docplayer.net/15630715-Event-driven-applications-costs-benefits-and-design-approaches-gartner-application-integration-and-web-services-summit-2006.html](https://docplayer.net/15630715-Event-driven-applications-costs-benefits-and-design-approaches-gartner-application-integration-and-web-services-summit-2006.html) ( K.Mani Chandy Event-Driven Applications: Costs, Benefits and Design Approaches, California Institute of Technology, 2006). An event can be a change in an AWS environment. For example, [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) generates events when it launches or terminates instances. A message however has a clear direction: it’s a command sent to a system. The destination reacts on the message and starts an action.

## Observability and tracing
<a name="observability-and-tracing"></a>

As already outlined, reactive systems are defined as message-driven and resilient, which means, a reactive system - by nature - will be a distributed system. This necessarily includes additional network communication. In a traditional monolithic application (for example, a JavaEE application) the complete application resides in the same memory on one device, potentially with full redundant copies on other machines to allow for failover. In many cases, monolithic applications have better latency compared to distributed application but with limitations in scalability and availability. The example application discussed later shows patterns and best practices to reduce latency, but in many cases, workloads that have very low latency requirements such as high-frequency trading, are not good candidates for reactive systems. Due to the distributed nature of reactive systems that involve communication over network and across server-boundaries, the additional latency has a huge impact on the performance of the overall application.

 If there is an error in a traditional monolithic application, for example an exception was found in one of the log files, debugging this problem is often relatively easy due to the non-distributed nature of the application. A typical microservices based application that passes messages for communication is harder to debug, because it is sometimes not possible to reproduce the exact state of the complete system and replay events in order to reproduce issues. Each service has a separate log file, even though those log files are often consolidated in a central system such as [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) or [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/). An additional critical piece of the puzzle is to correlate an event with a specific set of log entries. Each event needs a unique identifier which needs to be logged on each step of its journey through different microservices. You can add the following [tracing header](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-tracingheader) to incoming HTTP requests that don't already have one using services such [as Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) or [Amazon API Gateway](https://aws.amazon.com/api-gateway/):

```
X-Amzn-Trace-Id: Root=1-5759e988-bd862e3fe1be46a994272793
```

 This tracing header can be used to correlate events with log entries. In addition, you can use services such as [AWS X-Ray](https://aws.amazon.com/xray/) to trace and analyze requests as they travel through your entire system, from Application Load Balancer or Amazon API Gateway APIs to the underlying services, making it much easier to identify issues and visualize service calls. AWS X-Ray helps developers analyze and debug production, distributed applications, which are built using a microservices architecture. X-Ray’s service maps let you see relationships between services and resources in your application in real time. You can easily detect where high latencies are occurring, visualize node and edge latency distribution for services, and then drill down into the specific services and paths impacting application performance.

## Reactive programming and reactive streams
<a name="reactive-programming-and-reactive-streams"></a>

It is important to make a distinction between reactive systems and reactive programming because these two completely different concepts are often confused. Reactive systems are responsive, resilient, elastic, and message driven as per preceding paragraphs. This description shows that reactive systems are an architectural approach to design distributed responsive systems. Reactive programming, however, is a software design approach which focusses on asynchronous data streams. Everything in the application is seen as a stream of data which can be observed (observer pattern). An interesting approach to simplify the challenges of reactive programming are [Reactive eXtensions](http://reactivex.io/) , an “*API for asynchronous programming with observable streams*”. Reactive Programming can help to build a system based on the principles of the Reactive Manifesto, but the use of reactive programming doesn’t necessarily mean that a system is reactive.

 [Reactive Streams](https://www.reactive-streams.org/) is an initiative to define a standard for asynchronous stream processing with non-blocking backpressure. The main goal of this concept is to control the exchange of streaming data across an asynchronous boundary. Backpressure is an integral part of this model: The recipient is only sent as much data as it can process or buffer in and the receiver explicitly requests the data according to its capacity. This means, the sender may only send as much data as the receiver has requested.

 The goal behind the Reactive Streams’ specification is to create the basis for compatible implementations that can communicate with each other. This specification includes a minimal set of interfaces, methods, and protocols, that define operations and entities that are necessary to implement a compatible version.
