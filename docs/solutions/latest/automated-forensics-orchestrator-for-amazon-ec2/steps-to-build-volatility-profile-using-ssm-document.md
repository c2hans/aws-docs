---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/steps-to-build-volatility-profile-using-ssm-document.html
---

# Steps to build LiME module and volatility profile using SSM document
<a name="steps-to-build-volatility-profile-using-ssm-document"></a>

The below diagram explains the overall architecture of building volatility profile.

 **steps to build volatility profile using SSM document**

![volatility profile using ssm](http://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/images/volatility-profile-using-ssm.png)

The diagram below details the usage of a Volatility profile in the memory investigation flow.

**usage of a volatility profile in the memory investigation flow**
image::images/volatility-profile-using-ssm-flow.png[scaledwidth=100%]. Launch an [Amazon EC2](https://aws.amazon.com/ec2/) instance (Amazon Linux 2) to build a LiME module volatility profile. Ensure the SSM is appropriately configured on the EC2 instance or EKS cluster. Record the instance ID. . Navigate to the AWS Systems Manager documents and select the previously created SSM document example **Documents** tab. Record the name of the SSM document to build the profile.

\+ .SSM document image::images/ssm-document.png[scaledwidth=100%] Run AWS SSM document to build LiME module and Volatility 3 symbol tables for a launched Amazon EC2 instance or EKS cluster that matches the OS and kernel version.

\+ NOTE: Currently the profile and tools are loaded into the S3 bucket for Amazon Linux EC2 instance. For other operating systems, modify the SSM document to create Volatility profiles.

## Automate the creation of LiME and Volatility 3 symbol tables
<a name="automate-creation-of-lime-and-volatility-profiles"></a>

You can incorporate the module build process for LiME and Volatility (or your preferred forensic tools) into a hardened AMI pipeline prior to allowing AMI use by developers and application teams. These modules are prerequisites for running the Automated Forensics Orchestrator for Amazon EC2 and EKS Guidance to allow the capture and analysis of volatile memory. You also need to incorporate a mechanism to build these modules for the specific kernel versions in the event they do not exist. This can occur if an EC2 instance or EKS cluster is updated after being launched or if an EC2 instance or EKS cluster was launched from a non-hardened AMI that is not managed by a central team.

For more information, refer to the [How to automatically build forensic kernel modules for Amazon Linux EC2 instances](https://aws.amazon.com/blogs/security/how-to-automatically-build-forensic-kernel-modules-for-amazon-linux-ec2-instances/) blog, which will walk you through deploying a Guidance to automatically build modules for specific EC2 instance or EKS cluster OS kernel versions based on input parameters of AMI ID and kernel version. You can use the blog Guidance with the Automated Forensics Orchestrator for Amazon EC2 and EKS Guidance in the event that specific kernel module versions are missing and need to be created.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Forensics Orchestrator for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
