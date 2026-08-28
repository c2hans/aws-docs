---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/route-53-resolver-endpoints-and-forwarding-rules.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Route 53 Resolver endpoints and forwarding rules
<a name="route-53-resolver-endpoints-and-forwarding-rules"></a>

 Route 53 Resolver endpoints and forwarding rules allow you to forward traffic between your Amazon VPC and on-premises data center without having to deploy additional DNS servers.

 For more detailed information about Amazon Route 53 Resolver, refer to the [Amazon Route 53 Resolver Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html).

 You use the following features of Route 53 resolver in this solution: *inbound endpoint*, *outbound endpoint*, and *forwarding rules* to make the hybrid resolution possible between on-premises and AWS.

 *Table 1 — Solution highlights - Route 53 Resolver endpoint *

|   Use case   |   Advantages   |   Limitations   |
| --- | --- | --- |
| Customers that must forward queries between an Amazon VPC and on-premises data center <br />Customers that have one or more VPCs connected to an on- premises environment through AWS Direct Connect or Amazon VPN  | Low management overhead: you only have to manage forwarding rules and monitor query limits by using Amazon CloudWatch alarms. <br />Uses the highly available AWS backbone  | Approximately 10,000 QPS limit per elastic network interface on resolver endpoints <br />No logging visibility on queries answered by Resolver <br />Query source IP address is replaced with IP address of the endpoint from which it is forwarded  |

 The following diagram represents a sample architecture utilizing Route 53 Resolver endpoints to resolve domain names in a hybrid fashion.

![A diagram depciting Route 53 Resolver endpoints and forwarding rules.](http://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/images/forwarding-rules.jpeg)

1.  Private Hosted Zones are associated with a Shared Service VPC.

1.  Create forward rules in the on-premises DNS server for Route 53 names you want to resolve from on-premises. These rules use an inbound endpoint as their destination.

1.  Create Route 53 Resolver rules for names you want to resolve on-premises from your Amazon VPC. These rules use an outbound endpoint and can be shared with other VPCs through [Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) (RAM).

 **Considerations:**
+  Though you can have multiple VPCs across many accounts, only a single, Availability Zone-redundant set of inbound endpoints is required in your Shared Services VPC.
+  You need only one outbound endpoint for multiple VPCs. You don’t have to create an outbound endpoint in each VPC. Instead, you share an outbound endpoint by sharing the rules created for that endpoint with additional accounts using RAM.
+  Endpoints cannot be used across Regions.

 **Best practices:**
+  Manually specify the private IP addresses of the inbound Route 53 resolver endpoint while creating it, as opposed to having the resolver choose a random IP address from the subnet. This way, if there is an accidental deletion of the endpoint, you can reuse those IP addresses.
+  When you create the inbound or outbound endpoints, we recommend that you use at least two subnets in different Availability Zones for high availability. For the inbound resolver, ensure that you use both endpoint IP addresses in your on-premises DNS resolver so the load can be spread across all available IP addresses.
+  For environments that require a high number of queries per second, be aware that there is a limit of 10,000 queries per second per ENI in an endpoint. More ENIs can be added to an endpoint to scale QPS.
+  We publish `InboundQueryVolume` and `OutboundQueryVolume` metrics through [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), and recommend that you set up monitoring rules that alert you if the threshold exceeds a certain value (for example, 80 percent of 10,000 QPS).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
