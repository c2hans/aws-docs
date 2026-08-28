---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp05.html
---

# MIDASEC03-BP05 Implement data retention policies for each data class
<a name="midasec03-bp05"></a>

 Define and enforce data retention rules based on classification and regulatory requirements to reduce storage costs and minimize compliance risks.

 **Desired outcome:** Only required data is retained, improving cost efficiency and reducing exposure of legacy data.

 **Benefits of establishing this best practice:** Helps prevent unnecessary storage costs, reduce audit complexity, and support lifecycle compliance.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-18"></a>

 Use Amazon S3 lifecycle policies, AWS Glue table TTLs, and tagging strategies to automate enforcement of retention policies.

### Implementation steps
<a name="implementation-steps-19"></a>
+  Define data retention durations based on classification and compliance needs.
+  Apply tags and metadata to datasets to identify lifecycle requirements.
+  Use S3 lifecycle rules or Glue jobs to delete or archive data.
+  Regularly review and update retention policies based on changing regulations.

## Resources
<a name="resources-19"></a>
+  [ Managing your storage lifecycle ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
+  [AWS Glue Documentation ](https://docs.aws.amazon.com/glue/index.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
