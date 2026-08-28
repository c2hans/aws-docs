---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-explain.html
---

# Analyzing Neptune query execution using Gremlin `explain`
<a name="gremlin-explain"></a>

Amazon Neptune has added a Gremlin feature named *explain*. This feature is a self-service tool for understanding the execution approach taken by the Neptune engine. You invoke it by adding an `explain` parameter to an HTTP call that submits a Gremlin query.

The `explain` feature provides information about the logical structure of query execution plans. You can use this information to identify potential evaluation and execution bottlenecks and tune your query, as explained in [Tuning Gremlin queries](gremlin-traversal-tuning.md). You can also use [query hints](gremlin-query-hints.md) to improve query execution plans.

**Topics**
+ [Understanding how Gremlin queries work in Neptune](gremlin-explain-background.md)
+ [Using the Gremlin `explain` API in Neptune](gremlin-explain-api.md)
+ [Gremlin `profile` API in Neptune](gremlin-profile-api.md)
+ [Tuning Gremlin queries using `explain` and `profile`](gremlin-traversal-tuning.md)
+ [Native Gremlin step support in Amazon Neptune](gremlin-step-support.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
