---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-cloud-wan.html
---

# AWS Cloud WAN
<a name="aws-cloud-wan"></a>

 AWS Cloud WAN is an intent-driven managed wide area network (WAN), described by a policy you define that unifies your data center, branch, and AWS networks. While you can create your own global network by interconnecting multiple Transit Gateways across Regions, Cloud WAN provides built-in automation, segmentation, and configuration management features designed specifically for building and operating global networks, based on your core network policy. Cloud WAN has added features such as automated VPC attachments, integrated performance monitoring, and centralized configuration.

 The core network policy is written in a declarative language that defines segments, AWS Region routing, and how the attachments should map to segments. With a core network policy, you can describe your intent for access control and traffic routing, while AWS Cloud WAN handles the network configuration details.

 Cloud WAN is managed within AWS Network Manager, which enables you to centrally manage and visualize your Cloud WAN core network and Transit Gateway networks across AWS accounts, Regions, and on-premises locations. Network Manager provides you several dashboard visualizations to help you view and monitor all aspects of your global network. Some of the dashboards include:
+  World maps that pinpoint where your network resources, such as edge locations, devices, and attachments, are located.
+  Monitoring that uses CloudWatch Events to track 15 months' worth of statistics, giving you a better perspective on how your networks are performing.
+  Event tracking that streams real-time events to an events dashboard.
+  Topological and logical diagrams of your transit gateway networks and transit gateways.

 Both Transit Gateway and Cloud WAN allow centralized connectivity between VPCs and on-premises locations. Transit Gateway is a regional network connectivity hub and is optimal for customers that operate in a few AWS Regions, want to manage their own peering and routing configuration, or prefer to use their own automation. Cloud WAN is optimal for customers who want to define their global network through policy and have the service implement the underlying components automatically.

## Things to know
<a name="things-to-know-cloud-wan"></a>
+  CNE (Core network edge) inherits many Transit Gateway characteristics, such as throughput per VPC attachment.
+  Cloud WAN supports both IPv4 and IPv6.
+  For large networks with many changes, consider creating a separate development and testing global network where you can validate changes.

![Diagram showing AWS Cloud WAN.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/image26.png)

## Additional resources
<a name="additional-resources-17"></a>
+  [AWS Cloud WAN Documentation](https://docs.aws.amazon.com/vpc/latest/cloudwan/what-is-cloudwan.html)
+  [Blog post: AWS Cloud WAN and AWS Transit Gateway migration and interoperability patterns](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-cloud-wan-and-aws-transit-gateway-migration-and-interoperability-patterns/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
