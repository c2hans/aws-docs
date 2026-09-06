---
source_url: https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/amazon-ec2-cost-breakdown.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon EC2 cost breakdown
<a name="amazon-ec2-cost-breakdown"></a>

 The following table shows the characteristics for Amazon EC2 used for this dynamic site in the US East (Northern Virginia) Region.

|  |  |  |
| --- |--- |--- |
|  Characteristic  |  Estimated Usage  |  Description  |
|  Utilization  |  100%  |  All infrastructure components run 24 hours per day, seven days per week  |
|  Instance  |  t3a.xlarge  |  16 GB memory, 4 vCPU  |
|  Storage  |  Amazon EBS SSD gp2  |  One Amazon EBS volume per instance with 30 GB of storage per volume  |
|  Data backup  |  Daily Amazon EBS snapshots  |  One Amazon EBS volume per instance with 30 GB of storage per volume  |
|  Data transfer  |  Data in: 1 TB/month <br /> Data out: 1 TB/month  |  10% incremental change per day  |
|  Instance scale  |  4  |  On average per day, there are four instances running  |
|  Load Balancing  |  20 GB/hour  |  ELB is used 24 hours per day, seven days per week. It processes a total of 20 GB/hour (data in and data out)  |
|  Database  |  MySQL, db.m5.large instance with 8 GB memory, 2 vCPUs, 100 GB storage  |  Multi-AZ deployment with synchronous standby replica in a separate Availability Zone  |

 The total cost for one month is the sum of the cost of the running services and data transfer out, minus the AWS Free Tier discount. We calculated the total cost using the [AWS Pricing Calculator](https://calculator.aws/).

 **Table: Cost breakdown**

|  |  |  |  |
| --- |--- |--- |--- |
|  Service  |  Monthly  |  Annually  |  Conﬁguration  |
|  ELB  |  $87.60  |  $1,051.20  |  Number of Network Load Balancers (one), Processed bytes per Network Load Balancer (NLB) for TCP (20 GB per hour)  |
|  Amazon EC2  |  $439.16  |  $5,269.92  |  Operating system (Linux), quantity (four), storage for each Amazon EC2 instance (General Purpose SSD (gp2)), storage amount (30 GB), instance type (t3a.xlarge)  |
|  Amazon Elastic IP address  |  $0  |  $0  |  Number of Amazon EC2 instances (one), Number of EIPs per instance (one)  |
|  Amazon RDS for MySQL  |  $272.66  |  $3,271.92  |  Quantity (one) db.m5.large, Storage for each Amazon RDS instance (General Purpose SSD (gp2)), storage amount (100 GB)  |
|  Amazon Route 53  |  $183.00  |  $2,196.00  |  Hosted Zones (1), Number of Elastic Network Interfaces (2), Basic Checks Within AWS (0)  |
|  Amazon Virtual Private Cloud (Amazon VPC)  |  $92.07  |  $1,104.84  |  Data transfer cost, inbound (from: internet) 1 TB per month, outbound (to: internet) 1 TB per month, intra-Region 0 TB per month  |
