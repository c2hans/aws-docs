---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-cleanup.html
---

# Step 13: Clean up
<a name="pb-es68-cleanup"></a>

Only after the rollback window has passed should you remove the Migration Assistant infrastructure. Remove the workload, its storage, and the AWS CloudFormation stack.

1. Uninstall the Migration Assistant release and delete its persistent volume claims in the `ma` namespace:

   ```
   helm uninstall -n ma ma
   kubectl delete pvc --all -n ma
   ```

1. Delete the AWS CloudFormation stack that created the deployment:

   ```
   aws cloudformation delete-stack --stack-name MA --region <REGION>
   ```

1. Optionally, remove the snapshot bucket once you are certain you no longer need the snapshot. This is destructive and permanent:

   ```
   aws s3 rb s3://<SNAPSHOT_BUCKET> --force --region <REGION>
   ```

**Warning**
Deleting the AWS CloudFormation stack and the snapshot bucket is irreversible. Confirm the migration succeeded and the rollback window has fully passed before you run these commands. For the full removal procedure, see [Uninstall the solution](uninstall-the-solution.md).

For deployment, connectivity, authentication, and metadata issues encountered during any step of this playbook, see [Troubleshooting](troubleshooting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
