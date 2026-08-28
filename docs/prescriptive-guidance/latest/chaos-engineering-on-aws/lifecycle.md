---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/lifecycle.html
---

# Continuous chaos engineering experiment lifecycle
<a name="lifecycle"></a>

As discussed in the [previous section](implementation.md), you can implement chaos engineering experiments in different ways. In all cases, the key to building a meaningful chaos experiment is to understand the application, historical incidents, and implemented remediations, and to clearly understand the areas to investigate, such as resilience or security. Your knowledge about the application helps you formulate a hypothesis on the application's potential weaknesses and understand how it will detect, remediate, and recover when the fault is injected.

The chaos experiment lifecycle includes these steps:

1. Define the objective of the experiment.

2. Select the target application.

3. Align mental maps.

4. Address the known issues with your application.

5. Define the hypothesis and the experiment.

6. Ensure operational readiness for the experiment.

7. Run controlled scenarios and experiments.

8. Learn from and fine-tune the experiment.

 These steps are illustrated in the diagram and discussed in the following sections.

![Eight steps in the chaos experiment lifecycle.](http://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/images/guide-img/4119a10b-a241-4431-9681-0b62a5da1a70/images/7cd7aa92-0181-488b-b9ac-2a9be4529fca.png)

## Define objectives and set expectations
<a name="define-objectives"></a>

Before each experiment, make sure that your objectives and expectations are specific, measurable, achievable, relevant, and time-bound. Clearly define the following:
+ **Identify** potential failures or weaknesses in systems and services, to understand how they might impact users. This includes identifying possible failure modes, such as server crashes, network failures, or software bugs, and assessing their potential impact on the system's overall performance and reliability.
+ **Quantify** the impact of failures by defining key risk indicators (KRIs) on your systems and services. This includes measuring the effect of failures when metrics such as latency, throughput, and error rates deviate from their steady state. By understanding the impact of such deviations, you can prioritize efforts to mitigate failures based on business risks.
+ **Develop** and **verify** strategies for mitigating or preventing failures. This includes identifying potential solutions, such as redundancy, error correction, or fallback strategies, and testing their effectiveness in a controlled environment. By verifying these strategies, you can ensure that you are effective in preventing or mitigating failures, and can deploy them in your production systems with confidence.
+ **Improve** incident response and disaster recovery processes. By replaying failures in a controlled environment, you can test incident response processes, identify potential bottlenecks or gaps, and refine disaster recovery procedures. This helps ensure that you are prepared to respond quickly and effectively in the event of unexpected failures.

## Select the target application
<a name="select-target"></a>

Chaos engineering is a powerful technique but requires thoughtful prioritization to maximize value. When deciding where to focus chaos engineering efforts, start by considering your business's critical services. Ask your teams to iterate through the software development lifecycle stages, and start to inject faults in testing environments first. Business-critical applications are directly tied to revenue, customer experience, and core operations. Chaos experiments on these services can uncover vulnerabilities that can severely impact the organization―and potentially entire markets―if they aren't addressed. For example, focus on customer-facing services such as trading systems or order systems first. Prioritizing these central services provides the most protection per investment of time.

After critical services, look at foundational components such as databases, message queues, networks, and shared services APIs. These might be used as shared components or services across your organization, so their failure will cause widespread problems. Confirming the resilience of infrastructure services provides confidence that they won't cripple the dependent applications above them. For example, a chaos engineering experiment that takes down a Kafka cluster reveals a lot about the fault tolerance of downstream applications. Although system infrastructure isn't directly customer-facing, it is a prime chaos engineering target.

Don't forget to map the mental gaps of people, processes, facilities information and third-party dependencies, because these can cause major disruptions if they aren't aligned with your organization's impact tolerance objectives. For more information about measuring the ROI of chaos engineering, read [Quantifying the ROI of chaos engineering](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-chaos-engineering-journey/roi-chaos-engineering.html) in the strategy document *Investing in chaos engineering as a strategic necessity*.

The following diagram shows the return on investment for running chaos experiments on different tiers of services.

![ROI for running chaos experiments across different application tiers.](http://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/images/guide-img/4119a10b-a241-4431-9681-0b62a5da1a70/images/4a098ab9-acc2-49f9-a30e-20489be0c12f.png)

## Align mental maps (application discovery)
<a name="align-mental-maps"></a>

When you run ad-hoc experiments or game days, you will begin the application discovery process by holding a whiteboarding session that focuses on mapping out the details of your application. (If you run the experiments in the chaos pipeline, you will have already aligned that mental map, by defining the target application.) A good approach to understanding mental gaps is to have the most junior team member draw a diagram of the application first, and then ask more senior staff members to add to the diagram progressively. This will uncover any gaps in understanding across experience levels.

The diagram should depict both direct upstream and downstream dependencies of the application, as well as any critical third-party integrations. Make sure that there is alignment on the expected flow of a request through the application. Map out the key workflows and user journeys to gain clarity on how customers use the application. Consider using a [sequence diagram](https://en.wikipedia.org/wiki/Sequence_diagram) to capture this information.

After this collaborative session, the team should have a shared mental model of the application, its critical dependencies, and its monitoring capabilities, and an understanding of the risks to make an informed decision to proceed with, or cancel, a potential chaos experiment.

## Address the known issues with your application
<a name="address-issues"></a>

Chaos engineering experiments are designed to proactively surface defects in an application. By injecting failures such as latency increases, server reboots, or Availability Zone power impairments, you can verify your application's ability to tolerate realistic disruptions. However, this process assumes an underlying level of stability and health in the target application. Running chaos experiments on an already problematic application risks masking deeper issues.

Before undertaking chaos engineering, teams should resolve any known defects, bugs, and performance problems in their application.

## Define the hypothesis and the experiment
<a name="define-hypothesis"></a>

Past incidents that have caused disruptions to your application or other applications within your organization can serve as excellent sources for chaos experiment ideas. For example, were previous outages triggered by configuration errors or missing resilience patterns? Reviewing incident histories and replaying the root causes of those real-world failures through chaos experiments is an effective way to develop resilience against similar issues in the future.

Another valuable source of experiment concepts can come directly from the engineers, architects, and operators who are most familiar with an application. Allowing team members to submit hypothetical failure scenarios that they believe could significantly disrupt the application enables you to collect ideas based on insider knowledge. The application team can then evaluate which of these proposed scenarios might have the largest potential impact or expose the biggest unknown risks. Targeting chaos experiments for such high-risk, lesser understood scenarios can generate important learnings and prevent problems in the future.

A third source of ideas comes from performing resilience modeling to anticipate the conditions that would lead to identified business losses. Some resilience modeling exercises have a component-based approach to building a resilience model whereas others have a systems-based approach. A component-based approach asks the question, "What happens when component *x* is under extreme load or has failed?" The team that develops the resilience model then speculates the effect of such a scenario on the wider application, and identifies the monitoring and preventative controls currently in place to detect and mitigate the effects of the scenario. Alternatively, a systems-based approach follows a top-down process to highlight an undesirable state of the application―such as, "The web storefront is showing stale inventory levels"―and invites the application team to anticipate which condition or conditions would cause the application to behave in this way.

## Ensure operational readiness for the experiment
<a name="ensure-readiness"></a>

You need quantifiable indicators to measure the impact of adverse conditions on the application and its behavior, as described previously in the section on [observability](getting-started.md#observability). Being able to measure the application's behavior enables you to determine whether the adverse conditions impacted the application and to what magnitude.

The best way to understand whether there is an impact to your application is to measure its steady state. Steady state measures what normal operation looks like and typically aligns with the business and client experience indicators for a given application. Before you move to the next step, make sure that you have the observability in place to understand impact, and rollback mechanisms ready in case the experiment doesn't turn out as expected.

## Run controlled experiments and scenarios
<a name="run-experiment"></a>

At AWS, we do not recommend conducting an initial chaos experiment on an application that is in production. The purpose of a chaos experiment is to learn something new about how the application behaves under stressful conditions. The application's behavior might be unpredictable during the experiment, so performing an experiment for the first time in production could have customer-impacting consequences. Therefore, you should always run an initial chaos experiment in a lower-level environment that has minimal potential for affecting real-world users, and then iterate through your environments after you verify and are confident that your application can absorb, adapt to, and recover from the injected actions.

Plan each experiment thoroughly by using a document that captures key details, similar to the [experiment planning document](sample-planning.md) provided in the appendix. Some of the critical fields to include are the steady state definition, hypothesis, and method of failure injection. The planning, execution, and analysis of a chaos experiment can be covered in a single artifact.

After you finalize the written plan for the experiment, prepare any necessary code to inject the planned disruptions that are outlined in the document.

To capture potential impact during the experiment, make sure that observability mechanisms are in place. If you do not yet have an automated way to capture experiment outcomes, such as AWS FIS experiment reports, identify the team members who will take notes during execution, capture screenshots of dashboards, and lead the team through the experiment.

## Learn and fine-tune
<a name="learn"></a>

After each experiment, get together as a team to review and reflect on the chaos experiment. Make a conscious effort to maintain a blameless mindset. Your goal should be to have an open, constructive dialogue that focuses entirely on deriving maximum learning, not assigning blame.

Start by reviewing the steady state definition and hypothesis for the experiment. Did the application behave as expected? Were there any surprises that invalidated assumptions? Discuss observations of how the application reacted during the experiment, both good and bad. The data collected―metrics, logs, screenshots, and so on―should tell the story of exactly what happened.

Approach this data review with curiosity instead of judgment, and identify areas where improvements can be made to application design, documentation, monitoring, or other capabilities based on the learnings. These action items are captured as follow-up projects to make the application more resilient.

Through this blameless approach, you can have candid conversations about what went wrong and how you can fix it. Assume positive intent from everyone who is involved, and trust that they were working toward good outcomes. Your shared goal is organizational growth and progression through continuous learning and adapting. Chaos experiment reviews that are conducted in a constructive, blameless manner provide a safe space for your team to gain valuable insights that make your applications and organization more reliable and resilient in the long term. The focus stays on the learnings, not the people. To spread the learnings across your teams, publish the [experiment report](sample-result.md) in a central place and advertise the findings so that others can learn from it.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
