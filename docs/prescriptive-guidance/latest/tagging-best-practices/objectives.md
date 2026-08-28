---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tagging-best-practices/objectives.html
---

# Objectives
<a name="objectives"></a>

Use tagging to realize the following business outcomes.

## Achieve more detailed cost tracking
<a name="cost-tracking"></a>

In the cost management dashboard, you can segment your costs according to resource types, AWS account, AWS Region, and other factors. However, business context isn't included. For example, the dashboard won't tell you which department owes how much money, or whether the data pipeline costs more than the machine learning pipeline. The answers to these questions can be obtained only by adding business context in the form of tags. You can then use the tags to filter the cost management dashboard.

### Tagging for tracking costs
<a name="tagging-for-tracking-costs.671cd9f4-7913-5fdc-8680-a0664218fbd3"></a>

To use tags for billing purposes, [select cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html), which will be activated within 24 hours. Then you can choose these tags as a filter for the chart, or you can download a report. For more information and an example report, see the [AWS Billing documentation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/configurecostallocreport.html#allocation-viewing).

## Generate more accurate reports
<a name="reporting"></a>

Reports of usage, costs, and resources are often required by higher management and audit organizations. These reports require intrinsic knowledge about how each component in a technical application maps to the business use case or department. Tagging can provide that knowledge.

With tagging implemented, you can use filters in AWS Cost Explorer to distinguish between the different values. This provides you with more efficient and accurate reporting or monitoring options.
+ **Department or Program** – Department name (for example, D72, IT, or Operations)

  In the case of consolidated billing or when one AWS account is used for multiple departments, this value can be filtered to find the costs for each department accurately.
+ **Project** – Project name (for example, Sales Forecasting, Hiring Forecast)

  In the case of consolidated billing or when one AWS account is used for multiple projects, this value can be filtered to find the costs for each project accurately.
+ **Phase** – Phase or status name (for example, Dev, Test)

  A project has different phases, such as development, testing, bug fixing, and reporting. By adding this tag, you can filter costs or performance for each phase of the project. This helps to plan the next iteration of the project more accurately.
+ **Process** – Process name (for example, Data Ingestion, Data Cleaning/processing, Machine Learning, Modeling)

  Using this information, you can distinguish between cost, time, or performance for each process. For example, if you find that data cleaning has very high runtimes or costs, you can optimize the data source should to reduce costs and improve performance.

## Speed up cleanup
<a name="cleanup"></a>

Annual cleanup is required to maintain costs and make sure that resources no longer needed for testing, proof of concepts (PoCs), and development are removed. Without the right tags, it's difficult to distinguish between resources used in production or in the latest development version.

With all production components tagged in an application, you can decide to delete or retain a component based on whether it has tags. For example, an AWS Lambda function with zero tags that has not been run in a long time was probably created for development or a quick test by one of the team members. If tagging is fully automated by using infrastructure as code, all components from production will have a tag associated with them, such as `key:environment` and `value:prod`.

## Manage permissions efficiently
<a name="permissions"></a>

Without tagging, assigning AWS Identity and Access Management (IAM) roles to AWS services in an application requires creating roles individually for each service and instance. This can be time consuming, because there might be several services that require the same IAM actions throughout the application.

You can assign permissions more efficiently by creating tags based on [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) (or based on AWS CloudFormation stacks). You can assign the IAM permissions to a broader group to allow or restrict access. In the following excerpt of an IAM policy that allows certain actions on a group of resources, you are simplifying your IAM policy.

```
"Action": [
      "resource-groups:List*",
      "resource-groups:action2",
      "resource-explorer:action3"
]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
