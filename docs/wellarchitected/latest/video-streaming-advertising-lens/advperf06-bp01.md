---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf06-bp01.html
---

# ADVPERF06-BP01 Adopt a chipset-agnostic workload design for best availability of cloud resources and cost
<a name="advperf06-bp01"></a>

 Implement an x86 chip-agnostic design for workloads to optimize the compute price of your advertising workload.

## Implementation guidance
<a name="implementation-guidance-55"></a>

 Adtech customers that use Amazon EC2 Spot Instances may have found that Spot Instance costs have swung between a preference towards AMD and Intel. As a result, implement a chipset-agnostic design, and make your design configuration-based for seamless adoption and to get the best compute price.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
