---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/overview.html
---

# Overview of the framework
<a name="overview"></a>

The resilience analysis framework was developed by identifying the desired resilience properties of a workload. Desired properties are the things that you want to be true about the system. Resilience is typically measured by availability, so five properties are the characteristics of a highly available distributed system: redundancy, sufficient capacity, timely output, correct output, and fault isolation. These properties are shown in the following diagram.

![Relationships of the desired resilience properties](http://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/images/guide-img/23d14f60-5174-4aff-bb7a-ef108169ec57/images/5357b2c5-a4fe-484f-8ae1-d940a66de2d2.png)

+ **Redundancy** – Fault tolerance is achieved through redundancy that eliminates single points of failure (SPOFs). Redundancy can span from spare components in your workload to full replicas of your entire application stack. When you consider redundancy for your applications, it's important to take into account the level of redundancy provided by the infrastructure, data stores, and dependencies that you use. For example, Amazon DynamoDB and Amazon Simple Storage Service (Amazon S3) provide redundancy by replicating data across multiple Availability Zones in a Region, and AWS Lambda runs your functions across multiple worker nodes in multiple Availability Zones. For each service that you use, take into account what is provided by the service and what you need to design for.
+ **Sufficient capacity **– Your workload requires sufficient resources to function as intended. Resources include memory, CPU cycles, threads, storage, throughput, service quotas, and many others.
+ **Timely output **– When customers use your workload, they expect it to perform its intended function within a reasonable amount of time. Unless the service provides a service-level agreement (SLA) for latency, their expectation is generally based on empirical evidence―that is, their own experience. This *average* customer experience is usually considered to be the median (P50) latency in your system. If your workload takes longer than expected, this latency can affect your customers' experience.
+ **Correct output**– The correct output of your workload's software is required for it to provide its intended functionality. An incorrect or incomplete outcome can be worse than no response at all.
+ **Fault isolation** – Fault isolation restricts the scope of impact to an intended fault container when a failure occurs. It ensures that specific components of your workload fail together while preventing a failure from cascading to other unintended components. It also helps limit the scope of impact to the customers of your workload. Fault isolation is somewhat different from the previous four properties, because it accepts that a failure has already occurred but should be contained. You can create fault isolation in your infrastructure, dependencies, and software functions.

When a desired property is violated, it could cause a workload to be, or perceived to be, unavailable. Based on these desired resilience properties and our experience working with many AWS customers, we've identified five common failure categories: single points of failure, excessive load, excessive latency, misconfigurations and bugs, and shared fate, which we abbreviate as SEEMS. These provide a consistent method for categorizing potential failure modes and are described in the following table.

|
|
| Failure category | Violates | Definition |
| --- |--- |--- |
| **Single points of failure (SPOFs)** | Redundancy | A failure in a single component disrupts the system due to lack of redundancy of the component. |
| **Excessive load** | Sufficient capacity | Over-consumption of a resource through excessive demand or traffic prevents the resource from performing its expected function. This can include reaching limits and quotas, which cause throttling and rejection of requests. |
| **Excessive latency** | Timely output | System processing or network traffic latency exceeds the expected time, service-level objectives (SLOs), or service-level agreements (SLAs). |
| **Misconfiguration and bugs** | Correct output | Software bugs or system misconfiguration leads to incorrect output. |
| **Shared fate** | Fault isolation | A fault that's caused by any of the previous failure categories crosses intended fault isolation boundaries and cascades to other parts of the system or to other customers. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
