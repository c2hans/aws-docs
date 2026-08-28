---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/cost.html
---

# Cost
<a name="cost"></a>

The following tables provide a sample cost breakdown for deploying this solution with the default parameters in the US East (N. Virginia) Region for one month. There are additional minimal costs for a hub stack and a spoke stack.

**Note**
The monthly cost was estimated for a quota size of 2,000, as of this revision. If more quotas are supported by Service Quotas for additional resource types, the quota size would increase and monthly estimated cost could be higher. The costs provided are estimates based on a 6-hour monitoring frequency.
The scalable costs (Amazon SQS and DynamoDB) increase with the number of accounts and Regions.

 **Monthly cost by number of accounts**

| Deployment size | Number of accounts | Number of AWS Regions | Cost per month [USD] |
| --- | --- | --- | --- |
|  **Small**  | 10 | 8 | $11.01 \+ 0.00355\*10\*8 \+ 0.01\*10 \+ $5.24\*10\*8 = **$430.39**  |
|  **Medium**  | 100 | 10 | $11.01 \+ 0.00355\*100\*10 \+ $0.01\*100 \+ 5.24\*100\*10 = **$5,253.55**  |
|  **Large**  | 1000 | 15 | $11.01 \+ 0.00355\*1000\*15 \+ 0.01\*1000 \+ 5.24\*1000\*15 = **$78,641.25**  |

**Note**
We calculated cost per month with the following formula: [monthly fixed cost for a hub stack] \+ [monthly scalable cost for a hub stack] \* [number of accounts] \* [number of regions] \+ [monthly cost for a Trusted Advisor spoke stack] \* [number of accounts] \+ [monthly cost for a Service Quotas spoke stack] \* [number of accounts] \* [number of regions]

 **Monthly Fixed cost for a hub stack**

| AWS service | Cost per month [USD] |
| --- | --- |
|  **Amazon SNS topic**  | <$0.01 |
| \* AWS Lambda\* | $10.00 |
| \* AWS KMS\* | $1.00 |
|  **Total cost:**  |  **$11.01**  |

 **Monthly Scalable cost for a hub stack**

| AWS service | Cost per month [USD] |
| --- | --- |
|  **Amazon SQS queue**  | $0.00178 |
|  **Amazon DynamoDB**  | $0.00177 |
|  **Total cost:**  |  **$0.00355**  |

 **Monthly cost for a Trusted Advisor spoke stack**

| AWS service | Cost per month [USD] |
| --- | --- |
|  **Amazon EventBridge**  | Free 1  |
|  **AWS Lambda**  | \~ $0.01 2  |
|  **Total cost:**  |  **$ 0.01**  |

 1 AWS default service events are free. For more information, refer to [Amazon EventBridge Pricing](https://aws.amazon.com/eventbridge/pricing/).

 2 The stack uses Support APIs which are not available under the free developer plan. For more information, refer to [Compare Support Plans](https://aws.amazon.com/premiumsupport/plans).

 **Monthly cost for a Service Quotas spoke stack**

| AWS service | Cost per month [USD] |
| --- | --- |
|  **Amazon EventBridge**  | $0.01 |
|  **Amazon CloudWatch (`GetMetricData` API)**  | $5.12 |
|  **AWS Lambda**  | \~ $0.02 |
|  **Amazon DynamoDB**  | \~ $0.09 |
|  **Total cost:**  |  **$5.24**  |

Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this solution.

**Note**
When you delete a stack, the DynamoDB table on the hub account is not deleted. DynamoDB will continue to incur costs until the you delete the table.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quota Monitor for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
