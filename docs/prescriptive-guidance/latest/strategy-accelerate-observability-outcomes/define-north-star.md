---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerate-observability-outcomes/define-north-star.html
---

# Stage 1: Define your North Star
<a name="define-north-star"></a>

A successful implementation of observability is not just about operations and tools—it is about fostering a culture of ownership, continuous improvement, and proactive problem-solving. As with any successful strategy, your strategy for observability requires a holistic consideration of three pillars: people, process, and technology.

When you want to establish or improve your observability posture, we recommend that you start by defining what matters, work back from your business outcomes, and continually review, adjust, and realign your strategy as your business, teams, and products evolve.

In this first stage, you define and establish your *North Star*, which is an agreed upon and well understood definition of what good looks like for your organization. We recommend that you revisit some or all of the activities in this stage as your business evolves, when you launch a new product, application, or service, or when you design a major architectural change, to reassess your observability platform and organizational needs.

## Integrate observability earlier in the development lifecycle (shift-left approach)
<a name="shift-left"></a>

Make observability a responsibility for every member of the engineering, operations, and product teams, and treat it as a primary functional requirement, similar to the way you treat unit tests or security. This does not shift the responsibility from the operations team to the development team, but highlights the collaboration required across the multiple teams. It's helpful for teams to perform the following activities in collaboration early in the development lifecycle. You might want to perform these on a per-ticket, per-feature, or per-product basis.
+ **Identify stakeholders.** Who are the stakeholders and what matters to them if this feature or product doesn't work as expected? When you identify stakeholders, consider aspects such as functionality, availability, security, cost, sales, and product usage. Stakeholders can include your team, your product's customers, internal business stakeholders, members of the platform operations team, and application developers. Depending on the scenario, your security and finance teams can be stakeholders too.
+ **Identify key outcomes.** Determine the key outcomes and their impact on the business and on each stakeholder. Identify success and failure for each outcome and stakeholder. Outcomes are typically defined as service-level objectives (SLOs) and must be quantifiable. An SLO is a measure for each outcome. A good SLO has a target value that should be strived for, or maintained, as a goal. An SLO can be a measure of user satisfaction. A service-level indicator (SLI) is the actual measurement or metrics that is used to determine if you're meeting the SLO: It is the quantifiable data point that you track against your objective. Examples include reducing MTTR by 60 percent, maintaining application availability at 99.99 percent, or improving developer productivity by 30 percent.

  Let's take the example of maintaining application availability at 99.99 percent and define the SLO, SLI, and metrics required to measure and validate success. For this example, let's consider a RESTful application and define application availability as the successful completion of all incoming requests. This requires measuring the total number of requests to the application and the completion status of each request. When you translate these into SLO and SLI, you need one metric that captures incoming requests and another metric that captures the status of requests. If all requests complete successfully, the application is considered to be available. If one or more requests result in errors, the application is considered to be unavailable. Therefore, the SLI would be the sum of request completions that are in error, divided by the sum of incoming requests in a 5-minute interval—effectively, an *error rate*. You can add a goal to this SLI to turn it into an SLO; for example: Strive for the error rate to be less than 0.1 percent across 3 consecutive 5-minute intervals.
+ **Prioritize key outcomes. **Based on the priority you set for each outcome, you can choose to focus on outcomes that have the highest impact first, instead of doing everything at the same time. Start small, iterate, and improve your observability posture in small increments. Observability is a process that requires ongoing reviews, audits, enhancements, and improvements toward increasing maturity and benefits. Prioritization can also give you an opportunity to define incremental milestones toward identified outcomes.
+ **Identify required instrumentation.** What are the components and related features of the architecture or implementation that can influence the outcomes that matter, as identified in the previous steps? For example, when you run an application on an Amazon Elastic Compute Cloud (Amazon EC2) instance, the number of cores and available RAM can impact the responsiveness and throughput of the application. At this stage, it might also be helpful to determine whether the tools or libraries you use already provide some of this instrumentation. Conducting a series of preliminary reviews or adding questions such as the following to a ticket's [definition of ready (DoR)](https://scrum-master.org/en/definition-of-ready-dor-an-essential-tool-for-improving-software-development-quality/) can make this activity part of the standard process.
  + If this operation were to fail, what would you need to know to address the failure? How does a typical or problematic operation affect the components involved? What kind of signal should this operation send: log, metric, or trace? What is the cost of this instrumentation compared with its value? What kind of aggregation would be acceptable without breaching SLOs?
  + What are the components and dependencies that can cause a failure in this operation? How will you identify which component or dependency caused the failure? What are the different configuration levers of these components and dependencies, and how does each affect the operation?
  + What is the required metric granularity and sampling rate to ensure that the SLI and SLO can be accurately measured?
