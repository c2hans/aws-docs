---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/sparql-explain.html
---

# Analyzing Neptune query execution using SPARQL `explain`
<a name="sparql-explain"></a>

Amazon Neptune has added a SPARQL feature named *explain*. This feature is a self-service tool for understanding the execution approach taken by the Neptune engine. You invoke it by adding an `explain` parameter to an HTTP call that submits a SPARQL query.

The `explain` feature provides information about the logical structure of query execution plans. You can use this information to identify potential evaluation and execution bottlenecks. You can then use [query hints](sparql-query-hints.md) to improve your query execution plans.

**Topics**
+ [How the SPARQL query engine works in Neptune](sparql-explain-engine.md)
+ [How to use SPARQL `explain` to analyze Neptune query execution](sparql-explain-using.md)
+ [Examples of invoking SPARQL `explain` in Neptune](sparql-explain-examples.md)
+ [Neptune SPARQL `explain` operators](sparql-explain-operators.md)
+ [Limitations of SPARQL `explain` in Neptune](sparql-explain-limitations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
