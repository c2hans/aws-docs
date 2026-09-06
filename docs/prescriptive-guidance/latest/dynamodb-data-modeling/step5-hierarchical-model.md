---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step5-hierarchical-model.html
---

# Step 5: Create a DynamoDB data model
<a name="step5-hierarchical-model"></a>

Define the partition keys for your base table and global secondary indexes (GSIs):
+ Following the key design best practices, use `ComponentId` as the partition key for the base table in this example. Because it's unique, `ComponentId` can offer granularity. DynamoDB uses the hash value of your partition key to determine the partition where the data is stored physically. The unique component ID generates a different hash value, which can facilitate distribution of data inside the table. You can query the base table by using a `ComponentId` partition key.
+ To find immediate children of a component, create a GSI where `ParentId` is the partition key, and `ComponentId` is the sort key. You can query this GSI by using `ParentId` as the partition key.
+ To find all recursive children of a component, create a GSI where `GraphId` is the partition key, and `Path` is the sort key. You can query this GSI by using `GraphId` as the partition key and the `BEGINS_WITH(Path, "$path")` operator on the sort key.

|  |
| --- |
|  | Partition key | Sort Key | Mapping attributes |
| --- |--- |--- |--- |
| **Base table** | `ComponentId` |  | `ParentId`, `GraphId`, `Path` |
| **GSI1** | `ParentId` | `ComponentId` |  |
| **GSI2** | `GraphId` | `Path` | `ComponentId` |

## Storing components in the table
<a name="store"></a>

The next step is to store each component in the DynamoDB base table. After you insert all the components from the example tree, you get the following base table.

|
|
| ComponentId | ParentId | GraphId | Path |
| --- |--- |--- |--- |
|  <br />CM1 |  |  <br />CM1\#1 |  <br />CM1 |
|  <br />CM2 |  <br />CM1 |  <br />CM1\#1 |  <br />CM1\|CM2 |
|  <br />CM3 |  <br />CM1 |  <br />CM1\#1 |  <br />CM1\|CM3 |
|  <br />CM4 |  <br />CM2 |  <br />CM1\#1 |  <br />CM1\|CM2\|CM4 |
|  <br />CM5 |  <br />CM2 |  <br />CM1\#1 |  <br />CM1\|CM2\|CM5 |
|  <br />CM6 |  <br />CM3 |  <br />CM1\#1 |  <br />CM1\|CM3\|CM6 |
|  <br />CM7 |  <br />CM3 |  <br />CM1\#1 |  <br />CM1\|CM3\|CM7 |
|  <br />CM8 |  <br />CM4 |  <br />CM1\#1 |  <br />CM1\|CM2\|CM4\|CM8 |
|  <br />CM9 |  <br />CM4 |  <br />CM1\#1 |  <br />CM1\|CM2\|CM4\|CM9 |
|  <br />CM10 |  <br />CM5 |  <br />CM1\#1 |  <br />CM1\|CM2\|CM5\|CM10 |

## The GSI1 index
<a name="gsi1-index"></a>

To check all immediate children of a component, you create an index that uses `ParentId` as a partition key and `ComponentId` as a sort key. The following pivot table represents the GSI1 index. You can use this index to retrieve all immediate child components by using a parent component ID. For example, you can find out how many batteries are available in a car (CM1) or which cells are available in a module (CM4).

|
|
| ParentId | ComponentId |
| --- |--- |
| CM1 | CM2<br />CM3 |
| CM2 | CM4<br />CM5 |
| CM3 | CM6<br />CM7 |
| CM4 | CM8<br />CM9 |
| CM5 | CM10 |

## The GSI2 index
<a name="gsi2-index"></a>

The following pivot table represents the GSI2 index. It's configured using `GraphId` as a partition key and `Path` as a sort key. Using `GraphI`d and the `begins_with` operation on the sort key (`Path`), you can find the full lineage of a component in a tree.

|
|
| GraphId | Path | ComponentId |
| --- |--- |--- |
| CM1\#1 | CM1<br />CM1\|CM2<br />CM1\|CM3<br />CM1\|CM2\|CM4<br />CM1\|CM2\|CM5<br />CM1\|CM2\|CM4\|CM8<br />CM1\|CM2\|CM4\|CM9<br />CM1\|CM2\|CM5\|CM10<br />CM1\|CM3\|CM6<br />CM1\|CM3\|CM7 | CM1<br />CM2<br />CM3<br />CM4<br />CM5<br />CM8<br />CM9<br />CM10<br />CM6<br />CM7 |
