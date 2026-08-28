---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-ec2fastlaunch.html
---

# Using EC2 Fast Launch with Windows platform branches
<a name="dotnet-ec2fastlaunch"></a>

The EC2 Fast Launch feature reduces Windows instance launch times in your Elastic Beanstalk environments. The purpose of this topic is to guide you on using this feature with your Elastic Beanstalk environments. Starting with Windows platform version 2.16.2, released on [January 22, 2025](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2025-01-22-windows.html), Elastic Beanstalk platform releases include base AMIs with EC2 Fast Launch enabled.

## Default EC2 Fast Launch availability
<a name="dotnet-ec2fastlaunch-default"></a>

The latest Elastic Beanstalk Windows platform versions include base AMIs with EC2 Fast Launch automatically enabled, with no additional costs. However, when newer platform versions are released, EC2 Fast Launch may not remain automatically enabled on base AMIs from older platform versions.

We recommend upgrading to the latest Windows platform version to use base AMIs with EC2 Fast Launch automatically enabled. However, if you need to continue using your existing platform version, you can manually enable EC2 Fast Launch on your environment's base AMI. For instructions, see [Manually configuring EC2 Fast Launch](#dotnet-ec2fastlaunch-manual).

## Manually configuring EC2 Fast Launch
<a name="dotnet-ec2fastlaunch-manual"></a>

**Note**
Manually enabling EC2 Fast Launch may incur additional costs compared to using platform versions with EC2 Fast Launch automatically enabled. For more information about EC2 Fast Launch costs, see the [Manage costs for EC2 Fast Launch underlying resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-fast-launch-manage-costs.html) page in the *Amazon EC2 User Guide*.

Follow these steps to enable EC2 Fast Launch on a Windows base AMI used by your Elastic Beanstalk environment:

**To manually enable EC2 Fast Launch for your Elastic Beanstalk environment**

1. Identify your environment's base AMI:

   Follow the steps in [Creating a Custom AMI](using-features.customenv.md) to identify your environment's base AMI ID. Note that you don't need to create a custom AMI - you only need to follow the steps to locate your current base AMI ID.

1. Enable EC2 Fast Launch on the AMI:

   Use the instructions in [Enable EC2 Fast Launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-fast-launch-configure.html) in the *Amazon EC2 User Guide* to configure EC2 Fast Launch for your AMI.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
