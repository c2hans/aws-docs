---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-aoss-cleanup.html
---

# Step 10: Clean up
<a name="pb-aoss-cleanup"></a>

After the rollback window has passed and the collection is serving production traffic successfully, remove the migration scaffolding.

1. Unregister the snapshot repository and remove the snapshot from Amazon S3 if you no longer need it:

   ```
   console snapshot delete
   console snapshot unregister-repo
   ```

1. Reset the migration custom resources on Amazon EKS:

   ```
   workflow reset --all
   ```

1. Remove the Migration Assistant infrastructure once you are done with all migrations. See [Uninstall the solution](uninstall-the-solution.md).

**Warning**
Deleting a collection is irreversible and removes all of its indexed data. Only delete a collection you created purely for testing, and never delete a production collection without explicit confirmation that it is no longer needed.

If you created a **throwaway** test collection (not your production target), delete it and its policies after you are finished:

```
aws opensearchserverless delete-collection --name vector-search
```

After the collection is deleted, you can detach and delete its network, encryption, and data access policies. Leave your production collection and its policies in place.

For deeper guidance on the destination platform, see [Migrate to Amazon OpenSearch Serverless NextGen](migrate-to-serverless.md). For error-specific help, see [Troubleshooting](troubleshooting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
