---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step1-hierarchical-model.html
---

# Step 1: Identify the use cases and logical data model
<a name="step1-hierarchical-model"></a>

An automotive company wants to build a transactional component management system to store and search for all of the available car parts and to build relationships between different components and parts. For example, a car contains multiple batteries, each battery contains multiple high-level modules, each module contains multiple cells, and each cell contains multiple low-level components.

Generally, for building a hierarchical relationship model, a graph database such as [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html) is a better choice. In some cases, however, Amazon DynamoDB is a better alternative for hierarchical data modeling because of its flexibility, security, performance, and scale.

For example, you might build a system where 80–90 percent of the queries are transactional, where DynamoDB fits well. In this example, the other 10–20 percent of queries are relational, where a graph database such as Neptunefits better. In this case, including an additional database in the architecture to fulfill only 10–20 percent of the queries could increase cost. It also adds the operational burden of maintaining multiple systems and synchronizing the data. Instead, you can model that 10–20 percent relational queries in DynamoDB.

Diagramming an example tree for car components can help you map the relationship between them. The following diagram shows a dependency graph with four levels. CM1 is the top-level component for the example car itself. It has two subcomponents for two example batteries, CM2 and CM3. Each battery has two subcomponents, which are the modules. CM2 has modules CM4 and CM5, and CM3 has modules CM6 and CM7. Each module has several subcomponents, which are the cells. The CM4 module has two cells, CM8 and CM9. CM5 has one cell, CM10. CM6 and CM7 don't have any associated cells yet.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/images/guide-img/225c2600-95f1-4c8c-9e23-419bc7ae3c55/images/add4af92-a6e7-4cec-b42f-534de207a2b3.png)

This guide will use this tree and its component identifiers as a reference. A top component will be referred to as a *parent*, and a subcomponent will be referred to as a *child***.** For example, top component CM1 is the parent of CM2 and CM3. CM2 is the parent of CM4 and CM5. This graphs the parent-child relationships.

From the tree, you can see the complete dependency graph of a component. For example, CM8 is dependent on CM4, which is dependent on CM2, which is dependent on CM1. The tree defines the complete dependency graph as the path. A path describes two things:
+ The dependency graph
+ The position in the tree

Filling the templates for business requirements:

Provide information about your users:

|
|
| User | Description |
| --- |--- |
| Employee | Internal employee of the automotive company that needs information of cars and its components |

Provide information about the sources of data and how data will be ingested:

|
|
| Source | Description | User |
| --- |--- |--- |
| Management system | System that will store all the data related to available car parts and their relationships with other components and parts. | Employee |

Provide information about how data will be consumed:

|
|
| Consumer | Description | User |
| --- |--- |--- |
| Management system | Retrieve all the immediate child components for a parent component ID. | Employee |
| Management system | Retrieve a recursive list of all child components for a component ID. | Employee |
| Management system | See the ancestors of a component. | Employee |
