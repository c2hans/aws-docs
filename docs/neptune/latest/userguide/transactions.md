---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/transactions.html
---

# Transaction Semantics in Neptune
<a name="transactions"></a>

Amazon Neptune is designed to support highly concurrent online transactional processing (OLTP) workloads over data graphs. The [W3C SPARQL Query Language for RDF](https://www.w3.org/TR/rdf-sparql-query/) specification and the [Apache TinkerPop Gremlin Graph Traversal Language](http://tinkerpop.apache.org/gremlin.html) documentation do not define transaction semantics for concurrent query processing. Because ACID support and well-defined transaction guarantees can be very important, we enforce strict semantics to help avoid data anomalies.

This section defines these semantics and illustrates how they apply to some common use cases in Neptune.

**Topics**
+ [Definition of Isolation Levels](transactions-isolation-levels.md)
+ [Transaction Isolation Levels in Neptune](transactions-neptune.md)
+ [Examples of Neptune transaction semantics](transactions-examples.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
