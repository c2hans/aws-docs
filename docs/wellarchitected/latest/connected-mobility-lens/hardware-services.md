---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/hardware-services.html
---

# Hardware and services
<a name="hardware-services"></a>

| CMSUS\_10: Are you using the correct compute instance type and the minimum size needed to process your workload?  |
| --- |
|   |

**CMSUS\_BP10.1: Use the minimum amount of hardware to meet your needs and use instance types with the least impact**

For more details, see  [SUS05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a2.html) and [SUS05-BP02](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a3.html) in the *Sustainability Pillar whitepaper*.

**Prescriptive guidance:**
+  Right size your edge device to do required processing and maintain performance.
+  Right size your cloud resources helps to reduce a workload's environmental impact, save money, and maintain performance benchmarks. Use Graviton-based EC2 instances to reduce cost and power consumption.

|  CMSUS\_11: Are you using managed services and serverless?  |
| --- |
|   |

**CMSUS\_BP11.1: Use managed services to operate more efficiently in the cloud**

 For more details, see  [SUS05-BP03](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a4.html) in the *Sustainability Pillar whitepaper*.

**Prescriptive guidance:**
+  Use managed services in the cloud to shift responsibility to AWS for maintaining high utilization and sustainability optimization of the deployed hardware. Managed services also remove the operational and administrative burden of maintaining a service, which allows your team to have more time to focus on innovation.
+  Use the managed service's agent or extension in the device to optimize data transfer and network connectivity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
