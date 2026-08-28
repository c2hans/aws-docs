---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-data-model.html
---

# Neptune Graph Data Model
<a name="feature-overview-data-model"></a>

The basic unit of Amazon Neptune graph data is a four-position (quad) element, which is similar to a Resource Description Framework (RDF) quad. The following are the four positions of a Neptune quad:
+ `subject    (S)`
+ `predicate  (P)`
+ `object     (O)`
+ `graph      (G)`

Each quad is a statement that makes an assertion about one or more resources. A statement can assert the existence of a relationship between two resources, or it can attach a property (key-value pair) to a resource. You can think of the quad predicate value generally as the verb of the statement. It describes the type of relationship or property that's being defined. The object is the target of the relationship, or the value of the property. The following are examples:
+ A relationship between two vertices can be represented by storing the source vertex identifier in the `S` position, the target vertex identifier in the `O` position, and the edge label in the `P` position.
+ A property can be represented by storing the element identifier in the `S` position, the property key in the `P` position, and the property value in the `O` position.

The graph position `G` is used differently in the different stacks. For RDF data in Neptune, the `G` position contains a [named graph identifier](https://www.w3.org/TR/rdf11-concepts/#section-dataset). For property graphs in Gremlin, it is used to store the edge ID value in the case of an edge. In all other cases, it defaults to a fixed value.

A set of quad statements with shared resource identifiers creates a graph.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
