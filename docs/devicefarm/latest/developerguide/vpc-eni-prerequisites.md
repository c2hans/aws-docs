---
source_url: https://docs.aws.amazon.com/devicefarm/latest/developerguide/vpc-eni-prerequisites.html
---

# Prerequisites
<a name="vpc-eni-prerequisites"></a>

The following list describes some requirements and suggestions to review when creating VPC-ENI configurations:
+ Private devices must be assigned to your AWS Account.
+ You must have an AWS account user or role with permissions to create a Service-linked role. When using Amazon VPC endpoints with Device Farm mobile testing features, Device Farm creates an AWS Identity and Access Management (IAM) service-linked role.
+ Device Farm can connect to VPCs only in the `us-west-2` Region. If you don't have a VPC in the `us-west-2` Region, you need to create one. Then, to access resources in a VPC in another Region, you must establish a peering connection between the VPC in the `us-west-2` Region and the VPC in the other Region. For information on peering VPCs, see the [Amazon VPC Peering Guide](https://docs.aws.amazon.com/vpc/latest/peering/).

  You should verify that you have access to your specified VPC when you configure the connection. You must configure certain Amazon Elastic Compute Cloud (Amazon EC2) permissions for Device Farm.
+ DNS resolution is required in the VPC that you use.
+ Once your VPC has been created, you will need the following information about the VPC in the `us-west-2` Region:
  + VPC ID
  + Subnet IDs (private subnets only)
  + Security group IDs
+ You must configure Amazon VPC connections on a per-project basis. At this time, you can configure only one VPC configuration per project. When you configure a VPC, Amazon VPC creates an interface within your VPC and assigns it to the specified subnets and security groups. All future sessions associated with the project will use the configured VPC connection.
+ You cannot use VPC-ENI configurations along with the legacy VPCE feature.
+ We strongly recommend **not updating an existing project** with a VPC-ENI configuration as existing projects may have VPCE settings that persist on the run level. Instead, if you already use the existing VPCE features, use VPC-ENI for all new projects.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
