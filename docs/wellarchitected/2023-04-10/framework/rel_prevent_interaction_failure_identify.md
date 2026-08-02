---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_prevent_interaction_failure_identify.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL04-BP01 Identify which kind of distributed system is required
<a name="rel_prevent_interaction_failure_identify"></a>

 Hard real-time distributed systems require responses to be given synchronously and rapidly, while soft real-time systems have a more generous time window of minutes or more for response. Offline systems handle responses through batch or asynchronous processing. Hard real-time distributed systems have the most stringent reliability requirements.

 The most difficult [challenges with distributed systems](https://aws.amazon.com/builders-library/challenges-with-distributed-systems/) are for the hard real-time distributed systems, also known as request/reply services. What makes them difficult is that requests arrive unpredictably and responses must be given rapidly (for example, the customer is actively waiting for the response). Examples include front-end web servers, the order pipeline, credit card transactions, every AWS API, and telephony.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Identify which kind of distributed system is required. Challenges with distributed systems involved latency, scaling, understanding networking APIs, marshalling and unmarshalling data, and the complexity of algorithms such as Paxos. As the systems grow larger and more distributed, what had been theoretical edge cases turn into regular occurrences.
  +  [The Amazon Builders' Library: Challenges with distributed systems](https://aws.amazon.com/builders-library/challenges-with-distributed-systems/)
    +  Hard real-time distributed systems require responses to be given synchronously and rapidly.
    +  Soft real-time systems have a more generous time window of minutes or greater for response.
    +  Offline systems handle responses through batch or asynchronous processing.
    +  Hard real-time distributed systems have the most stringent reliability requirements.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon EC2: Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html)
+  [The Amazon Builders' Library: Challenges with distributed systems](https://aws.amazon.com/builders-library/challenges-with-distributed-systems/)
+  [The Amazon Builders' Library: Reliability, constant work, and a good cup of coffee](https://aws.amazon.com/builders-library/reliability-and-constant-work/)
+  [What Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html)
+  [What Is Amazon Simple Queue Service?](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)

 **Related videos:**
+  [AWS New York Summit 2019: Intro to Event-driven Architectures and Amazon EventBridge (MAD205)](https://youtu.be/tvELVa9D9qU)
+  [AWS re:Invent 2018: Close Loops and Opening Minds: How to Take Control of Systems, Big and Small ARC337 (includes loose coupling, constant work, static stability)](https://youtu.be/O8xLxNje30M)
+  [AWS re:Invent 2019: Moving to event-driven architectures (SVS308)](https://youtu.be/h46IquqjF3E)
