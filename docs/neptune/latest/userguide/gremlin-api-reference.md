---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-api-reference.html
---

# Using the Gremlin API with Amazon Neptune
<a name="gremlin-api-reference"></a>

**Note**
Amazon Neptune does not support the `bindings` property.

Gremlin HTTPS requests all use a single endpoint: `https://{{your-neptune-endpoint}}:{{port}}/gremlin`. All Neptune connections must use HTTPS.

You can connect the Gremlin Console to a Neptune graph directly through WebSockets.

For more information about connecting to the Gremlin endpoint, see [Accessing a Neptune graph with Gremlin](access-graph-gremlin.md).

The Amazon Neptune implementation of Gremlin has specific details and differences that you need to consider. For more information, see [Gremlin standards compliance in Amazon Neptune](access-graph-gremlin-differences.md).

For information about the Gremlin language and traversals, see [The Traversal](https://tinkerpop.apache.org/docs/current/reference/#traversal) in the Apache TinkerPop documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
