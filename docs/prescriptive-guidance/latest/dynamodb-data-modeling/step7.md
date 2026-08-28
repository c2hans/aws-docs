---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step7.html
---

# Step 7. Validate the data model
<a name="step7"></a>

## Objective
<a name="obj7"></a>
+ Ensure that the data model will satisfy your requirements.

## Process
<a name="proc7"></a>
+ Database engineer populates the DynamoDB table with sample data.
+ Database engineer runs the code to query the DynamoDB table.
+ Database engineer collects the query results.
+ Database engineer collects the query performance metrics.
+ Business user validates that query results satisfy business needs.
+ Business analysts validate the technical requirements.

## Tools and resources
<a name="tools7"></a>
+ An active AWS account, to gain access to the DynamoDB console
+ [DynamoDB Local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) (optional), if you want to build the database on your computer without accessing the DynamoDB web service
+ [AWS SDK](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.html) in your choice of language

## RACI
<a name="raci7"></a>

|
|
| Business user | Business analyst | Solutions architect | Database engineer | Application developer | DevOps engineer |
| --- |--- |--- |--- |--- |--- |
| A | R | I | C |   |   |

## Outputs
<a name="outputs7"></a>
+ Approved data model

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
