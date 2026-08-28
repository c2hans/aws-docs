---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/post-deployment.html
---

# Post-deployment activities
<a name="post-deployment"></a>

Resilience is an ongoing process and the evaluation of your application's resilience must continue after the application has been deployed. The results of your post-deployment activities, such as ongoing resilience assessments, might require that you re-evaluate and update some of the resilience activities you performed earlier in the resilience lifecycle.

## Conducting resilience assessments
<a name="conducting-resilience-assessments"></a>

Assessing resilience doesn't stop after you deploy your application into production. Even if you have well-defined and automated deployment pipelines, changes can sometimes occur directly in a production environment. Additionally, there might be factors that you have not yet taken into consideration in your pre-deployment resilience verification. [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) provides a central place where you can assess whether your deployed architecture meets your defined RPO and RTO needs. You can use this service to run on-demand assessments of your application's resilience, automate assessments, and even integrate them into your CI/CD tools, as discussed in the AWS blog post [Continually assessing application resilience with AWS Resilience Hub and AWS CodePipeline](https://aws.amazon.com/blogs/architecture/continually-assessing-application-resilience-with-aws-resilience-hub-and-aws-codepipeline/). Automating these assessments is a best practice because it helps ensure that you are continuously evaluating your resilience posture in production.

## DR testing
<a name="dr-testing"></a>

In the [*Stage 2: Design and implement*](stage-2.md) stage, you developed disaster recovery (DR) strategies as part of your system.  During Stage 4, you should test your DR procedures to ensure that your team is fully prepared for an incident and your procedures work as expected. You should test all your DR procedures, including failover and failback, on a regular basis and review the results of each exercise to determine if and how your system's procedures should be updated for the best possible outcome. When you initially develop your DR test, schedule the test well in advance and ensure that the entire team understands what to expect, how the outcomes will be measured, and what feedback mechanism will be used to update procedures based on the outcome. After you become proficient in running scheduled DR tests, consider running unannounced DR tests. Real disasters don't occur on a schedule, so you need to be prepared to exercise your plan at any time. However, unannounced doesn't mean unplanned. Key stakeholders still need to plan the event to ensure that proper monitoring is in place and that customers and critical applications are not adversely impacted.

## Drift detection
<a name="drift-detection"></a>

Unanticipated changes to configuration in production applications can occur even when automation and well-defined procedures are in place. To detect changes to your application's configuration, you should have mechanisms for detecting *drift*, which refers to deviations from a baselined configuration. To learn how to detect drift in your AWS CloudFormation stacks, see [Detecting unmanaged configuration changes to stacks and resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) in the AWS CloudFormation documentation. To detect drift in your application's AWS environment, see [Detect and resolve drift in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/drift.html) in the AWS Control Tower documentation.

## Synthetic testing
<a name="synthetic-testing"></a>

[Synthetic testing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) is the process of creating configurable software that runs in production, on a scheduled basis, to test your application's APIs in a way that simulates the end-user experience. These tests are sometimes referred to as *canaries*, in reference to the term's original use in coal mining. Synthetic tests can often provide early warnings when an application suffers from a disruption, even if the impairment is partial or intermittent, as is often the case with [gray failures](https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/gray-failures.html).

## Chaos engineering
<a name="chaos-engineering"></a>

Chaos engineering is a systematic process that involves deliberately subjecting an application to disruptive events in a risk-mitigated way, closely monitoring its response, and implementing necessary improvements. Its purpose is to validate or challenge assumptions about the application's ability to handle such disruptions. Instead of leaving these events to chance, chaos engineering empowers engineers to orchestrate experiments in a controlled environment, typically during periods of low traffic and with readily available engineering support for effective mitigation.

Chaos engineering begins with understanding the normal operating conditions, known as the *steady state*, of the application under consideration. From there, you formulate a hypothesis that details the successful behavior of the application in the presence of disruption. You run the experiment, which involves deliberate injection of disruptions, including, but not limited to, network latency, server failures, hard drive errors, and impairment of external dependencies. You then analyze the results of the experiment and enhance the application's resilience based on your learnings. The experiment serves as a valuable tool for improving various facets of the application, including its performance, and uncovers latent issues that might have remained hidden otherwise. Additionally, chaos engineering helps reveal deficiencies in observability and alarming tools, and helps you refine them. It also contributes to reducing recovery time and enhancing operational skills. Chaos engineering accelerates the adoption of best practices and cultivates a mindset of continuous improvement. Ultimately, it enables teams to build and hone their operational skills through regular practice and repetition.

AWS recommends that you start your chaos engineering efforts in a non-production environment. You can use [AWS Fault Injection Service (AWS FIS)](https://aws.amazon.com/fis/) to run chaos engineering experiments with general-purpose faults as well as faults that are unique to AWS. This fully managed service includes stop-condition alarms and full permission controls so you can easily adopt chaos engineering with safety and confidence.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
