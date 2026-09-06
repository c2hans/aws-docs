---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/fundamental-4.html
---

# Multi-Region fundamental 4: Operational readiness
<a name="fundamental-4"></a>

Operating a multi-Region workload is a complex task that comes with operational challenges that are specific to a multi-Region architecture. These include AWS account management, retooled deployment processes, creating a multi-Region observability strategy, creating and testing recovery processes, and then managing the cost. An [Operational Readiness Review (ORR)](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/the-orr-mechanism.html) can help teams prepare a workload for production, whether it's running in a single Region or across multiple Regions.

## 4.a: AWS account management
<a name="4a-account-management"></a>

To deploy a workload across AWS Regions, make sure that there is parity across all [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) within an account across Regions. First, identify all AWS services that are part of the architecture, look at the planned usage in the standby Regions, and then compare planned usage to current usage. In some cases, if the standby Region hasn't been used before, you can reference the [default service quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) to understand the starting point. Then, across all the services that will be used, request a quota increase by using the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home) (login required) or [APIs](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_Operations.html).

Configure [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) roles in each Region to give operators, automation tooling, and AWS services the appropriate permissions to resources within the standby Region. To achieve Regional isolation for multi-Region architectures, isolate roles by Region. Make sure that permissions are in place before going live with a standby Region.

## 4.b: Deployment practices
<a name="4b-deployment-practices"></a>

