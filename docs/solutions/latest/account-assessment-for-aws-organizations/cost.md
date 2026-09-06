---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/cost.html
---

# Cost
<a name="cost"></a>

**Note**
You are responsible for the cost of the AWS services used while running this solution. As of this revision, the cost for running this solution with the default settings in the US East (N. Virginia) Region is approximately **$45 per month**, based on the assumptions in [Sample cost table](#sample-cost-table).
Refer to the pricing webpage for each AWS service used in this solution.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help you manage costs. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this solution.

## Sample cost table
<a name="sample-cost-table"></a>

The following table provides a sample cost breakdown for deploying this solution with the default parameters in the US East (N. Virginia) Region for one month.

The cost is based on the following assumptions:
+ You are assessing 100 AWS accounts in 10 AWS Regions
+ You are running each assessment type 30 times a month
+ In each account you have a total of 1,000 policies
+ You conduct on average 100 searches per month with the Policy Explorer
+ You are creating 1 Cognito user

| AWS service | Dimensions | Variable or fixed | Cost [USD] |
| --- | --- | --- | --- |
| Amazon API Gateway | 3,000 REST API calls per month | variable | <$0.01 |
| Amazon Cognito | 1 active user per month without the advanced security feature | variable | <$0.01 |
| Amazon CloudFront | 1,000 requests | variable | <$1.00 |
| Amazon S3 | <1 GB storage | variable | <$1.00 |
| AWS Lambda | 90,000 requests with 1,000 ms average duration | variable | <$1.00 |
| AWS Step Functions | 189,000 state transitions | variable | $4.73 |
| Amazon DynamoDB | 20 million read capacity units, 15 million write capacity units, 0.5 GB storage | variable | $23.88 |
| AWS WAF | 1 web ACL, 1 custom rule, 7 managed rule groups | fixed | $13.00 |
| AWS X-Ray | \~150 traces recorded (3,000 API calls with default 5% sampling rate) | variable | <$0.01 |
|  |  |  **Total monthly cost:**  |  **$44.64**  |
