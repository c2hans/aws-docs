---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step2-hierarchical-model.html
---

# Step 2: Create a preliminary cost estimation
<a name="step2-hierarchical-model"></a>

It's important to calculate an estimation of the cost for all environments of your application so you can check if the solution is financially viable. A best practice is to make a high-level estimation and get approval from the business analyst before proceeding with the development and deployment.
+ Database engineer creates the initial cost analysis using available information and the examples presented on the [DynamoDB pricing page](https://aws.amazon.com/dynamodb/pricing/).
  + Create a cost estimate for on-demand capacity (see [example](https://aws.amazon.com/dynamodb/pricing/on-demand/)).
  + Create a cost estimate for provisioned capacity (see [example](https://aws.amazon.com/dynamodb/pricing/provisioned/)).
    + For the provisioned capacity model, get the estimated cost from the calculator, and apply the discount for reserved capacity.
  + Compare the estimated costs of the two capacity models.
  + Create an estimation for all the environments (Dev, Prod, QA).
+ Business analyst reviews and approves or rejects the preliminary cost estimate.

Using these reference values, you can create an estimated price to submit for approval. To create the budget, you can use the [DynamoDB pricing page](https://aws.amazon.com/dynamodb/pricing/) and [AWS Pricing Calculator](https://calculator.aws/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
