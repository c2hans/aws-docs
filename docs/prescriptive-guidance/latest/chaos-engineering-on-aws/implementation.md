---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/implementation.html
---

# Implementing chaos engineering on AWS
<a name="implementation"></a>

Chaos engineering is part of the evaluate and test stage of the [AWS resilience lifecycle](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/introduction.html), as illustrated in the following diagram. Distributed applications do not operate in isolation from other applications or clients, so we recommend that you review the entire resilience lifecycle. Change is constant for distributed applications as the network evolves, upstream and downstream applications undergo shifts, and client usage changes over time.

![Five key stages in the AWS resilience lifecycle.](http://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/images/guide-img/4119a10b-a241-4431-9681-0b62a5da1a70/images/92ccf34b-c4dc-4bf5-8923-b44a157b9b96.png)

To understand how these changes to your application might impact its resilience, make chaos engineering a part of your day-to-day operations. You can implement chaos experiments in different ways:
+ **Ad hoc** – You can perform chaos experiments as one-time experiments to address a specific issue or question.
+ **Chaos game days** – These are structured and recurring events that are designed to verify the reliability and resilience of an application. The purpose of a chaos game day is to identify potential resilience issues or deficiencies across people, processes, and technologies, and to practice the processes and procedures for identifying, mitigating, and responding to incidents.
+ **Chaos pipeline** - Continuous integration and continuous delivery (CI/CD) is about building new features and deploying them safely throughout the environments. To implement chaos engineering experiments, create a chaos pipeline that's separate from your CI/CD pipeline. To understand why, let's assume that you want to add a single chaos engineering experiment to your CI/CD pipeline that injects increasing packet loss for downstream components. That experiment runs 3 times and takes 5 minutes to finish each time. Packet loss increases from 10 percent to 20 percent to 30 percent with each run, and the experiment takes 15 minutes overall to complete. If you have 100 parallel deployments, you'll have to wait 1500 minutes for a single experiment to complete. If you have 10 experiments to run, the impact to your developers would be unbearable. At scale, chaos engineering needs its own pipeline that allows you to run experiments in parallel to your software development lifecycle (SDLC) process.
+ **Canary deployments** – Canaries provide a testing environment for chaos experiments. By directing a small percentage of traffic to a canary service or using methods such as traffic mirroring or replay, you can verify new infrastructure or code changes with zero impact to your stable production system. You can run experiments against the canary and inject faults as necessary, because you can limit the scope of impact to the end-user.
+ **Scheduled experiments**  – You can schedule experiments to verify predictable recovery mechanisms for your application. Use scheduled experiments to replay commonly known events to capture how your systems can recover from events such as terminating an EC2 instance behind an automatic scaling group, removing a Kubernetes pod, or deleting an Amazon ECS task.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
