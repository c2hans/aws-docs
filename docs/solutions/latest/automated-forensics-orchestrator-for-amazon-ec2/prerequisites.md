---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/prerequisites.html
---

# Prerequisites
<a name="prerequisites"></a>

## Tools
<a name="tools"></a>
+ The latest version of the [AWS CLI](https://aws.amazon.com/cli/) (2.2.37 or newer), installed and configured.
+ The latest version of the [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/home.html) V2 (2.2 or newer).
+ A [CDK bootstrapped](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html) forensic AWS account and Security Hub account.
+  [NodeJS](https://docs.npmjs.com/getting-started) version 16.
+ Ensure GraphQL - AppSync is activated in the forensic AWS account.
+  [AWS SSM agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) is installed in EC2 instances or EKS clusters (Application Instances).
+ AWS Security Hub must be activated as the Guidance creates custom action in AWS Security Hub.
+ Python version 3.8 or above

## Forensic AMI
<a name="forensic-ami"></a>

Build a forensic AMI and update the AWS Systems Manager Parameter Store with AMI ID. For more details, refer to [Sample steps to create Forensic AMI using EC2 Image Builder](https://github.com/aws-samples/amazon-ec2-image-builder-samples/tree/master/CDK/Linux/hello-world). Be sure to replace the image builder component yml with the sample `san-sift.yml` provided in the forensic Guidance.

**Note**
This Guidance requires knowledge of [SAN SIFT](https://www.sans.org/tools/sift-workstation/), [LiME](https://github.com/504ensicsLabs/LiME) and Volatility tools to customize deployment the Guidance based on your forensic requirements. For more information, refer to the [Post deployment: Plugin points](post-deployment-plugin-points.md) section.

## Compromised instance memory size and investigation instance mount disk volume
<a name="compromised-instance-memory-size-and-investigation-instance-mount-disk-volume"></a>

The investigation instance mount volume must always be greater than the memory of the compromised instance. This ensures that memory loaded into investigation instance does not error out. The Guidance uses `M5.2Xlarge` Amazon EC2 instance type by default.

## CDK context configurations
<a name="cdk-context-configurations"></a>

| CDK config | Description |
| --- | --- |
|  **ec2ForensicImage**  | Forensic AMI name stored in SSM Parameter Store. SSM Parameter Store will contain AMI ID of forensic investigation instance prebuilt with forensic tools. Guidance is tested with Ubuntu AMI. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Forensics Orchestrator for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
