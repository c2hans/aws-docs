---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/operations-perspective-health-and-availability-of-the-aiml-landscape.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Operations perspective: Health and availability of the AI landscape
<a name="operations-perspective-health-and-availability-of-the-aiml-landscape"></a>

 Operating ML applications is new for many customers. In the new CAF-AI capability [AI lifecycle management and MLOps](platform-perspective-infrastructure-for-and-applications-of-aiml.md#aiml-lifecycle-management-and-mlops), we have already introduced a few perspectives and guidance on tackling this. Beyond what has already been covered, what remains are considerations around incident management and performance. To dive deeper beyond this CAF-AI perspective, we recommend reviewing the [MLOps Maturity Framework](https://aws.amazon.com/blogs/machine-learning/mlops-foundation-roadmap-for-enterprises-with-amazon-sagemaker/) and the [Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/well-architected-machine-learning.html) of the AWS Well-Architected Framework, as they both provide extensive documentation and best practices on these challenges.

|  **Foundational Capability**  |  **Explanation**  |
| --- | --- |
|  Incident and Problem Management  |  Identify and manage unforeseen AI behavior. |
|  Performance and Capacity  |  Monitor and handle AI workload performance. |
|  Observability  |  This capability is not enriched for AI, [refer to the AWS CAF](https://aws.amazon.com/professional-services/CAF/).  |
|  Event Management (AIOps)  |  This capability is not enriched for AI, [refer to theAWS CAF](https://aws.amazon.com/professional-services/CAF/).  |
|  Change and Release Management;  |  This capability is not enriched for AI, [refer to the AWS CAF](https://aws.amazon.com/professional-services/CAF/).  |
|  Configuration Management  |  This capability is not enriched for AI, [refer to the AWS CAF](https://aws.amazon.com/professional-services/CAF/).  |
|  Patch Management  |  This capability is not enriched for AI, [refer to the AWS CAF](https://aws.amazon.com/professional-services/CAF/).  |
|  Availability and Continuity Management  |  This capability is not enriched for AI, [refer to the AWS CAF](https://aws.amazon.com/professional-services/CAF/).  |

## Incident and problem management
<a name="incident-and-problem-management"></a>

 **Identify and manage unforeseen AI behavior.**

AI systems are often used in situations where the expertise of a single person is not enough to grasp or solve a problem. This nature of AI systems makes it hard to understand the general behavior of the system and the edge cases, making it difficult to foresee the potentially degrading performance over time. Therefore, practitioners look at AI systems through proxies and simplified statistics. When adopting AI [observing and monitoring](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/), these simplified views into the AI system become key. This is already true in the early phases of development, but is especially important when the system is used under real world conditions.

Make sure to establish practices that acknowledge that AI systems get validated but never verified, and that they need constant and ongoing control and observation. One example is training-serving skew, where the performance of the in-lab developed AI system significantly differs from what’s being seen in production. When needed, allow your customers and users to flag results as unfavorable or wrong. Open up pathways for them to engage directly to report incidents. From the beginning, prepare or a change in data and hence performance through drift, training-serving skew, black swan events, and unobserved data-points. Where the system allows for it, provide ways to gracefully fail and to report and react to such incidents and learn from them. Anticipate that customers and users for which the system does not work well will often not be represented in the data. Finally, expect such incidents to occur and be suspicious if none are reported. Expect this challenge to grow with the size and complexity of your AI system. For example, foundation models are significantly harder to correct and monitor than simple decision trees.

## Performance and capacity
<a name="performance-and-capacity"></a>

 **Monitor and handle AI workload performance.**

 AI follows different development cycles than traditional software and comes with different performance and workload profiles: In the early stages of development, data is explored and cost and performance require the capability to adapt to numerous and very different workloads, often dominated by experiments and training workloads that require strong machines, specialized hardware and memory-effective architectures. Use the cloud to enable this multitude of workloads as it delivers the capability to react dynamically to these workload profiles, each of which occur sparsely and only at certain points in the development lifecycle.

Over time, training and streamlined pre-processing takes over and dominates the workload profile, becoming more consistent and predictable. Your speed of innovation will be impacted by your ability to adapt to this new profile and move quickly and continuously between the two while keeping clear lines between development and production. Make sure that model artifacts and the data that has been fueling these streamlined workloads are available for potential fallbacks. Once a model moves into a deployed and operationalized stage, make sure that the inference gets optimized for non-functional requirements (such as, latency or throughput) cost and monitoring of performance and capacity are in place. In the [AI lifecycle management](platform-perspective-infrastructure-for-and-applications-of-aiml.md#aiml-lifecycle-management-and-mlops) capability, we introduced the MLOps maturity model, refer to it for deeper operations insights. Over time, multiple types of [workload-profiles will mix and mingle](https://www.amazon.science/blog/building-systems-that-automatically-adjust-to-workloads-and-data) and are rarely comparable to the ones data-scientists experience when they develop them in isolation before launching (often called *in the lab*). Take a deep-dive into the Well-Architected-Framework and its purpose-built ML Lens that addresses how to architect such systems in the cloud.
