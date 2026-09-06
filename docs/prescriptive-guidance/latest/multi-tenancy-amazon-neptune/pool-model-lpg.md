---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/multi-tenancy-amazon-neptune/pool-model-lpg.html
---

# Pool model for labeled property graphs
<a name="pool-model-lpg"></a>

There are three different approaches to the pool model for LPGs on Amazon Neptune:
+ **Property strategy** ‒ Choose the property strategy when you need to prioritize use of established library constructs such as the Apache TinkerPop Gremlin language's [PartitionStrategy](https://tinkerpop.apache.org/docs/current/reference/#partitionstrategy) over performance.
+ **Prefix-label strategy** ‒ We recommend the prefix-label strategy for most scenarios based on performance and limiting noisy neighbor effects.
+ **Multiple-label strategy** ‒ The multiple-label strategy has the improved performance of the prefix-label strategy. It also supports running queries that span all of the tenants on a cluster (for example, ISV queries for reporting or monitoring across all tenants).

## Property strategy
<a name="property"></a>

With LPGs, users can add key-value pair properties to nodes, or vertices, and edges. To achieve logical separation, most customers intuitively model this as a unique property on every node and edge with a common *tenant property key*. The tenant property key represents the all the tenants that own the node. The *tenant identifier* is a unique value that identifies an individual tenant.

The following diagram shows this model. The two disconnected subgraphs have various labeled nodes and edges, with the tenant property key represented by `TId`. Every node and edge from one subgraph has a `TId` value of `1`. In the other subgraph, every node and edge has a `TId` value of `2`.

