---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step2.html
---

# Step 2. Create a preliminary cost estimation
<a name="step2"></a>

## Objective
<a name="obj2"></a>
+ Develop a preliminary cost estimation for DynamoDB.

## Process
<a name="proc2"></a>
+ Database engineer creates the initial cost analysis using available information and the examples presented on the [DynamoDB pricing page](https://aws.amazon.com/dynamodb/pricing/).
  + Create a cost estimate for on-demand capacity (see [example](https://aws.amazon.com/dynamodb/pricing/on-demand/)).
  + Create a cost estimate for provisioned capacity (see [example](https://aws.amazon.com/dynamodb/pricing/provisioned/)).
    + For the provisioned capacity model, get the estimate cost from the calculator and apply discount for reserved capacity.
  + Compare the estimated costs of the two capacity models.
  + Create an estimation for all the environments (Dev, Prod, QA).
+ Business analyst reviews and approves or rejects the preliminary cost estimate.

## Tools and resources
<a name="tools2"></a>
+ [AWS Pricing Calculator](https://calculator.aws/#/)

## RACI
<a name="raci2"></a>

|
|
| Business user | Business analyst | Solutions architect | Database engineer | Application developer | DevOps engineer |
| --- |--- |--- |--- |--- |--- |
| C | A | I | R |   |   |

## Outputs
<a name="outputs2"></a>
+ Preliminary cost estimation

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
