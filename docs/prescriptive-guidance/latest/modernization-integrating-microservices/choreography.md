---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/choreography.html
---

# Choreography
<a name="choreography"></a>

In a choreographed system, individual components receive a task, perform some work, and possibly emit a task for subsequent work to be performed. There is no central orchestration mechanism. Choreography makes it easy to scale services independently, because each service operates in relative isolation. It performs work when it receives work, at whatever throughput the service is capable of. Choreography is often a central part of an [event-driven architecture (EDA)](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/event-driven-architectures.html).

In the following diagram, there is no coordination between the Lambda functions. Each function only processes messages in the subscribed queue. Each function is responsible for its own error handling and can control concurrency—for example, if a downstream dependency has a requests per second (RPS) limit.

![How choreography works in a microservices architecture on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/images/guide-img/89e63ee3-ec0f-41b0-920f-39a1fbded9a6/images/9363c951-0935-4851-bfbd-baa663484c70.png)

An EDA provides a number of benefits, such as loose coupling of services and extensibility. A full discussion of EDA principles is beyond the scope of this guide. For more information, see:
+ [AWS Well-Architected Framework – Serverless Application Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/event-driven-architectures.html)
+ [Introduction to Event Driven Architecture](https://serverlessland.com/event-driven-architecture) (*Serverless Land*)
+ [Transitioning to event-driven architecture](https://docs.aws.amazon.com/serverless/latest/devguide/serverless-transition.html) (*Serverless Developer Guide*)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
