---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel07-bp02.html
---

# LSREL07-BP02 Build idempotent and reproducible processing pipelines
<a name="lsrel07-bp02"></a>

 Design processing systems that produce consistent results regardless of retries or partial failures. Incorporate unique identifiers, transaction logs, and state tracking to verify that retries don't duplicate or corrupt data. In research and clinical analysis, reproducibility of results under repeated execution is a cornerstone of scientific and regulatory assurance.

 **Desired outcome:** Processing pipelines can be retried without causing duplication or corruption, maintaining reproducibility of results under repeated execution.

 **Common anti-patterns:**
+  Designing pipelines that overwrite intermediate results without safeguards.
+  Using non-unique identifiers for jobs, leading to duplication of processed data.
+  Failing to persist state, making retries non-deterministic.

 **Benefits of establishing this best practice:**
+  Maintains scientific reproducibility by producing consistent outputs from the same inputs.
+  Reduces wasted compute cycles by allowing safe retries after transient errors.
+  Increases confidence in regulatory submissions where reproducibility is scrutinized.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Idempotency should be a foundational principle in workflow design. Each job execution must generate unique identifiers tied to input datasets and persist transaction logs or checkpoints. State tracking should record which inputs have been successfully processed, enabling retries without duplication. For long-running genomic analysis, idempotency verifies that a failed job can be retried without corrupting downstream results.

### Implementation steps
<a name="implementation-steps"></a>

1.  Processing pipelines should use AWS Step Functions or AWS Batch to track execution state and verify that retries are idempotent.

1.  Use Amazon DynamoDB or Amazon RDS to persist transaction logs and job state.

1.  Store intermediate artifacts in Amazon S3 with unique identifiers as S3 prefixes (for example, prefixing with dataset UUIDs) to maintain reproducibility.

1.  Implement retry policies with exponential backoff in AWS Step Functions, so transient failures don't result in duplicate or corrupted processing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
