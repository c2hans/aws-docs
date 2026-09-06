---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/cost1.html
---

# Cost
<a name="cost1"></a>

You are responsible for the cost of the AWS services used while running this solution. As of this revision, the cost for running this solution with the default settings with no incoming bidding traffic to the solution in the US East (N. Virginia) Region is approximately **$237.50 per month** .

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
+ Each incoming HTTP request to the solution is of a fixed size (0.5 KB), and three bidders participate in a single auction request.

### Sample cost table 1
<a name="sample-cost-table-1"></a>

 **No incoming bidding traffic to the solution, two Amazon ECS tasks**

| AWS service | Dimensions | Monthly cost [USD] |
| --- | --- | --- |
| Amazon ECS | Operating system (Linux), CPU architecture (x86), Average duration (30 days), Number of tasks or pods (2 per month), Amount of memory allocated (4 GB), Amount of ephemeral storage allocated for Amazon ECS (20 GB) | $54.50 |
| AWS WAF | Number of Web Access Control Lists (Web ACLs) utilized (1 per month), Number of Managed Rule Groups per Web ACL (6 per month) | $15.00 |
| Elastic Load Balancing | Number of Application Load Balancers (1) | $17.00 |
| Amazon EC2 - other | Number of NAT gateways (2) DT inbound: Not selected (0 TB per month), DT outbound: Internet (<50 GB per month), DT Intra-Region: (0 TB per month) | $69.00 |
| Amazon EFS | Desired storage capacity (1 TB per month), Infrequent access requests (<2 GB per month) | $25.00 |
| Amazon S3 | S3 Standard storage | $4.00 |
| Amazon CloudWatch | Number of Standard Resolution Alarm Metrics (20), Standard logs: Data ingested (<20 GB) | $10.00 |
| Other servicess | Amazon CloudFront, AWS CloudTrail AWS DataSync, IAM, AWS Glue, AWS KMS, AWS Lambda, and Amazon VPC | $47.00 |
|  |  **Total:**  |  **$241.50**  |

### RTB Fabric cost (optional)
<a name="rtb-fabric-cost"></a>

When deploying with the bidder simulator and RTB Fabric integration (`--include-rtb-fabric`), additional costs apply:

 **RTB Fabric with 50GB monthly outbound traffic**

Assuming \~10 KB average bid request, 3 AWS RTB Fabric linked internal bidders per auction, 50 GB outbound traffic (responses are DT-IN and free):

| AWS service | Dimensions | Monthly cost [USD] |
| --- | --- | --- |
| AWS RTB Fabric | Transaction pricing ($3/billion), Data transfer pricing ($0.02/GB). Total auctions: \~1.67 million. Total bid requests: \~5 million (0.005 billion) | $16.00 |

 **Cost comparison: RTB Fabric vs NAT Gateway (50GB monthly outbound traffic)**

| Connectivity Method | Monthly Cost [USD] |
| --- | --- |
| RTB Fabric (transaction \+ data transfer) | $16.00 |
| NAT Gateway (baseline from table above) | $69.00 |
|  **Monthly savings with RTB Fabric**  |  **$53.00 (77% reduction)**  |

