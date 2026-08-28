---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/design-principles-perf.html
---

# Design principles
<a name="design-principles-perf"></a>

 In addition to the overall Well-Architected Framework performance efficiency design principles, there are four design principles for performance efficiency for IoT:
+  **Use managed services**: AWS provides several managed services across databases, compute, and storage that can assist your architecture in increasing the overall reliability and performance.
+  **Decouple ingestion and processing**: Decouple the connectivity portion of IoT applications from the ingestion and processing portion in IoT. By decoupling the ingestion layer, your IoT application can handle data in aggregate and can scale more seamlessly by processing multiple IoT messages at once.
+  **Use event-driven architectures**: IoT systems publish events from devices and permeate those events to other subsystems in your IoT application. Design mechanisms that cater to event-driven architectures include using queues, message handling, idempotency, dead-letter queues, and state machines.
+  **Push device complexity away from deployed devices**: IoT hardware devices are frequently resource constrained. The overall logic tasks workflow of your IoT application must push compute and energy-intensive activities away from field-deployed devices and concentrate them in the cloud. However, data engineering, data contextualization, data enrichment and aggregation can be performed at the edge. This is often the case for OT/IIoT environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
