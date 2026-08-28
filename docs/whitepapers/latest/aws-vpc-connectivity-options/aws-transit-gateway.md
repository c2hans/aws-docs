---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-transit-gateway.html
---

# AWS Transit Gateway
<a name="aws-transit-gateway"></a>

 AWS Transit Gateway is a highly available and scalable service to consolidate the AWS VPC routing configuration for a region with a hub-and-spoke architecture. Each spoke VPC only needs to connect to the Transit Gateway to gain access to other connected VPCs. Both IPv4 and IPv6 traffic is supported in AWS Transit Gateway.

 You can take advantage of several Transit Gateway route tables, associations, and propagations to segment your traffic within the same Transit Gateway. You will be able to manage different routing domains (for example, production and non-production traffic) from a single point of management, ensuring that these routing domains won’t be able to communicate between each other.

 You can also take advantage of the hub-and-spoke architecture created by Transit Gateway to centralize access to shared services such as traffic inspection, interface VPC endpoint access, or egress traffic through a NAT gateway or NAT instances. This centralization simplifies the complexity of managing these resources in several VPCs, and allow for a better control as you extend your footprint in AWS.

 Transit Gateways can be peered with each other within the same AWS Region or between different AWS Regions. AWS Transit Gateway traffic always stays on the global AWS backbone and never traverses the public internet, thereby reducing threat vectors such as common exploits and DDoS attacks.

 With a large number of VPCs, Transit Gateway provides simpler VPC-to-VPC communication management over VPC Peering, as shown in the following figure.

![A diagram showing VPC communication over VPC peering.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/aws-transit-gateway.png)

 For a central visibility of IP traffic going to and from your Transit Gateways, you can publish Transit Gateway Flow Logs to Amazon CloudWatch Logs and Amazon S3. Flow log data is collected outside of the path of your network traffic, and therefore does not affect network throughput or latency.

## Additional resources
<a name="additional-resources-9"></a>
+  [Amazon VPC transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
+  [Transit gateway peering attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html)
+  [Work with Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/working-with-transit-gateways.html)
+  [Logging network traffic using Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/logging-tgws.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
