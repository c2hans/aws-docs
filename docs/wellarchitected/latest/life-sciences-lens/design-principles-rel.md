---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/design-principles-rel.html
---

# Design principles
<a name="design-principles-rel"></a>
+  **Preserve data integrity throughout the entire lifecycle:** Implement checksums, validation mechanisms, and lineage tracking at every stage where data is ingested, transferred, processed, or stored. Design idempotent and reproducible pipelines that maintain scientific validity and regulatory adherence even under failure conditions.
+  **Build reliability into architecture from the start:** Design for Multi-AZ redundancy, fault isolation, and graceful degradation rather than relying solely on reactive recovery. Incorporate redundancy and failover mechanisms as foundational architectural elements, not afterthoughts.
+  **Implement proactive monitoring and predictive maintenance:** Detect reliability issues before they affect operations through comprehensive monitoring of system health, data integrity, and equipment telemetry.
+  **Design for regulatory adherence and auditability:** Map regulatory requirements (like FDA, EMA, and ICH) to reliability controls and maintain auditable evidence throughout the workload lifecycle.
+  **Enable fault isolation with checkpointing and recovery:** Break complex scientific workflows into modular, independently testable steps with well-defined checkpoints. Preserve intermediate progress so that transient failures don't force complete reruns, reducing cost and maintaining research momentum.
+  **Plan for long-term data preservation and recovery:** Implement tiered storage strategies with immutability controls and efficient recovery mechanisms that meet retention requirements spanning decades. Verify that archived data remains retrievable, verifiable, and usable for reproducibility and regulatory audits.
+  **Test reliability under realistic failure scenarios:** Validate both technical resilience and regulatory adherence through comprehensive testing that includes chaos engineering, data integrity verification under failure conditions, and validation of regulated workloads.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
