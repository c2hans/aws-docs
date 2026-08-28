---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/stage-4.html
---

# Stage 4: Operate
<a name="stage-4"></a>

After you've completed *Stage 3: Evaluate and test*, you're ready to deploy the application to production. In the *Operate* stage, you deploy your application to production and manage your customers' experience.  The design and implementation of your application determine many of its resilience outcomes, but this stage focuses on the operational practices your system uses to maintain and improve resilience. Building a culture of operational excellence helps create standards and consistency in these practices.

## Observability
<a name="observability"></a>

The most important part of understanding the customer experience is through monitoring and alarming. You need to instrument your application to understand its state, and you need diverse perspectives, which means that you need to measure from both the server side and the client side, typically with canaries. Your metrics should include data about your application's interactions with its dependencies and [dimensions that align to your fault isolation boundaries](https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/multi-az-observability.html). You should also produce logs that provide additional details about every unit of work performed by your application. You might consider combining metrics and logs by using a solution such as the [Amazon CloudWatch embedded metric format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html). You'll likely find that you always want more observability, so consider the cost, effort, and complexity trade-offs required to implement your desired level of instrumentation.

The following links provide best practices for instrumenting your application and creating alarms:
+ [Monitoring production services at Amazon](https://youtu.be/hnPcf_Czbvw) (AWS re:Invent 2020 presentation)
+ [Amazon Builders' Library: Operational Excellence at Amazon](https://youtu.be/7MrD4VSLC_w) (AWS re:Invent 2021 presentation)
+ [Observability best practices at Amazon](https://youtu.be/zZPzXEBW4P8) (AWS re:Invent 2022 presentation)
+ [Instrumenting distributed systems for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/) (Amazon Builders' Library article)
+ [Building dashboards for operational visibility](https://aws.amazon.com/builders-library/building-dashboards-for-operational-visibility/) (Amazon Builders' Library article)

## Event management
<a name="event-mgmt"></a>

You should have an event management process in place to handle impairments when your alarms (or worse, your customers) tell you that something is going wrong. This process should include engaging an on-call operator, escalating problems, and establishing runbooks for consistent approaches to troubleshooting that help remove human errors. However, impairments typically don't happen in isolation; a single application could impact multiple other applications that depend on it. You can rapidly address issues by understanding all applications that are impacted and bringing operators from multiple teams together on a single conference call. However, depending on your organization's size and structure, this process might require a centralized operations team.

In addition to setting up an event management process, you should regularly review your metrics through dashboards. Regular reviews help you understand the customer experience and longer-term trends in the performance of your application. This helps you identify issues and bottlenecks before they cause significant production impact. Reviewing metrics in a consistent, standardized way provides significant benefits but requires top-down buy-in and an investment of time.

The following links provide best practices on building dashboards and operational metrics reviews:
+ [Building dashboards for operational visibility](https://aws.amazon.com/builders-library/building-dashboards-for-operational-visibility/) (Amazon Builders' Library article)
+ [Amazon's approach to failing successfully](https://youtu.be/yQiRli2ZPxU) (AWS re:Invent 2019 presentation)

## Continuous resilience
<a name="continuous-resilience-4"></a>

During the *design and implement* and *evaluate and test* stages, you initiated review and test activities before deploying your application to production. During the *operate* stage, you should continue iterating on those activities in production. You should periodically review the resilience posture of your application through [AWS Well-Architected Framework reviews](https://aws.amazon.com/architecture/well-architected/), [Operational Readiness Reviews (ORRs)](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html), and the [resilience analysis framework](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-analysis-framework/introduction.html). This helps ensure that your application hasn't drifted from established baselines and standards and keeps you up to date with new or updated guidance. These continuous resilience activities help you discover previously unanticipated disruptions and help you come up with new mitigations.

You might also want to consider running [game days](https://aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.gameday.en.html) and [chaos engineering](https://aws.amazon.com/blogs/architecture/chaos-engineering-in-the-cloud/) experiments in production after you've successfully run them in pre-production environments. Game days simulate known events that you have built resilience mechanisms to mitigate. For example, a game day might simulate an AWS Regional service impairment and implement a multi-Region failover. Although implementing these activities can require a significant level of effort, both practices help you build confidence that your system is resilient to the failure modes that you've designed it to withstand.

By operating your applications, encountering operational events, reviewing metrics, and testing your application, you'll encounter numerous opportunities to respond and learn.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
