---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_manage_service_limits_suff_buffer_limits.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL01-BP06 Ensure that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover
<a name="rel_manage_service_limits_suff_buffer_limits"></a>

When a resource fails or is inaccessible, that resource might still be counted against a quota until it’s successfully terminated. Verify that your quotas cover the overlap of failed or inaccessible resources and their replacements. You should consider use cases like network failure, Availability Zone failure, or Regional failures when calculating this gap.

 **Desired outcome:** Small or large failures in resources or resource accessibility can be covered within the current service thresholds. Zone failures, network failures, or even Regional failures have been considered in the resource planning.

 **Common anti-patterns:**
+  Setting service quotas based on current needs without accounting for failover scenarios.
+  Not considering the principals of static stability when calculating the peak quota for a service.
+  Not considering the potential of inaccessible resources in calculating total quota needed for each Region.
+  Not considering AWS service fault isolation boundaries for some services and their potential abnormal usage patterns.

 **Benefits of establishing this best practice:** When a service disruption events impact application availability, the cloud allows you to implement strategies to mitigate or recover from these events. Such strategies often include creating additional resources to replace failed or inaccessible ones. Your quota strategy would accommodate these failover conditions and not layer in additional degradations due to service limit exhaustion.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 When evaluating quota limits, consider failover cases that might occur due to some degradation. The following types of failover cases should be considered:
+  A VPC that is disrupted or inaccessible.
+  A Subnet that is inaccessible.
+  An Availability Zone has been degraded sufficiently to impact the accessibility of many resources.
+  Various networking routes or ingress and egress points are blocked or changed.
+  A Region has been degraded sufficiently to impact the accessibility of many resources.
+  There are multiple resources but not all are affected by a failure in a Region or an Availability Zone.

 Failures like the ones listed could be the reason to initiate a failover event. The decision to failover is unique for each situation and customer, as the business impact can vary dramatically. However, when operationally deciding to failover application or services, the capacity planning of resources in the failover location and their related quotas must be addressed before the event.

 Review the service quotas for each service considering the high than normal peaks that might occur. These peaks might be related to resources that can be reached due to networking or permissions but are still active. Unterminated active resources will still be counted against the service quota limit.

 **Implementation steps**
+  Verify that there is enough gap between your service quota and your maximum usage to accommodate for a failover or loss of accessibility.
+  Determine your service quotas, accounting for your deployment patterns, availability requirements, and consumption growth.
+  Request quota increases if necessary. Plan for necessary time for quota increase requests to be fulfilled.
+  Determine your reliability requirements (also known as your number of nines).
+  Establish your fault scenarios (for example, loss of a component, an Availability Zone, or a Region).
+  Establish your deployment methodology (for example, canary, blue/green, red/black, or rolling).
+  Include an appropriate buffer (for example, 15%) to the current limit.
+  Include calculations for static stability (Zonal and Regional) where appropriate.
+  Plan consumption growth (for example, monitor your trends in consumption).
+  Consider the impact of static stability for your most critical workloads. Assess resources conforming to a statically stable system in all Regions and Availability Zones.
+  Consider the use of On-Demand Capacity Reservations to schedule capacity ahead of any failover. This can a useful strategy during the most critical business schedules to reduce potential risks of obtaining the correct quantity and type of resources during failover.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [REL01-BP01 Aware of service quotas and constraints](rel_manage_service_limits_aware_quotas_and_constraints.md)
+  [REL01-BP02 Manage service quotas across accounts and regions](rel_manage_service_limits_limits_considered.md)
+  [REL01-BP03 Accommodate fixed service quotas and constraints through architecture](rel_manage_service_limits_aware_fixed_limits.md)
+  [REL01-BP04 Monitor and manage quotas](rel_manage_service_limits_monitor_manage_limits.md)
+  [REL01-BP05 Automate quota management](rel_manage_service_limits_automated_monitor_limits.md)
+  [REL03-BP01 Choose how to segment your workload](rel_service_architecture_monolith_soa_microservice.md)
+  [REL10-BP01 Deploy the workload to multiple locations](rel_fault_isolation_multiaz_region_system.md)
+  [REL11-BP01 Monitor all components of the workload to detect failures](rel_withstand_component_failures_monitoring_health.md)
+  [REL11-BP03 Automate healing on all layers](rel_withstand_component_failures_auto_healing_system.md)
+  [REL12-BP05 Test resiliency using chaos engineering](rel_testing_resiliency_failure_injection_resiliency.md)

 **Related documents:**
+ [AWS Well-Architected Framework’s Reliability Pillar: Availability ](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/availability.html)
+  [AWS Service Quotas (formerly referred to as service limits)](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
+  [AWS Trusted Advisor Best Practice Checks (see the Service Limits section)](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/)
+  [AWS limit monitor on AWS answers](https://aws.amazon.com/answers/account-management/limit-monitor/)
+  [Amazon EC2 Service Limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html)
+  [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)
+ [ How to Request Quota Increase ](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html)
+ [ Service endpoints and quotas ](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html)
+  [Service Quotas User Guide](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)
+ [ Quota Monitor for AWS](https://aws.amazon.com/solutions/implementations/quota-monitor/)
+ [AWS Fault Isolation Boundaries ](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html)
+ [ Availability with redundancy ](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-with-redundancy.html)
+ [AWS for Data ](https://aws.amazon.com/data/)
+ [ What is Continuous Integration? ](https://aws.amazon.com/devops/continuous-integration/)
+ [ What is Continuous Delivery? ](https://aws.amazon.com/devops/continuous-delivery/)
+ [ APN Partner: partners that can help with configuration management ](https://partners.amazonaws.com/search/partners?keyword=Configuration+Management&ref=wellarchitected)
+ [ Managing the account lifecycle in account-per-tenant SaaS environments on AWS](https://aws.amazon.com/blogs/mt/managing-the-account-lifecycle-in-account-per-tenant-saas-environments-on-aws/)
+ [ Managing and monitoring API throttling in your workloads ](https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/)
+ [ View AWS Trusted Advisor recommendations at scale with AWS Organizations](https://aws.amazon.com/blogs/mt/organizational-view-for-trusted-advisor/)
+ [ Automating Service Limit Increases and Enterprise Support with AWS Control Tower](https://aws.amazon.com/blogs/mt/automating-service-limit-increases-enterprise-support-aws-control-tower/)
+ [ Actions, resources, and condition keys for Service Quotas ](https://docs.aws.amazon.com/service-authorization/latest/reference/list_servicequotas.html)

 **Related videos:**
+  [AWS Live re:Inforce 2019 - Service Quotas](https://youtu.be/O9R5dWgtrVo)
+ [ View and Manage Quotas for AWS Services Using Service Quotas ](https://www.youtube.com/watch?v=ZTwfIIf35Wc)
+ [AWS IAM Quotas Demo ](https://www.youtube.com/watch?v=srJ4jr6M9YQ)
+ [AWS re:Invent 2018: Close Loops and Opening Minds: How to Take Control of Systems, Big and Small ](https://www.youtube.com/watch?v=O8xLxNje30M)

 **Related tools:**
+ [AWS CodeDeploy](https://aws.amazon.com/codedeploy/)
+ [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
+ [ Amazon CloudWatch ](https://aws.amazon.com/cloudwatch/)
+ [ Amazon EventBridge ](https://aws.amazon.com/eventbridge/)
+ [ Amazon DevOps Guru ](https://aws.amazon.com/devops-guru/)
+ [AWS Config](https://aws.amazon.com/config/)
+ [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)
+ [AWS CDK ](https://aws.amazon.com/cdk/)
+ [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
+ [AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=CMDB)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