+ **Define success criteria.** For each prioritized outcome, define thresholds that are aligned with the impact of meeting or not meeting objectives. The success criteria provide additional context to teams when they respond to alerts. They also give you the ability to forecast and make tradeoffs against the cost of the instrumentation for the visibility required.

## Set up an effective organization and team structure
<a name="team-structure"></a>

Based on the architectural complexity and size of your business, you might need to set up a dedicated team that focuses on observability. This team will be responsible for configuring the observability tools and setting up the observability platform for other teams. We also recommend setting up a dedicated team if you choose a standard OpenTelemetry implementation. In smaller organizations, you can assign observability as an additional responsibility for every team member and also appoint observability champions who evangelize and enforce best practices across teams. These champions volunteer a part of their day to define processes and set standards for the organization. They work either as a self-norming team or can be led by dedicated observability specialists. The following diagram shows how your investment can determine your organizational approach.

![How to determine responsibility for observability based on investments.](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerate-observability-outcomes/images/guide-img/81bb2e9d-84eb-4662-8792-f2a3fb2603f4/images/608a6dd3-738e-4c0e-9a97-5e0490368694.png)

The champions could be fully embedded in teams (as shown for Team 2 in the following illustration) or be part of an enabling team that rotates across the teams to establish and promote best practices (Team 1 in the illustration).

![Setting up enabling teams or embedding observability champions.](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerate-observability-outcomes/images/guide-img/81bb2e9d-84eb-4662-8792-f2a3fb2603f4/images/58424583-46f1-4ad5-ac46-43265cfdde06.png)

## Track cost allocation
<a name="cost-allocation"></a>

Organizations should implement comprehensive cost tracking and visibility across metrics, logs, and traces while establishing team-specific accountability for resource usage and costs. Successful integration of financial operations (FinOps) practices requires automated monitoring systems with budget alerts that are paired with systematic data retention and collection optimization. The engineering and finance teams should align their objectives through shared dashboards and regular reviews. Organizations benefit from implementing clear chargeback models and cost allocation strategies to drive ownership and accountability.

## Define standards
<a name="standards"></a>

Identify and define the base signals and telemetry that an application requires, including alerting and dashboard strategies. Create a checklist or formal review process for every application. The [AWS Observability Best Practices](https://aws-observability.github.io/observability-best-practices/) website provides guidelines for alerting and dashboard creation, such as setting appropriate alert thresholds, minimizing alert fatigue, creating dashboards with enough context for each persona, and so on. For connected and curated observability experiences, see [Application signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) in the Amazon CloudWatch documentation.

## Establish escalation processes
<a name="escalation"></a>

It is important to establish and enforce escalation mechanisms, alert ownership, and response procedures. We recommend that you promote a culture where escalation is not frowned upon.

## Improve skills through training
<a name="skills"></a>

Identify the best way to upskill existing and new team members, reinforce the importance of observability, and foster a culture of continuous improvement. Based on your organization's needs, you can choose between pre-recorded, on-demand training or classroom training that is delivered by observability champions or specialists. Your AWS account team can deliver in-depth, hands-on training sessions such as the [One Observability Workshop](https://catalog.workshops.aws/observability/en-US) or [GameDays](https://aws.amazon.com/gameday/) to coach and improve observability skills and best practices. Additionally, incorporate mechanisms to reinforce best practices and to promote the standards defined by your organization.
