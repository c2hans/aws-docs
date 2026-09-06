---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-cost-optimization/cost-optimization-services.html
---

# Cost optimization services
<a name="cost-optimization-services"></a>

This section reviews some of the following AWS services and tools, which can provide insights and assist in the cost optimization process:
+ [AWS Cost Explorer](#aws-cost-explorer)
+ [AWS Trusted Advisor](#aws-trusted-advisor)
+ [AWS Compute Optimizer](#aws-compute-optimizer)
+ [AWS Config](#aws-config)

|
|
| Important These AWS services might make recommendations to optimize your costs. However, these recommendations might not be compatible with operating SAP workloads. Before acting, confirm that the recommendations are compatible with operating SAP on AWS:+ [SAP Applications on AWS: Supported DB/OS and AWS EC2 products – 1656099](https://launchpad.support.sap.com/#/notes/1656099) (SAP note)<br />+ [SAP on AWS: Support prerequisites - 1656250](https://launchpad.support.sap.com/#/notes/1656250) (SAP note) |
| --- |

## AWS Cost Explorer
<a name="aws-cost-explorer"></a>

[AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) is a tool in the AWS Cost Management service. It helps you visualize your costs and usage associated with AWS services. The tool provides a default report that displays your top-five cost-accruing AWS services. This report is an excellent place to start your cost optimization efforts.

As part of your cost optimization strategy, this tool provides the necessary information to identify which services you should target in order to optimize the associated costs. You should regularly use and monitor this tool to identify cost optimization opportunities and monitor the cost-related effects of changes in your environment.

## AWS Trusted Advisor
<a name="aws-trusted-advisor"></a>

[AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) provides recommendations that help you adhere to best practices and reduce your costs for AWS services. Confirm that Trusted Advisor recommendations are compatible with SAP environments. You should regularly use Trusted Advisor for recommendations about how to reduce costs and remain compliant with best practices.

## AWS Compute Optimizer
<a name="aws-compute-optimizer"></a>

[AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) uses actual usage data to make recommendations about how to balance performance and cost. Over-provisioning resources leads to unnecessary infrastructure costs, and under-provisioning resources leads to potential performance problems. As part of your cost optimization strategy, this service helps you analyze whether your AWS resources, such as Amazon Elastic Compute Cloud (Amazon EC2) instances, are over or under-provisioned. Use this service when you're optimizing costs for EC2 instances, Amazon EC2 Auto Scaling groups, Amazon Elastic Block Store (Amazon EBS) volumes, or AWS Lambda functions.

Recommendations from Compute Optimizer must be cross-referenced with SAP support documents. For example, if you have a large, over-provisioned EC2 instance in your account, Cost Optimizer might recommend changing to a smaller instance type. Confirm that SAP supports the instance type recommended by Cost Optimizer. If it isn't supported, you should still consider changing the type to optimize cost. However, you need to select a different type that SAP supports. For more information about the available instance types, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) (Amazon EC2 documentation).

## AWS Config
<a name="aws-config"></a>

[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) continuously monitors your AWS resources and provides a detailed view of how the AWS resources in your account are configured. AWS Config can take specific actions based on evaluated findings. Although this service isn't directly related to cost, it does provide an automated solution for checking that your SAP environment is compliant. You can use existing rules or create custom rules to set up alerts. For example, you can configure automated alerts if an EC2 instance type is changed or if an EBS volume is detached. You can also customize the rules to automate remediation and bring the resource back into compliance. For more information about using AWS Config for SAP environments, see [part I](https://aws.amazon.com/blogs/awsforsap/audit-your-sap-systems-with-aws-config-part-i/) and [part II](https://aws.amazon.com/blogs/awsforsap/audit-your-sap-systems-with-aws-config-part-ii/) of *Audit your SAP systems with AWS Config* (AWS blog posts).

Consider using this service for automatic detection of cost-related scenarios associated with changes to AWS resources.
