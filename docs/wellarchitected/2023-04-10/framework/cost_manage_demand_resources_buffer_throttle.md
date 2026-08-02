---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/cost_manage_demand_resources_buffer_throttle.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST09-BP02 Implement a buffer or throttle to manage demand
<a name="cost_manage_demand_resources_buffer_throttle"></a>

 Buffering and throttling modify the demand on your workload, smoothing out any peaks. Implement throttling when your clients perform retries. Implement buffering to store the request and defer processing until a later time. Verify that your throttles and buffers are designed so clients receive a response in the required time.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

**Throttling:** If the source of the demand has retry capability, then you can implement throttling. Throttling tells the source that if it cannot service the request at the current time it should try again later. The source will wait for a period of time and then re-try the request. Implementing throttling has the advantage of limiting the maximum amount of resources and costs of the workload. In AWS, you can use [Amazon API Gateway](https://aws.amazon.com/api-gateway/) to implement throttling. Refer to the [Well-Architected Reliability pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) for more details on implementing throttling.

**Buffer based: **Similar to throttling, a buffer defers request processing, allowing applications that run at different rates to communicate effectively. A buffer-based approach uses a queue to accept messages (units of work) from producers. Messages are read by consumers and processed, allowing the messages to run at the rate that meets the consumers’ business requirements. You don’t have to worry about producers having to deal with throttling issues, such as data durability and backpressure (where producers slow down because their consumer is running slowly).

In AWS, you can choose from multiple services to implement a buffering approach. [Amazon Simple Queue Service(Amazon SQS)](https://aws.amazon.com/sqs/) is a managed service that provides queues that allow a single consumer to read individual messages. [Amazon Kinesis](https://aws.amazon.com/kinesis/) provides a stream that allows many consumers to read the same messages.

When architecting with a buffer-based approach, ensure that you architect your workload to service the request in the required time, and that you are able to handle duplicate requests for work.

**Implementation steps**
+ ** Analyze the client requirements: **Analyze the client requests to determine if they are capable of performing retries. For clients that cannot perform retries, buffers will need to be implemented. Analyze the overall demand, rate of change, and required response time to determine the size of throttle or buffer required.
+ ** Implement a buffer or throttle:** Implement a buffer or throttle in the workload. A queue such as Amazon Simple Queue Service (Amazon SQS) can provide a buffer to your workload components. Amazon API Gateway can provide throttling for your workload components.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
+  [AWS Instance Scheduler](https://aws.amazon.com/answers/infrastructure-management/instance-scheduler/)
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
+  [Amazon Simple Queue Service](https://aws.amazon.com/sqs/)
+  [Getting started with Amazon SQS](https://aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html)
+  [Amazon Kinesis](https://aws.amazon.com/kinesis/)
