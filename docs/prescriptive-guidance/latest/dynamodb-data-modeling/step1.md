---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step1.html
---

# Step 1. Identify the use cases and logical data model
<a name="step1"></a>

## Objectives
<a name="obj1"></a>
+ Gather the business needs and use cases that require a NoSQL database.
+ Define the logical data model by using an entity-relationship (ER) diagram.

## Process
<a name="proc1"></a>
+ Business analysts interview business users to identify the use cases and the expected outcomes.
+ Database engineer creates the conceptual data model.
+ Database engineer creates the logical data model.
+ Database engineer gathers information about item size, data volume, and expected read and write throughput.

## Tools and resources
<a name="tools1"></a>
+ Business requirements assessment (see [template](template-business-req.md))
+ Access patterns matrix (see [template](template-access-patterns.md))
+ Your preferred tool for creating diagrams

## RACI
<a name="raci1"></a>

|
|
| Business user | Business analyst | Solutions architect | Database Engineer | Application Developer | DevOps Engineer |
| --- |--- |--- |--- |--- |--- |
| C | R/A | I | R |   |   |

## Outputs
<a name="outputs1"></a>
+ Documented use cases and business requirements
+ Logical data model (ER diagram)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
