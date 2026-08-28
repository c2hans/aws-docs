---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/connect-to-workloads-on-vmware-cloud-using-albs.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Connect to workloads on VMware Cloud using Application Load Balancers
<a name="connect-to-workloads-on-vmware-cloud-using-albs"></a>

 Once the migration is completed, the Oracle E-Business Suite can be accessed using Application Load Balancers and protected using AWS WAF. The VMware Cloud on AWS environment is connected to the Application Load Balancer and AWS WAF using a private ENI.

![Reference architecture diagram showing using AWS Application Load Balancer with Oracle VMs](http://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/aws-alb-after-migration.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
