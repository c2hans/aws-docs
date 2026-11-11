---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/savings-plans.html
---

# Optimize spending for Windows on Amazon EC2
<a name="savings-plans"></a>

## Overview
<a name="savings-plans-overview"></a>

One of the top concerns about migrating servers to AWS is the infrastructure costs. It's true that one of the benefits of the cloud is paying for the resources on demand, but there are production workloads that need to be available 24/7/365. [Savings Plans](https://aws.amazon.com/savingsplans/) are designed to save money on your steady-state AWS usage across EC2 instances, AWS Lambda, and AWS Fargate.

Savings Plans offer a flexible pricing model and can help you reduce pricing on Amazon EC2, Fargate, Lambda, and Amazon SageMaker AI usage in exchange for a commitment to a consistent amount of usage (for example, $10/hour). You commit to a consistent amount of hourly compute spending over one or three years and, in exchange, you receive a discount for that usage.

You can choose from three different payment options with Savings Plans:
+ The **No Upfront** option doesn't require any upfront payment, and AWS bills your commitment monthly.
+ The **Partial Upfront** option offers lower prices on Savings Plans. You pay at least half of your commitment upfront, and AWS bills the remainder monthly.
+ The **All Upfront** option offers greater discounts than the other options, and you pay your entire commitment in one payment.

You can track your Savings Plans expirations and upcoming queued Savings Plans in AWS Cost Explorer. You can use Savings Plans alerts to receive advance email alerts 1, 7, 30, or 60 days before your plan expiration date, or when a commitment is queued for purchase. These notifications also alert you on the expiration date. You can send notifications to up to 10 email recipients.

## Understanding Savings Plans
<a name="savings-plans-work"></a>

Every type of compute usage has an on-demand rate and a Savings Plans rate. If you commit to $10/hour of compute usage, then you get Savings Plans prices on all usage up to $10 at the Savings Plans rate. Any usage beyond the compute spending commitment is charged at regular on-demand rates. You can get started with Savings Plans by using Cost Explorer in the AWS Management Console.

