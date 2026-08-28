---
source_url: https://docs.aws.amazon.com/outposts/latest/userguide/disaster-recovery-resiliency.html
---

# Resilience in AWS Outposts
<a name="disaster-recovery-resiliency"></a>

AWS Outposts is designed to be highly available. Outposts racks are designed with redundant power and networking equipment. For additional resilience, we recommend that you provide dual power sources and redundant network connectivity for your Outpost.

For high availability, you can provision additional built-in and always active capacity on Outposts rack. Outpost capacity configurations are designed to operate in production environments, and support N\+1 instances for each instance family when you provision the capacity to do so. AWS recommends that you allocate sufficient additional capacity for your mission-critical applications to enable recovery and failover if there is an underlying host issue. You can use the Amazon CloudWatch capacity availability metrics and set alarms to monitor the health of your applications, create CloudWatch actions to configure automatic recovery options, and monitor the capacity utilization of your Outposts over time.

When you create an Outpost, you select an Availability Zone from an AWS Region. This Availability Zone supports control plane operations such as responding to API calls, monitoring the Outpost, and updating the Outpost. To benefit from the resiliency provided by Availability Zones, you can deploy applications on multiple Outposts, each attached to a different Availability Zone. This enables you to build additional application resilience and avoid a dependence on a single Availability Zone. For more information about Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

You can use a placement group with a spread strategy to ensure that instances are placed on distinct Outposts racks. By doing so, this can help reduce correlated failures. For more information, see [Placement groups on Outposts](outposts-optimizations.md#placement-groups-outpost).

You can launch instances in Outposts using Amazon EC2 Auto Scaling and create an Application Load Balancer to distribute traffic between the instances. For more information, see [Configuring an Application Load Balancer on AWS Outposts](https://aws.amazon.com/blogs/networking-and-content-delivery/configuring-an-application-load-balancer-on-aws-outposts/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
