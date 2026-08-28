---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step3-hierarchical-model.html
---

# Step 3: Identify your data-access patterns
<a name="step3-hierarchical-model"></a>

This example use case has the following access patterns for managing relationships between different car components.

|
|
| Access pattern | Priority | Read or write | Description | Type | Filters | Result ordering |
| --- |--- |--- |--- |--- |--- |--- |
| Immediate child | High | Read | Retrieve all the immediate child components for a parent component ID. | Multiple | `ComponentID` | N/A |
| All child components | High | Read | Retrieve a recursive list of all child components for a component ID. | Multiple | `ComponentID` | N/A |
| Ancestors | High | Read | Retrieve the ancestors of a component. | Multiple | `ComponentID` | N/A |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
