---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running this Guidance. As of this revision, the cost for running it with the default settings in the US East (N. Virginia) Region is approximately **$85.22 a month**. These costs are for the resources shown in the [Sample cost table](#sample-cost-table).

See the pricing webpage for each AWS service used in this Guidance.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each AWS service used.

## Sample cost table
<a name="sample-cost-table"></a>

The following table provides a sample cost breakdown for deploying with the default parameters in the US East (N. Virginia) Region for one month. This cost estimate assumes the following:
+ Two VPCs are managed, each attached to one transit gateway and containing two subnets in different Availability Zones.
+ Automated queries to DynamoDB from an actively running web UI run every five minutes. This estimate does not include manual queries.
+ One GB of data a month travels between the two VPCs through the transit gateway.
+ The number of requests to the GraphQL API is 10,000 a month.

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
|  **Variable Costs**  |  |  |
| Transit Gateway | Hourly charge (containing two VPC attachments) | $72.00 |
| Transit Gateway | Data processing charge (data transfer of 1 GB from two attached VPCs) | $0.60 |
| Transit Gateway | Data processing and outbound inter-Region transfer charge (data transfer of 1 GB between two inter-Region peered transit gateways) | $0.40 |
| Amazon DynamoDB | Includes automated queries only | $3.27 |
| AWS AppSync | Includes auto approval workflow only | $1.23 |
|  **Fixed Costs**  |  |  |
| Amazon EventBridge |  | < $ 0.01 |
| AWS WAF |  | $ 7.61 |
| AWS Step Functions | State transitions: 100-120 transitions per month (5-6 workflow executions × 20 transitions each). State machine has 20 Task states that invoke Lambda | < $ 0.01 |
| AWS Lambda | Duration: 700-850 GB-seconds per month (StateMachineLambdaFunction: 100-120 invocations at 4 sec with 1.5 GB, CustomResourceLambda: 2-4 invocations at 10 sec with 1.5 GB, MetricsCollectorLambda: 30 invocations at 5 sec with 0.5 GB) | < $ 0.01 |
| AWS X-Ray | 100,000 Traces recorded for 2 services (Step Functions and AppSync) with default 5% sampling rate | < $ 0.10 |
|  |  **Total:**  | \~ $85.22 / month |

**Note**
AWS Step Functions state transitions and AWS Lambda duration charges are included in this estimate. With the assumed usage pattern (5-6 workflow executions per month for 2 VPCs with minimal tag changes), both services operate within AWS Free Tier limits (4,000 state transitions/month and 400,000 GB-seconds/month), resulting in negligible charges. For environments with more frequent network changes, costs may increase proportionally but remain minimal.
