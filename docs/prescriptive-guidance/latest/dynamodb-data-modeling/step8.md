---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step8.html
---

# Step 8. Review the cost estimation
<a name="step8"></a>

## Objectives
<a name="obj8"></a>
+ Define the capacity model and estimate DynamoDB costs to refine the cost estimation from [step 2](step2.md).
+ Get the final financial approval from the business analyst and stakeholders.

## Process
<a name="proc8"></a>
+ Database engineer identifies the data volume estimate.
+ Database engineer identifies the data transfer requirements.
+ Database engineer defines the required read and write capacity units.
+ Business analyst decides between [on-demand and provisioned capacity models](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html).
+ Database engineer identifies the need for [DynamoDB auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html).
+ Database engineer inputs the parameters in the AWS Pricing Calculator.
+ Database engineer presents the final price estimation to business stakeholders.
+ Business analyst and stakeholders approve or reject the solution.

## Tools and resources
<a name="tools8"></a>
+ [AWS Pricing Calculator](https://calculator.aws/#/)

## RACI
<a name="raci8"></a>

|
|
| Business user | Business analyst | Solutions architect | Database engineer | Application developer | DevOps engineer |
| --- |--- |--- |--- |--- |--- |
| C | A | I | R |   |   |

## Outputs
<a name="outputs8"></a>
+ Capacity model
+ Revised cost estimation
