---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/lambda-functions-gremlin-write-recommendations.html
---

# Recommendations for using Gremlin write-requests in Lambda
<a name="lambda-functions-gremlin-write-recommendations"></a>

If your Lambda function modifies graph data, consider adopting a back-off-and-retry strategy to handle the following exceptions. For detailed guidance on developing a practical retry strategy, see [Exception Handling and Retries](transactions-exceptions.md).
+ **`ConcurrentModificationException`**   –   The Neptune transaction semantics mean that write requests sometimes fail with a `ConcurrentModificationException`. In these situations, try an exponential back-off-based retry mechanism.
+ **`ReadOnlyViolationException`**   –   Because the cluster topology can change at any moment as a result of planned or unplanned events, write responsibilities may migrate from one instance in the cluster to another. If your function code attempts to send a write request to an instance that is no longer the primary (writer) instance, the request fails with a `ReadOnlyViolationException`. When this happens, close the existing connection, reconnect to the cluster endpoint, and then retry the request.

Also, if you use a back-off-and-retry strategy to handle write request issues, consider implementing idempotent queries for create and update requests using [Making efficient upserts with Gremlin `mergeV()` and `mergeE()` steps](gremlin-efficient-upserts.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