Multi-Region capabilities can make it complicated to deploy a workload to multiple Regions. You need to make sure that you deploy to one Region at a time. For example, if you use an active-passive approach, you should deploy to the primary Region first and then to the standby Region. [AWS CloudFormation](https://aws.amazon.com/cloudformation/) helps you deploy infrastructure to a single or multiple Regions, and can be tailored according to your needs. [AWS CodePipeline](https://aws.amazon.com/codepipeline/) helps you build a continuous integration/continuous delivery (CI/CD) pipeline, which has [cross-Region actions](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-create-cross-region.html) that allow deployment to Regions that are different from the Region the pipeline is in. This, combined with robust [deployment strategies](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/deployment-strategies.html) such as [blue/green](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/bluegreen-deployments.html), allows for a minimum to zero downtime deployment.

However, the deployment of stateful capabilities can become more complex when the state of the application or data is not externalized to a persistent store. In these situations, carefully tailor the deployment process to suit your needs. Design the deployment pipeline and process to deploy to one Region at a time instead of deploying to multiple Regions simultaneously. This reduces the chance of correlated failures between the Regions. To learn about techniques Amazon uses to automate software deployments, see the AWS Builders' Library article [Automating safe, hands-off deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/).

## 4.c: Observability
<a name="4c-observability"></a>

When you design for multi-Region, consider how you will monitor the health of all components in each Region to get a holistic view of Regional health. This could include monitoring metrics for replication lag, which is not a consideration for a single-Region workload.

When you build a multi-Region architecture, consider observing the performance of the workload from the standby Regions as well. This includes having health checking and canaries (synthetic testing) running from the standby Region to provide an outside view of the health of the primary Region. In addition, you can use [Amazon CloudWatch Internet Monitor](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-amazon-cloudwatch-internet-monitor/) to understand the state of the external network and performance of your workloads from an end user's perspective. The primary Region should have the same observability in place to monitor the standby Region.

The canaries from the standby Region should monitor customer experience metrics to determine the overall health of the workload. This is required because if there is a problem in the primary Region, the observability in the primary could be impaired and would impact your ability to assess the health of the workload.

In that case, observing outside that Region can provide insight. These metrics should be rolled up into dashboards that are available in each Region and alarms that are created in each Region. Because [CloudWatch](https://aws.amazon.com/cloudwatch/) is a Regional service, having alarms in both Regions is a requirement. This monitoring data will be used to make the call to fail over from a primary to a standby Region.

## 4.d: Processes and procedures
<a name="4d-processes-procedures"></a>

The best time to answer the question, "When should I fail over?" is long before you need to. Define recovery plans that are inclusive of people, processes, and technology well in advance of an issue, and test them regularly. Decide on a recovery decision framework. If there is a well-practiced recovery process and the time to recovery is well understood, you can choose to start the recovery process by using a failover that meets the RTO target. This point in time could be immediately after an issue with the application in the primary Region is identified, or it could be further into an event when recovery options within the application in the Region have been exhausted.

The failover action itself should be 100 percent automated, but the decision to activate the failover should be made by humans—usually a small number of predetermined individuals in the organization. These individuals should consider data loss and information about the event. Also, the criteria for a failover need to be clearly defined and globally understood within the organization. To define and complete these processes, you can use [Amazon Application Recovery Controller (ARC) Region switch](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch.html), which allows for complete end-to-end automation and ensures consistency of processes running during testing and failover.

When you create a Region switch plan, it automatically replicates your plan in the primary and standby Regions to ensure that there is no dependency on a single Region. When this automation is in place, define and follow a regular testing cadence. This ensures that when there is an actual event, the response follows a well-defined, practiced process that the organization has confidence in. It's also important to consider the established tolerances for data reconciliation processes. Confirm that the proposed process meets established RPO/RTO requirements.

## 4.e: Testing
<a name="4e-testing"></a>

Having an untested recovery approach is equal to not having a recovery approach. A basic level of testing would be to run a recovery procedure to switch the operating Region for your application. Sometimes this is referred to as an *application rotation* approach. We recommend that you build the capability to switch Regions into your normal operating posture; however, this test alone is not enough.

Resilience testing is also critical for validating an application's recovery approach. This involves injecting particular failure scenarios, understanding how your application and recovery process react, and then implementing any mitigations required if the test didn't go as planned. Testing your recovery procedure in the absence of errors won't tell you how your application behaves as a whole when faults occur. You must develop a plan to test your recovery against expected failure scenarios. [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/) provides a growing list of [scenarios](https://docs.aws.amazon.com/fis/latest/userguide/scenario-library.html) to get you started.

This is especially important for high availability applications, where rigorous testing is required to ensure that business continuity targets are met. Proactively testing recovery capabilities reduces the risk of failures in production, which builds confidence that the application can achieve a desired bounded recovery time. Regular testing also builds operational expertise, which allows the team to quickly and reliably recover from outages when they occur. Exercising the human element, or process, of your recovery approach is just as critical as the technical aspects.

## 4.f: Cost and complexity
<a name="4f-cost-complexity"></a>

Cost implications of a multi-Region architecture are driven by higher infrastructure usage, operational overhead, and resource time. As mentioned previously, the infrastructure cost in a standby Region is similar to the infrastructure cost in a primary Region when pre-provisioning, so it doubles your total cost. Provision capacity so that it is sufficient for daily operations but still reserves enough buffer capacity to tolerate spikes in demand. Then configure the same limits in each Region.

Additionally, if you are adopting an active-active architecture, you might have to make application-level changes to run your application successfully in a multi-Region architecture. These changes can be time-intensive and resource-intensive to design and operate. At a minimum, organizations need to spend time understanding technical and business dependencies in each Region, and designing failover and failback processes.

Teams should also go through normal failover and failback exercises to feel comfortable with runbooks that would be used during an event. Although these exercises are crucial to getting the expected outcome from a multi-Region investment, they represent an opportunity cost, and take time and resources away from other activities.

## 4.g: Organizational multi-Region failover strategy
<a name="4g-failover-strategy"></a>

AWS Regions provide fault isolation boundaries that prevent correlated failure and contain the impact from AWS service impairments, when they occur, to a single Region. You can use these fault boundaries to build multi-Region applications that consist of independent, fault-isolated replicas in each Region to limit shared fate scenarios. This allows you to build multi-Region applications and use a range of approaches—from backup and restore, to pilot light, to active-active—to implement your multi-Region architecture. However, applications typically don't operate in isolation, so consider both the components you will use and their dependencies as part of your failover strategy. Generally, multiple applications work together to support a *user story*, which is a specific capability offered to an end user, such as posting a picture and caption on a social media app or checking out on an ecommerce site. Because of this, you should develop an organizational multi-Region failover strategy that provides the necessary coordination and consistency to make your approach successful.

There are four high-level strategies that organizations can pick from to guide a multi-Region approach. These are listed from the most granular to the broadest approach:
+ Component-level failover
+ Individual application failover
+ Dependency graph failover
+ Entire application portfolio failover

Each strategy has trade-offs and addresses different challenges, including flexibility of failover decision-making, ability to test the failover combinations, presence of modal behavior, and organizational investment in planning and implementation. To dive into each strategy in more detail, see the AWS blog post [Creating an organizational multi-Region failover strategy](https://aws.amazon.com/blogs/architecture/creating-an-organizational-multi-region-failover-strategy/).

## Key guidance
<a name="key-guidance-4"></a>
+ Review all AWS service quotas to make sure that they are in parity across all Regions in which the workload will operate.
+ The deployment process should target one Region at a time instead of involving multiple Regions simultaneously.
+ Additional metrics such as replication lag are specific to multi-Region scenarios and should be monitored.
+ Extend monitoring for the workload beyond the primary Region. Monitor customer experience metrics for each Region, and measure this data from outside each Region in which a workload is running.
+ Test failover and failback regularly. Implement a single runbook for failover and failback processes and use it both for testing and live events. Runbooks for testing and live events should not be different.
+ Understand the trade-offs of the failover strategies. Implement a dependency graph or entire application portfolio strategy.
