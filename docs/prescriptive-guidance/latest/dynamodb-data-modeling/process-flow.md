---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/process-flow.html
---

# Data-modeling process flow
<a name="process-flow"></a>

We recommend the following process when modeling data using Amazon DynamoDB. The steps are discussed in detail [later in this guide](steps.md).

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/images/guide-img/225c2600-95f1-4c8c-9e23-419bc7ae3c55/images/8b50f5f7-c678-4d07-9ef2-a1feedca427a.png)

## RACI matrix
<a name="raci-matrix"></a>

Some organizations use a responsibility assignment matrix (also known as a *RACI matrix*) to describe the various roles involved in one specific project or business process. This guide presents a suggested RACI matrix that could help your organization identify the right people and right responsibilities for the DynamoDB data modeling process. For each step in the process, it lists the stakeholders and their involvement:
+ **R** – responsible for completing the step
+ **A** – accountable for approving and signing off on the work
+ **C** – consulted to provide input for a task
+ **I** – informed of progress, but not directly involved in the task

Depending on the structure of your organization and project team, the roles in the following RACI matrix can be performed by the same stakeholder. In some situations, stakeholders are both responsible and accountable for specific steps. For example, database engineers can be responsible for both creating and approving the data model, because this is their domain area.

|  |  |  |  |  |  |
| --- |--- |--- |--- |--- |--- |
| Process step | Business user | Business analyst | Solutions architect | Database engineer | Application developer | DevOps engineer |
| --- |--- |--- |--- |--- |--- |--- |
| 1. Identify the use cases and logical data model | C | R/A | I | R |   |   |
| 2. Create a preliminary cost estimation | C | A | I | R |   |   |
| 3. Identify the data access patterns | C | A | I | R |   |   |
| 4. Identify the technical requirements | C | C | A | R |   |   |
| 5. Create the DynamoDB data model | I | I | I | R/A |   |   |
| 6. Create the data queries | I | I | I | R/A | R |   |
| 7. Validate the data model | A | R | I | C |   |   |
| 8. Review the cost estimation | C | A | I | R |   |   |
| 9. Deploy the DynamoDB data model | I | I | C | C |   | R/A |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
