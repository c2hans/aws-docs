---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/cost-management-on-aws-how-to-choose.html
---

# Choosing an AWS cost management strategy
<a name="cost-management-on-aws-how-to-choose"></a>

**Taking the first step**

|  |  |
| --- |--- |
| **Purpose** | Help determine which cost management services and tools are the best fit for your needs. |
| **Last updated** | December 20, 2024 |
| **Covered services** |  +  [AWS Billing Conductor](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html) <br />+  [AWS Billing Console](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html) <br />+  [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) <br />+  [AWS Budget Actions](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html) <br />+  [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) <br />+  [AWS Consolidated Billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) <br />+  [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html) <br />+  [AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html) <br />+  [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) <br />+  [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) <br />+  [AWS Cost Optimization Hub](https://aws.amazon.com/aws-cost-management/cost-optimization-hub/faqs/) <br />+  [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) <br />+  [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) <br />+  [AWS Pricing Calculator](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html) <br />+  [AWS Purchase Order Management](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-purchaseorders.html) <br />+  [Amazon EC2 Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) <br />+  [AWS Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) <br />+  [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) <br />+  [Amazon S3 Intelligent Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html) <br />+  [Migration Evaluator](https://aws.amazon.com/migration-evaluator/features)   |

## Introduction to AWS cost management
<a name="intro"></a>

Cost management and optimization in the cloud are important for businesses of all sizes. An effective cost management strategy ensures that you only pay for what you need and that you maximize the return on your cloud investment.

With cloud services, costs are dynamic and can escalate if not monitored closely. Financial planning, coupled with a clear understanding of the cost models for each service that you use, lets you allocate resources strategically, aligning spending with your business goals. This includes choosing the right pricing models, such as pay-as-you-go or Reserved Instances, and using auto-scaling to match resource provisioning with actual demand.

We offer services and tools to help you with cost management and optimization, including resources to:
+ Organize and track your cost and usage data.
+ Improve control through consolidated billing and access permissions.
+ Enable better planning through budgeting and forecasts.
+ Lower your costs by using the right resources and pricing optimizations.

This decision guide will help you determine which cost management services and tools are the best fit for your needs.

[![AWS Videos](http://img.youtube.com/vi/0aYZUqpwJKE?start=192&end=611/0.jpg)](http://www.youtube.com/watch?v=0aYZUqpwJKE?start=192&end=611)

## Understand AWS cost management
<a name="understand"></a>

AWS cost management strategy can be broken down into several key areas:

**Plan and evaluate:** When planning for future cloud spend, start by defining your key performance indicators (KPIs), such as the monthly cost of a specific project. Make sure that cloud resources related to a project are properly tagged with cost allocation tags, cost categories, or both. Then calculate and track the monthly cost of the project with the cost and usage data available in your AWS Cost Explorer and AWS Cost and Usage Report.

![Diagram showing the AWS Cloud Financial Management Portfolio.](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/cfm-portfolio.png)

Decide the project budget based on the trend shown by your KPIs, and the available funds set aside for the project. Set the budget thresholds using AWS Budgets for cost or resource usage.

**Manage and control:** As your organization evolves, you need the freedom to experiment and innovate in the cloud, while maintaining control over cost, governance, and security. One way to do that is to establish centralized ownership through a center of excellence or cloud business team. While cost management is a shared responsibility across an organization, a centralized team can design policies and governance mechanisms, implement and monitor the effort, and drive best practices.

This team can be supported by services such as [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) and [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).

Use the [AWS Billing Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/billinginfo.html) to track your overall spend, view your cost breakdown by service and by account on your billing dashboard, and handle data exports with AWS CloudFormation.

![Diagram showing the AWS Billing Conductor and AWS Application Cost Profiler.](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/billing-console-cost-profiler.png)

**Track and allocate:** Tracking spending and allocating that spending to the right team can be vital to effective cost optimization. It's useful to know when you're spending more than you planned, but even more useful when you can clearly identify where that spending is happening. We offer several tools to help you get started.

AWS Cost Explorer (when paired with Cost Allocation Tags) lets you categorize your resources and spending to fit your organization’s needs, while AWS Billing Conductor lets you customize your pricing and billing report to align with your business logic.

**Optimize and save:** Cost optimization is about making sure that you pay only for what you need. Two of the more useful strategies for optimizing spending are:
+ **Using the right pricing models.**
+ **Identifying and removing any idle or over-provisioned resources.** Use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-getting-started.html) resource recommendations to see top-level KPIs for rightsizing and instance selection recommendations.

Focus on these four areas to manage your AWS costs more effectively, maintain financial control, and optimize your cloud operations for maximum efficiency and value.

## Consider AWS cost management criteria
<a name="consider"></a>

The following section outlines some of the key criteria to consider when choosing a cost management strategy and supporting tools and services.

------
#### [ Business goals and priorities ]

How you manage the costs of your cloud investment depends on what you’re trying to do, as well as how you’re tracking performance. If your organization is in a growth phase, then your KPIs may focus on market share, customer growth, and getting the best return on investment. If your focus is on reducing operating costs, then you will concentrate more on achieving the right balance between spending and delivering for your customers.

Set your budget based on the trend shown by your KPIs, as well as your available funds. Then set the budget thresholds using [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) for cost or resource usage and to set utilization or coverage targets for your [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) (RIs) and [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html).

Monitor how the budget portfolio is progressing in your AWS Budgets Reports dashboard. Create notification alerts, which will be sent whenever cost and usage either reach your forecasts or exceed your threshold limits.

------
#### [ Budget policy and control ]

One key strategy for controlling cost is to have control over which services can be used by which members of your organization. If you need this kind of access control, use [IAM](https://aws.amazon.com/iam/getting-started/) to control individual and group access to your resources. This involves being able to create, manage, and grant permissions to IAM users to let them access the appropriate resources for their role and location. Use [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) to enable automatic policy-based account creation, management, and billing at scale.

------
#### [ Budget target tracking ]

It’s useful to get alerts that let you know if you’ve exceeded your budget, but it’s even more useful to see what is causing your bill to exceed your budget. Use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html), to see which AWS services are increasing your spend.

To see which parts of your organization drive increased spend and usage, you can categorize your resources and spending using Cost Allocation Tags with AWS Cost Explorer.

------
#### [ Detailed reporting ]

If you want your cost management strategy to scale with your usage, it is important to get detailed reporting when you have multiple users working with multiple AWS services.

You can use the billing dashboard on the [AWS Billing Console](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html) to:
+ Track your overall spend.
+ View your cost breakdown by service and account.
+ Get a unified view of spend in a single bill.
+ Establish rules for how to organize costs.
+ Share discount benefits associated with RIs and Savings Plans.

------
#### [ Business logic alignment ]

It’s not only about the numbers. Your cost optimization strategy must also align with the logic of your business. [AWS Billing Conductor](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html) lets you customize your AWS pricing and billing report to provide that alignment with your business logic. To help address your cost allocation needs, group accounts according to their financial relationships, adjust ratings, share credits and savings, or add overhead costs.

With AWS Billing Conductor, you can customize a second, alternative version of your monthly billing data. This alternative version models the billing relationship between you and your customers or business units, but doesn't change the way that AWS bills you. Using the alternative version provides you with a mechanism to configure, generate, and display rates to certain customers over a given billing period. Analyze the difference between the rates that you apply to your groupings, relative to the actual rates for those same accounts from AWS.

------
#### [ Pricing model ]

Customers with predictable, steady workloads on Amazon EC2, Amazon SageMaker AI, and Amazon RDS should consider [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) (RIs) to save up to 75% over equivalent on-demand capacity. RIs are available in three options: all upfront, partial upfront, and no upfront. To maximize your savings, when you buy RIs, the larger the upfront payment, the greater the discount. Partial upfront RIs offer lower discounts, but give you the option to spend less up front. Lastly, you can choose to spend nothing up front and receive a smaller discount, which lets you free up capital to spend on other projects.

We offer Reserved Instance and Savings Plans purchase recommendations through [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html), based on your past usage. AWS Cost Explorer identifies and recommends the commitment value that it estimates will result in the largest savings.

------
#### [ Rightsizing services ]

Another key element of cost management is identifying and removing any idle or over-provisioned resources. [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) resource recommendations let you view top-level KPIs for rightsizing and instance selection recommendations.

These recommendations identify idle and underutilized instances, and search for smaller instance sizes in the same instance family.

------

## Choose an AWS cost management service
<a name="choose"></a>

Now that you know the criteria by which you will evaluate your cost management options, you are ready to choose which AWS cost management service is a good fit for your organizational requirements.

The following table highlights which services are optimized for which circumstances. Use the table to help determine the service that is the best fit for your organization and use case.

| Service category | What is it optimized for? | Cost management services |
| --- |--- |--- |
|  **Plan and evaluate**  |  **Services optimized for improving planning, to create accurate forecasting of variable usage.**  |  |
| --- |--- |--- |
|  | Helps you create a directional business case for AWS Cloud planning and migration. | [Migration Evaluator](https://aws.amazon.com/migration-evaluator/features/) |
|  | Provides a free web-based planning tool for creating cost estimates for using AWS services. | [AWS Pricing Calculator](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html) |
|  | Provides improved planning and cost control with flexible budgeting and forecasting. | [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) |
|  | Helps you centrally govern your AWS environment as you grow and scale on AWS. | [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) |
|  **Manage and control**  |  **Services optimized to provide centralized billing, automatic cost governance, and a streamlined procure-to-purchase process.**  |   |
| --- |--- |--- |
|  | Provides a dashboard to track overall spend and view cost breakdown by service and account. | [AWS Billing Console](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html) |
|  | Helps you to configure multiple purchase orders (POs), define how POs are mapped to their invoices, and access invoices generated against those POs. | [AWS Purchase Order Management](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-purchaseorders.html) |
|  | Provides functionality to run an action when a budget exceeds a certain cost or usage threshold, either automatically or after manual approval. | [AWS Budget Actions](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html) |
|  | Helps you use machine learning models to detect and alert on anomalous spend patterns in your deployed AWS services. | [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html) |
|  | Consolidates billing and payment for multiple AWS accounts, allowing shared volume discounts across all accounts. | [AWS Consolidated Billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) |
|  | Enables you to create billing and cost management data exports using basic SQL, and visualize data by integrating with Amazon Quick. | [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) |
|  **Track and allocate**  |  **Services optimized to track and analyze cost trends and drivers in aggregate.**  |  |
| --- |--- |--- |
|  | Provides visualization of cost and utilization with default reports, and creates specific views with filters and grouping. | [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) |
|  | Delivers cost and usage data to an S3 bucket where it can be integrated into other AWS tools or ERP for further analysis. | [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) |
|  | Group accounts, tags, services, and charge types into meaningful categories with custom rules. | [AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html) |
|  | Supports the showback and chargeback workflows of AWS Solution Providers and Enterprise customers. | [AWS Billing Conductor](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html) |
|  **Optimize and save**  |  **Services optimized for resource right-sizing, reserve capacity planning, and data transfer and storage optimization.**  |   |
| --- |--- |--- |
|  | Provides a flexible pricing model that can help reduce your bill by up to 72% over on-demand prices. | [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) |
|  | Offers a billing discount that provides savings on Amazon EC2 costs compared to on-demand instance pricing. | [Amazon EC2 Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) |
|  | Recommends optimal AWS compute resources for your workloads, helping you reduce costs and improve performance. | [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) |
|  | Provides Amazon EC2 instances that use spare Amazon EC2 capacity that is available for less than the on-demand price. | [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) |
|  | Optimizes storage costs by automatically moving data to the most cost-effective access tier when access patterns change.  | [Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html) |
|  | Provides you with a comprehensive view of your cost optimization recommendations across your AWS Regions and AWS accounts within your organization. | [AWS Cost Optimization Hub](https://aws.amazon.com/aws-cost-management/cost-optimization-hub/faqs/) |

## Use an AWS cost management service
<a name="use"></a>

You should now have a clear understanding of what each AWS cost management service (and the supporting AWS tools and services) does—and which might be right for you.

We have provided a pathway to explore how each of the available AWS cost management services work. The following section provides links to in-depth documentation, hands-on tutorials, and resources to get you started.

------
#### [ AWS Billing Conductor ]
+  **Getting started with AWS Billing Conductor**

  Learn how to create billing groups, pricing configurations, and custom line items in AWS Billing Conductor.

   [Explore the guide ](https://docs.aws.amazon.com/billingconductor/latest/userguide/creating-abc.html)
+  **Getting Started with AWS Billing Conductor**

  Learn how to customize billing data and reporting in a way that aligns with your unique business logic.

   [Read the blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/getting-started-with-aws-billing-conductor/)
+  **Best practices for AWS Billing Conductor**

  Explore best practices when working with AWS Billing Conductor.

   [Explore the guide](https://docs.aws.amazon.com/billingconductor/latest/userguide/best-practices.html)
+  **AWS Billing Conductor FAQs**

  Learn about Billing Groups, configuring pricing, custom line items, and more.

   [Explore the guide](https://aws.amazon.com/aws-cost-management/aws-billing-conductor/faqs/)
+  **AWS Billing Conductor pricing**

  Learn about pricing options, examples, and calculation resources.

   [Explore the guide](https://aws.amazon.com/aws-cost-management/aws-billing-conductor/pricing/)

------
#### [ AWS Budgets ]
+  **Best practices for AWS Budgets**

  Explore best practices to use when working with AWS Budgets.

   [Explore the guide ](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-best-practices.html)
+  **Getting Started with AWS Budgets**

  Use AWS Budgets to set a custom cost budget that tracks your costs at a monthly level, and to configure alerts that will notify you when you reach your user-defined spend thresholds.

   [Explore the blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/getting-started-with-aws-budgets/)
+  **Control your AWS costs**

  Control your costs while exploring AWS service offerings using the AWS Free Tier, and how to use AWS Budgets to set up a cost budget to monitor usage.

   [Get started with the tutorial ](https://aws.amazon.com/getting-started/hands-on/control-your-costs-free-tier-budgets/)
+  **AWS Budgets FAQs**

  Learn how AWS Budgets works, and how to add alerts and subscribers.

   [Explore the guide ](https://aws.amazon.com/aws-cost-management/aws-budgets/faqs/)
+  **AWS Budgets Pricing**

  Learn about pricing options and request quotes.

   [Explore the guide ](https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/)

------
#### [ Compute Optimizer ]
+  **Getting started with AWS Compute Optimizer**

  Learn how to access AWS Compute Optimizer for the first time, and how to opt in your accounts.

   [Explore the guide ](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html)
+  **Rightsizing recommendation preferences **

  Learn how the rightsizing recommendation feature allows you to customize the settings you want Compute Optimizer to consider when generating Amazon EC2 and Auto Scaling group instance recommendations.

   [Explore the guide](https://docs.aws.amazon.com/compute-optimizer/latest/ug/rightsizing-preferences.html)
+  **AWS Graviton-based instance recommendations**

  Learn how to view the price and performance impact of running your workload on AWS Graviton-based instances.

   [Explore the guide ](https://docs.aws.amazon.com/compute-optimizer/latest/ug/graviton-recommendations.html)

------
#### [ Cost Explorer ]
+  **Getting started with Cost Explorer**

  Explore how to get started with Cost Explorer from the AWS Cost Management Console.

   [Explore the guide ](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-getting-started.html)
+  **Exploring your data using Cost Explorer**

  Discover how to see your estimated costs for the month to date, your forecasted costs for the month, a graph of daily costs, your top five cost trends, and a list of recently viewed reports.

   [Explore the guide](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-exploring-data.html)
+  **Exploring more data for advanced cost analysis**

  Learn how to enable multi-year data (at monthly granularity) and more granular data (at hourly and daily granularity) for the previous 14 days.

   [Explore the guide](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-advanced-cost-analysis.html)
+  **Forecasting with Cost Explorer**

  Learn how to create a forecast, a prediction of how much you will use AWS services over a selected forecast time period.

   [Explore the guide ](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-forecast.html)

------
#### [ AWS Data Exports ]
+  **Creating Data Exports**

  Learn how to use Data Exports in the AWS Billing and Cost Management console.

   [Explore the guide ](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create.html)
+  **Migrating from CUR to Data Exports CUR 2.0**

  Learn how to create exports of AWS Cost and Usage Report 2.0 (CUR 2.0) for more consistent schema and nested data.

   [Explore the guide](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-migrate.html)
+  **Data Exports for FOCUS 1.0 is now in general availability**

  Standardize exports of your AWS cost and usage data with the FOCUS 1.0 (FinOps Open Cost and Usage Standard) schema.

   [Read the blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/data-exports-for-focus-1-0-is-now-generally-available/)

------
#### [ RI Reporting ]
+  **Getting started with Amazon EC2 Reserved Instances**

  Dive deeper into the details of how RIs work.

   [Explore the guide ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html)
+  **Reserved Instance (RI) Reporting FAQs**

  Get answers to frequently asked questions about Reserved Instance reporting and recommended best practices.

   [Explore the FAQs](https://aws.amazon.com/aws-cost-management/reserved-instance-reporting/faqs/)
+  **Accessing Reserved Instance Recommendations**

  If you enable Cost Explorer, you automatically get Amazon EC2, Amazon RDS, ElastiCache, OpenSearch Service, Amazon Redshift, and Amazon MemoryDB Reserved Instance (RI) purchase recommendations that could help you reduce your costs. Learn how to use those recommendations.

   [Explore the guide ](https://docs.aws.amazon.com/cost-management/latest/userguide/ri-recommendations.html)

------
#### [ Savings Plans ]
+  **Getting started with Savings Plans**

  Learn how to get started with optimizing your AWS costs with Savings Plans.

   [Explore the guide ](https://docs.aws.amazon.com/savingsplans/latest/userguide/get-started.html)
+  **Developing a compute Savings Plans**

  Explore the overview of Savings Plans for Amazon EC2, AWS Fargate, and AWS Lambda.

   [Explore the guide](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/savings-plans.html)
+  **Savings Plans FAQs**

  Get answers to frequently asked questions about Savings Plans.

   [Explore the FAQs ](https://aws.amazon.com/savingsplans/faq/)
+  **Announcing Savings Plans Purchase Analyzer**

  Model Savings Plans purchases and evaluate the impact on cost, coverage, and utilization in the AWS Billing and Cost Management AWS Billing and Cost Management Console.

   [Read the blog ](https://aws.amazon.com/blogs/aws-cloud-financial-management/announcing-savings-plans-purchase-analyzer/)

------
#### [ Amazon EC2 Spot Instances ]
+  **Getting started with EC2 Spot Instances **

  Learn how to get started with optimizing your AWS costs with Amazon EC2 Spot Instances.

   [Explore the guide ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
+  **Best practices for EC2 Spot Instances**

  Learn the best practices for utilizing Amazon EC2 Spot Instances to save up to 90% over on-demand instances.

   [Explore the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html)
+  **Spot Instance pricing history**

  Learn how pricing history works and see links to the latest pricing options.

   [Explore the guide ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances-history.html)

------
#### [ S3 Intelligent Tiering ]
+  **How S3 Intelligent-Tiering works**

  Dive deeper into how Amazon S3 Intelligent-Tiering works.

   [Explore the guide ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html)
+  **Using S3 Intelligent-Tiering**

  Learn how to move data to Amazon S3 Inteligent-Tiering.

   [Explore the guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-intelligent-tiering.html)

------

## Explore AWS cost management resources
<a name="explore"></a>
+ **Patterns**

  Explore patterns to help you develop your AWS cost management strategy.

  [ Explore patterns](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23pattern&awsf.methodology=*all&awsf.tech-category=*all&awsf.industries=*all&awsf.business-category=*all&cards-all.q=cost&cards-all.q_operator=AND)
+ **Whitepapers**

  Explore whitepapers to help you get started in developing your cost management strategy.

  [Explore whitepapers ](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=*all&awsf.industries=*all&awsf.business-category=*all&cards-all.q=cost&cards-all.q_operator=AND)
+ **AWS Solutions**

  Explore vetted solutions and architectural guidance for common cost control and management use cases.

  [Explore solutions](https://aws.amazon.com/solutions/cloud-operations/cost-control-management/)
