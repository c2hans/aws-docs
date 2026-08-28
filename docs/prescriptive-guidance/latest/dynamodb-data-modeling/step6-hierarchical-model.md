---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step6-hierarchical-model.html
---

# Step 6: Create data queries
<a name="step6-hierarchical-model"></a>

After you define your access patterns and design your data model, you can query hierarchical data in the DynamoDB database. As a best practice to save on costs and help ensure performance, the following examples use only the query operation without `Scan`.
+ **Find ancestors of a component.**

  To find the ancestors (parent, grandparent, great-grandparent, and so on) of the CM8 component, query the base table using `ComponentId = "CM8"`. The query will return the following record.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step6-hierarchical-model.html)

  To reduce the size of the result data, you can use a projection expression to return only the `Path` attribute.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step6-hierarchical-model.html)
+ **Find immediate children of a component.**

  To get all immediate child, or one-level downstream, components for the CM2 component, query GSI1 using `ParentId = "CM2"`. The query will return the following record.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step6-hierarchical-model.html)
+ **Find all downstream child components using a top-level component.**

  To get all child, or downstream, components for top-level component CM1, query GSI2 using `GraphId = "CM1#1"` and `begins_with("Path", "CM1|")`, and use a projection expression with `ComponentId`. It will return all the components related to that tree.

  This example has a single tree, with CM1 as the top component. In reality, you could have millions of top-level components in the same table.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step6-hierarchical-model.html)
+ **Find all downstream child components using a middle-level component.**

  To get all child, or downstream, components recursively for component CM2, you have two options. You can query recursively level by level, or you can query the GSI2 index.
  + Query GSI1, level by level, recursively, until reaching the last level of child components.

    1. Query GSI1 using `ParentId = "CM2"`. It will return the following record.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step6-hierarchical-model.html)

    1. Again, query GSI1 using `ParentId = "CM4"`. It will return the following record.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step6-hierarchical-model.html)

    1. Again, query GSI1 using `ParentId = "CM5"`. It will return the following record.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step6-hierarchical-model.html)

       Continue the loop: Query for each `ComponentId` until you reach the last level. When a query using `ParentId = "<ComponentId>"` doesn't return any results, the previous result was from the last level of the tree.

    1. Merge all results.

       result=[CM4, CM5] \+ [CM8, CM9] \+ [CM10]

                =[CM4, CM5, CM8, CM9, CM10]
  + Query GSI2, which stores a hierarchical tree for a top-level component (a car, or CM1).

    1. First, find the top-level component or top ancestor and `Path` of CM2. For that, query the base table by using `ComponentId = "CM2"` to find the path of that component in the hierarchical tree. Select the `GraphId` and `Pat`h attributes. The query will return the following record.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step6-hierarchical-model.html)

    1. Query GSI2 by using `GraphId = "CM1#1" AND BEGINS_WITH("Path", "CM1|CM2|")`. The query will return the following results.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step6-hierarchical-model.html)

    1. Select the `ComponentId` attribute to return all the child components for CM2.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
