---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_efa.html
---

# Using Elastic Fabric Adapter (EFA) with AWS PCS
<a name="working-with_networking_efa"></a>

 Elastic Fabric Adapter (EFA) is a high performance advanced networking interconnect from AWS that you can attach to your EC2 instance to accelerate High Performance Computing (HPC) and machine learning applications. Enabling your applications running on an AWS PCS cluster with EFA involves configuring the AWS PCS compute node group instances to use EFA as follows.

**Note**
**Install EFA on an AWS PCS-compatible AMI** – The AMI used in the AWS PCS compute node group must have the EFA driver installed and loaded. For information on how to build a custom AMI with EFA software installed, see [Custom Amazon Machine Images (AMIs) for AWS PCS](working-with_ami_custom.md).

**Contents**
+ [Identify EFA-enabled EC2 instances](working-with_networking_efa_identify-instances.md)
+ [Create a security group to support EFA communications](working-with_networking_efa_create-sg.md)
+ [(Optional) Create a placement group](working-with_networking_efa_create-placement-group.md)
+ [Create or update an EC2 launch template](working-with_networking_efa_create-lt.md)
+ [Create or update compute node groups for EFA](working-with_networking_efa_create-cng.md)
+ [(Optional) Test EFA](working-with_networking_efa_test-efa.md)
+ [(Optional) Use a CloudFormation template to create an EFA-enabled launch template](working-with_networking_efa_create-lt-cfn.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
