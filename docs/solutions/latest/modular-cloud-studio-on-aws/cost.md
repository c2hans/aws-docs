---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running this solution. As of this revision, the cost for running this solution with the default settings in the US East (N. Virginia) Region is approximately **$591.55 per month** when deploying the main stack, Managed VPC module, Managed Active Directory module, and FSx for Windows File Server module in the hub Region. These costs are for the resources shown in the [Sample cost table](#sample-cost-table).

**Note**
Third-Party modules' costs are not included in the monthly cost estimate, including Leostream workstation management modules and storage partner modules.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this solution.

## Sample cost table
<a name="sample-cost-table"></a>

Total cost varies depending on how many modules and Regions you deploy. The following tables give a sample cost breakdown for deploying this solution and internal hub modules with the default parameters in the US East (N. Virginia) Region for one month.

 **MCS stack deployment**

|  **AWS service**  |  **Dimensions**  |  **Cost [USD]**  |
| --- | --- | --- |
|  **Amazon API Gateway**  | First 333 million REST API calls per month | $ 3.50 |
|  **Amazon Cognito**  | 1,000 active users per month without the advanced security feature | $ 0.00 |
|  **Amazon CloudFront**  | 1,000,000 HTTPS requests | $ 1.00 |
|  **Amazon S3**  | <1 GB storage for web assets and logging | $ 0.023 |
|  **AWS Lambda**  | Modules = 5<br />Requests = <1,000,000 = $ 0.20<br />Enable module = 3,000 ms duration x \+ $ 0.0000000021 per ms<br /> *$ 0.20 \+ (3,000 x $ 0.0000000021) x 5 = $0.2000315*  | $ 0.20 |
|  **Systems Manager Parameter Store**  | Standard parameters and throughput | $0.00 |
|  **Amazon DynamoDB**  | <1 GB storage, <1M write request units (WRUs) and read request units (RRUs) | $ 1.75 |
|  **AWS Service Catalog**  | <1,000 API calls | $ 0.70 |
|  **Amazon EventBridge Event Bus**  | AWS default service events | $ 0.00 |
|  **Amazon EventBridge Pipe**  | <1M requests after filtering per month | $ 0.40 |
|  **Amazon EventBridge API Destination**  | <1M requests per month | $ 0.20 |
|  **Amazon Simple Queue Service**  | Standard queue with <1M requests per month | $ 0.00 |
|  **AWS Step Functions**  | <4,000 state transitions AWS Free Tier | $ 0.00 |
|  **Amazon CloudWatch**  | AWS Free Tier | $ 0.00 |
|  |  **Total:**  |  **$ 7.77 [USD] / month**  |

 **Managed VPC module**

|  **AWS service**  |  **Dimensions**  |  **Cost [USD]**  |
| --- | --- | --- |
|  **Amazon VPC**  | Public IPv4 address<br />NAT Gateway cost is highly variable depending on modules deployed | $ 3.65 |
|  **Systems Manager Parameter Store**  | Standard parameters and throughput | $ 0.00 |
|  **Amazon CloudWatch**  | AWS Free Tier | $ 0.00 |
|  |  **Total:**  |  **$ 3.65 [USD] / month**  |

 **Managed Active Directory module**

|  **AWS service**  |  **Dimensions**  |  **Cost [USD]**  |
| --- | --- | --- |
|  **AWS Directory Service**  | $0.12 per hour | $ 87.60 |
|  **Systems Manager Parameter Store**  | Standard parameters and throughput | $ 0.00 |
|  **AWS Secrets Manager**  | 1 secret | $ 0.45 |
|  **Amazon CloudWatch**  | AWS Free Tier | $ 0.00 |
|  **EC2**  | t3.micro (5 minute deployment) | <$ 0.01 |
|  |  **Total:**  |  **$ 88.05 [USD] / month**  |

 **FSx for Windows File Server module**

|  **AWS service**  |  **Dimensions**  |  **Cost [USD]**  |
| --- | --- | --- |
|  **Amazon FSx for Windows File Server**  | 256 GiB SSD storage capacity, 64 MBps throughput | $ 288.28 |
|  **Systems Manager Parameter Store**  | Standard parameters and throughput | $ 0.00 |
|  **Amazon CloudWatch**  | AWS Free Tier | $ 0.00 |
|  |  **Total:**  |  **$ 288.28 [USD] / month**  |

 **FSx for Lustre File Server module**

|  **AWS service**  |  **Dimensions**  |  **Cost [USD]**  |
| --- | --- | --- |
|  **Amazon FSx for Lustre File Server**  | 1,200 GiB SSD storage capacity, LZ4 Compression Disabled | $ 168.19 |
|  **Systems Manager Parameter Store**  | Standard parameters and throughput | $ 0.00 |
|  **Amazon CloudWatch**  | AWS Free Tier | $ 0.00 |
|  |  **Total:**  |  **$ 168.19 [USD] / month**  |

## Third-Party modules cost
<a name="third-party-modules-cost"></a>

This solution includes Third-Party Leostream workstation management modules available for deployment, and storage partner modules available for registration and deployment.

**Note**
Refer to the [Leostream documentation](https://support.leostream.com/support/solutions/articles/66000513448-leostream-platform-quick-starts-and-guides) or contact Leostream for more detailed and up-to-date Leostream module costs.
Refer to individual Third-Party module support page or contact partners for their respective costs.

Here is a **simplified cost table** for core AWS services in the hub region for Leostream modules using default settings. Actual costs may vary depending on your configuration and chosen modules:

 **Leostream Broker module**

|  **AWS service**  |  **Dimensions**  |  **Cost [USD]**  |
| --- | --- | --- |
|  **Amazon RDS**  | db.r6g.large (Aurora Postgresql) | $ 229.95 |
|  **Application Load Balancer**  |  | $ 16.51 |
|  **EC2**  | t3.large (min 2 by default):<br />($0.112 / hour) \* 24 hour \* 31 days \* 2 = $166.66 | $ 166.66 |
|  **EC2**  | g4dn.xlarge with Windows OS<br />($0.71 / hour) \* 24 hour \* 31 days = $528.24 | $ 528.24 |
|  **EC2**  | g4dn.xlarge with Linux OS<br />($0.584 / hour) \* 24 hour \* 31 days = $434.50 | $ 434.50 |
|  **Route 53**  | Hosted Zone (per-request cost assumed to be negligible) | $ 0.50 |
|  |  **Total:**  |  **$ 1376.36 [USD] / month**  |

 **Leostream Gateway module**

|  **AWS service**  |  **Dimensions**  |  **Cost [USD]**  |
| --- | --- | --- |
|  **Application Load Balancer**  |  | $ 16.51 |
|  **EC2**  | m5.xlarge (min 2 by default) with RHEL OS<br />($0.269 / hour) \* 24 hour \* 31 days \*2 = $400.27 | $ 400.27 |
|  **AWS Global Accelerator**  | Standard | $ 18 |
|  **AWS Global Accelerator Data Transfer**  | Varies depending on regions used | \~ $ 0.015 per GB |
|  **EC2 Egress**  | First 100 GB per month is free | \~ $ 0.09 per GB |
|  **EC2 Elastic IP Address**  | 2 used by Global Accelerator | $ 7.32 |
|  |  **Total (excluding data transfer costs):**  |  **$ 442.10 [USD] / month**  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
