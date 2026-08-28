---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/design-principles-perf.html
---

# Design principles
<a name="design-principles-perf"></a>
+  **Match compute resources to workload characteristics:** Select specialized hardware and architectures based on specific life sciences workload requirements—high-memory instances for genomic analysis, GPU acceleration for molecular modeling, and consistent low-latency compute for clinical applications. Benchmark and validate performance against scientific and regulatory requirements.
+  **Design for variable and unpredictable workloads:** Implement auto-scaling, containerized workflows, and serverless architectures that dynamically adapt to the highly variable patterns of genomic sequencing, molecular modeling, and research cycles. Avoid over-provisioning by matching resource consumption to actual demand while maintaining performance during peak loads.
+  **Balance performance optimization with regulatory adherence:** Apply risk-based validation frameworks that provide full qualification for high-risk clinical systems while using streamlined approaches for research environments. Integrate automated testing and continuous validation to maintain adherence without creating bottlenecks that slow innovation.
+  **Implement intelligent data management strategies:** Deploy tiered storage architectures that balance high-performance access for active research with cost-efficient archival for long-term retention. Use data classification, lifecycle policies, and caching strategies to optimize both performance and cost across diverse dataset types from basic records to terabyte-scale scientific data.
+  **Optimize network performance for large-scale data movement:** Design network architectures that support secure, high-throughput transmission of large datasets while maintaining encryption controls. Implement intelligent traffic management, compression, and content delivery solutions for global research collaboration and multi-site clinical trials.
+  **Foster cross-functional performance culture:** Establish collaborative reviews between IT and scientific teams that align technical metrics with scientific outcomes. Create integrated monitoring dashboards showing both system performance and metrics, enabling data-driven optimization decisions that preserve scientific rigor and patient safety.
+  **Continuously monitor and optimize based on real-world usage:** Track comprehensive performance metrics including system latency, resource utilization, and clinical workflow impact. Use monitoring data to identify bottlenecks, validate performance against SLAs, and make evidence-based improvements to both research and clinical systems.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
