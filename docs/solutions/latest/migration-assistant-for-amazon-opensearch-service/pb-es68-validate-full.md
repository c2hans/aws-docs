---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-validate-full.html
---

# Step 11: Validate and switch traffic
<a name="pb-es68-validate-full"></a>

When the full backfill completes, validate completeness across all indexes:

```
console clusters cat-indices --refresh
```

Compare source and target document counts. For a comprehensive check that identifies any documents that failed to index, query the `OpenSearchMigrations` log group in [Amazon CloudWatch](https://aws.amazon.com/cloudwatch) for bulk failures.

After validation passes and your application team is ready, switch traffic to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. For the cutover checklist and the rollback principle, see [Cutover and rollback](cutover.md). In practice, cutover usually means updating a DNS record, a load balancer backend, an application connection string, or a service-discovery entry to point clients at the target.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
