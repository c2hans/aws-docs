---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-sparql-query.html
---

# Querying All Named Graphs by Default
<a name="best-practices-sparql-query"></a>

Amazon Neptune associates every triple with a named graph. The default graph is defined as the union of all named graphs.

If you submit a SPARQL query without explicitly specifying a graph via the `GRAPH` keyword or constructs such as `FROM NAMED`, Neptune always considers all triples in your DB instance. For example, the following query returns all triples from a Neptune SPARQL endpoint:

```
SELECT * WHERE { ?s ?p ?o }
```

Triples that appear in more than one graph are returned only once.

For information about the default graph specification, see the [RDF Dataset](https://www.w3.org/TR/sparql11-query/#rdfDataset) section of the SPARQL 1.1 Query Language specification.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
