---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/aossus03-bp03.html
---

# AOSSUS03-BP03 Take manual snapshots of your indices only when it is difficult to recreate the dataset
<a name="aossus03-bp03"></a>

 Reduce unnecessary snapshot creation, Amazon EBS, and Amazon S3 storage costs by taking manual snapshots only when it's difficult to recreate the dataset.

 **Level of risk exposed if this best practice is not established:** Medium

 **Desired outcome:** You take manual snapshots of indices only when it is difficult to recreate the dataset, reducing unnecessary snapshot creation and Amazon S3 storage.

 **Benefits of establishing this best practice:**
+  Reduced Amazon EBS and Amazon S3 storage costs
+  Improved resource utilization and reduced waste

## Implementation guidance
<a name="implementation-guidance-62"></a>

 Snapshots in Amazon OpenSearch Service serve as backups for a domain's indexes and state. Excessive snapshot leads to unnecessary storage and energy wastage.

 Delete unneeded snapshots using `DELETE _snapshot/repository-name/snapshot-name`.

## Resources
<a name="resources-62"></a>
+  [Deleting manual snapshots](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-snapshots.html#managedomains-snapshot-delete)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
