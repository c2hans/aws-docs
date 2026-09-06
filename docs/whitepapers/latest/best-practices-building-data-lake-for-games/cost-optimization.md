---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/cost-optimization.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Cost optimization
<a name="cost-optimization"></a>

 Cost is derivative from the usage of the underlying services that contribute to the data lake. There is no additional charge for using features in Lake Formation; however, standard usage rates apply when using services such as AWS Glue, Amazon S3, Amazon EMR, Amazon Athena, Amazon Redshift, Amazon Kinesis, and so on.

 A few things to consider regarding cost when building a data lake on AWS include:
+  **Cost drivers** — There are three main drivers of cost with AWS: Compute, storage and outbound data transfer. These vary depending on AWS product, pricing model and the Region (Data location).
+  **Cost optimization strategies** — Based on the three main drivers of costs, and we can leverage a plethora of cost-efficient solutions on AWS to help meet the right use-case and budget. For example:
  +  **Compute: On-Demand Instances vs. Savings Plans vs. Spot Instances vs. Reservations** — Customers can pick and choose the right model, based on workload type and costs. For services such as Amazon Redshift and EMR, it is important to “right-size” your solution to best fit your business needs, and then use Reserved Instances to further reduce costs. Refer to [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/).
  +  Most AWS analytics services are serverless, which means you pay only for the compute you use and nothing more. When optimizing for cost with serverless services, there are some key considerations:
    +  Avoiding re-processing data when possible, and only process what you need. As an example, this can be done by using AWS Glue Job bookmarks when processing data, or targeting only the data you need within a partition when using Athena.
    +  Assigning the correct number of resources for data processing.
    +  Correct partitioning, compression, storage, and lifecycle policy strategies when storing data in Amazon S3.
+ **Storage:**
  + **[S3 Tiers vs. EBS vs. EFS vs. Amazon FSx vs. Snow Family](https://aws.amazon.com/products/storage/)**: — You can choose from a variety of storage tools available on AWS. Intelligent options are also available if you prefer to let AWS decide the right S3 tier, depending on your unique usage.
  +  **Outbound data transfer** — Customers do not pay for inbound data transfer across all services in all Regions. Data transfer from AWS to the internet is charged per service, with rates specific to the originating Region. Refer to the pricing pages for each service to get more detailed pricing information. Best practices include:
    +  Avoid routing traffic over the internet when connecting to AWS services. Use VPC endpoints if available.
    +  Consider AWS Direct Connect for connecting to on-premises networks.
    +  Avoid cross-Region costs unless your business case requires it.
    +  [Create a data transfer cost analysis dashboard](https://wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/) to be strategic in managing your capacity and usage.
+  **Cost calculation tools** — For a more detailed calculation of monthly costs on AWS, refer to the [AWS Pricing Calculator.](https://calculator.aws/) For existing infrastructure on your AWS account, refer to [AWS Cost Management Console](https://console.aws.amazon.com/cost-management) in your AWS Management Console for a detailed analysis on your usage (sign-in required). Subscribe to your [Trusted Advisor reports](https://console.aws.amazon.com/trustedadvisor) in your AWS account for cost optimization checks that can save you money (sign-in required). For example, you might have unused resources in your AWS account that can be deleted.
