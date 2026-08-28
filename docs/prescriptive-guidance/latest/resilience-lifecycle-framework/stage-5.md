---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/stage-5.html
---

# Stage 5: Respond and learn
<a name="stage-5"></a>

How your application responds to disruptive events influences its reliability. Learning from experience and how your application has responded to disruption in the past is also critical to improving its reliability.

The *Respond and learn* stage focuses on practices that you can implement to better respond to disruptive events in your applications. It also includes practices to help you distill the maximum amount of learning from the experiences of your operations teams and engineers.

## Creating incident analysis reports
<a name="create-incident-analysis-reports"></a>

When an incident occurs, the first action is to prevent further harm to customers and the business as quickly as possible. After the application has recovered, the next step is to understand what happened and to identify steps to prevent reoccurrence. This post-incident analysis is usually captured as a report that documents the set of events that led to an impairment of the application, and the effects of the disruption on the application, customers, and the business. Such reports become valuable learning artifacts and should be shared widely across the business.

**Note**
It's critical to perform incident analysis without assigning any blame. Assume that all operators took the best and most appropriate course of action given the information they had. Do not use the names of operators or engineers in a report. Citing human error as a reason for impairment might cause team members to be guarded in order to protect themselves, resulting in the capture of incorrect or incomplete information.

A good incident analysis report, like that documented in the [Amazon Correction of Error (COE) process](https://aws.amazon.com/wat.concept.coe.en.html), follows a standardized format and tries to capture, in as much detail as possible, the conditions that led to an impairment of the application. The report details a time-stamped series of events and captures quantitative data (often metrics and screenshots from monitoring dashboards) that describe the measurable state of the application over the timeline. The report should capture the thought processes of operators and engineers who took action, and the information that led them to their conclusions. The report should also detail the performance of different indicators―for example, which alarms were raised, whether those alarms accurately reflected the state of the application, the time lag between events and the resulting alarms, and the time to resolve the incident. The timeline also captures the runbooks or automations that were initiated and how they helped the application regain a useful state. These elements of the timeline help your team understand the effectiveness of automated and operator responses, including how quickly they addressed the problem and how effective they were in mitigating the disruption.

This detailed picture of a historical event is a powerful educational tool. Teams should store these reports in a central repository that is available to the entire business so that others can review the events and learn from them. This can improve your teams' intuition about what can go wrong in production.

A repository of detailed incident reports also becomes a source of training material for operators. Teams can use an incident report to inspire a table-top or live game day, where teams are given information that plays back the timeline that's captured in the report. Operators can walk through the scenario with partial information from the timeline and describe what actions they would take. The moderator for the game day can then provide guidance on how the application responded based on the operator's actions. This develops the troubleshooting skills of operators, so they can more easily anticipate and troubleshoot issues.

A centralized team that's responsible for application reliability should maintain these reports in a centralized library that the entire organization can access. This team should also be responsible for maintaining the report template and training teams on how to complete the incident analysis report. The reliability team should periodically review the reports to detect trends across the business that can be addressed through software libraries, architecture patterns, or changes to team processes.

## Conducting operational reviews
<a name="conduct-operational-reviews"></a>

As discussed in [*Stage 4: Operate*](stage-4.md), operational reviews are an opportunity to review recent feature releases, incidents, and operational metrics. The operational review is also an opportunity to share learnings from feature releases and incidents with the wider engineering community in your organization. During the operational review, the teams review feature deployments that were rolled back, incidents that occurred, and how they were handled. This gives engineers across the organization an opportunity to learn from the experiences of others and to ask questions.

Open your operational reviews to the engineering community in your company so they can learn more about the IT applications that run the business and the types of issues they can encounter. They will carry this knowledge with them as they design, implement, and deploy other applications for the business.

## Reviewing alarm performance
<a name="review-alarm-performance"></a>

Alarms, as discussed in the *operate* stage, might result in dashboard alerts, tickets being created, emails being sent, or operators being paged.  An application will have numerous alarms configured to monitor various aspects of its operation. Over time, the accuracy and effectiveness of these alarms should be reviewed to increase alarm precision, reduce false positives, and consolidate duplicate alerts.

### Alarm precision
<a name="alarm-precision.47279360-cdae-563b-9a99-a58e0d674e80"></a>

Alarms should be as specific as possible to reduce the amount of time that you have to spend interpreting or diagnosing the specific disruption that caused the alarm. When an alarm is raised in response to an application impairment, the operators who receive and respond to the alarm must first interpret the information that the alarm conveys. The information might be a simple error code that maps to a course of action such as a recovery procedure, or it might include lines from application logs that you have to review to understand why the alarm was raised. As your team learns to operate an application more effectively, they should refine these alarms to make them as clear and concise as possible.

You can't anticipate all possible disruptions to an application, so there will always be general alarms that require an operator to analyze and diagnose. Your team should work to reduce the number of general alarms in order to improve response times and decrease the mean time to repair (MTTR). Ideally, there should be a one-to-one relationship between an alarm and an automated or human-performed response.

### False positives
<a name="false-positives.eb9c05e8-f442-50a7-bba6-3562d246c246"></a>

Alarms that require no action from operators but produce alerts as emails, pages, or tickets will be ignored by operators over time.  Periodically, or as part of an incident analysis, review alarms to identify those that are often ignored or require no action from operators (*false positives*).  You should work to either remove the alarm, or improve the alarm so that it issues an actionable alert to operators.

### False negatives
<a name="false-negatives.facbaf72-8f46-5343-99d5-86861357d020"></a>

During an incident, alarms that are configured to alert during the incident might fail, perhaps because of an event that impacts the application in an unexpected way.  As part of an incident analysis, you should review the alarms that should have been raised but weren't. You should work to improve these alarms so they better reflect the conditions that might arise from an event. Alternatively, you might have to create additional alarms that map to the same disruption but are raised by a different symptom of the disruption.

### Duplicative alerts
<a name="duplicative-alerts.37990799-f2a2-57c8-881e-bec09cbc4022"></a>

A disruption that impairs your application is likely to cause multiple symptoms and might result in multiple alarms.  Periodically, or as part of an incident analysis, you should review the alarms and alerts that were issued.  If operators received duplicate alerts, create aggregate alarms to consolidate them into a single alert message.

## Conducting metrics reviews
<a name="conduct-metrics-reviews"></a>

Your team should collect operational metrics about your application, such as the number of incidents by severity per month, the time to detect the incident, the time to identify the cause, the time to remediate, and the number of tickets created, alerts sent, and pages raised. Review these metrics at least monthly to understand the burden on operational staff, the signal-to-noise ratio they deal with (for example, informational versus actionable alerts), and whether the team is improving its ability to operate the applications under their control. Use this review to understand trends in the measurable aspects of the operations team. Solicit ideas from the team on how to improve these metrics.

## Providing training and enablement
<a name="provide-training-enablement"></a>

It's difficult to capture a detailed description of an application and its environment that led to an incident or unexpected behavior. Furthermore, modeling the resilience of your application to anticipate such scenarios isn't always straightforward. Your organization should invest in training and enablement materials for your operations teams and developers to participate in activities such as resilience modeling, incident analysis, game days, and chaos engineering experiments. This will improve the fidelity of the reports that your teams produce and the knowledge that they capture. The teams will also become better equipped to anticipate failures without relying on a smaller, more experienced group of engineers who have to lend their insight through scheduled reviews.

## Creating an incident knowledge base
<a name="create-incident-kb"></a>

An incident report is a standard output from an incident analysis. You should use the same or a similar report to document scenarios where you detected anomalous application behavior, even if the application didn't become impaired. Use the same standardized report structure to capture the outcome of chaos experiments and game days. The report represents a snapshot of the application and its environment that led to an incident or otherwise unexpected behavior. You should store these standardized reports in a central repository that all engineers within the business can access.

Operations teams and developers can then search this knowledge base to understand what has disrupted applications in the past, what types of scenarios could have caused disruption, and what prevented application impairment. This knowledge base becomes an accelerator for improving the skills of your operations teams and your developers, and enables them to share their knowledge and experiences. Additionally, you can use the reports as training material or scenarios for game days or chaos experiments to improve the operational team's intuition and ability to troubleshoot disruptions.

**Note**
A standardized report format also provides readers with a sense of familiarity and helps them find the information they are looking for more quickly.

## Implementing resilience in depth
<a name="implement-resilience-in-depth"></a>

As discussed earlier, an advanced organization will implement multiple responses to an alarm. There is no guarantee that a response will be effective, so by layering responses an application will be better equipped to fail gracefully. We recommend that you implement at least two responses for each indicator to ensure that an individual response doesn't become a single point of failure that might lead to a DR scenario.  These layers should be created in serial order, so that a successive response is performed only if the previous response was ineffective. You shouldn't run multiple layered responses to a single alarm. Instead, use an alarm that indicates whether a response has been unsuccessful, and, if so, initiates the next layered response.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