For current RTB Fabric pricing details, see the [AWS RTB Fabric pricing page](https://aws.amazon.com/rtb-fabric/pricing/). With incoming traffic, costs scale based on the volume and size of RTB requests sent through the Fabric Link. Note that bid responses returning to Prebid Server are data transfer IN and incur no charges.

### Sample cost table 2
<a name="sample-cost-table-2"></a>

 **1,500 incoming requests per second (appoximately 1.3B × 3 = 3.7B impressions per month), 10 tasks total**

| AWS service | Dimensions | Monthly Cost [USD] |
| --- | --- | --- |
| Amazon CloudFront | Data transfer out to origin (1.5 TB per month), Data transfer out to internet (0.75 TB per month), Number of requests (HTTPS) (1.3 billion per month) | $967.50 |
| Amazon ECS | Operating system (Linux), CPU architecture (x86), Average duration (30 days), Number of tasks or pods (10 per month), Amount of memory allocated (4 GB), Amount of ephemeral storage allocated for Amazon ECS (20 GB) | $276.00 |
| AWS WAF | Number of Web Access Control Lists (Web ACLs) utilized (1 per month), Number of Managed Rule Groups per Web ACL (6 per month) | $211.00 |
| Elastic Load Balancing | Number of Application Load Balancers (1) | $133.00 |
| Amazon EC2 - other | Number of NAT Gateways (2) DT inbound: Not selected (0 TB per month), DT outbound: Internet (1.5 TB per month), DT Intra-Region: (0 TB per month), Data transfer cost (13.5) | $273.00 |
| Amazon EFS | Desired storage capacity (1 TB per month), Infrequent access requests (2 GB per month) | $96.00 |
| Amazon S3 | S3 Standard storage (2.5 TB per month) | $59.00 |
| Amazon CloudWatch | Number of Standard Resolution Alarm Metrics (20), Standard logs: Data ingested (41 GB) | $23.00 |
| AWS Glue | Data processing unit-hour for AWS Glue ETL job, approx. 200 DPU-hour | $92.00 |
|  |  **Total:**  |  **$2,130.50**  |

 **With RTB Fabric (optional):**

Assuming \~10 KB average bid request, 3 AWS RTB Fabric linked internal bidders per auction, 1.5 TB outbound traffic:

| AWS service | Dimensions | Monthly cost [USD] |
| --- | --- | --- |
| AWS RTB Fabric | Transaction pricing ($3/billion), Data transfer pricing ($0.02/GB). Total auctions: \~1.3 billion. Total bid requests: \~3.9 billion (0.0039 billion) | $42.42 |
| Amazon EC2 - other (NAT Gateway baseline) | Number of NAT Gateways (2) with 1.5 TB outbound | $273.00 |
|  **Monthly savings with RTB Fabric**  |  |  **$230.58 (84% reduction)**  |

### Sample cost table 3
<a name="sample-cost-table-3"></a>

 **9,000 incoming requests per second (7.8B × 3 = 23B impressions per month), 60 Amazon ECS tasks**

| AWS service | Dimensions | Monthly cost [USD] |
| --- | --- | --- |
| Amazon CloudFront | Data transfer out to origin (30 TB per month), Data transfer out to internet (5.75 TB per month), Number of requests (HTTPS) (7.8 billion per month) | $6,256.00 |
| Amazon ECS | Operating system (Linux), CPU architecture (x86), Average duration (30 days), Number of tasks or pods (60 per month), Amount of memory allocated (4 GB), Amount of ephemeral storage allocated for Amazon ECS (20 GB) | $1,660.00 |
| AWS WAF | Number of Web Access Control Lists (Web ACLs) utilized (1 per month), Number of Managed Rule Groups per Web ACL (6 per month) | $1,717.00 |
| Elastic Load Balancing | Number of Application Load Balancers (1) | $717.00 |
| Amazon EC2 - other | Number of NAT Gateways (2) DT inbound: Not selected (0 TB per month), DT outbound: Internet (1.2 TB per month), DT Intra-Region: (0 TB per month), Data transfer cost (13.5) | $748.00 |
| Amazon EFS | Desired Storage Capacity (1 TB per month), Infrequent access requests (5 GB per month) | $96.00 |
| Amazon S3 | S3 Standard storage (5 TB per month) | $118.00 |
| Amazon CloudWatch | Number of Standard Resolution Alarm Metrics (20), Standard logs: Data ingested (41 GB) | $23.00 |
| AWS Glue | Data processing unit-hour for AWS Glue ETL job, approx. 200 DPU-hour | $92.00 |
|  |  **Total:**  |  **$11,427.00**  |

 **With RTB Fabric (optional):**

Assuming \~10 KB average bid request, 3 AWS RTB Fabric linked internal bidders per auction, 1.2 TB outbound traffic:

| AWS service | Dimensions | Monthly cost [USD] |
| --- | --- | --- |
| AWS RTB Fabric | Transaction pricing ($3/billion), Data transfer pricing ($0.02/GB). Total auctions: \~7.8 billion. Total bid requests: \~23.4 billion (0.0234 billion) | $94.78 |
| Amazon EC2 - other (NAT Gateway baseline) | Number of NAT Gateways (2) with 1.2 TB outbound | $748.00 |
|  **Monthly savings with RTB Fabric**  |  |  **$653.22 (87% reduction)**  |
