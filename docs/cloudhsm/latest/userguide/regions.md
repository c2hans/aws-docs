---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/regions.html
---

# Supported Regions for AWS CloudHSM
<a name="regions"></a>

For information about the supported Regions for AWS CloudHSM, see [AWS CloudHSM Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/cloudhsm.html) in the *AWS General Reference*, or the [Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

AWS CloudHSM might not be available in all Availability Zones in a given Region. However, this should not affect performance, as AWS CloudHSM automatically load balances across all HSMs in a cluster.

Like most AWS resources, clusters and HSMs are regional resources. You cannot reuse or extend a cluster across Regions. You must perform all the required steps listed in [Getting started with AWS CloudHSM](getting-started.md) to create a cluster in a new Region.

For disaster recovery purposes, AWS CloudHSM allows you to copy backups of your AWS CloudHSM Cluster from one region to another. For more information, see [AWS CloudHSM cluster backups](backups.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
