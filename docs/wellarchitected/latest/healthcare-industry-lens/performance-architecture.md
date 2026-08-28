---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/performance-architecture.html
---

# Performance architecture
<a name="performance-architecture"></a>

| HCL\_PERF1. How do you encrypt data while ensuring performance? |
| --- |
|   |

 **Offload encryption to hardware**

 Certain encryption approaches, such as VPN tunnels or IPsec meshes, can impact performance when implemented at scale. Where possible, offload encryption to hardware to maintain security while improving performance.

 The [AWS Nitro System](https://aws.amazon.com/ec2/nitro/) provides hardware components that allow for easy offloading of encryption services to the hardware. For example, some instance types use the hardware capabilities of the Nitro System hardware to encrypt in-transit traffic between instances with no impact to network performance. This allows healthcare organizations to enable encryption in-transit for sensitive healthcare data. Use instance types that support the Nitro System where possible.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
