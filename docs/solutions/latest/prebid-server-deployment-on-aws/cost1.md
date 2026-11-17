---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/cost1.html
---

# Cost
<a name="cost1"></a>

You are responsible for the cost of the AWS services used while running this solution. As of November 2026, the cost for running this solution with the default settings with no incoming bidding traffic to the solution in the US East (N. Virginia) Region is approximately **USD $291.09 per month**.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through AWS Cost Explorer to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each AWS service used in this solution.

**Note**
If you want to opt out of using CloudFront and AWS WAF and directly send requests to the ALB, see [Opting out of using CloudFront and AWS WAF](configure-the-solution.md#opt-out-of-cloudfront-and-waf).

## Cost tables
<a name="sample-cost-table"></a>

The total cost of this solution includes two parts:
+ Cost for deploying the solution without incoming bidding traffic
+ Cost incurred from the traffic flowing through the solution

The following assumptions apply for calculating the cost:
+ The cost breakdown per month includes deploying this solution with the default parameters in the US East (N. Virginia) Region.
+ The Fargate to Fargate Spot pricing ratio is 1:1. With Fargate Spot instances, customers can run interrupt-tolerant Amazon ECS tasks on spare capacity at up to a 70% discount off of the regular Fargate instance price. For more information, see [AWS Fargate Pricing](https://aws.amazon.com/fargate/pricing/).
+ Each ad request to the solution is 0.5 KB, and the response to the browser is 1 KB. Each ad request goes to three bidders over the public internet through the NAT gateways. Bid requests are 10 KB uncompressed (10,000 bytes), and bid responses average 1 KB (half are bids of about 2 KB, half are no-bids).
+ Data volumes are in binary units (1 GiB = 230 bytes, 1 TB = 1,024 GiB), and prices quoted per GB apply to GiB.

### Sample cost table 1
<a name="sample-cost-table-1"></a>

 **No incoming bidding traffic to the solution, two Amazon ECS tasks**

The following table provides a sample cost breakdown for deploying this solution with the default parameters in the US East (N. Virginia) Region for one month with no incoming bidding traffic.

| AWS service | Dimensions | Monthly cost [USD] |
| --- | --- | --- |
| AWS Fargate (Amazon ECS) | 2 tasks (minimum capacity), each 2 vCPU and 4 GB memory, Linux/x86, 730 hours, 20 GB ephemeral storage (included at no charge); priced at On-Demand rates ($0.04048 per vCPU-hour, $0.004445 per GB-hour) | $144.16 |
| Elastic Load Balancing | 2 Application Load Balancers (internet-facing and internal) at $0.0225 per hour; LCU charges are negligible with no traffic | $32.85 |
| NAT gateway | 2 NAT gateways at $0.045 per hour; data processing ($0.045 per GB) is negligible with no traffic | $65.70 |
| Public IPv4 addresses | 4 in-use public IPv4 addresses (2 NAT gateway Elastic IP addresses, 2 for the internet-facing load balancer) at $0.005 per hour | $14.60 |
| AWS WAF | 1 web ACL ($5.00) and 7 rules (6 AWS managed rule groups and 1 custom rule) at $1.00 each; request charges ($0.60 per million) are negligible with no traffic | $12.00 |
| Amazon CloudFront | 1 distribution in front of the internet-facing Application Load Balancer. CloudFront has no fixed monthly charge; it bills per request and per GB of data transfer out, and the always-free tier covers the first 1 TB of data transfer out and 10 million HTTPS requests each month | $0.00 |
| Amazon ElastiCache Serverless (Valkey) | Minimum billed data storage of 100 MB at $0.084 per GB-hour; ECPU charges are negligible with no traffic | $6.13 |
| AWS KMS | 6 customer managed keys at $1.00 each | $6.00 |
| Amazon CloudWatch | 19 standard-resolution alarms at $0.10 each, about 5 GB of log ingestion at $0.50 per GB | $4.40 |
| Amazon EFS | About 10 GB of Standard storage at $0.30 per GB-month (files move to Infrequent Access after 7 days, which lowers this) | $3.00 |
| Amazon S3 | About 11 GB of S3 Standard storage at $0.023 per GB-month | $0.25 |
| Other services | AWS CloudTrail, AWS DataSync, AWS Lambda, Amazon VPC gateway endpoint, and IAM, which are within free tiers or negligible with no traffic | $2.00 |
|  |  **Total:**  |  **$291.09**  |

Prices were taken from the AWS Price List API for US East (N. Virginia) in November 2026. The amounts in this table are On-Demand. With the default `SpotInstanceWeight` of 1, about half of the Fargate tasks run on Fargate Spot, which lowers the Fargate line. AWS Glue (the metrics ETL job) is billed at $0.44 per DPU-hour, with a 1-minute minimum, for each run. The job runs only after a DataSync transfer delivers new log files, so its cost depends on how often Prebid Server writes metrics and analytics logs.

### AWS RTB Fabric cost comparison (optional)
<a name="rtb-fabric-cost"></a>

AWS RTB Fabric is used when the solution is deployed with `--deploy-bidding-simulator` on the default `rtb-fabric` connectivity, or with `--enable-rtb-requester-gateway`. RTB Fabric has no hourly or gateway charge, so with no traffic it adds $0.00 to the cost in sample cost table 1.

The following tables compare sending bid requests through the NAT gateways and through an RTB Fabric Requester Gateway, for 1 billion ad requests per month arriving through CloudFront and the Application Load Balancer. Each ad request goes to 3 bidders, so Prebid Server sends 3 billion bid requests per month. Not applicable means the item does not apply to that option.

 **Bidders on AWS in the same Region (internal RTB Fabric links)**

| Line item | Current path (NAT gateway) [USD] | AWS RTB Fabric path [USD] |
| --- | --- | --- |
| Amazon CloudFront requests (1 billion HTTPS at $0.0100 per 10,000) | $1,000.00 | $1,000.00 |
| Amazon CloudFront data transfer out to viewers (931 GiB at $0.085 per GB) | $79.16 | $79.16 |
| Amazon CloudFront data transfer to origin (466 GiB at $0.020 per GB) | $9.31 | $9.31 |
| AWS WAF web ACL and 7 rules | $12.00 | $12.00 |
| AWS WAF requests (1 billion at $0.60 per million) | $600.00 | $600.00 |
| Application Load Balancer hourly (2 Application Load Balancers, internet-facing and internal, at $0.0225 per hour) | $32.85 | $32.85 |
| Application Load Balancer capacity units (about 1,397 LCU-hours at $0.008 per LCU-hour) | $11.18 | $11.18 |
| NAT gateway hourly (2 NAT gateways) | $65.70 | $65.70 |
| Public IPv4 addresses (4 in-use addresses at $0.005 per hour) | $14.60 | $14.60 |
| NAT gateway data processing, bid requests (27,940 GiB at $0.045 per GB) | $1,257.29 | Not applicable |
| NAT gateway data processing, bid responses (2,794 GiB at $0.045 per GB) | $125.73 | Not applicable |
| Data transfer to bidders over public IP addresses in the same Region ($0.01 per GB each direction) | $307.34 | Not applicable |
| RTB Fabric bid request transactions (3 billion at $4.50 per billion) | Not applicable | $13.50 |
| RTB Fabric payload above the 2 KiB included per transaction (22,218 GiB at $0.0015 per GiB) | Not applicable | $33.33 |
|  **Total**  |  **$3,515.16**  |  **$1,871.63**  |
|  **Monthly difference**  |  |  **$1,643.53 lower (47%)**  |

 **Bidders outside AWS (external RTB Fabric links)**

| Line item | Current path (NAT gateway) [USD] | AWS RTB Fabric path [USD] |
| --- | --- | --- |
| Amazon CloudFront requests | $1,000.00 | $1,000.00 |
| Amazon CloudFront data transfer out to viewers | $79.16 | $79.16 |
| Amazon CloudFront data transfer to origin | $9.31 | $9.31 |
| AWS WAF web ACL and 7 rules | $12.00 | $12.00 |
| AWS WAF requests | $600.00 | $600.00 |
| Application Load Balancer hourly (2 Application Load Balancers) | $32.85 | $32.85 |
| Application Load Balancer capacity units | $11.18 | $11.18 |
| NAT gateway hourly (2 NAT gateways) | $65.70 | $65.70 |
| Public IPv4 addresses (4 in-use addresses) | $14.60 | $14.60 |
| NAT gateway data processing, bid requests | $1,257.29 | Not applicable |
| NAT gateway data processing, bid responses | $125.73 | Not applicable |
| Internet data transfer out to bidders (first 10 TB at $0.09 per GB, rest at $0.085) | $2,426.07 | Not applicable |
| RTB Fabric bid request transactions (3 billion at $34.00 per billion) | Not applicable | $102.00 |
| RTB Fabric payload above the 2 KiB included per transaction (22,218 GiB at $0.011 per GiB) | Not applicable | $244.39 |
|  **Total**  |  **$5,633.89**  |  **$2,171.19**  |
|  **Monthly difference**  |  |  **$3,462.70 lower (61%)**  |

The following assumptions apply to both RTB Fabric comparison tables:
+ Bid requests average 10 KB uncompressed. Bid responses average 1 KB (half are bids of about 2 KB, half are no-bids). Ad requests are 0.5 KB and browser responses are 1 KB.
+ Each RTB Fabric gateway is billed only for the traffic it sends. The Requester Gateway pays per bid request and is not billed for the responses it receives. RTB Fabric does not fan out requests, so 3 bidders means 3 transactions.
+ NAT gateways process both directions, so responses add NAT processing on the current path. The RTB Fabric path does not send bid traffic through the NAT gateways.
+ The NAT gateways stay in both options for other outbound traffic (image pulls, AWS API calls, and bidders not on RTB Fabric), so their hourly charge is in both columns.
+ Both columns include the 2 Application Load Balancers, NAT gateway hourly charges, and public IPv4 addresses from sample cost table 1. Fargate, ElastiCache, AWS KMS, CloudWatch, Amazon EFS, Amazon S3, AWS Glue, and the other services in sample cost table 1 are the same in both options and are not included in these totals.
+ Prices are On-Demand in US East (N. Virginia), without free tier or discounts. All RTB Fabric volume is in the first pricing tier (up to 2 trillion transactions per month).

For current RTB Fabric pricing details, see the [AWS RTB Fabric pricing page](https://aws.amazon.com/rtb-fabric/pricing/).

### Sample cost table 2
<a name="sample-cost-table-2"></a>

 **1,500 incoming requests per second at peak (approximately 1.3 billion ad requests and 3.9 billion bid requests per month), 10 Amazon ECS tasks**

The following table provides a sample cost breakdown for one month in the US East (N. Virginia) Region with 1.3 billion ad requests per month and 10 Amazon ECS tasks. This volume is about 500 requests per second on average (about 1,500 at peak). The task count is illustrative and conservative. The service scales on request count per task, CPU, and memory utilization, between 2 and 300 tasks by default, so the actual task count depends on the shape of your traffic.

| AWS service | Dimensions | Monthly cost [USD] |
| --- | --- | --- |
| AWS Fargate (Amazon ECS) | 10 tasks, each 2 vCPU and 4 GB memory, Linux/x86, 730 hours, 20 GB ephemeral storage (included at no charge); priced at On-Demand rates ($0.04048 per vCPU-hour, $0.004445 per GB-hour) | $720.80 |
| Elastic Load Balancing | 2 Application Load Balancers (internet-facing and internal) at $0.0225 per hour ($32.85), plus about 1,816 LCU-hours on the internet-facing load balancer (1,816 GiB processed, 1.5 KB per ad request, 1 GB per LCU-hour) at $0.008 per LCU-hour ($14.53) | $47.38 |
| NAT gateway | 2 NAT gateways at $0.045 per hour | $65.70 |
| NAT gateway data processing | 3.9 billion bid requests (36,322 GiB) and 3.9 billion bid responses (3,632 GiB), 39,954 GiB in total at $0.045 per GB | $1,797.92 |
| Data transfer out to the internet | 36,322 GiB of bid requests to bidders: first 10,240 GiB at $0.09 per GB ($921.60) and next 26,082 GiB at $0.085 per GB ($2,216.93); inbound bid responses are not charged | $3,138.53 |
| Public IPv4 addresses | 4 in-use public IPv4 addresses (2 NAT gateway Elastic IP addresses, 2 for the internet-facing load balancer) at $0.005 per hour | $14.60 |
| AWS WAF | 1 web ACL ($5.00) and 7 rules (6 AWS managed rule groups and 1 custom rule) at $1.00 each ($12.00), plus 1.3 billion requests at $0.60 per million ($780.00) | $792.00 |
| Amazon CloudFront | 1.3 billion HTTPS requests at $0.0100 per 10,000 ($1,300.00), 1,211 GiB of data transfer out to viewers at $0.085 per GB (first 10 TB tier, $102.91), and 605 GiB of data transfer to origin at $0.020 per GB ($12.11) | $1,415.02 |
| Amazon ElastiCache Serverless (Valkey) | About 1 GB of average data storage at $0.084 per GB-hour ($61.32), plus about 2.6 billion ECPUs (one write and one read per ad request) at $0.0023 per million ECPUs ($5.98) | $67.30 |
| AWS KMS | 6 customer managed keys at $1.00 each; request charges ($0.03 per 10,000 requests) are not included | $6.00 |
| Amazon CloudWatch | 19 standard-resolution alarms at $0.10 each ($1.90), 41 GB of log ingestion at $0.50 per GB ($20.50) | $22.40 |
| Amazon EFS | 1 TB of storage, about 20% in Standard at $0.30 per GB-month ($61.44) and 80% in Infrequent Access at $0.025 per GB-month ($20.48), plus 2 GB of Infrequent Access requests at $0.01 per GB ($0.02) | $81.94 |
| Amazon S3 | 2.5 TB of S3 Standard storage at $0.023 per GB-month | $58.88 |
| AWS Glue | About 200 DPU-hours for the metrics ETL job at $0.44 per DPU-hour | $88.00 |
| Other services | AWS CloudTrail, AWS DataSync, AWS Lambda, Amazon VPC gateway endpoint, and IAM | $2.00 |
|  |  **Total:**  |  **$8,318.47**  |

The amounts in this table are On-Demand, without free tier or discounts. Each ad request is 0.5 KB and the browser response is 1 KB. Each ad request goes to 3 bidders over the public internet, with 10 KB (10,000 byte) bid requests and 1 KB average bid responses. Data volumes are in GiB (230 bytes), and data transfer out uses the tiered rates for US East (N. Virginia). With the default `SpotInstanceWeight` of 1, about half of the Fargate tasks run on Fargate Spot, which lowers the Fargate line. The Other services line does not include invocations of the cache Lambda function, whose cost depends on how many bid responses are cached.

Sending bid requests through AWS RTB Fabric replaces the NAT gateway data processing and data transfer out to the internet rows. For details, see [AWS RTB Fabric cost comparison](#rtb-fabric-cost).

### Sample cost table 3
<a name="sample-cost-table-3"></a>

 **9,000 incoming requests per second at peak (approximately 7.8 billion ad requests and 23.4 billion bid requests per month), 60 Amazon ECS tasks**

The following table provides a sample cost breakdown for one month in the US East (N. Virginia) Region with 7.8 billion ad requests per month and 60 Amazon ECS tasks. This volume is about 3,000 requests per second on average (about 9,000 at peak). The task count is illustrative and conservative. The service scales on request count per task, CPU, and memory utilization, between 2 and 300 tasks by default, so the actual task count depends on the shape of your traffic.

| AWS service | Dimensions | Monthly cost [USD] |
| --- | --- | --- |
| AWS Fargate (Amazon ECS) | 60 tasks, each 2 vCPU and 4 GB memory, Linux/x86, 730 hours, 20 GB ephemeral storage (included at no charge); priced at On-Demand rates ($0.04048 per vCPU-hour, $0.004445 per GB-hour) | $4,324.81 |
| Elastic Load Balancing | 2 Application Load Balancers (internet-facing and internal) at $0.0225 per hour ($32.85), plus about 10,896 LCU-hours on the internet-facing load balancer (10,896 GiB processed, 1.5 KB per ad request, 1 GB per LCU-hour) at $0.008 per LCU-hour ($87.17) | $120.02 |
| NAT gateway | 2 NAT gateways at $0.045 per hour | $65.70 |
| NAT gateway data processing | 23.4 billion bid requests (217,929 GiB) and 23.4 billion bid responses (21,793 GiB), 239,722 GiB in total at $0.045 per GB | $10,787.51 |
| Data transfer out to the internet | 217,929 GiB of bid requests to bidders: first 10,240 GiB at $0.09 per GB ($921.60), next 40,960 GiB at $0.085 per GB ($3,481.60), next 102,400 GiB at $0.07 per GB ($7,168.00), and 64,329 GiB over 150 TB at $0.05 per GB ($3,216.47); inbound bid responses are not charged | $14,787.67 |
| Public IPv4 addresses | 4 in-use public IPv4 addresses (2 NAT gateway Elastic IP addresses, 2 for the internet-facing load balancer) at $0.005 per hour | $14.60 |
| AWS WAF | 1 web ACL ($5.00) and 7 rules (6 AWS managed rule groups and 1 custom rule) at $1.00 each ($12.00), plus 7.8 billion requests at $0.60 per million ($4,680.00) | $4,692.00 |
| Amazon CloudFront | 7.8 billion HTTPS requests at $0.0100 per 10,000 ($7,800.00), 7,264 GiB of data transfer out to viewers at $0.085 per GB (first 10 TB tier, $617.47), and 3,632 GiB of data transfer to origin at $0.020 per GB ($72.64) | $8,490.11 |
| Amazon ElastiCache Serverless (Valkey) | About 6 GB of average data storage at $0.084 per GB-hour ($367.92), plus about 15.6 billion ECPUs (one write and one read per ad request) at $0.0023 per million ECPUs ($35.88) | $403.80 |
| AWS KMS | 6 customer managed keys at $1.00 each; request charges ($0.03 per 10,000 requests) are not included | $6.00 |
| Amazon CloudWatch | 19 standard-resolution alarms at $0.10 each ($1.90), 41 GB of log ingestion at $0.50 per GB ($20.50) | $22.40 |
| Amazon EFS | 1 TB of storage, about 20% in Standard at $0.30 per GB-month ($61.44) and 80% in Infrequent Access at $0.025 per GB-month ($20.48), plus 5 GB of Infrequent Access requests at $0.01 per GB ($0.05) | $81.97 |
| Amazon S3 | 5 TB of S3 Standard storage at $0.023 per GB-month | $117.76 |
| AWS Glue | About 200 DPU-hours for the metrics ETL job at $0.44 per DPU-hour | $88.00 |
| Other services | AWS CloudTrail, AWS DataSync, AWS Lambda, Amazon VPC gateway endpoint, and IAM | $2.00 |
|  |  **Total:**  |  **$44,004.35**  |

The amounts in this table are On-Demand, without free tier or discounts. Each ad request is 0.5 KB and the browser response is 1 KB. Each ad request goes to 3 bidders over the public internet, with 10 KB (10,000 byte) bid requests and 1 KB average bid responses. Data volumes are in GiB (230 bytes), and data transfer out uses the tiered rates for US East (N. Virginia). With the default `SpotInstanceWeight` of 1, about half of the Fargate tasks run on Fargate Spot, which lowers the Fargate line. The Other services line does not include invocations of the cache Lambda function, whose cost depends on how many bid responses are cached.

Sending bid requests through AWS RTB Fabric replaces the NAT gateway data processing and data transfer out to the internet rows. For details, see [AWS RTB Fabric cost comparison](#rtb-fabric-cost).
