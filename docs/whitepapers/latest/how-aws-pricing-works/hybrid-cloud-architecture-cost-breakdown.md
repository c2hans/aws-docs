---
source_url: https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/hybrid-cloud-architecture-cost-breakdown.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hybrid cloud architecture cost breakdown
<a name="hybrid-cloud-architecture-cost-breakdown"></a>

 Hybrid cloud costs include multiple layers and components deployed across the AWS cloud and on-premises location. When you use AWS Managed Services on Outposts, you are charged for the services based only on usage by instance-hour and not for the underlying Amazon EC2 instance and Amazon EBS storage.

 Breakdown of these services is showcased in next sections for a three-year term with partial upfront, all upfront, and no upfront options (Amazon EC2 and Amazon EBS capacity). Price includes delivery, installation, servicing, and removal at the end of term—there is no additional charge.

## Outpost rack charges (customized example)
<a name="outpost-rack-charges-customized-example"></a>

 Amazon EC2 Charges
+  `c5.24xlarge`, 11 TB

+  $7,148.67 monthly;
+  $123,650.18 up front, $3,434.73 monthly
+  $239,761.41 up front

+  1 `m5.24xlarge`, 11 TB

+  $7,359.69 monthly
+  $127,167.06 up front, $3,532.42 monthly
+  $246,373.14 up front
+ Amazon EBS
+  11 TB EBS tier is priced at $0.30/GB monthly

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
