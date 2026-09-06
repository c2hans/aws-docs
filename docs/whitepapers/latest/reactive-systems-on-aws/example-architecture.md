---
source_url: https://docs.aws.amazon.com/whitepapers/latest/reactive-systems-on-aws/example-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Example architecture
<a name="example-architecture"></a>

To help explain how reactive principles can be applied to real world application, the following [example architecture](https://aws.amazon.com/blogs/architecture/reactive-microservices-architecture-on-aws/) implements a reactive system for the following common ad-tech use case.

 Many ad-tracking companies collect large amounts of data in near-real-time. In many cases, these workloads are very spiky and heavily depend on the success of the ad-tech company’s customers; they also need to be responsive and resilient, as these systems form part of the backbone of many ad-tech companies.

![Diagram showing an Example architecture](http://docs.aws.amazon.com/whitepapers/latest/reactive-systems-on-aws/images/example-architecture.png)

In this example architecture the system can be logically divided into one part focused on *data collection* and another part focuses on *core data updates*. The *data collection* subsystem is responsible for collecting, validating, and persisting the tracking data, potentially enriching it with some *core* data in the process. In the *core data update* subsystem, the data that is used to validate and enrich the incoming raw tracking data —this typically includes data on ad inventory, campaigns, publishers, publishers’ remaining campaign budgets, and etc.— receives updates from upstream back-office systems (not implemented in the example architecture) and notifies all subscribers about the changed and added data.

 Typically for an ad-tracking use case, the data collection subsystem can be separated further into a real-time part and a *non*-real-time part. For the real-time part, it is most important to collect data as quickly as possible and ask several questions such as:
+  Is this a valid combination of parameters?
+  Does this campaign exist?
+  Is this campaign still valid?

Because response time has a huge impact on conversion rate in advertising, it is important for advertisers to respond as quickly as possible. Any information required to decide on a response should be kept in memory to reduce communication overhead with the caching infrastructure. The tracking application itself should be as lightweight and scalable as possible. For example, the application shouldn’t have any shared mutable state. In the example architecture, one main application running in Amazon ECS is responsible for the *real-time part*, which collects and validates data, responds to the client as fast as possible, and asynchronously sends events to backend systems.

 The *non-real-time* part of the application consumes the generated events and persists them in a NoSQL database. In a standard tracking implementation this includes clicks, cookie information, and transactions; once stored, these are later matched asynchronously and persisted in a data store. At the time of publication, matching is not implemented in the example architecture. However, you can use big-data frameworks like Hadoop or Spark for the matching implementation. The results of this matching process and other back-office processes (fraud checks, billing of providers of ad inventory, payouts to ad space providers, and etc.) often result in updates to the *core data*, and is then fed back into the *core data updates* subsystem via an event stream.

 In the example architecture shown in the architecture diagram, the request (ad impression or clicked ad) is ingested to the Application Load Balancer which routes the incoming request to one of the service instances in the main application. The L1 cache – which is stored in the memory of the application - stores the most recent core data updates. In addition, there is an open connection to the L2 cache. The application processes each incoming request separately. It is implemented in a responsive and resilient manner and doesn’t write directly to a database: using Amazon Kinesis Data Streams new events are added to a data stream and consumed by an AWS Lambda function which writes the data into an Amazon DynamoDB table. The data stream – implemented with Amazon Kinesis Data Streams - acts as a main buffer to decouple the database from the application and ensure that this event data under load isn’t lost.

 With this architecture you can reliably process a huge number of events and store them safely. The application does not live in a vacuum - typically, it needs to rely on other data that is not present in the event. In the ad tech example, this *core data* would include information about the available event inventory, the ad publishers, their budgets and preferences, etc. This data lives in a variety of upstream systems - the challenge is that it needs to be available to our application at any time and without having to wait for the source system. To reduce latency of access to this *core data* and to simplify the architecture, Amazon ElastiCache (Redis OSS) is used as the main interface, which means all the necessary data is cached for the application. As with any cache, you still need to track updates to our core data sets. These source systems are out of scope for this whitepaper, but assume that you get update events whenever something changes. In this situation, you rely on message-passing. The application offers an event stream that all the source systems can write to whenever they see a change. This offers a fairly minimal interface to the outside world and decouples it from our system; using Kinesis Data Streams you can handle various request rates without having to worry a lot about the infrastructure. In some situations, you might have to deal with different request rates and many different types of data, depending on how many source systems the core data comes from. Similar to how this is done in the main event pipeline, you can use a Lambda function to have an elastic, resilient processing mechanism to process new data on the stream and updates the main cache to make it available to the application.

## Using an event driven and non-blocking framework
<a name="using-an-event-driven-and-non-blocking-framework"></a>

The main application in the example architecture, is using a framework called [Eclipse Vert.x](https://vertx.io/), which is a toolkit for building reactive applications on the JVM. Vert.x is *event driven* and *non-blocking*. This means Vert.x applications can handle a large number of concurrent connections using a small number of kernel threads. The same or similar patterns and paradigms can be used with Akka, Micronaut or other frameworks. Vert.x uses a simple, scalable, actor-like deployment and concurrency model based on so called verticles which are chunks of code extending an abstract class. Due to the polymorphic nature of Vert.x, verticles can be implemented in different languages and a single application can consist of verticles written in multiple languages. The verticles communicate with each other using the event bus - which supports publish/subscribe, point-to-point, and request-response messaging - by sending messages. In the example architecture this means that is has the same architectural principles on a micro- as well as on a macro-level. The different parts of the architecture communicate by exchanging messages and this also applies to the internal communication of the main application.

 In most cases Vert.x calls your handlers using a thread called an event loop. Aside from the updates to the external Redis cache the application also keeps its own L1, in-process cache. Whenever the Redis cache is updated, you need to update the in-process cache. Going with the design principles you will want to get these updates pushed into the application. But why is it necessary to store data in a L1-cache? This is important to distribute core data changes using Redis, because it is necessary to reduce the number of accesses to the L2-cache. After 10 minutes the data is automatically invalidated and a data refresh is necessary. This behavior is a trade-off, because you might run into situation where you have to deal with stale data. Doing so also protects the application from failures that cause the Redis cluster to become unreachable or slows down its responses. The following code snippet shows an excerpt from the verticle which is responsible for the communication with Redis, that you can use to subscribe to the event bus.

```
void registerToEventBusForPubSub(final EventBus eb) {
    eb.<JsonObject>consumer(REDIS_PUBSUB_CHANNEL_VERTX)
            .handler(received -> {
                JsonObject value = received.body().getJsonObject("value");

                String message = value.getString("message");

                JsonObject jsonObject = new JsonObject(message);
                eb.send(CACHE_REDIS_EVENTBUS_ADDRESS, jsonObject);
            });
    redis.connect()
            .onSuccess(conn -> {
                conn
                        .send(cmd(SUBSCRIBE).arg(Constants.REDIS_PUBSUB_CHANNEL))
                        .onSuccess(res -> LOGGER.info("Subscribed to " + Constants.REDIS_PUBSUB_CHANNEL))
                        .onFailure(err -> LOGGER.info("Subscription failed: " + err.getMessage()));

            })
            .onFailure(err -> LOGGER.info("Failure during connection: " + err.getMessage()));
}
```

 In this code snippet, the Redis client first subscribes to the Redis channel using `redis.connect()`. After successful subscription, data is sent to the verticle over the event bus. The verticle unwraps the data and sends it to the caching verticle to store the data in the L1-cache. This is a very fast and lightweight implementation and you can reuse existing infrastructure, because Redis is already being used for caching purposes.
