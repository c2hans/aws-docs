---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sus_sus_software_a2.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS03-BP01 Optimize software and architecture for asynchronous and scheduled jobs
<a name="sus_sus_software_a2"></a>

Use efficient software and architecture patterns such as queue-driven to maintain consistent high utilization of deployed resources.

 **Common anti-patterns:**
+  You overprovision the resources in your cloud workload to meet unforeseen spikes in demand.
+  Your architecture does not decouple senders and receivers of asynchronous messages by a messaging component.

 **Benefits of establishing this best practice:**
+  Efficient software and architecture patterns minimize the unused resources in your workload and improve the overall efficiency.
+  You can scale the processing independently of the receiving of asynchronous messages.
+  Through a messaging component, you have relaxed availability requirements that you can meet with fewer resources.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Use efficient architecture patterns such as [event-driven architecture](https://aws.amazon.com/event-driven-architecture/) that result in even utilization of components and minimize overprovisioning in your workload. Using efficient architecture patterns minimizes idle resources from lack of use due to changes in demand over time.

 Understand the requirements of your workload components and adopt architecture patterns that increase overall utilization of resources. Retire components that are no longer required.

 **Implementation steps**
+  Analyze the demand for your workload to determine how to respond to those.
+  For requests or jobs that don’t require synchronous responses, use queue-driven architectures and auto scaling workers to maximize utilization. Here are some examples of when you might consider queue-driven architecture:

<table>
<thead>
  <tr><th>Queuing mechanism</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><a href="https://docs.aws.amazon.com/batch/latest/userguide/job_queues.html">AWS Batch job queues</a></td><td>AWS Batch jobs are submitted to a job queue where they reside until they can be scheduled to run in a compute environment.</td></tr>
  <tr><td><a href="https://aws.amazon.com/blogs/compute/running-cost-effective-queue-workers-with-amazon-sqs-and-amazon-ec2-spot-instances/">Amazon Simple Queue Service and Amazon EC2 Spot Instances</a></td><td>Pairing Amazon SQS and Spot Instances to build fault tolerant and efficient architecture.</td></tr>
</tbody>
</table>

+  For requests or jobs that can be processed anytime, use scheduling mechanisms to process jobs in batch for more efficiency. Here are some examples of scheduling mechanisms on AWS:

<table>
<thead>
  <tr><th>Scheduling mechanism</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><a href="https://aws.amazon.com/blogs/compute/introducing-amazon-eventbridge-scheduler/">Amazon EventBridge Scheduler</a></td><td>A capability from <a href="https://aws.amazon.com/eventbridge/">Amazon EventBridge</a> that allows you to create, run, and manage scheduled tasks at scale.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html">AWS Glue time-based schedule</a></td><td>Define a time-based schedule for your crawlers and jobs in AWS Glue.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduled_tasks.html">Amazon Elastic Container Service (Amazon ECS) scheduled tasks</a></td><td>Amazon ECS supports creating scheduled tasks. Scheduled tasks use Amazon EventBridge rules to run tasks either on a schedule or in a response to an EventBridge event.</td></tr>
  <tr><td><a href="https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/">Instance Scheduler</a></td><td>Configure start and stop schedules for your Amazon EC2 and Amazon Relational Database Service instances.</td></tr>
</tbody>
</table>

+  If you use polling and webhooks mechanisms in your architecture, replace those with events. Use [event-driven architectures](https://docs.aws.amazon.com/lambda/latest/operatorguide/event-driven-architectures.html) to build highly efficient workloads.
+  Leverage [serverless on AWS](https://aws.amazon.com/serverless/) to eliminate over-provisioned infrastructure.
+  Right size individual components of your architecture to prevent idling resources waiting for input.

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
+  [Moving to event-driven architectures](https://www.youtube.com/watch?v=h46IquqjF3E)
