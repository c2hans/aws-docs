---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tdvk-identify-fields.html
---

# Identifying dense\_vector fields before you migrate
<a name="tdvk-identify-fields"></a>

Before you run metadata migration, find which indexes use `dense_vector` so you can plan validation around them. Query the source cluster’s mappings from the Migration Console pod (`migration-console-0`):

```
console clusters curl source /_mapping?pretty
```

To inspect a single index:

```
console clusters curl source /<INDEX>/_mapping?pretty
```

Look for fields whose `type` is `dense_vector`. Note the field name, the configured number of dimensions, and the similarity setting for each one — you will compare these against the transformed `knn_vector` definition on the target during validation.

You can also preview the transformation outcome without writing to the target by running the metadata evaluate step. This scans the source, applies the built-in transformations, and reports what would be migrated:

```
console metadata evaluate
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