You can make a commitment to Savings Plans by using the recommendations in [Cost Explorer](https://console.aws.amazon.com/cost-reports/home?region=us-east-1#/dashboard) to help maximize your savings. The recommended hourly commitment is based on your historical on-demand usage and your choice of plan type, term length, and payment option. Savings Plans apply first to the account that purchased the plan, and then they're shared with other accounts in the consolidated billing family.

**Note**
The Savings Plans sharing option in AWS Organizations is enabled by default. You can decline this option in the AWS Billing console of the payer account. You can visit your [Recommendations](https://console.aws.amazon.com/cost-management/home) page to see the Savings Plans that AWS recommends to help you save on eligible usage. You can refresh these recommendations at any time to help you purchase Savings Plans that fit your needs.

### Compute Savings Plans
<a name="compute-9999999999999999sps-.47d9eb80-b9a1-5b11-adb8-f195d15436ab"></a>

Compute Savings Plans offer flexibility and help reduce your costs. These plans automatically apply to EC2 instance usage regardless of instance family, size, Availability Zone, Region, operating system, or tenancy. They also apply to Fargate or Lambda usage. For example, with Compute Savings Plans, you can change from C4 to M5 instances, shift a workload from EU (Ireland) to EU (London), or move a workload from EC2 to Fargate or Lambda at any time. You automatically continue to pay the Savings Plans price.

### EC2 Instance Savings Plans
<a name="ec2-instance-9999999999999999sps-.1957f3b3-879a-5d81-86bb-c35cff9aa09a"></a>

EC2 Instance Savings Plans provide higher discounts in exchange for a commitment to usage of individual instance families in a Region (for example, committing to a consistent level of M5 usage in N. Virginia). This automatically provides you with discounts on the on-demand price of the selected instance family in that Region regardless of Availability Zone, size, operating system, or tenancy. EC2 Instance Savings Plans allow you to change your usage between instances within a family in that Region. For example, you can move from c5.xlarge running Windows to c5.2xlarge running Linux, and automatically benefit from the Savings Plans prices.

Both Compute and EC2 Instance Savings Plans apply to EC2 instances that are a part of Amazon EMR, Amazon Elastic Kubernetes Service (Amazon EKS) and Amazon Elastic Container Service (Amazon ECS) clusters. Amazon EMR, Amazon EKS, and Amazon ECS charges aren't covered by Savings Plans, but the underlying EC2 instances are. EC2 Instance Savings Plans are applied before Compute Savings Plans because Compute Savings Plans have broader applicability.

**Note**
You can't change a Savings Plans easily after you've made a commitment. We recommend that you plan carefully before making a commitment to either Savings Plans option. Savings Plans offer lower prices compared to on-demand pricing in exchange for a commitment, and you can't cancel them during the term.

### Hourly commitment example
<a name="hourly-commitment-example.41cddd2b-0906-5137-905a-12e76e77e410"></a>

If you purchase a Savings Plans, you make an hourly monetary commitment for the term of the plan. If you commit to $10/hour of compute usage, the Savings Plans pricing automatically applies to all usage up to $10 every hour. AWS charges any usage beyond the commitment at the regular on-demand rates. You can use the Savings Plans purchase recommendations tool in Cost Explorer to get recommended commitments that can help increase your savings. You can't modify the hourly financial commitment for a specific plan during the term of the plan. If you want an increased commitment after analyzing usage, then you can purchase an additional Savings Plans to cover excess usage.

### Benefits of Savings Plans
<a name="benefits-of-9999999999999999sps-.23b2f063-933e-5cb6-8905-c523453ee94f"></a>

Compared to Reserved Instances, Savings Plans offer a more flexible pricing model that can save you money while you take advantage of a broader selection of compute options. Savings Plans offer discounts, even as your compute needs change. This can help you keep up with your ever-changing environment without incurring additional management overhead. Here are some other benefits of using Savings Plans:
+ **Easy to use** – Receive automatic discounts in exchange for monetary commitment.
+ **Flexibility** – A single commitment that applies across multiple usage types.
+ **Potential savings** – There are a variety of ways to save. Consider the following examples:
  + 60 percent savings on Windows Server workloads using Compute Savings Plans ([d2.8xlarge, 3 years, all upfront, Windows, shared tenancy, us-east-2](https://aws.amazon.com/savingsplans/compute-pricing/))
  + 73 percent savings on Windows Server workloads using EC2 Instance Savings Plans ([d2.8xlarge, 3 years, all upfront, Windows, shared tenancy, us-east-2](https://aws.amazon.com/savingsplans/compute-pricing/))
  + 28–41 percent savings on general purpose instance types ([t3 family, 3 years, all upfront, Windows, shared tenancy, us-east-2](https://aws.amazon.com/savingsplans/compute-pricing/))
  + 25–40 percent average savings for Windows Servers

**Note**
EC2 Instance Savings Plans offer a greater discount than Compute Savings Plans because of the reduced flexibility. You commit to usage for a discounted price.

Every type of compute usage has a Savings Plans rate and on-demand rate. The following table shows the Savings Plans and on-demand rates for every operating system type. You're charged the Savings Plans rates on the committed usage and any usage beyond the commitment is charged at regular on-demand rates.

|
|
| Instance name | Savings Plans rate | On-demand savings | On-demand rate | Operating system | Region | Payment option | Term length |
| --- |--- |--- |--- |--- |--- |--- |--- |
| x2iedn.xlarge | $0.32 | 61% | $0.83 | Linux | US East (N. Virginia) | No upfront | 3 years |
| x2iedn.xlarge | $2.01 | 50% | $1.02 | Windows | US East (N. Virginia) | No upfront | 3 years |
| x2iedn.xlarge | $1.02 | 20% | $2.52 | Windows license included \+ SQL Server Enterprise edition | US East (N. Virginia) | No upfront | 3 years |
| x2iedn.xlarge | $0.32 | 61% | $0.83 | Bring your own license (BYOL) | US East (N. Virginia) | No upfront | 3 years |

Savings Plans include the operating system, and they have a separate discount for BYOL. The [Compute Savings Plans calculator](https://aws.amazon.com/savingsplans/compute-pricing/) breaks down all of these rates.

### Reserved Instance pricing model
<a name="reserved-instance-pricing-model.50908f39-89b9-5e72-b2e3-df20a3433e7c"></a>

AWS has another commitment-based pricing model known as Reserved Instances. With this model, Reserved Instances can go unused if your compute needs change after you make a commitment. Savings Plans are designed to offer cost reductions similar to [Standard and Convertible Reserved Instances](https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/), but with greater flexibility. Compute Savings Plans provide lower prices on EC2 instance usage regardless of instance family, size, operating system, tenancy, or Region.

The following table can help you choose between Savings Plans or Reserved Instances.

|  |
| --- |
|  | Reserved Instance | EC2 Instance Savings Plans | Compute Savings Plans |
| --- |--- |--- |--- |
| Average 1-year discount | Up to 38% | Up to 29% | Up to 29% |
| Average 3-year discount | Up to 58% | Up to 73% | Up to 60% |
| Instance family | Fixed | Fixed | Flexible |
| Instance size | Fixed (not Linux) | Flexible | Flexible |
| Geography | 1 Region | 1 Region | Flexible |
| Operating system | Fixed | Flexible | Flexible |
| Service | Amazon EC2 or Amazon RDS | Amazon EC2 | Amazon EC2, Fargate, Lambda |
| Payment options | All, partial, no upfront | All, partial, no upfront | All, partial, no upfront |
| Instance limits | 20 per Availability Zone | No limit | No limit |

**Note**
Savings Plans work by giving you a discount based on an hourly monetary commitment. The hourly financial commitment can't be canceled or changed during the term of your plan, but you can purchase additional Savings Plans to cover additional usage. This enables you to keep a consistent hourly commitment as your fleet grows.

You can use tools like [AWS Cost Explorer](https://docs.aws.amazon.com/savingsplans/latest/userguide/ce-sp-usingCR.html) or [AWS Cloud Intelligence Dashboards](https://wellarchitectedlabs.com/cloud-intelligence-dashboards/) to track your commitment. Cost Explorer provides a coverage target line that can help your organization plan its Savings Plans coverage strategy. If 75 percent of your workload is steady state, then 75 percent is a good target. This leaves 25 percent of the spending on-demand/variable based on dynamic workloads. If you need to increase that to 85 percent coverage, you can buy another Savings Plans commitment to increase the hourly monetary commitment.

**Note**
We recommend that you purchase Savings Plans instead of Reserved Instances, but the two commitment models can work together if you have already purchased Reserved Instances.

Consider an example where you purchased a Reserved Instance, but you want to start trying a Savings Plans option. AWS applies this combination to your final billing in a defined order. The following hierarchy applies to your AWS accounts:

1. Zonal Reserved Instance applies to the account that owns it. If a Reserved Instance has hours left, it applies to the rest of the organization.

1. Non-size-flexible Regional Reserved Instances for Windows apply to matching usage on the account that owns them. Anything that remains applies to the rest of the organization.

1. Size-flexible Regional Reserved Instances apply to the account that owns them (smallest instance within the family first and going up to larger instances), and then to the rest of the organization.

1. Regional Reserved Instances apply to any unused on-demand capacity reservation.

1. EC2 Instance Savings Plans apply within the account that purchased them.

1. Compute Savings Plans apply within the account that purchased them.

**Note**
Discounts apply first to the usage that results in the highest discount, and then to usage with progressively lower discounts. Windows instances typically have a lower discount potential than Linux instances for most common instance types (for example, T3, M6, and C5). This means that Linux instances benefit more than Windows instances in most cases.

The following graphic shows the price after separating Reserved Instances from Savings Plans. Both Compute and EC2 Instance Savings Plans apply to running instances first and then to the unused On-Demand Capacity Reservations.

![Price after dividing Reserved Instances from Savings Plans](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/388680b2-a2d2-47e0-bc7c-582507d490fb.png)

## Cost optimization scenarios
<a name="savings-plans-guided-scenarios"></a>

This section covers cost optimization scenarios for Amazon EC2 Dedicated Hosts and Amazon EC2 instances that use a license-included billing model.

### Amazon EC2 Dedicated Hosts
<a name="9999999999999999ec2dedicatedhosts-.463d402a-216b-5f24-93bc-5e880cac1205"></a>

Consider a scenario where you're going to migrate your on-premises Windows workloads to AWS. Your data center has the following servers:
+ Two servers with 16 vCPU and 128 GB RAM
+ Two servers with 32 vCPU and 164 GB RAM
+ One server with 8 vCPU and 64 GB RAM
+ 16 servers with 4 vCPU and 32 GB RAM

Additionally, assume that you can bring your own license to AWS because you have enough licenses to bring over. The following table shows the server instances that you can use in AWS.

|
|
| Instance type | CPU | RAM | Amount |
| --- |--- |--- |--- |
| r5.4xlarge | 16 | 128 | 2 |
| r5.8xlarge | 32 | 256 | 2 |
| r5.2xlarge | 8 | 64 | 1 |
| r5.xlarge | 4 | 32 | 16 |
|  |  |  | 21 |

An analysis shows that these 21 virtual machines can be distributed across two Dedicated Hosts with an R5 instance family host. The following table shows the cost of these two Dedicated Hosts.

|
|
| Dedicated Host on-demand scenario | Upfront pay | 1 month | 1 year | 3 years | AWS Pricing Calculator |
| --- |--- |--- |--- |--- |--- |
| On-demand | None | $10,123 | $121,475 | $364,392 | [AWS Pricing Calculator estimate](https://calculator.aws/#/estimate?id=9b6fdbace0ec97b7e70237ad829d2bdcfad188f0) |
| 1-year Savings Plans | None | $7,447 | $89,362 | - | [AWS Pricing Calculator estimate](https://calculator.aws/#/estimate?id=c43d9d05ed79fd21acb0290f81ed0116e3e88e7d) |
| 3-year Savings Plans | None | $5,476 | $65,712 | $197,128 | [AWS Pricing Calculator estimate](https://calculator.aws/#/estimate?id=21ece549ef4298895940c80eb780d44d0789a405) |
| 3-year Savings Plans with upfront payment | $84,438 | $2,755 | $117,499 | $183,618 | [AWS Pricing Calculator estimate](https://calculator.aws/#/estimate?id=97bb06dc65e70b78e3066a66b15e37de5b63d8c4) |

If you have the servers that you want to migrate to AWS, the final price for a 1-year Savings Plans is $89,362 instead of $121,475 for an on-demand price. This represents a 26.5 percent discount after one year. If you're considering staying in AWS for a longer period, then you can choose the 3-year Savings Plans for even deeper cost savings. At the end of three years, you pay $197,128 instead of $364,392. This results in a savings of 46 percent of the total amount after three years.

### Amazon EC2 instances with licenses included
<a name="9999999999999999ec2--instances-with-licenses-included.161f2678-9a6b-5d2d-af6a-34b6fe1ecb9f"></a>

Consider a scenario where you're going to migrate a single three-tier application to AWS, and you want to use the licenses provided by AWS. Furthermore, assume that your application works with the following servers:
+ Two web servers with two vCPUs and 4 GB RAM
+ Two application servers with eight vCPUs and 16 GB RAM
+ Two database servers with 16 vCPUs and 64 GB RAM (using SQL Server Standard edition)

The following table shows the server instances that you can use in AWS.

|
|
| Instance type | CPU | RAM | Amount |
| --- |--- |--- |--- |
| c5.large | 2 | 4 | 2 |
| c5.2xlarge | 8 | 16 | 2 |
| r5.2xlarge | 8 | 64 | 2 |
|  |  |  | 6 servers |

The following table shows the cost of these servers in AWS.

|
|
| License included by AWS | Upfront pay | 1 month | 1 year | 3 years | AWS Pricing Calculator |
| --- |--- |--- |--- |--- |--- |
| On-demand | None | $3,912 | $46,950    | $140,849   | [AWS Pricing Calculator estimate](https://calculator.aws/#/estimate?id=f611f476d6939302fb58164f9f2d8b2da6810683) |
| 1-year Savings Plans | None | $3,466 | $41,952 |  | [AWS Pricing Calculator estimate](https://calculator.aws/#/estimate?id=69688cd1cf31470af71e63ec75624ae010a5059e) |
| 3-year Savings Plans with no upfront payment | None | $3,189 | $38,264 | $114,804 | [AWS Pricing Calculator estimate](https://calculator.aws/#/estimate?id=0c67021f43a719223efed88a63f35eac05e41728) |
| 3-year Savings Plans with upfront payment | $112,110 | None | None | None | [AWS Pricing Calculator estimate](https://calculator.aws/#/estimate?id=6ed7e1f92deba1ca67cdfd2dcc4d54af098c0653) |

If you want to run these servers for production environments (24/7) with on-demand pricing, you pay a monthly cost of $3,912. Paying this monthly cost equates to $46,950 after one year and a total of $140,849 after three years.

If you choose the 1-year Savings Plans with no upfront payment, the monthly cost decreases to $3,466. At the end of the first year, you pay $41,952. This is a total discount of 11 percent. If you choose the 3-year Savings Plans with no upfront payment, the monthly cost decreases to $3,189. At the end of three years, you pay $114,804. That gives you an 18.5 percent savings.

## Cost optimization recommendations
<a name="cost-optimization-recommendations"></a>

Both scenarios help you save money when you plan and forecast your workloads in AWS. The discount in the second scenario is smaller than the discount in the first scenario. In the second scenario, the license price is included in the price of the cloud server. AWS doesn't offer a discount on the license price. However, under specific scenarios, you can bring your own licenses and still benefit from discounted compute and instance pricing.

We recommend that you do the following to control your AWS spending on compute and instance resources:
+ Access recommendations
+ Customize recommendations according to your needs
+ Review the hourly commitment

### Access recommendations
<a name="access-recommendations.f5a4ddff-876b-5e99-9c9a-55d3eda11a9b"></a>

You can use the [Billing and Cost Management console](https://console.aws.amazon.com/costmanagement/) to access recommendations for your Savings Plans. You can also download your recommendations in CSV format to review later. For more information, see [Monitoring your Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-monitoring.html) in the Savings Plans documentation.

### Customize recommendations according to your needs
<a name="customize-recommendations-according-to-your-needs.477dae51-013b-5b43-bd45-19d8d493c307"></a>

Open the [Billing and Cost Management console](https://console.aws.amazon.com/costmanagement/), and then in the navigation pane under **Savings Plans**, choose **Recommendations**. This page shows you instance and compute pricing before and after making a recommendation. You can also adjust the following factors for your recommendation:
+ **Term** – For example, 1–3 years
+ **Payment option** – For example, **Upfront**, **Partial Upfront**, or **No Upfront**
+ **History** – For example, the last 7, 30, or 60 days

### Review the hourly commitment
<a name="review-the-hourly-commitment.f3994bca-ccdc-52b7-9ae7-bdaa82af5384"></a>

Using the same example, assume that you have an instance that runs continuously. The recommendation is to use a Savings Plans. Based on the instance size, the on-demand price is $120 per hour. You can commit to $90 per hour, but this amount might vary depending on the Region, instance, and purchase option. In this example, you save 25 percent compared with the on-demand cost. You can also track your utilization and coverage, and configure an alert for when either metric falls below the threshold that you define.

### Review recommendations
<a name="review-recommendations.738eb0c1-c94f-5dfd-a67f-6c991f451909"></a>

We recommend that you review Savings Plans recommendations carefully. These are recommendations only. AWS doesn't make changes to your account unless you choose to apply them.

### Purchase a plan
<a name="purchase-a-plan.9d0d0f8a-664c-56b3-b99c-2fa828bde413"></a>

Open the [Billing and Cost Management console](https://console.aws.amazon.com/costmanagement/), and then in the navigation pane under **Savings Plans**, choose **Purchase Savings Plans**. Based on your requirements, you can select the following options: term, Region, instance family, hourly commitment, payment option, and start date. You can choose from Compute Savings Plans, Amazon EC2 Instance Savings Plans, Database Savings Plans, and SageMaker AI Savings Plans. For more information, see [Purchasing Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-purchase.html) in the Savings Plans documentation.

### Get a utilization report
<a name="get-a-utilization-report.e49065cd-23d1-5aee-9382-9814210396c3"></a>

After you purchase a Savings Plans, you can generate a utilization report. The report helps you check your utilization and determine whether your purchased plan provides the coverage that you need. Based on the results, you can purchase additional plans. You can export this report to other formats, such as CSV. For more information, see [Using the utilization report](https://docs.aws.amazon.com/savingsplans/latest/userguide/ce-sp-usingPR.html) in the Savings Plans documentation.

### Follow purchasing recommendations
<a name="follow-purchasing-recommendations.a5c5e54f-138b-5250-ad0e-e7a968ee542a"></a>

We recommend that you do the following before you purchase Savings Plans:
+ Use [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) to identify and remove idle Amazon EC2 resources.
+ Right size your resources before you purchase Savings Plans.
+ Establish an hourly usage rate that you consistently maintain for 30–60 days.
+ Purchase a commitment to cover the portion of the consistent hourly rate that meets your organization's risk tolerance. Consider fluctuations in demand and seasonality.
+ Create a Savings Plans coverage budget and review it quarterly to maintain a consistent rate (for example, a 70 percent coverage target). If coverage drops below your target, purchase an additional Savings Plans as a true-up to meet your coverage goal.

## Additional resources
<a name="savings-plans-rec-resources"></a>
+ [Savings Plans for Amazon EC2 Reserved Instances](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/savings-plans.html) (AWS Whitepapers)
+ [Understanding how Savings Plans apply to your AWS usage](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-applying.html) (Savings Plans documentation)
+ [Announcing per second billing for EC2 Windows Server and SQL Server Instances](https://aws.amazon.com/about-aws/whats-new/2021/06/announcing-per-second-billing-for-ec2-windows-server-and-sql-server-instances/) (AWS documentation)
+ [AWS Cost Optimization Series: Savings Plans Video \| Amazon Web Services](https://www.youtube.com/watch?v=2LJwrTtg2IU) (YouTube)
