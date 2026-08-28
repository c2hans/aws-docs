---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/foundations.html
---

# Foundations
<a name="foundations"></a>

| DRHCREL01: How do you manage Service Quotas for resources running in AWS Local Zones and AWS Outposts? |
| --- |
|   |

 For cloud-based workload architectures, there are Service Quotas (also referred to as service limits). These quotas exist to prevent accidentally provisioning more resources than you need and to limit request rates on API operations to protect services from abuse. Both [AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html) and [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) are homed to specific [AWS Regions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html). Regional [service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) apply to AWS resources (for example, Amazon EC2 instances) running on Local Zones or Outposts.

| DRHCREL02: Do you have redundant power and network to on-premises AWS components? |
| --- |
|   |

 AWS Outposts depends on a resilient connection to its anchor Availability Zone for management, monitoring, and service operations to function properly. Redundant network connections for each Outpost are needed for reliable connectivity back to the anchor points in the AWS Cloud. Outposts have [documented power requirements](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html), and it is recommended to provide dual power sources for resilience in case of power failure.

**Topics**
+ [DRHCREL01-BP01 Set service quotas to accommodate for the peak usage of AWS resources on Outposts for their homed Regions](drhcrel01-bp01.md)
+ [DRHCREL02-BP01 Provision redundant power and network to on-premises components](drhcrel02-bp01.md)
+ [DRHCREL02-BP02 Use AWS Direct Connect with redundant tunnels and connections to the AWS Region for Outposts control plane actions and high availability requirements](drhcrel02-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
