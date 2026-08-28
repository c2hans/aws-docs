---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-aoss-validate.html
---

# Step 8: Validate in three levels
<a name="pb-aoss-validate"></a>

Validate the collection in increasing depth before you trust it with production traffic.

## Level 1: The collection is reachable
<a name="pb-aoss-validate-reachable"></a>

Confirm the Migration Console can reach and authenticate to the collection:

```
console clusters connection-check --cluster target
console clusters curl target /
```

## Level 2: Index and document counts match
<a name="pb-aoss-validate-counts"></a>

Compare index lists and per-index document counts between the source domain and the collection:

```
console clusters cat-indices --refresh
console clusters curl target /<index>/_count
```

Document counts on the target may differ slightly from the source if the source had deleted-but-not-merged documents; investigate only material gaps. Use the failed-document [Amazon CloudWatch](https://aws.amazon.com/cloudwatch) Logs Insights query in [Verifying no failed documents](running-backfill.md#verify-failed-documents) to confirm nothing was dropped.

## Level 3: Representative vector queries
<a name="pb-aoss-validate-vectors"></a>

For a vector-search workload, run representative k-NN queries against the collection and confirm the results match what the source returns for the same query vectors:

```
console clusters curl target /<index>/_search?pretty -XPOST \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 5,
    "query": {
      "knn": {
        "<vector-field>": { "vector": [0.1, 0.2, 0.3], "k": 5 }
      }
    }
  }'
```

Verify that the `dense_vector`-to-`knn_vector` field-type transformation produced the expected mapping on the target, and that scores and ranking are consistent with the source for a sample of known queries.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
