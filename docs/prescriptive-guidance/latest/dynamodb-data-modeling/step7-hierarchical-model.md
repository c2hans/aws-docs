---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step7-hierarchical-model.html
---

# Step 7: Validate the data model
<a name="step7-hierarchical-model"></a>

In this step, the business user validates the query results and checks whether they satisfy business needs. You can use the following table to check the access patterns against the requirements of the user.

|
|
| Question | Base table / GSI | Query |
| --- |--- |--- |
| As a user, I want to retrieve all the immediate child components for a parent component ID. | GSI1 | `ParentId = "<ComponentId>"`<br />(Find immediate children of a component.) |
| As a user, I want to retrieve a recursive list of all child components for a component ID. | GSI1 or GSI2 | GSI1: `ParentId = "<ComponentId>"`<br />or<br />GSI2: `GraphId = "<TopLevelComponentId>#N" AND BEGINS_WITH("Path", "<PATH_OF_Component>")`<br />(Find all down-level child components using a top- level component. Find all down-level child components using a middle-level component.) |
| As a user, I want to see the ancestors of a component. | Base table | `ComponentId = "<ComponentId>"`, then select the Path attribute.<br />(Find ancestors of a component.) |

You can also implement a script (test) in any programming language to query DynamoDB directly and compare the results with the expected results.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
