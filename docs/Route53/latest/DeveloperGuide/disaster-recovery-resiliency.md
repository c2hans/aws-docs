---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/disaster-recovery-resiliency.html
---

# Resilience in Amazon Route 53
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

Route 53 divides its functionality into a control and a data plane. Route 53 service, like most AWS services, includes a control plane that enables you to perform management operations such as creating, updating, and deleting resources, and a data plane that provides the service's core functionality. For more information about control and data planes in Route 53, see [Control and data plane concepts](route-53-concepts.md#route-53-concepts-control-and-data-plane).

Route 53 is primarily a global service, but the following features support AWS Regions:
+ If you're using Route 53 VPC Resolver to set up hybrid configurations, you create endpoints in AWS Regions that you choose, and you specify IP addresses in multiple Availability Zones. For outbound endpoints, you create rules in the same Region where you created the endpoint. For more information, see [What is Route 53 VPC Resolver?](resolver.md).
+ You can configure Route 53 health checks to check the health of resources that you create in specific Regions, such as Amazon EC2 instances and Elastic Load Balancing load balancers.
+ When you create a health check that monitors an endpoint, you can optionally specify the Regions that you want Route 53 to perform health checks from.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
