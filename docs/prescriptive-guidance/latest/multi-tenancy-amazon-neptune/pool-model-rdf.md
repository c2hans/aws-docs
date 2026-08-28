---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/multi-tenancy-amazon-neptune/pool-model-rdf.html
---

# Pool model for RDF
<a name="pool-model-rdf"></a>

The Resource Description Framework (RDF) has a concept of named graphs, which provides a logical way of separating data. In Amazon Neptune, you have a default named graph and user-defined named graphs. You can create as many named graphs as you want. Collectively, they are called the RDF dataset. All named graphs, default or user-defined, are defined by an Internationalized Resource Identifier(IRI) within the RDF dataset. In Neptune, unless a user declared a named graph when writing data, all [triples](https://www.w3.org/TR/PR-rdf-syntax/#model) are considered part of the default named graph.

There are multiple use cases for named graphs:
+ Data partitioning and data isolation
+ Data provenance
+ Versioning
+ Inference

This guide focuses on the data-partitioning use case. We recommend creating one user-defined named graph for each tenant.

## SPARQL query options using Graph Store HTTP Protocol
<a name="sparql"></a>

The following example queries use SPARQL Protocol and RDF Query Language (SPARQL) and Graph Store HTTP Protocol to query or create a named graph for a tenant.
+ `HTTP GET` ‒ To retrieve a specific graph of a tenant:

  ```
  curl --request GET 'https://your-neptune-endpoint:port/sparql/gsp/?graph=http%3A//www.example.com/named/tenant1'
  ```
+ `HTTP PUT` ‒ To create or replace a specific named graph with a payload specified in the request:

  ```
  curl --request PUT -H "Content-Type: text/turtle" \  --data-raw "@prefix ex: http://example.com/ . ex:subject ex:predicate ex:object ." \
  'https://your-neptune-endpoint:port/sparql/gsp/?graph=http%3A//www.example.com/named/tenant1'
  ```

  In RDF, an object is a triple.
+ `HTTP POST` ‒ To create a new named graph if one doesn't exist, or merge with an existing graph:

  ```
  curl --request POST -H "Content-Type: text/turtle" \
  --data-raw "@prefix ex: http://example.com/ . ex:subject ex:predicate ex:object ." \
  'https://your-neptune-endpoint:port/sparql/gsp/?graph=http%3A//www.example.com/named/tenant1'
  ```

## Tenant isolation for RDF
<a name="isolation"></a>

For logical isolation of data with necessary guardrails in place at the application layer, create a mapping between the tenant and user-defined named graphs. When you design multi-tenancy for an RDF dataset, be aware of the following aspects of RDF and [SPARQL](https://www.w3.org/TR/sparql11-query/):
+ In Neptune, when you query without specifying a named graph, it retrieves all triples that match the pattern across all named graphs in the database.
+ In RDF, there are no constraints around connections between nodes of different named graphs. For instance, in the previous diagram, a node in `:G1` can be connected to a node in :`G2` through an edge.

For example, if an end user of a particular tenant submits a query to the API, the API should validate the following requirements before it submits the query to the Neptune database:
+ Any query scoped at a single tenant must specify a named graph. Otherwise, you risk leaking data across tenants.
+ Update or Delete queries should always specify a named graph.
+ Nodes on either side of an edge or relationship should always belong to the correct named graph.

For additional information about best practices, see the [Neptune documentation](https://docs.aws.amazon.com/neptune/latest/userguide/feature-sparql-compliance.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
