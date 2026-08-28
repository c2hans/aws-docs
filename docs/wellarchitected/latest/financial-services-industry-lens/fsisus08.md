---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus08.html
---

# FSISUS08: How do you optimize your resource usage?
<a name="fsisus08"></a>

 Review and optimize your resource usage by implementing either a pub/sub or pull mechanism instead of relying on a polling approach.

## FSISUS08-BP01 Use event-driven architecture
<a name="fsisus08-bp01-use-event-driven-architecture"></a>

 Implement either a pub/sub or pull mechanism instead of using a polling approach.

### Prescriptive guidance
<a name="prescriptive-guidance-16"></a>
+  Implement event-driven architecture where possible to avoid idling of resources running and waiting for state changes.
+  If event-driven architecture is not possible, modify the capacity of individual components to prevent idling downstream resources waiting for input.
+  Avoid polling APIs or queues, instead have components and services subscribe to events or be notified of changes to reduce the idling of resources.
+  Implement auto scaling and serverless architectures for generative AI workloads.
+  Use managed generative AI services like Amazon Bedrock to optimize resource utilization.
+  Apply model optimization techniques like quantization and pruning.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
