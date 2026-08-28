---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel02-bp02.html
---

# LSREL02-BP02 Maintain continuous data availability and integrity
<a name="lsrel02-bp02"></a>

 Implement real-time or near-real-time data replication strategies across Availability Zones or AWS Regions to protect against system failures or maintenance interruptions. Use warm standby environments with synchronized datasets to enable quick failover and avoid data loss or research disruption.

 **Desired outcome:**
+  Continuous data access during maintenance and outages.
+  Minimal risk of data loss or corruption across failure events.
+  Trust in the accuracy, completeness, and reproducibility of research datasets.

 **Common anti-patterns:**
+  Relying on manual backups without automated validation or recovery testing.
+  Replicating data without maintaining consistency or integrity verification.
+  Treating replication as optional for intermediate or temporary data sources unless cost/time-effective to reproduce.

 **Benefits of establishing this best practice:**
+  Enables uninterrupted access to experimental results and research datasets.
+  Reduces risk of losing critical data from unique or costly experiments.
+  Supports reproducibility and regulatory adherence (like audit trails and traceability).
+  Strengthens collaboration by making shared datasets available globally.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Data availability must be preserved even when system components undergo maintenance or fail unexpectedly. Structured research data, such as LIMS transactions, should use multi-zone replication to maintain availability, while unstructured research datasets should be replicated across independent storage domains. Monitoring replication lag and validating dataset consistency are critical to avoid silent data corruption. Automated recovery validation and regular restore drills build trust that data can be recovered accurately and within defined RPO and RTO objectives.

### Implementation steps
<a name="implementation-steps"></a>

1.  Configure Amazon RDS Multi-AZ deployments for LIMS databases to achieve transactional durability.

1.  Use Amazon S3 Cross-Region Replication (CRR) for uninterrupted access to critical datasets, and protect large-scale file-based research workloads with Amazon FSx for Lustre combined with snapshot policies managed by AWS Backup.

1.  Define automated recovery validation policies in AWS Backup for audit tracking.

1.  Continuously monitor replication lag and recovery objectives through Amazon CloudWatch, aligning recovery metrics with the needs of research workflows.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  Data lifecycle management for research datasets
+  Data integrity and reproducibility controls
+  Governance documentation for GxP-relevant systems

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
