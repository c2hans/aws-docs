---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/applying-framework.html
---

# Applying the framework
<a name="applying-framework"></a>

The best way to apply the resilience analysis framework is by starting with a standard set of questions, organized by failure category, that you should ask about each component in the user story that you're analyzing. If some questions don't apply to every component in your workload, use the questions that are the most applicable.

You can approach thinking about failure modes from two perspectives:
+ How does the failure impact the component's ability to support the user story?
+ How does the failure impact the component's interactions with the other components?

For example, when you consider data stores and excessive load, you might think about failure modes where the database is under excessive load and queries time out. You might also think about how your database client might overwhelm the database with retries or fail to close database connections, exhausting the connection pool. Another example is an authentication process, which might comprise several steps. You need to think through how the failure of a multi-factor authentication (MFA) application or third-party identity provider (IdP) could impact a user story in this authentication system.

As you answer the following questions, you should consider the source of the failure. For example, was the overload caused by a customer surge or by a human operator who took too many nodes out of service during a maintenance activity? You might be able to identify multiple sources of failure in each question, which could require different mitigations. As you ask the questions, keep a record of the potential failure modes that you discover, which component(s) they apply to, and the source of each failure.

**Single points of failure**
+ Is the component architected for redundancy?
+ What happens if the component fails?
+ Can your application tolerate the partial or total loss of a single Availability Zone?

**Excessive latency**
+ What happens if this component experiences increased latency, or a component it interacts with has increased latency (or network interruptions such as TCP resets)?
+ Do you have appropriately configured timeouts with a retry strategy?
+ Do you fail fast or slow? Are there cascading effects such as unintentionally sending all traffic to an impaired resource because it fails fast?
+ What are the most expensive requests made to this component?

**Excessive load**
+ What can overwhelm this component? How can this component overwhelm other components?
+ How can you prevent wasting resources on work that will never succeed?
+ Do you have a circuit breaker that's configured for the component?
+ Can something create an insurmountable backlog?
+ Where can this component experience bimodal behavior?
+ What limits or service quotas can be exceeded (including storage capacity)?
+ How does the component scale under load?

**Misconfiguration and bugs**
+ How do you prevent misconfigurations and bugs from being deployed to production?
+ Can you automatically roll back a bad deployment or shift traffic away from the fault container where the update or change was deployed?
+ What guardrails do you have in place to prevent operator errors?
+ What items (such as credentials or certificates) can expire?

**Shared fate**
+ What are your fault isolation boundaries?
+ Are changes made to deployment units at least as small as your intended [fault isolation boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html) but ideally smaller, such as a one-box environment (a single instance within the fault isolation boundary)?
+ Is this component shared between user stories or other workloads?
+ What other components are tightly coupled to this component?
+ What happens if this component or its dependencies experience a partial or gray failure?

After asking these questions, you can also use SEEMS to develop other questions that are specific to your workload and to each component. SEEMS is best used as a structured way to think about failure modes and as a source of inspiration when you perform a resilience analysis. It is not a rigid taxonomy. Don't spend time worrying about which category a particular failure mode fits into―it's not important. What *is* important is that you thought of the failure and wrote it down. There are no wrong answers; being creative and thinking outside of the box is beneficial. Additionally, don't assume that a failure mode is already mitigated; include all the potential failure modes that you can think of.

You are unlikely to anticipate all potential failure modes in your first exercise. Multiple iterations of the framework help you generate a more complete model, so you don't have to try and solve for everything on the first pass. You can run the analysis in a regular, weekly or biweekly, cadence. In each session, focus on a specific failure mode or component. This can help make steady, incremental progress on improving the resilience of your workload. After you collect a list of potential failure modes for a user story, you can decide what to do about them.
