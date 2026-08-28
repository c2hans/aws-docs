---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/workflow-driven-operating-model.html
---

# Workflow-driven operating model
<a name="workflow-driven-operating-model"></a>

Migration Assistant 3.0 is built around three ideas:

1.  **Declare the migration once** in workflow configuration instead of stitching together long-lived infrastructure by hand.

1.  **Let Amazon EKS run the work** so migration tasks can be created, retried, scaled, and cleaned up as Kubernetes-managed workloads.

1.  **Use the Workflow CLI** for submission, approval, validation, and cutover so customers think in terms of workflow configuration and approval gates rather than individual infrastructure commands.

A typical migration follows this lifecycle:

1.  **Assess** compatibility, unsupported components, and downtime needs.

1.  **Deploy** Migration Assistant on Amazon EKS using the bootstrap script.

1.  **Configure** the workflow from the version-matched sample on the Migration Console.

1.  **Run a pilot** on a small index allowlist.

1.  **Submit** the real workflow and monitor it through `workflow manage`.

1.  **Approve** gated transitions only after validation.

1.  **Cut over** to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

1.  **Remove infrastructure** only after the rollback window has passed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
