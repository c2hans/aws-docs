---
source_url: https://docs.aws.amazon.com/guidance/latest/migrating-vmware-virtual-machines-to-nutanix-cloud-clusters-on-aws/nutanix-sizer-and-deployment-planning.html
---

# Nutanix Sizer and deployment planning
<a name="nutanix-sizer-and-deployment-planning"></a>

It's important to right-size the environment when migrating to NC2 on AWS. Nutanix [Collector](https://portal.nutanix.com/page/products?product=collector) provides a simple method to quickly capture production workload utilization metrics, which are then imported into the Nutanix [Sizer](https://www.nutanix.com/uk/products/sizer), which enables the most accurate planning recommendations. The Nutanix Sizer product also supports [RVTools](https://www.robware.net/) extracts, which can be used as input for making accurate decisions around planning, deploying, and managing complex workloads.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Migrating VMWare Virtual Machines to Nutanix Cloud Clusters on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