![Nodes and their relationships.](http://docs.aws.amazon.com/prescriptive-guidance/latest/multi-tenancy-amazon-neptune/images/guide-img/d9a33330-1308-4d3e-b2de-9b5b65b34e0f/images/89c0183e-e639-4f19-90e9-edac2d28aec8.png)

Within labeled property graphs, there are two ways to manage this. The Gremlin query language offers the  [PartitionStrategy](https://tinkerpop.apache.org/docs/current/reference/#partitionstrategy) traversal library to help manage data partitioning of the data. The code in the following example expects every node and edge to have a property called `TId`:

```
strategy1 = new PartitionStrategy(partitionKey: "TId", writePartition: "1", readPartitions: ["1"])
strategy2 = new PartitionStrategy(partitionKey: "TId", writePartition: "2", readPartitions: ["2"])
```

When new nodes or edges are written, the property `"TId"` is added with a value of `"1"` or `"2"`, depending on whether `strategy1` or `strategy2` was selected. For the customer with `"TId"` of `"1"`, you use `strategy1`. The following example shows writing data for that customer:

```
g.withStrategies(strategy1).addV("Label1").property("Value", "123456").property(id, "Item_1")
```

For read queries, a filter for `"TId == '1'"` or `"TId == '2'"` is added to every node or edge traversal by using `strategy1` or `strategy2`, respectively. These partition strategies simplify your code, but they aren't necessary. The benefit of using the strategy is that it can be injected at an authorization level and passed to the lower-level code that forms the query. This separates the code that determines the customer identifier (`TId`) from the logic of the query.

The following example code shows a Gremlin query to read data:

```
g.withStrategies(strategy1).V().hasLabel("Label1")
```

The preceding code is equivalent to the following example:

```
g.V().hasLabel("Label1").has("TId", "1")
```

Likewise, when writing data by using Gremlin, you can use the following query:

```
g.withStrategies(strategy1).addV("Label1").property("Value").property(id, "Item_1")
```

The preceding code is equivalent to the following example, which does not use the partition strategy and therefore requires the `"TId"` property to be explicitly written:

```
g.addV("Label1").property("TId", "1").property("Value").property(id, "Item_1")
```

In openCypher, these libraries do not exist. You are responsible for writing and modifying your queries to add the tenant identifier as a property on nodes and edges. For example:

```
CREATE (n:Item {`~id`: 'Item_1', Value: '123456', TId: '1'})
CREATE (n:Item {`~id`: 'Item_2', Value: '123456', TId: '2'})
```

Note the similarity between the Gremlin code without the partition strategy. You can then read the node written from the first `CREATE` statement by using the following code:

```
MATCH (n:Item {TId: '1'})
RETURN n
--or
MATCH (n:Item)
WHERE n.TId == '1'
RETURN n
```

You might choose the property strategy when you want to use native TinkerPop Gremlin constructs such as PartitionStrategy. However, this model has performance drawbacks on Amazon Neptune compared with the prefix-label strategy. For a discussion of these performance drawbacks, see the [Performance implications for the LPG models](#perf) section.

If the following conditions apply, consider modeling the property strategy only on nodes, not on edges:
+ Your graph has significantly more edges than labels.
+ Each tenant is a disconnected graph.
+ You access the graph only by using nodes as a starting point, not labels.

## Prefix-label strategy
<a name="prefix-label"></a>

If performance is a top concern, we highly recommend considering the prefix-label strategy over the property strategy.

In the prefix-label strategy, you label each node with a combination of tenant identifier and node label. For example, if the tenant has an identifier of `"1"` and the node label is `"Label1"`, you specify the node label as `"1-Label1"`. The following diagram shows two disconnected subgraphs that use this model.

![Nodes with labels that include prefixes, and node relationships.](http://docs.aws.amazon.com/prescriptive-guidance/latest/multi-tenancy-amazon-neptune/images/guide-img/d9a33330-1308-4d3e-b2de-9b5b65b34e0f/images/63e9d001-757f-4c92-8142-f598f4ef50f6.png)

When writing data in Gremlin, you can add an identifying number to any node's label:

```
g.addV("1-Label1")
g.addV("2-Label6")
```

When querying this graph, you can check for the existence of this prefix on a node:

```
g.V().hasLabel("1-Label1")
```

In openCypher you can write data by using a `CREATE` statement:

```
CREATE (n:`1-Label1` {`~id`: 'Item_1', Value: 'XYZ123456'})
```

To query the data that you wrote in openCypher, use the following code:

```
MATCH n= (:`1-Label1`)
RETURN n
```

The prefix-label strategy assumes that all nodes are assigned to one or more tenants and that permissions are not assigned at the edge scope. Avoid using this strategy on edge labels, because that will cause a large number of predicates and will negatively impact Neptune performance.

There are two primary drawbacks to the prefix label approach. First, it's difficult to run any queries that span across tenants. An example is a query that counts all nodes of a given label for reporting or monitoring. If this is your use case, consider combining this strategy with the multiple-label strategy. For more information about combining strategies, see the [Hybrid model](hybrid-model.md) section. Second, the prefix-label strategy requires controls that enforce proper application of the appropriate prefix to every query to prevent data leakage. However, this strategy is the most efficient option for workloads that require low latency queries, and we highly recommend it. The [Performance implications for LPG models](#perf) section provides examples of why this is the most efficient strategy.

## Multiple-label strategy
<a name="multi-label"></a>

The third option is to use a multiple-label strategy. For this approach, you add extra labels to every node on the graph. For example, if you need to filter across all of the data for a given tenant, add the tenant ID label. If you need to filter across all data for a given label regardless of tenant, add that label. The following diagram shows the multiple-label strategy applied by using three labels for each node.

![Nodes and their relationships, where each node has LabelX, X, X-LabelX.](http://docs.aws.amazon.com/prescriptive-guidance/latest/multi-tenancy-amazon-neptune/images/guide-img/d9a33330-1308-4d3e-b2de-9b5b65b34e0f/images/afa0545d-d140-4ee5-9577-afdc81e4ca9a.png)

You can now access the graph by using three different patterns:
+ Filter on `Label1` to return all nodes with `Label1` across all tenants.
+ Filter on `1` to return all nodes for tenant 1.
+ Filter on `1-Label1` to return all nodes for only tenant 1 with label `Label1`.

For LPGs, there are two ways to implement this.

In Gremlin, you can use the traversal strategy called [SubgraphStrategy](https://tinkerpop.apache.org/javadocs/current/full/org/apache/tinkerpop/gremlin/process/traversal/strategy/decoration/SubgraphStrategy.html) to limit the scope of all queries to only vertices with a specific label, such as `"Label1"`:

```
g.withStrategies(
    new SubgraphStrategy(
        vertices=hasLabel("Label1")
    )
)
```

Unlike PartitionStrategy, SubgraphStrategy impacts reading data only, not writing data. To write the data, manually assign the labels in each query:

```
g.addV("Label1").property("Value","XYZ123456")
.addV("Label2").property("Value","XYZ123456")
```

When reading the data, you can use SubgraphStrategy to query all nodes with `"Label1"`:

```
g.withStrategies(
new SubgraphStrategy(vertices=.hasLabel("Label1"))
).
V().has("Value","XYZ123456")
```

Neptune returns only the first record, which has `"Label1"` and a value of `"XYZ123456"`. It's equivalent to the following query, which doesn't use SubgraphStrategy:

```
g.V().hasLabel("Label1").hasValue("XYZ123456")
```

In this basic query, it appears that SubgraphStrategy is more complex to use. Keep in mind that your libraries can provide an instance of `g` with the strategy already defined. Developers don't have to ensure that the proper filters are applied:

```
def getGraphTraversal():
return g.withStrategies(new SubgraphStrategy(vertices=.hasLabel("Label1"))

getGraphTraversal().has("Value","XYZ123456")
```

The openCypher libraries don't have these constructs, so you must create multiple labels for each node:

```
CREATE (n:`1`:`Label1`:`1-Label1` {`~id`: 'Item_1', Value: '12345'})
```

When you use these labels to filter for a subgraph, you can return nodes that have the customer label you are looking for or that share a relationship with another node that has that label:

```
MATCH n=(:Label1:`1`)
// or
MATCH n=(:`1-Label1`)
```

The multiple-label strategy gives you the most flexibility to query nodes by type (`Label1`) or tenant (`1`), or to use the more efficient prefix-label strategy when performance is of most importance (`1-Label1`).

The major drawback to this strategy is that each label is an extra object stored in your graph. An object is a node, edge, or a property on a node or edge in LPGs. Ingestion speed is measured and bound by objects per second, and storage costs depend on the number of gigabytes consumed. This means that extra objects might have a measurable impact at large scale.

## Performance implications for the LPG models
<a name="perf"></a>

The AWS Skill Builder course [Data Modeling for Amazon Neptune](https://explore.skillbuilder.aws/learn/course/external/view/elearning/16133/data-modeling-for-amazon-neptune) describes in depth the Neptune data model internals and modeling implications, but we will summarize the important considerations for these designs here. Consider having three tenants (T1, T2, T3) on a single Neptune cluster. These tenants have the following attributes:
+ Tenant 1 (T1) has 100 million nodes total, and 10 million are of type Item.
+ Tenant 2 (T2) has 10 million nodes total, and 1 million are of type Item.
+ Tenant 3 (T3) has 100 million nodes total, and 1 million are of type Item.

Run a query that will retrieve the items for Tenant 3 by using the property strategy. Neptune inspects the statistics for two index calls:
+ Where `tenant property key=T3` has 100 million results
+ Where `label = Item` has 12 million results (10 million from T1 \+ 1 million from T2 \+ 1 million from T3)

The Neptune query optimizer determines that the latter query is best applied first (12 million results) and then inspects each item for `tenant property key=T3`. You retrieve 12 million items to find the 1 million results.

Notice the noisy neighbor impact of this query. If you had 100 million Item nodes per tenant, the first query would have 300 million results instead of 12 million (This is overly simplified for illustrative purposes. The Neptune optimizer might have applied a different order of operations).

Next, consider the prefix-label strategy. Make a single index call where `label=T3-Item`, which  returns 1 million results. This accomplishes the same result as the property strategy, but it retrieves 11 million fewer records. In addition, you no longer have noisy neighbor concerns because the label doesn't overlap in the index.

The multiple-label strategy doesn't provide query performance improvement over the property strategy directly. Filtering by property value is comparable to filtering by label value when the search space is also comparable. Instead, the multiple-label strategy supports more flexibility.  The multiple-label strategy provides performance equivalent to the prefix-label strategy for `label=T3` or the label `T3-Item`. The multiple-label strategy provides performance equivalent to the property strategy for `label=Item`. The benefit is to support a variety of access patterns.
