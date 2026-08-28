---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step8-hierarchical-model.html
---

# Step 8: Review the cost estimation
<a name="step8-hierarchical-model"></a>

Review and refine the cost estimation again. Additionally, it's a good practice to validate it with business stakeholders and get approval to move to the next step.

## Objectives
<a name="obj8-hierarchical-model"></a>
+ Define the capacity model, and estimate DynamoDB costs to refine the cost estimation from [step 2](step2-hierarchical-model.md).
+ Get the final financial approval from the business analyst and stakeholders.

## Process
<a name="proc8-hierarchical-model"></a>
+ Database engineer identifies the data volume estimate.
+ Database engineer identifies the data transfer requirements.
+ Database engineer defines the required read and write capacity units.
+ Business analyst decides between [on-demand and provisioned capacity models](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html).
+ Database engineer identifies the need for [DynamoDB auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html).
+ Database engineer inputs the parameters in the AWS Pricing Calculator.
+ Database engineer presents the final price estimation to business stakeholders.
+ Business analyst and stakeholders approve or reject the solution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
