---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-APIs-cancel-query.html
---

# CancelQuery
<a name="query-APIs-cancel-query"></a>

CancelQuery cancels a specific query request.

## CancelQuery inputs
<a name="query-APIs-cancel-query-inputs"></a>
+ graph-identifier (required)

  Type: `String`

  The identifier representing a graph.
+ region (required)

  Type: `String`

  The region where the graph is present.
+ query-id (required)

  Type: `String`

  The id of the query request for which you want to cancel.

## CancelQuery outputs
<a name="query-APIs-cancel-query-outputs"></a>

CancelQuery does not have any output.

## CancelQuery examples
<a name="query-APIs-cancel-query-examples"></a>

------
#### [ AWS CLI ]

```
aws neptune-graph cancel-query \
    --graph-identifier <graph-id> \
    --region <region> \
    --query-id <query-id>
```

------
#### [ AWSCURL ]

```
awscurl -X DELETE "https://<graph-id>.<endpoint>/queries/<query-id>"  --region us-east-1 --service neptune-graph
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
