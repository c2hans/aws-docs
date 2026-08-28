---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/tradeoffs.html
---

# Understanding trade-offs and risks
<a name="tradeoffs"></a>

Resilient architectures should use a handful of well-tested, simple, and reliable mechanisms to respond to failures. To achieve the highest levels of resilience, workloads should automatically detect and recover from as many failure modes as possible. Doing so requires extensive investment in performing resilience analysis. This means that achieving higher levels of resilience involves making trade-offs. However, as you continue to make trade-offs, you reach a point of diminishing returns relative to your resilience objectives. Here are the most typical trade-offs:
+ **Cost** – Redundant components, enhanced observability, additional tools, or increased resource utilization will result in increased costs.
+ **System complexity** –Detecting and responding to failure modes, including the mitigation solutions, and potentially not using managed services result in increased system complexity.
+ **Engineering effort** – Additional developer hours are required to build solutions to detect and respond to failure modes.
+ **Operational overhead** – Monitoring and operating a system that handles more failure modes can add operational overhead, particularly when you can't use managed services to mitigate specific failure modes.
+ **Latency and consistency** – Building distributed systems that favor availability require trade-offs in consistency and latency, as described in the [PACELC theorem](https://www.cs.umd.edu/~abadi/papers/abadi-pacelc.pdf).

![The probability of achieving resilience objectives based on the trade-offs being made, where you reach a point of diminishing returns](http://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/images/guide-img/23d14f60-5174-4aff-bb7a-ef108169ec57/images/c782ed9b-2a4d-4692-a6b2-5109b097839f.png)

As you consider the mitigations for the identified failure modes in the user story, consider the trade-offs you need to make. As with security, resilience is an optimization problem. You have to make a decision on whether to avoid, mitigate, transfer, or accept the risks posed by the identified failure. There might be some failure modes you can avoid, a set that you accept, and a few that you can transfer. You might choose to mitigate many of the failure modes you identify. To determine which approach to take, perform an assessment by asking two questions: What is the likelihood that the failure will occur? What is the impact to the workload if it does occur?

**Likelihood** is how plausible it is that an event will occur. For example, if the user story has a component that operates on a single Amazon Elastic Compute Cloud (Amazon EC2) instance, the component might be disrupted at some point during the system's operation, perhaps due to patching procedures or operating system errors.  Alternatively, a database that's managed by Amazon Relational Database Service (Amazon RDS) that synchronizes data between its primary and secondary instances has a low plausibility of becoming completely unavailable.

**Impact** is an estimate of the harm that an event can cause. It should be assessed from both a financial and a reputational perspective, and is relative to the value of the user stories it impacts. For example, an overwhelmed database could have a significant impact on an e-commerce system's ability to accept new orders. However, the loss of a single instance out of a fleet of 20 instances behind a load balancer would likely have very little impact.

You can compare the answers to these questions against the cost of the trade-offs you have to make to mitigate the risk. When you consider this information in view of your risk threshold and your resilience objectives, it informs your decision on which failure modes you plan to actively mitigate.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
