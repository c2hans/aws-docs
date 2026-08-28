---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/sustainability.html
---

# Sustainability
<a name="sustainability"></a>

The sustainability pillar provides design principles, operational guidance, best practices, and improvement plans to meet sustainability targets for your AWS workloads. You can find additional guidance on implementation in the [Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) of the AWS Well-Architected Framework.

## Design principles
<a name="sus-design-principles"></a>

 When designing advertising workloads, consider the following principles to optimize your workloads for sustainability objectives:
+  Set sustainability goals internally and with advertising partners to meet business objectives.
+  Implement low-latency workloads only for time-critical business requirements.
+  Use serverless computing, containerisation, and cloud-native technologies to scale resources dynamically.
+  Region selection is a complex factor for implementing advertising workloads.
+  Back up and archive data only when challenging to recreate.
+  Establish an iterative process to review sustainability objectives and ensure workload usage is not exceeding service level agreements (SLAs).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
