---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Working with public parameters in Parameter Store
<a name="parameter-store-public-parameters"></a>

Some AWS services publish information about common artifacts as AWS Systems Manager *public* parameters. For example, the Amazon Elastic Compute Cloud (Amazon EC2) service publishes information about Amazon Machine Images (AMIs) as public parameters.

**Topics**
+ [Discovering public parameters in Parameter Store](parameter-store-finding-public-parameters.md)
+ [Calling AMI public parameters in Parameter Store](parameter-store-public-parameters-ami.md)
+ [Calling the ECS optimized AMI public parameter in Parameter Store](parameter-store-public-parameters-ecs.md)
+ [Calling the EKS optimized AMI public parameter in Parameter Store](parameter-store-public-parameters-eks.md)
+ [Calling public parameters for AWS services, Regions, endpoints, Availability Zones, local zones, and Wavelength Zones in Parameter Store](parameter-store-public-parameters-global-infrastructure.md)

**Related AWS blog posts**
+ [Query for AWS Regions, Endpoints, and More Using AWS Systems Manager Parameter Store](https://aws.amazon.com/blogs/aws/new-query-for-aws-regions-endpoints-and-more-using-aws-systems-manager-parameter-store/)
+ [Query for the latest Amazon Linux AMI IDs using AWS Systems Manager Parameter Store](https://aws.amazon.com/blogs/compute/query-for-the-latest-amazon-linux-ami-ids-using-aws-systems-manager-parameter-store/)
+ [Query for the Latest Windows AMI Using AWS Systems Manager Parameter Store](https://aws.amazon.com/blogs/mt/query-for-the-latest-windows-ami-using-systems-manager-parameter-store/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
