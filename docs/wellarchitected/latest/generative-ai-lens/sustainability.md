---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/sustainability.html
---

# Sustainability
<a name="sustainability"></a>

 The sustainability best practices introduced in this paper are represented by at least of one of the following principles:
+  **Identify if generative AI is the right solution:** Always ask if generative AI is right for your workload. There is no need to use computationally intensive AI when a simpler, more sustainable approach might achieve the same outcome. For instance, when searching for information, search engines can return results with fewer resources required than generative AI (which is intended to create new content based off of existing information).
+  **Design for environmental efficiency:** Select and deploy generative AI components with consideration for their environmental impact. By choosing right-sized models, optimizing data operations, and implementing efficient customization approaches, you can minimize the energy footprint of your AI workloads while maintaining necessary functionality. This approach helps verify that your system delivers value while minimizing unnecessary environmental costs from over-provisioned or inefficient resources.
+  **Implement dynamic resource optimization:** Deploy infrastructure that automatically adjusts to actual demand, avoiding waste from idle resources. By leveraging auto-scaling capabilities and serverless architectures, you can verify that computing resources are only consumed when needed and scaled appropriately to the workload. This approach reduces energy consumption through efficient resource utilization while maintaining system performance and reliability.

**Topics**
+ [Energy-efficient infrastructure and services](gensus01.md)
+ [Consume sustainable data processing and storage services](gensus02.md)
+ [Consume energy efficient models](gensus03.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
