---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/endpoints-for-iot-sitewise-edge-gateways/architecture-options.html
---

# Architecture options
<a name="architecture-options"></a>

There are various architectures you can use to connect the AWS IoT SiteWise Edge gateways to service endpoints in the cloud. For more information, see [Network-to-Amazon VPC connectivity options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html) (AWS Whitepaper). The following diagram is an example of how connect to service endpoints in the cloud from your industrial control network:

1. The AWS IoT Greengrass virtual machine that is running AWS IoT SiteWise Edge software sends API calls for AWS services to the interface VPC endpoints in the AWS Cloud. For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the AWS PrivateLink documentation.

1. For DNS queries, the AWS IoT Greengrass virtual machine resolves the service API endpoints with the DNS server in the corporate data center.

1. The DNS server forwards the DNS queries to the inbound Amazon Route 53 Resolver endpoints in the AWS Cloud. For more information, see [Forwarding inbound DNS queries to your VPCs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html) in the Route 53 documentation.

![Connections from the corporate data center to the Route 53 and Amazon VPC endpoints in the AWS Cloud](http://docs.aws.amazon.com/prescriptive-guidance/latest/endpoints-for-iot-sitewise-edge-gateways/images/guide-img/056ac4cc-e4c2-45b8-a939-a8d051fafe4d/images/b40f67cc-0fa8-4b6a-85d3-8e2ed04e6394.png)

To support this architecture, you configure private hosted zones in Route 53. A *private hosted zone* is a container that holds information about how you want Amazon Route 53 to respond to DNS queries for a domain and its subdomains within one or more VPCs. The following are the Route 53 private hosted zones for this architecture:
+ `iotsitewise.<region>.amazonaws.com`
+ `iotsitewise.<region>.amazonaws.com`
+ `iotsitewise.<region>.amazonaws.com`
+ `(s3) - *.vpce-x.s3.<region>.vpce.amazonaws.com`

For more information, see [Working with private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) in the Route 53 documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
