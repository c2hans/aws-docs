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
+ The **No Upfront** option doesn't require any upfront payment, and your commitment is charged purely on a monthly basis.
+ The **Partial Upfront** option offers lower prices on Savings Plans. You are charged at least half of your commitment upfront and the remaining is charged on a monthly basis.
+ The **All Upfront** option offers the lowest prices and your entire commitment is charged in one payment.

You can track your Savings Plans expirations and upcoming queued Savings Plans in AWS Cost Explorer. You can use Savings Plans alerts to receive advance email alerts 1, 7, 30, or 60 days before your plan expiration date, or when a commitment is queued for purchase. These notifications also alert you on the expiration date. You can send notifications to up to 10 email recipients.

## Understanding Savings Plans
<a name="savings-plans-work"></a>

Every type of compute usage has an on-demand rate and a Savings Plans rate. If you commit to $10/hour of compute usage, then you get Savings Plans prices on all usage up to $10 at the Savings Plans rate. Any usage beyond the compute spending commitment is charged at regular on-demand rates. You can get started with Savings Plans by using Cost Explorer in the AWS Management Console.

You can easily make a commitment to Savings Plans by using the recommendations provided in [Cost Explorer](https://console.aws.amazon.com/cost-reports/home?region=us-east-1#/dashboard) to realize the biggest savings. The recommended hourly commitment is based on your historical on-demand usage and your choice of plan type, term length, and payment option. Savings Plans is first applied to the account that purchased the plan, and then it's shared to other accounts in the consolidated billing family.

**Note**
The Savings Plans sharing option in AWS Organizations is enabled by default. You can decline this option in the AWS Billing console of the payer account. You can visit your [Recommendations](https://console.aws.amazon.com/cost-management/home) page to see the Savings Plans that AWS recommends to help you save on eligible usage. These recommendations can be refreshed at any time to make it easy for you to purchase the optimal Savings Plans.

### Compute Savings Plans
<a name="compute-9999999999999999sps-.885151c9-5fc2-5637-9d26-4eae8e6c3db6"></a>

Compute Savings Plans provide the most flexibility and help reduce your costs. These plans automatically apply to EC2 instance usage regardless of instance family, size, Availability Zone, Region, operating system, or tenancy. They also apply to Fargate or Lambda usage. For example, with Compute Savings Plans, you can change from C4 to M5 instances, shift a workload from EU (Ireland) to EU (London), or move a workload from EC2 to Fargate or Lambda at any time. You automatically continue to pay the Savings Plans price.

### EC2 Instance Savings Plans
<a name="ec2-instance-9999999999999999sps-.31fa0670-678f-5d44-a9e7-7ac1d0807288"></a>

EC2 Instance Savings Plans provide the deepest discounts in exchange for a commitment to usage of individual instance families in a Region (for example, committing to a consistent level of M5 usage in N. Virginia). This automatically provides you with discounts on the on-demand price of the selected instance family in that Region regardless of Availability Zone, size, operating system, or tenancy. EC2 Instance Savings Plans allow you to change your usage between instances within a family in that Region. For example, you can move from c5.xlarge running Windows to c5.2xlarge running Linux, and automatically benefit from the Savings Plans prices.

Both Compute and EC2 Instance Savings Plans apply to EC2 instances that are a part of Amazon EMR, Amazon Elastic Kubernetes Service (Amazon EKS) and Amazon Elastic Container Service (Amazon ECS) clusters. Amazon EMR, Amazon EKS, and Amazon ECS charges aren't covered by Savings Plans, but the underlying EC2 instances are. EC2 Instance Savings Plans are applied before Compute Savings Plans because Compute Savings Plans have broader applicability.

**Note**
You can't change a Savings Plans easily after you've made a commitment. We recommend that you plan carefully before making a commitment to either Savings Plans option. Savings Plans offer lower prices compared to on-demand pricing in exchange for a commitment, and can't be cancelled during the term.

### Hourly commitment example
<a name="hourly-commitment-example.9dec0f86-70bd-5899-a520-4de57720a790"></a>

If you purchase a Savings Plans, you make an hourly monetary commitment to the term of the plan. If you commit to $10/hour of compute usage, the Savings Plans pricing is automatically applied on all usage up to $10 dollars every hour. Any usage beyond the commitment is charged at the regular on-demand rates. You can use the Savings Plans purchase recommendations tool in Cost Explorer to get recommended commitments that can maximize your savings. The hourly financial commitment for a specific plan can't be modified for the term of the plan. If you want an increased commitment after analyzing usage, then you can purchase an additional Savings Plans to cover excess usage.

### Benefits of Savings Plans
<a name="benefits-of-9999999999999999sps-.923bd177-1ada-5f4d-86d5-f233485d0098"></a>

Compared to Reserved Instances, Savings Plans offer a more flexible pricing model that can save you money while you take advantage of the broader selection of compute options offered by Savings Plans. Savings Plans offer discounts, even as your compute needs change. This can help you keep up with your ever changing dynamic environment without incurring any additional management overhead. Here are some other benefits of using Savings Plans:
+ **Easy to use** – Receive automatic discounts in exchange for monetary commitment.
+ **Flexibility** – A single commitment that applies across multiple usage types.
+ **Potential savings** – There are a variety of ways to save. Consider the following examples:
  + 60 percent savings on Windows Server workloads using Compute Savings Plans ([d2.8xlarge, 3 years, all upfront, windows, shared tenancy, us-east-2](https://aws.amazon.com/savingsplans/compute-pricing/))
  + 73 percent savings on Windows Server workloads using EC2 Instance Savings Plans ([d2.8xlarge, 3 years, all upfront, windows, shared tenancy, us-east-2](https://aws.amazon.com/savingsplans/compute-pricing/))
  + 28–41 percent savings on non-exotic instance types ([t3 family, 3 years, all upfront, windows, shared tenancy, us-east-2](https://aws.amazon.com/savingsplans/compute-pricing/))
  + 25–40 percent average savings for Windows Servers

**Note**
EC2 Instance Savings Plans offer a greater discount than Compute Savings Plans because of the reduced flexibility. You commit to usage for a discounted price.

Every type of compute usage has a Savings Plans rate and on-demand rate. The following table shows the Savings Plans and on-demand rates for every operating system type. You're charged the Savings Plans rates on the committed usage and any usage beyond the commitment is charged at regular on-demand rates.

|
|
| Instance name | Savings Plans rate | On-demand savings | On-demand rate | Operating system | Region | Payment option | Term length |
| --- |--- |--- |--- |--- |--- |--- |--- |
| x2iedn.xlarge | $0.32 | 61% | $0.83 | Linux | US East (N. Virginia) | No upfront | 3 |
| x2iedn.xlarge | $2.01 | 50% | $1.02 | Windows | US East (N. Virginia) | No upfront | 3 |
| x2iedn.xlarge | $1.02 | 20% | $2.52 | Windows license included \+ SQL Server Enterprise edition | US East (N. Virginia) | No upfront | 3 |
| x2iedn.xlarge | $0.32 | 61% | $0.83 | BYOL | US East (N. Virginia) | No upfront | 3 |

Savings Plans include the operating system, and they have a separate discount for BYOL. They are all broken down in the [Compute Savings Plans calculator](https://aws.amazon.com/savingsplans/compute-pricing/).

### Reserved Instance pricing model
<a name="reserved-instance-pricing-model.106d2976-3428-52a6-93ac-ef23935e2dc2"></a>

AWS has another pricing model based on commitment known as Reserved Instances. This model can be problematic if your compute changes after you already make a commitment, causing the Reserved Instances to go unused. Savings Plans are designed to offer similar cost reductions as [Standard and Convertible Reserved Instances](https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/), but with much greater flexibility. Compute Savings Plans provide lower prices on EC2 instance usage regardless of instance family, size, operating system, tenancy, or Region. They also enable maximum flexibility.

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
We recommend that you purchase Savings Plans instead of Reserved Instances, but the two commitment models can work together if you already purchased Reserved Instances.

Consider an example where you purchased a Reserved Instance, but you want to start trying a Savings Plans option. There is logic for this combination to apply to your final billing. Here's a hierarchy that you can apply to your AWS accounts:

1. Zonal Reserved Instance applies to the account that owns it. If a Reserved Instance has hours left, it applies to the rest of the organization.

1. Non size-flexible Regional Reserved Instances for Windows apply to matching usage on the account that owns it. Anything that remains rolls out to the rest of the organization.

1. Size-flexible Regional Reserved Instances apply to the account that owns it (smallest instance within the family first and going up to larger instances), and then to the rest of organization.

1. Regional Reserved Instances apply to any unused on-demand capacity reservation.

1. EC2 Instance Savings Plans apply within the account that purchased it.

1. Compute Savings Plans apply within the account that purchased it.

**Note**
Discounts start with the usage that result in the highest discount and then down to the least discount. Windows instances traditionally have a lower discount potential then Linux for most common instance types (for example, T3, M6, and C5). This means that Linux instances benefit more than Windows instances in most cases.

The following graphic shows the price after dividing Reserved Instances from Savings Plans. Both Compute and EC2 Instance Savings Plans apply to running instances first and then to the unused On-Demand Capacity Reservations.

![Price after dividing Reserved Instances from Savings Plans](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/388680b2-a2d2-47e0-bc7c-582507d490fb.png)

## Cost optimization scenarios
<a name="savings-plans-guided-scenarios"></a>

This section covers cost optimization scenarios for Amazon EC2 Dedicated Hosts and Amazon EC2 instances that use a license-included billing model.

### Amazon EC2 Dedicated Hosts
<a name="9999999999999999ec2dedicatedhosts-.c86b712d-2c05-5f5c-bc36-b1260c3402f0"></a>

Consider a scenario where you're going to migrate your on-premises Windows workloads to AWS. You data center has the following servers:
+ Two servers with 16 vCPU and 128 GB RAM
+ Two servers with 32 vCPU and 164 GB RAM
+ One server with 8 vCPU and 64 GB RAM
+ 16 servers with vCPU and 32 GB RAM

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
<a name="9999999999999999ec2--instances-with-licenses-included.4a8d7b8d-a87d-5016-b60f-a76f71b4c9b7"></a>

Consider a scenario where you're going to migrate a single three-tier application to AWS, and you want to use the licenses provided by AWS. Furthermore, assume that your application works with the following servers:
+ Two web servers with two vCPUs and 4 GB RAM
+ Two application servers with eight vCPUs and 16 GB RAM
+ Two databases servers with 16 vCPUs and 64 GB RAM (using SQL Server Standard edition)

The following table shows the server instances that you can use in AWS.

|
|
| Instance type | CPU | RAM | Amount |
| --- |--- |--- |--- |
| c5.large | 2 | 4 | 2 |
| c5.2xlarge | 8 | 16 | 2 |
| r5.2xlarge | 8 | 64 | 2 |
|  |  |  | 6 server |

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

Both scenarios help you save money when you plan and forecast your workloads in AWS. It's important to recognize that the discount in the second scenario is less compared with the first scenario. In the second scenario, the license price is included on the price of the cloud server. AWS doesn't offer a discount on the license price, but you can always bring your licenses (under specific scenarios) and AWS can always warranty the best compute/instance price.

We recommend that you do the following to control your AWS spending on compute and instance resources:
+ Access recommendations
+ Customize recommendations according to your needs
+ Review the hourly commitment

### Access recommendations
<a name="access-recommendations.a94eb77d-1243-5ec9-a3b0-33f489ea56e9"></a>

You can use the [Amazon EC2 console](https://console.aws.amazon.com/ec2/) to access recommendations for your Savings Plans. You can even download your recommendations to review later in CSV format. For more information, see [Monitoring your Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-monitoring.html) in the Savings Plans documentation.

### Customize recommendations according your needs
<a name="customize-recommendations-according-your-needs.0556e0b3-7a56-5e9e-907d-783c9c8a5a85"></a>

Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/), expand the **Instances** section, and then choose **Savings Plans**. This page shows you instance and compute pricing before and after making a recommendation. You can also adjust the following factors for your recommendation:
+ **Term** – For example, 1–3 years
+ **Payment option** – For example, **Upfront**, **Partial Upfront**, or **No Upfront**
+ **History **– For example, the last 7, 30 or 60 days

### Review the hourly commitment
<a name="review-the-hourly-commitment.efabd68a-5e4d-525e-9427-9b95f41e6026"></a>

Using the same example, assume you have an instance that's running 24/7. The recommendation is to use a Savings Plans. According to the size, you have an on-demand price of $120/hour. You have the option to commit $90/hour, but this may vary depending on the Region, instance, and purchase option. In this example, you can save 25 percent compared with the on-demand cost. You can also track your utilization and coverage, if they are under the threshold that you defined, and configure an alert when the budget is going to end.

### Review recommendations
<a name="review-recommendations.3aff3268-a70a-5354-b2d6-b237c0b4d5fc"></a>

We recommend that you review Savings Plans recommendations carefully. AWS won't change anything without your permission. These are recommendations only and it's up to you to apply them or not.

### Purchase a plan
<a name="purchase-a-plan.ade0b710-7490-50f5-ba42-6b59f7aaa7f2"></a>

Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/), expand the **Instances** section, and then choose **Savings Plans**. Then, choose **Purchase Savings Plans**. Based on your requirements, you can select the following options: term, Region, instance family, hourly commitment, payment option, and even start date. You can choose from Compute Savings Plans, EC2 Instance Savings Plans, and SageMaker AI Savings Plans. For more information, see [Purchasing Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-purchase.html) in the Savings Plans documentation.

### Get a utilization report
<a name="get-a-utilization-report.91640409-7a59-5a98-a474-7379b9b1be83"></a>

After you purchase a Savings Plans, you can get a utilization report. The report helps you check your utilization, see if the purchased plan is enough to cover and maximize the discount, and cancel or add new discounts. This report can be exported to other formats like CSV. For more information, see [Using the utilization report](https://docs.aws.amazon.com/savingsplans/latest/userguide/ce-sp-usingPR.html) in the Savings Plans documentation.

### Follow purchasing best practices
<a name="follow-purchasing-best-practices.3843535e-01f1-5dc4-8cde-e5a4f259b119"></a>

We recommend that you follow these best practices before purchasing Savings Plans:
+ Use [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) to remove idle EC2 resources.
+ Perform any right sizing ahead of Savings Plans purchases.
+ Establish an hourly rate that you consistently keep for 30–60 days.
+ Purchase a commitment to cover as much of the consistent hourly rate as your organization is comfortable with. Consider fluctuations in demand or season.
+ Choose a quarterly review Savings Plans budget to maintain a consistent rate (for example, 70 percent coverage target for Savings Plans coverage). If the rate drops below desired coverage, purchase an additional Savings Plans as a true-up to meet your coverage goal.

## Additional resources
<a name="savings-plans-rec-resources"></a>
+ [Savings Plans for Amazon EC2 Reserved Instances](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/savings-plans.html) (AWS Whitepapers)
+ [Understanding how Savings Plans apply to your AWS usage](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-applying.html) (Savings Plans documentation)
+ [Announcing per second billing for EC2 Windows Server and SQL Server Instances](https://aws.amazon.com/about-aws/whats-new/2021/06/announcing-per-second-billing-for-ec2-windows-server-and-sql-server-instances/) (AWS documentation)
+ [AWS Cost Optimisation Series: Savings Plans Video \| Amazon Web Services](https://www.youtube.com/watch?v=2LJwrTtg2IU) (YouTube)
