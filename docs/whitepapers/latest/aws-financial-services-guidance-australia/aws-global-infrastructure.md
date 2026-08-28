---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-financial-services-guidance-australia/aws-global-infrastructure.html
---

# AWS Global Infrastructure
<a name="aws-global-infrastructure"></a>

 The AWS Global Cloud Infrastructure comprises AWS Regions and Availability Zones. A Region is a physical location around the world where we cluster data centers. We call each group of logical data centers an Availability Zone (AZ). Each Region consists of multiple isolated and physically separate AZs within a geographic area. Each AZ has independent power, cooling, and physical security and is connected by redundant, ultra-low-latency networks. AWS customers focused on high availability can design their applications to run in multiple AZs to achieve even greater fault-tolerance. Customers can learn more about these topics by downloading the [Amazon Web Services' Approach to Operational Resilience in the Financial Sector & Beyond](https://docs.aws.amazon.com/whitepapers/latest/aws-operational-resilience/aws-operational-resilience.html) whitepaper.

 AWS customers choose the Regions in which their content and servers are located. This allows customers to establish environments that meet specific geographic or regulatory requirements. Additionally, this allows customers with business continuity and disaster recovery objectives to establish primary and backup environments in a location or locations of their choice. More information on our disaster recovery recommendations is available at [Disaster Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html). For example, AWS customers in Australia can choose to deploy their AWS services exclusively in the Asia Pacific (Sydney) Region or the AWS Asia Pacific (Melbourne) Region and store their content on shore in Australia, if this is their preferred location. If the customer makes this choice, their content will be located in Australia unless the customer chooses to move that content.

 The AWS Asia Pacific (Sydney) Region and AWS Asia Pacific (Melbourne) Region are designed and built to meet rigorous compliance standards globally, providing high levels of security for AWS customers. As with every Region, the Asia Pacific (Sydney) Region and AWS Asia Pacific (Melbourne) Region are aligned with applicable national and global data protection laws.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
