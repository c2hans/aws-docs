---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_software_a2.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS03-BP01 Optimize software and architecture for asynchronous and scheduled jobs
<a name="sus_sus_software_a2"></a>

 Use efficient software designs and architectures to minimize the average resources required per unit of work. Implement mechanisms that result in even utilization of components to reduce resources that are idle between tasks and minimize the impact of load spikes.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Queue requests that don’t require immediate processing.
+  Increase serialization to flatten utilization across your pipeline.
+  Modify the capacity of individual components to prevent idling resources waiting for input.
+  Create buffers and establish rate limiting to smooth the consumption of external services.
+  Use the most efficient available hardware for your software optimizations.
+  Use queue-driven architectures, pipeline management, and On-Demand Instance workers to maximize utilization for batch processing.
+  Schedule tasks to avoid load spikes and resource contention from simultaneous execution.
+  Schedule jobs during times of day where carbon intensity for power is lowest.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [What is Amazon Simple Queue Service?](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
+  [What is Amazon MQ?](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html)
+  [Scaling based on Amazon SQS](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html)
+  [What is AWS Step Functions?](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
+  [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
+  [Using AWS Lambda with Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html)
+  [What is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html)

 **Related videos:**
+  [Building Sustainably on AWS](https://www.youtube.com/watch?v=ARAitMSIxc8)
+  [Moving to event-driven architectures](https://www.youtube.com/watch?v=h46IquqjF3E)
