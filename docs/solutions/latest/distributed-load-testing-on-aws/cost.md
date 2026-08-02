---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running this solution. The total cost depends on the number of load tests run, the duration of those tests, and the amount of data generated. As of this revision, the estimated cost for running this solution with default settings in the US East (N. Virginia) Region is approximately $30.90 per month.

The following table provides a sample cost breakdown for deploying this solution with the default parameters in the US East (N. Virginia) Region for one month.

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
| AWS Fargate | 10 on-demand tasks (using two vCPUs and 4 GB memory) running for 30 hours | $29.62 |
| Amazon DynamoDB | 1,000 on-demand write capacity units<br />1,000 on-demand read capacity units | $0.0015 |
| AWS Lambda | 1,000 requests<br />10 minutes total duration | $1.25 |
| AWS Step Functions | 1,000 state transitions | $0.025 |
|  **Total:**  |  |  **$30.90 per month**  |

The solution resources are tagged with the Key=SolutionId and Value=SO0062. You can activate the tag key SolutionId by following the documentation [activating-tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html). Once the tag is activated, you can create a cost category rule by following the documentation to [create cost categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/create-cost-categories.html). You can view the cost incurred for the solution by monitoring the cost categories console and selecting the cost category name.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each [AWS service used in this solution](architecture-details.md#aws-services-in-this-solution).

**Note**
The default task configuration uses 2 vCPUs and 4 GB of memory per task. If your load tests do not require these resources, you can reduce them to lower costs. Conversely, you can increase resources to support higher concurrency per task. For more information, refer to the [Increase the container resources](increase-container-resources.md) section in this guide.

**Note**
This solution provides the option to include live data when running a test. This feature requires an additional AWS Lambda function and AWS IoT Core topic that incur extra costs.

## AWS DevOps Agent integration costs
<a name="devops-agent-cost"></a>

This solution deploys infrastructure to support integration with AWS DevOps Agent, including two Amazon DynamoDB tables for agent space registrations and investigation tracking. These tables use on-demand capacity mode, so you are charged per read and write request based on your usage. For more information about pricing, see [Amazon DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/).

When you use the DevOps Agent integration to run investigations on your test results, the AWS DevOps Agent service is billed separately per agent-second. This cost is not included in the estimate above. For full pricing details, see [AWS DevOps Agent Pricing](https://aws.amazon.com/devops-agent/pricing/).

## MCP Server additional costs (Optional)
<a name="mcp-server-cost"></a>

The following table provides a cost breakdown for the MCP Server integration with pricing in the US East (N. Virginia) Region for one month.

| Service component | Dimensions | Cost [USD] |
| --- | --- | --- |
| AgentCore Gateway - Tool Indexing | 10 tools × $0.02 per 100 tools | $0.002 |
| AgentCore Gateway - Search API | 10,000 interactions × $0.025 per 1,000 | $0.25 |
| AgentCore Gateway - API Invocations | 50,000 invocations × $0.005 per 1,000 | $0.25 |
| AWS Lambda Function | Variable based on usage (typical workloads) | $5.00 - $20.00 |
|  **Total estimated additional cost:**  |  |  **$5.50 - $20.50 per month**  |

Prices are subject to change. For full details on AgentCore Gateway pricing, refer to [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/) (AgentCore Gateway section). For Lambda pricing, refer to [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/).

## ALB \+ ECS Fargate hosted web console additional costs (Optional)
<a name="alb-ecs-cost"></a>

If you choose the ALB \+ ECS Fargate deployment option, the following additional costs apply. Pricing is for the US East (N. Virginia) Region.

| Service component | Dimensions | Cost [USD] |
| --- | --- | --- |
| Elastic Load Balancing | 1 Application Load Balancer | $19.35 |
| AWS Fargate | 2 tasks (0.25 vCPU, 0.5 GB memory) running 24/7 | $17.77 |
| Amazon Virtual Private Cloud (VPC) | 3 interface endpoints, 2 Availability Zones | $43.21 |
| Amazon CloudWatch | 10 metrics, 1,000 GetMetricData requests, 1,000 API requests, 5 GB log ingestion, 1 dashboard, 10 alarms | $6.54 |
| Amazon S3 | 0.1 GB S3 Standard storage, 100 PUT/COPY/POST/LIST requests, 10,000 GET/SELECT requests | $0.01 |
| AWS WAF | 1 web ACL, 3 managed rule groups (CRS, AmazonIpReputationList, AnonymousIpList), 10,000 requests (request cost negligible) | $8.00 |
|  **Total estimated additional cost:**  |  |  **$94.88 per month**  |

Prices are subject to change. For full details, refer to [Elastic Load Balancing pricing](https://aws.amazon.com/elasticloadbalancing/pricing/), [AWS Fargate pricing](https://aws.amazon.com/fargate/pricing/), and [AWS WAF pricing](https://aws.amazon.com/waf/pricing/).
