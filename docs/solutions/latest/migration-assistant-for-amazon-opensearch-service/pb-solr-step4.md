---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-solr-step4.html
---

# Step 4: Verify the migration
<a name="pb-solr-step4"></a>

After backfill completes, confirm the target holds the expected indexes and documents. List the indexes and compare document counts between source and target:

```
console clusters cat-indices --refresh
```

Check the document count for a migrated collection on the target. Each Apache Solr collection or core becomes an index of the same name on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection:

```
console clusters curl target /<collection>/_count
```

Compare the returned count against the document count reported by Apache Solr for the same collection. Then spot-check a few documents to confirm stored field values migrated correctly:

```
console clusters curl target /<collection>/_search?size=5&pretty
```

Solr backup backfill reconstructs target ` source<absoluteLuceneDocNumber>` document ID. For the full behavior, see [Document reconstruction](solr-document-reconstruction.md).

If you are migrating an application, also run representative production-like queries against the target to confirm that clients can locate the expected fields and retrieve expected results before you cut over. Remember that Apache Solr query syntax differs from the OpenSearch query DSL, so client query code generally needs to be rewritten — validate it against the migrated data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
