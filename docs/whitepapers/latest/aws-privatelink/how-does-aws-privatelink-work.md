---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/how-does-aws-privatelink-work.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# How does AWS PrivateLink work?
<a name="how-does-aws-privatelink-work"></a>

 AWS PrivateLink uses Network Load Balancers to connect interface endpoints to services. A Network Load Balancer functions at the network transport layer (layer 4) and can handle millions of requests per second. In the case of AWS PrivateLink, it is represented inside the consumer Amazon VPC as an endpoint network interface.

 Customers can specify multiple subnets in different Availability Zones to ensure that their service is resilient to an Availability Zone service disruption. To achieve this, they can create endpoint network interfaces in multiple subnets mapping to multiple Availability Zones.

 An endpoint network interface can be viewed in the account, but customers cannot manage it themselves. For more information, refer to *[Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html).*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
