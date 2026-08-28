---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-cost-optimization/pricing-models.html
---

# Choosing AWS pricing models for SAP workloads
<a name="pricing-models"></a>

One of the key benefits of running SAP on AWS is the *pay-as-you-go* pricing models, which means you pay only for what you use. Some models allow you reduce costs by committing to services or resources for a period of time. AWS also offers volume-based discounts so that you can realize savings as your usage increases. For more information, see [How does AWS pricing work? ](https://aws.amazon.com/pricing/)You can estimate the costs of running your SAP workloads on AWS by using the [AWS Pricing Calculator](https://calculator.aws/#/).

SAP workloads have varying degrees of required availability. Therefore, early in the migration process, you work with your account team to determine the most appropriate pricing model. Often your pricing model consists of a combination of multiple options, as determined by your availability requirements. For example, you might choose to include a Savings Plan for the resources associated with the production, quality, and development landscapes. Alternatively, because sandbox resources are only powered on when needed, you might choose an on-demand model for the resources in that environment.

This guide provides a brief summary of the following pricing models, which are applicable to SAP workloads on AWS:
+ [On-Demand](#on-demand)
+ [Savings Plans](#savings-plans)
+ [Dedicated Hosts](#dedicated-hosts)
+ [Reserved Instances](#reserved-instances)

Additional pricing models are available, but they are not discussed in this guide because they are not applicable to SAP workloads.

## On-Demand
<a name="on-demand"></a>

On-Demand pricing lets you pay for the compute capacity that you actually use, by the hour, with no long-term commitments. You can use this pricing model for workloads with varying degrees of availability, such as sandbox environment or a project environment (N\+1) that has a limited lifetime. If the average availability requirements of your EC2 instances is greater than approximately 70 hours each week, it might be more cost advantageous to consider putting these environments in a different pricing model.

For more information about this pricing model, see [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/).

## Savings Plans
<a name="savings-plans"></a>

Savings Plans are a flexible model that offers lower prices compared to On-Demand pricing, in exchange for specific usage commitments over a one-year or three-year period. The following types of Savings Plans are relevant to SAP workloads:
+ **Compute Savings Plans** – This type provides the most flexibility and helps reduce your costs by up to 66%. These plans apply to Amazon Elastic Compute Cloud (Amazon EC2) instance usage, regardless of the instance family, size, Availability Zone, Region, operating system, or tenancy. This plan also applies to AWS Fargate or AWS Lambda usage.
+ **EC2 Instance Savings Plans** – This type provides the lowest prices, offering savings up to 72% in exchange for commitment to usage of individual EC2 instance families in a single AWS Region.

When selecting a Savings Plan, confirm that your plan type and EC2 instance types are supported by your SAP products, databases, and operating systems. For more information, see [SAP Applications on AWS: Supported DB/OS and AWS EC2 products – 1656099](https://launchpad.support.sap.com/#/notes/1656099) (SAP note).

For more information about this pricing model, see [Compute Savings Plans](https://aws.amazon.com/savingsplans/compute-pricing/).

## Dedicated Hosts
<a name="dedicated-hosts"></a>

In this model, you pay for each active dedicated host, regardless of the quantity or size of the instances you launch on it. Dedicated Host pricing varies by instance family, Region and payment options. Compared to On-Demand pricing, this model can reduce costs up to 70%. This pricing model allows you to use your existing application license, which might be based on sockets, cores, or virtual machines (VMs). An example where this pricing model is typically used is for hosting workloads running on SQL Server.

For more information about this pricing model, see [Amazon EC2 Dedicated Hosts Pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/).

## Reserved Instances
<a name="reserved-instances"></a>

When reserved instances are assigned to a specific Availability Zone, they reserve capacity in that zone. This can be advantageous in the event of high demand for an Availability Zone because reserving the capacity means you can launch instances when needed. Reserved Instance (RI) pricing is offered in two options:
+ **Standard RI** – This option is typically used for workloads that have little variation in performance over the course of several months to years.
+ **Convertible RIs** – This option is typically used for workloads that require flexibility for changing instance families, operating systems, or tenancies, so that you can take advantage of the latest hardware enhancements.

For more information about this pricing model, see [Amazon EC2 Reserved Instances Pricing](https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
