---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/overview.html
---

# Overview
<a name="overview"></a>

## Comparing resilience testing with chaos engineering
<a name="comparison"></a>

Resilience testing is deterministic. That is, it validates known characteristics about resilience mechanisms, such as circuit breakers, retries, failovers or fallbacks, that have been implemented in your application. It confirms how these application components absorb controlled disruptions with minimal to no user impact. Therefore, resilience testing focuses on the validation of known failure modes that are injected into application components with the goal of producing pass/fail results. You should run resilience testing continuously as a step in your pipeline to ensure that you don't introduce regressions to your resilience posture. In resilience testing, you often do not run tests against real components, but mock APIs that simulate a certain component. This approach allows for consistent, reproducible testing of failure scenarios in a controlled environment, making it suitable for automated pipeline integration and regression testing.

![Characteristics of resilience testing.](http://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/images/guide-img/4119a10b-a241-4431-9681-0b62a5da1a70/images/124b911a-20f7-4ab6-b995-fd0774adbe6a.png)

 In contrast, chaos engineering is non-deterministic. That is, it is hypothesis-based and verifies your mental model on how the application and its dependencies (people, process, and technology) absorb, adapt to, and eventually recover from unanticipated failure modes. Therefore, chaos engineering focuses on the end-to-end verification of unknown failure modes, with the goal of catching defects early, and remediating these before they turn into large-scale events. Chaos engineering fosters continuous learning and should be practiced through a separate chaos pipeline or ad-hoc experiments that enable you to run multiple experiments at any point in time without blocking your developer's productivity in deploying code.

![Characteristics of chaos engineering.](http://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/images/guide-img/4119a10b-a241-4431-9681-0b62a5da1a70/images/4a8d5bf9-a79c-46a3-b883-1082925009f3.png)

The chaos engineering process often begins with a chaos game day, which is a dedicated event where teams intentionally inject controlled faults or failures into their application. The game day is progressive: It starts in lower-level environments (such as development or testing) and gradually advances to higher-level environments (such as staging and pre-production) as confidence builds. By systematically moving through these environments, teams can verify that their systems tolerate the injected faults properly before they reach production. This methodical progression ensures that by the time chaos experiments are conducted in production environments, teams have built substantial confidence in their system's resilience capabilities. The game day process is a proactive approach to identifying weaknesses and vulnerabilities in an application's architecture and operational practices, while eliminating the stress of learning during an unexpected production outage.

## The value of chaos engineering
<a name="value"></a>

Complex systems are ubiquitous in today's world. They play a critical role in many aspects of our lives, from financial markets to healthcare. We expect these systems to be always operational. However, complex systems are often vulnerable to unexpected events and behaviors that can have significant consequences. Organizations need to plan for disruption instead of wondering whether it will happen. They can do that by applying scenario testing across their critical or mission-critical business services. This is where chaos engineering comes into play.

Chaos engineering offers an approach to manage complex systems that can help mitigate risks and improve resilience. The process of preparing for chaos experiments requires teams to develop hypotheses about their system's behavior, which deepens their understanding of how systems are built and how they operate. This preparation often reveals mental gaps, architectural insights, and operational knowledge that might otherwise remain undiscovered. By furthering the understanding of how complex systems react to failures, chaos engineering promotes greater transparency and accountability in system design and management. The more frequently your organization practices chaos engineering, the better prepared they become operationally. Chaos engineering helps you establish best practices for designing resilient applications that can survive component failures with minimal to no user impact. This ensures that critical applications operate within expected service levels and impact tolerance, while continuously enhancing the team's knowledge of their own systems.

## Preparing for adverse conditions
<a name="preparation"></a>

When you build on AWS, you use different types of services, including zonal services such as Amazon Elastic Compute Cloud (Amazon EC2), Regional services such as Amazon Simple Storage Service (Amazon S3), global services such as AWS Identity and Access Management (IAM), third-party software as a service (SaaS) services, and on-premises services. Each type of service exposes different failure domains that you need to account for. How do you prepare for self-inflicted events, or events that are caused by third parties that your organization has no control over?

To help understand how your application might respond to adverse conditions, you can use [AWS Fault Injection Service (AWS FIS)](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html). AWS FIS is a fully managed service for running fault injection experiments in a controlled way. You can use this service to inject AWS-provided scenarios such as Availability Zone power interruptions and cross-Region connectivity issues, or build your own experiments by chaining together a wide variety of fault actions that are provided by the service. AWS FIS enables your teams to continuously practice and learn how their application would react to common faults and remediate defects as they detect them.

## Practicing controlled chaos engineering
<a name="principles"></a>

The key principles of controlled chaos experiments are:
+ Start with an environment that's similar to your production environment.
+ Establish a hypothesis and stop conditions for your experiment.
+ Start small.
+ Exercise control over your chaos experiments.
+ Set the scope of impact.
+ Know your service baseline.
+ Schedule experiments.
+ Remediate first, and then experiment.
+ Monitor the experiment closely.
+ Learn from your results.
+ Prioritize findings, remediate, and verify.
+ Propagate the learnings across your organization.

To successfully scale chaos engineering, you must implement chaos experiments in a controlled way. When you use AWS FIS, you can create stop conditions by using [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html). You can incorporate these conditions into an experiment template to ensure that experiments are stopped if out of bounds and rolled back to their last known state. AWS FIS also provides safety levers. When you engage these levers, AWS FIS stops and rolls back all running experiments in the account in the AWS Region, including multi-account experiments, and prevents new experiments from starting. This prevents fault injection during certain time periods, such as trading hours, sales events, or product launches, or in response to application health alarms. The safety lever remains engaged until it's manually disengaged.

When you conduct a chaos experiment, you should define safeguards to prevent undesirable side-effects in the environment, especially if there is a possibility that the experiment will affect applications that are in production. When you plan the experiment, anticipate any adverse effects it might have on other applications in the environment. For example, other applications could receive erroneous messages from the application that is part of the experiment, experience high request volumes, or encounter resource contention if they share infrastructure. Document these risks and address any known or unacceptable issues before you run the experiment.
