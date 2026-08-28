---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/managed-tier-checkpointing-remove.html
---

# Removing managed tiered checkpointing
<a name="managed-tier-checkpointing-remove"></a>

This section explains how to disable managed tiered checkpointing when you no longer need it.

To disable managed tiered checkpointing, use the [`update-cluster`](https://docs.aws.amazon.com/cli/latest/reference/sagemaker/update-cluster.html) AWS CLI to update your cluster configuration:

```
aws sagemaker update-cluster \
    --cluster-name {{cluster-name}} \
    --tiered-storage-config '{ "Mode": "Disable" }'
```

This removes the memory management daemon from your cluster. The daemon is implemented as a standard Kubernetes DaemonSet and follows standard Kubernetes lifecycle management.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
