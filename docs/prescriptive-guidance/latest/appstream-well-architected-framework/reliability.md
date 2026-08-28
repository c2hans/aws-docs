---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/appstream-well-architected-framework/reliability.html
---

# Reliability pillar
<a name="reliability"></a>

The [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/reliability.html) of the AWS Well-Architected Framework addresses how well a system maintains its intended functionality and performance levels during expected operational periods throughout its lifespan. It provides comprehensive guidelines for building and maintaining dependable systems on AWS, including strategies for testing and validation across all stages of the workload lifecycle.

Key focus areas for applying this pillar to your WorkSpaces Applications streaming environment:
+ Fleet management and scaling
+ Session reliability
+ Application availability
+ Recovery procedures

## Automatically recover from failure
<a name="reliability-recovery"></a>

Monitor KPIs for business value to trigger automated responses that can predict, prevent, or recover from failures before they impact operations.
+ Make sure that your IP subnet allocation accounts for expansion and availability.
+ Monitor critical CloudWatch metrics to ensure service availability and performance, including fleet capacity metrics such as `AvailableCapacity` and `InUseCapacity`, and streaming quality metrics such as `StreamingSessionLatency`.
+ Configure alerts for capacity thresholds, session health metrics, performance degradation, and fleet health status changes.
+ Use built-in WorkSpaces Applications automatic scaling capabilities to:
  + Configure minimum and maximum fleet capacity.
  + Set scaling policies based on capacity utilization.
  + Define scale-out and scale-in thresholds based on user experience metrics and business requirements instead of only technical metrics.
+ Build a disaster recovery environment for your WorkSpaces Applications environment. For more information, see the AWS blog post [Disaster recovery considerations with Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/disaster-recovery-considerations-with-amazon-appstream-2-0/).

## Test recovery procedures
<a name="reliability-test"></a>

Cloud environments enable automated testing of failure scenarios and recovery procedures. These capabilities help you identify and fix vulnerabilities before real failures occur.
+ **Fleet recovery testing.** Implement comprehensive fleet recovery testing across multiple scenarios:
  + Simulate instance termination to verify automatic scaling response.
  + Validate fleet minimum capacity maintenance.
  + Test instance replacement timing and user redirection.
  + Validate scaling policies effectiveness.
  + Test fleet capacity limits and overflow handling.
+ **Session recovery testing.** Implement session recovery validation procedures:
  + Test disconnect and reconnect scenarios.
  + Verify application state preservation.
  + Test various network interruption scenarios.
  + Validate session timeout behaviors.
  + Verify user authentication persistence.
  + Verify temporary storage handling.

## Scale horizontally to increase aggregate workload availability
<a name="reliability-scale"></a>

Distribute your workload across multiple, smaller resources to minimize the impact of individual failures and to eliminate single points of failure.
+ Deploy fleet instances across multiple Availability Zones.
+ Configure appropriate minimum fleet capacity.
+ Configure automatic scaling for fleets and set appropriate scaling thresholds.
+ Monitor capacity utilization across the fleet.
+ Deploy WorkSpaces Applications stacks across multiple Regions. For more information, see the AWS blog post [Optimize user experience with latency-based routing for Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/optimize-user-experience-with-latency-based-routing-for-amazon-appstream-2-0/).

## Stop guessing capacity
<a name="reliability-capacity"></a>

Use the automatic scaling capabilities of the cloud to dynamically adjust resources based on demand. This helps prevent resource saturation while maintaining optimal efficiency.
+ Monitor key metrics such as `CapacityUtilization`, `AvailableCapacity`, and `InUseCapacity` to understand capacity needs.
+ Track fleet utilization trends across different time periods. Monitor daily patterns, weekly variations, monthly trends, and seasonal peaks.
+ Set up scaling policies and configure scaling thresholds.
+ Make sure that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover.
+ Accommodate fixed service quotas and constraints through your architecture.

## Manage change through automation
<a name="reliability-change"></a>

Implement infrastructure changes through automation, including version-controlled changes to the automation code itself.
+ Use IaC for fleet configuration.
+ Implement consistent scaling policies.
+ Use the [Image Assistant CLI](https://docs.aws.amazon.com/appstream2/latest/developerguide/cli-operations-managing-creating-image-image-assistant.html) for consistent image creation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
