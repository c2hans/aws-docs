---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-self-managed-kubernetes-cluster-to-amazon-eks/rollback-and-cleanup.html
---

# Rollback and cleanup
<a name="rollback-and-cleanup"></a>

If issues arise after migration, use the rollback script to remove migrated resources from the target Amazon EKS cluster:

1. Switch kubectl context to the target Amazon EKS cluster:

   ```
   aws eks update-kubeconfig --name <cluster-name> --region <region>
   ```

1. Run a dry-run rollback:

   ```
   cd rollback/
   python3 rollback_eks_migration.py --dry-run
   ```

1. Review the dry-run rollback output. Confirm that only the expected migrated resources are listed for deletion. The rollback proceeds in reverse order: networking → workloads → CRDs → config → storage → RBAC → namespaces.

1. Run the full rollback:

   ```
   python3 rollback_eks_migration.py
   ```

1. Review the rollback report. The `rollback_report.json` file is saved alongside the migration report with details of what was deleted, what was skipped, and any errors encountered.

1. Verify cleanup by running these commands to confirm that all migrated resources have been removed from the target Amazon EKS cluster:

   ```
   kubectl get namespaces
   kubectl get deployments --all-namespaces
   kubectl get services --all-namespaces
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
