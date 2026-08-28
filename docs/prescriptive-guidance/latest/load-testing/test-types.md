---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/test-types.html
---

# Load test types
<a name="test-types"></a>

The following test types are based on the foundational questions listed earlier in the guide.

## How much load can my application withstand?
<a name="load-size"></a>

When setting up a test to determine the load that your application can withstand, first decide whether you want to measure in requests per second (req/s), response time (seconds), or in concurrent users. For either case, define which part of the application is tested.
+ Browsing the site is a load that is achieved by visiting a number of pages or endpoints, or by requesting data from a single endpoint using different parameters for each request. You can often achieve this by using the basic tools described in the *Tools to use* section. Because a cache is often a vital component of an application, decide whether you want to include a caching layer in the test.
+ Testing transactional workflows, such as a checkout where requests depend on each other and carry data forward between requests, require more complex tools. Also, because the measure of requests has limited relevance in the context of a multiple-step transaction, it's more accurate to count the whole transaction, which must be emitted as a separate datapoint by the tool. The Apache JMeter and k6 tools can be configured to provide these datapoints.

Define the acceptable threshold for the performance and error rate of your target system. For some systems, you might not care about response times as long as the event is successfully processed. For many applications, such as those with user interaction, define limits for what is acceptable for the end user.

It's often helpful to perform the tests in steps. The load is increased with each step until you reach the defined threshold. For repeated tests, you can learn from previous tests and improve your stepping to perform fewer steps in a test and still gain valid results.

## Can my application handle X load?
<a name="x-load"></a>

Similar to the previous test, the load in this test can be defined as req/s or as concurrent users, depending on the nature of the application you are testing. This test is a simplified version of the previous one. Here, a specific workloadmust be submitted, and the system should be able to handle it. It's important to choose a testing tool that supports specifying the load volume that you require.

The time to run the test can also be relevant. Some effects can be observed only when a test is run over a longer period of time. For example, back pressure can cause queues to overload. If you want to replicate a production system and draw valid conclusions, the time required to run the test can affect the sizing of the test system.

## Does my application automatically scale up and down?
<a name="scaling"></a>

Elasticity is a key selling point of the cloud, and it's a key source of cost reduction. Testing whether your application is properly scaling, so that you can confidently benefit from the elasticity, should be part of your cloud journey.

Key metrics that are used to scale up and down need to be identified. Typically, this is CPU load of the target systems. An endpoint that creates CPU load can be used as the target.

Because this test doesn't require representability, you can benefit from targeting an endpoint that is free from side effects. You also don't want to initiate a flow that persists data that could accumulate, or that initiates subsequent processes and induces either unnecessary costs or blocks the load.

Perform the test in a stepped process, gradually increasing the load. The intervals should be long enough so that on each step, the metrics are able to initiate the scaling. For example, if you have as a rule that the CPU load shall be higher than 70 percent over a period of 5 minutes, your steps should be longer than 5 minutes to provide time for the scaling event to be initiated and run. You also want to see that the scaling was working and remediated the load situation that you created.

Consider starting your scaling test with more than one server. In a small environment, scaling up can be slow and require multiple cycles to cope with the load. And an EC2 Auto Scaling cluster can only double in size. This means that if you start with one server and start the load test, the maximum first scaling event can only be two servers. If the load generated required three servers, you would need two scaling events, which could take 20 minutes or longer.

Monitor the desired trigger for the scale up event and whether scaling was appropriate for the actual load.

If you have implemented a scale down event, you can also test this in a stepped manner. Monitor whether the scale down is applicable and appropriate for the existing load, and confirm that it doesn't initiate an immediate scale up again.

## Does my application behavior degrade over time with a constant high load?
<a name="constant"></a>

Some effects can be observed only when load is generated over a prolonged period of time. One of the most important effects is back pressure. This means that when a system is too slow to process the number of requests at the speed that they are coming, the performance of its client systems will degrade.

This is easier to observe if the slow system is the load target. In a more complex setup, you can observe the effect only when the impact of the load test propagates. A tracing solution that is able to visualize the response times between each of the services in a distributed system not only shows the results faster, but can help to identify the system that is acting as a bottleneck. You can identify the bottleneck system by obtaining the message correlation ID from the log files. Each request retains the same ID across all the systems that go through the load test.

Using a correlation ID helps you track the whole journey of a single message through all the different components in your platform. With this information, you can calculate the processing time for each single component that your message is traversing (processing\_time = departure\_time – arrival\_time) and identify the slowest one. [Zipkin](https://zipkin.io/), [Jaeger](https://www.jaegertracing.io/), and [AWS X-Ray](https://aws.amazon.com/xray/) are prominent solutions in this space.

For the most reliable results, choose a tool that supports setting a *constant request rate*. This means that if the target system is getting slower, the concurrency of the test tool must increase of keep the req/s constant. When the system starts to respond more slowly, it will tie up more threads and lower the request rate of your load-generating tool. A tool with a constant request rate must increase concurrency when happens, and you will see failure faster. Instead of measuring degradation by achieved req/s, you will measure by latency and even failed requests.

## Is my application working?
<a name="working"></a>

This is not a typical load-testing domain, but you can use load-testing tools to perform basic tests such as checking a number of endpoints. Scenarios performed by complex tools can verify more complex behavior. On a blogging website a check would not only include reading posts, but also creating a blog post or commenting on one. For a shopping website, this could be a full transaction, including browsing the catalog, selecting two products, going through the checkout process, and making the purchase.

Usually, you would not create high load but rather a sensible number of requests that verify functionality. You can also do this periodically against production, when the customers are not visiting the tested flows, to have another layer of monitoring.

As a shortcut, scenarios already created for load testing can be reused on production with a lower load configured.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
