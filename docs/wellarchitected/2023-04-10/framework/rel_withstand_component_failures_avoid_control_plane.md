---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_withstand_component_failures_avoid_control_plane.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL11-BP04 Rely on the data plane and not the control plane during recovery
<a name="rel_withstand_component_failures_avoid_control_plane"></a>

 The control plane is used to configure resources, and the data plane delivers services. Data planes typically have higher availability design goals than control planes and are usually less complex. When implementing recovery or mitigation responses to potentially resiliency-impacting events, using control plane operations can lower the overall resiliency of your architecture. For example, you can rely on the Amazon Route 53 data plane to reliably route DNS queries based on health checks, but updating Route 53 routing policies uses the control plane, so do not rely on it for recovery.

 The Route 53 data planes answer DNS queries, and perform and evaluate health checks. They are globally distributed and designed for a [100% availability service level agreement (SLA).](https://aws.amazon.com/route53/sla/) The Route 53 management APIs and consoles where you create, update, and delete Route 53 resources run on control planes that are designed to prioritize the strong consistency and durability that you need when managing DNS. To achieve this, the control planes are located in a single Region, US East (N. Virginia). While both systems are built to be very reliable, the control planes are not included in the SLA. There could be rare events in which the data plane’s resilient design allows it to maintain availability while the control planes do not. For disaster recovery and failover mechanisms, use data plane functions to provide the best possible reliability.

 For more information about data planes, control planes, and how AWS builds services to meet high availability targets, see the [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones) paper and the [Amazon Builders’ Library.](https://aws.amazon.com/builders-library/)

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Rely on the data plane and not the control plane when using Amazon Route 53 for disaster recovery. Route 53 Application Recovery Controller helps you manage and coordinate failover using readiness checks and routing controls. These features continually monitor your application’s ability to recover from failures, and allows you to control your application recovery across multiple AWS Regions, Availability Zones, and on premises.
  +  [What is Route 53 Application Recovery Controller](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html)
  +  [Creating Disaster Recovery Mechanisms Using Amazon Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/)
  +  [Building highly resilient applications using Amazon Route 53 Application Recovery Controller, Part 1: Single-Region stack](https://aws.amazon.com/blogs/networking-and-content-delivery/building-highly-resilient-applications-using-amazon-route-53-application-recovery-controller-part-1-single-region-stack/)
  +  [Building highly resilient applications using Amazon Route 53 Application Recovery Controller, Part 2: Multi-Region stack](https://aws.amazon.com/blogs/networking-and-content-delivery/building-highly-resilient-applications-using-amazon-route-53-application-recovery-controller-part-2-multi-region-stack/)
+  Understand which operations are on the data plane and which are on the control plane.
  +  [Amazon Builders' Library: Avoiding overload in distributed systems by putting the smaller service in control](https://aws.amazon.com/builders-library/avoiding-overload-in-distributed-systems-by-putting-the-smaller-service-in-control/)
  +  [Amazon DynamoDB API (control plane and data plane)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.API.html)
  +  [AWS Lambda Executions](https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/lambda-executions.html) (split into the control plane and the data plane)
  +  [AWS Lambda Executions](https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/lambda-executions.html) (split into the control plane and the data plane)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [APN Partner: partners that can help with automation of your fault tolerance](https://aws.amazon.com/partners/find/results/?keyword=automation)
+  [AWS Marketplace: products that can be used for fault tolerance](https://aws.amazon.com/marketplace/search/results?searchTerms=fault+tolerance)
+  [Amazon Builders' Library: Avoiding overload in distributed systems by putting the smaller service in control](https://aws.amazon.com/builders-library/avoiding-overload-in-distributed-systems-by-putting-the-smaller-service-in-control/)
+  [Amazon DynamoDB API (control plane and data plane)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.API.html)
+  [AWS Lambda Executions](https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/lambda-executions.html) (split into the control plane and the data plane)
+  [AWS Elemental MediaStore Data Plane](https://docs.aws.amazon.com/mediastore/latest/apireference/API_Operations_AWS_Elemental_MediaStore_Data_Plane.html)
+  [Building highly resilient applications using Amazon Route 53 Application Recovery Controller, Part 1: Single-Region stack](https://aws.amazon.com/blogs/networking-and-content-delivery/building-highly-resilient-applications-using-amazon-route-53-application-recovery-controller-part-1-single-region-stack/)
+  [Building highly resilient applications using Amazon Route 53 Application Recovery Controller, Part 2: Multi-Region stack](https://aws.amazon.com/blogs/networking-and-content-delivery/building-highly-resilient-applications-using-amazon-route-53-application-recovery-controller-part-2-multi-region-stack/)
+  [Creating Disaster Recovery Mechanisms Using Amazon Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/)
+  [What is Route 53 Application Recovery Controller](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html)

 **Related examples:**
+  [Introducing Amazon Route 53 Application Recovery Controller](https://aws.amazon.com/blogs/aws/amazon-route-53-application-recovery-controller/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
