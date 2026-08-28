---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel10-bp03.html
---

# LSREL10-BP03 Test data integrity under failure conditions
<a name="lsrel10-bp03"></a>

 Design and execute specific tests to validate that data integrity is preserved during system failures, network outages, or recovery processes. For workloads involving trial data, manufacturing records, or patient datasets, enforce transactional boundaries, roll back partial updates safely, and block corrupted data from entering downstream systems.

 **Desired outcome:**
+  Data integrity maintained during failures and recovery.
+  Tests confirm correct handling of partial transactions and error scenarios.
+  Evidence demonstrates adherence to data integrity requirements.

 **Common anti-patterns:**
+  Relying on functional tests without failure/integrity validation.
+  No rollback or compensation testing for partial failures.
+  Assuming backups restore consistent datasets without testing.

 **Benefits of establishing this best practice:**
+  Protects against corrupted datasets invalidating scientific outcomes.
+  Builds trust in data reproducibility and traceability for regulators.
+  Avoids costly reruns of experiments or trials due to data loss.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Incorporate integrity validation into test plans for recovery and failover.

 Test for both transient disruptions and long-term outages.

 Use domain-specific integrity checks for genomic, clinical, or manufacturing datasets.

### Implementation steps
<a name="implementation-steps"></a>

1.  Enable Amazon RDS point-in-time recovery and validate consistency after restore.

1.  Run AWS Glue Data Quality jobs to verify schema and record consistency.

1.  Store validation reports in Amazon S3 with Object Lock for immutability.

1.  Integrate validation results into reports with AWS Audit Manager.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
