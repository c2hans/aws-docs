---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/rds-outpost-storage-autoscaling.html
---

# Amazon RDS storage autoscaling on AWS Outposts
<a name="rds-outpost-storage-autoscaling"></a>

If your workload is unpredictable, you can enable storage autoscaling for an Amazon RDS DB instance. Amazon Relational Database Service (Amazon RDS) on AWS Outposts supports manual and automatic storage scaling. With storage autoscaling enabled, when Amazon RDS detects that your DB instance is running out of free database space it automatically scales up your storage which is based on the EBS capacity sized for your Outposts deployment. The feature provide the same capabilities that have at Regions where there are some specific factors that apply for autoscaling what can be found in the [*Amazon RDS Autoscaling guide*](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.Autoscaling.html). It’s important to carefully manage the maximum storage allocated for RDS instances on Outposts, as EBS resources are restricted to the capacity provisioned in the Outpost. [Amazon RDS storage autoscaling](https://aws.amazon.com/about-aws/whats-new/2022/05/amazon-rds-aws-outposts-storage-autoscaling/) allows you to set a maximum storage limit, ensuring that your deployment stays within the available EBS capacity. For more information on managing your Outposts capacity, see the [Capacity management](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/capacity-management.html) section of this whitepaper.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
