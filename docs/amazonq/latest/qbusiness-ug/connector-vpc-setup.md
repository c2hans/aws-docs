---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-vpc-setup.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Set up an Amazon Q Business data source to connect to Amazon VPC
<a name="connector-vpc-setup"></a>

When you add a new data source in Amazon Q Business, you can use the Amazon VPC feature if the selected data source connector supports this feature.

You can set up a new Amazon Q Business data source with Amazon VPC enabled by using the AWS Management Console or the Amazon Q Business API. Specifically, use the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) API operation, and then use the `VpcConfiguration` parameter to provide the following information:
+ `SubnetIds` – A list of identifiers of Amazon VPC subnets
+ `SecurityGroupIds` – A list of identifiers of Amazon VPC security groups

If you use the console, you provide the required Amazon VPC information during connector configuration. To use the console to enable the Amazon VPC feature for a connector, you first choose an Amazon VPC. Then, you provide identifiers of any Amazon VPC subnets and identifiers of any Amazon VPC security groups. You can choose the Amazon VPC subnets and Amazon VPC security groups that you created in [Configuring Amazon VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-vpc-steps.html), or use any existing ones.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
