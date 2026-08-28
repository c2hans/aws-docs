---
source_url: https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Architecture
<a name="architecture"></a>

 ELB balances traffic to the Amazon EC2 instances in an AWS Auto Scaling group, which adds or subtracts Amazon EC2 instances to match the load. Deploying Amazon RDS across multiple Availability Zones enhances data durability and availability. Amazon RDS provisions and maintains a standby in a diﬀerent Availability Zone for automatic failover in the event of outages, planned or unplanned. The following illustration shows the example architecture for a dynamic website using Amazon EC2, Amazon EC2 Auto Scaling, and security groups to enforce least-privilege access to AWS infrastructure and selected architecture components, and one Amazon RDS database instance across multiple Availability Zones (Multi-AZ deployment). All these components are deployed into a single region and virtual private cloud (VPC). The VPC spans two availability zones to support failover scenarios. Route 53 Resolver is used to manage and route requests for one hosted zone towards the Elastic Load Balancer.

![AWS Cloud deployment architecture](http://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/images/aws-cloud-deployment-architecture.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
