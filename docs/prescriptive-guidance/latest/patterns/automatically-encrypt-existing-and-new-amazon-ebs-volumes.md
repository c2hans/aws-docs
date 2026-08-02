---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-encrypt-existing-and-new-amazon-ebs-volumes.html
---

# Automatically encrypt existing and new Amazon EBS volumes
<a name="automatically-encrypt-existing-and-new-amazon-ebs-volumes"></a>

*Tony DeMarco and Josh Joy, Amazon Web Services*

## Summary
<a name="automatically-encrypt-existing-and-new-amazon-ebs-volumes-summary"></a>

Encryption of Amazon Elastic Block Store (Amazon EBS) volumes is important to an organization's data protection strategy. It is an important step in establishing a well-architected environment. Although there is no direct way to encrypt existing unencrypted EBS volumes or snapshots, you can encrypt them by creating a new volume or snapshot. For more information, see [Encrypt EBS resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-parameters) in the Amazon EC2 documentation. This pattern provides preventative and detective controls for encrypting your EBS volumes, both new and existing. In this pattern, you configure account settings, create automated remediation processes, and implement access controls.

## Prerequisites and limitations
<a name="automatically-encrypt-existing-and-new-amazon-ebs-volumes-prereqs"></a>

**Prerequisites**
+ An active Amazon Web Services (AWS) account
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), installed and configured on macOS, Linux, or Windows
+ [jq](https://stedolan.github.io/jq/download/), installed and configured on macOS, Linux, or Windows
+ AWS Identity and Access Management (IAM) permissions are provisioned to have read and write access to AWS CloudFormation, Amazon Elastic Compute Cloud (Amazon EC2), AWS Systems Manager, AWS Config, and AWS Key Management Service (AWS KMS)
+ AWS Organizations is configured with all features enabled, a requirement for service control policies
+ AWS Config is enabled in the target accounts

**Limitations**
+ In your target AWS account, there must be no AWS Config rules named **encrypted-volumes**. This solution deploys a rule with this name. Preexisting rules with this name can cause the deployment to fail and result in unnecessary charges related to processing the same rule more than once.
+ This solution encrypts all EBS volumes with the same AWS KMS key.
+ If you enable encryption of EBS volumes for the account, this setting is Region-specific. If you enable it for an AWS Region, you cannot disable it for individual volumes or snapshots in that Region. For more information, see [Encryption by default](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default) in the Amazon EC2 documentation.
+ When you remediate existing, unencrypted EBS volumes, ensure that the EC2 instance is not in use. This automation shuts down the instance in order to detach the unencrypted volume and attach the encrypted one. There is downtime while the remediation is in progress. If this is a critical piece of infrastructure for your organization, make sure that [manual](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/scenarios-enis.html#create-a-low-budget-high-availability-solution) or [automatic](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) high-availability configurations are in place so as to not impact the availability of any applications running on the instance. We recommend that you remediate critical resources only during standard maintenance windows.

## Architecture
<a name="automatically-encrypt-existing-and-new-amazon-ebs-volumes-architecture"></a>

**Automation workflow**

![High-level architecture diagram showing the automation process and services](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/484fd5fe-e10a-41f6-aafe-260ea824883b/images/483f551c-ca1d-4c1e-b3c7-989df7d3b059.png)

1. AWS Config detects an unencrypted EBS volume.

1. An administrator uses AWS Config to send a remediation command to Systems Manager.

1. The Systems Manager automation takes a snapshot of the unencrypted EBS volume.

1. The Systems Manager automation uses AWS KMS to create an encrypted copy of the snapshot.

1. The Systems Manager automation does the following:

   1. Stops the affected EC2 instance if it is running

   1. Attaches the new, encrypted copy of the volume to the EC2 instance

   1. Returns the EC2 instance to its original state

## Tools
<a name="automatically-encrypt-existing-and-new-amazon-ebs-volumes-tools"></a>

**AWS services**
+ [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) – The AWS Command Line Interface (AWS CLI) provides direct access to the public application programming interfaces (APIs) of AWS services. You can explore a service's capabilities with the AWS CLI and develop shell scripts to manage your resources. In addition to the low-level API-equivalent commands, several AWS services provide customizations for the AWS CLI. Customizations can include higher-level commands that simplify using a service with a complex API.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) – AWS CloudFormation is a service that helps you model and set up your AWS resources. You create a template that describes all the AWS resources that you want (such as Amazon EC2 instances), and CloudFormation provisions and configures those resources for you.
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) – AWS Config provides a detailed view of the configuration of AWS resources in your AWS account. This includes how the resources are related to one another and how they were configured in the past so that you can see how the configurations and relationships change over time.
+ [Amazon EC2](https://docs.aws.amazon.com/ec2/?id=docs_gateway) – Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable computing capacity that you use to build and host your software systems.
+ [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) – AWS Key Management Service (AWS KMS) is an encryption and key management service scaled for the cloud. AWS KMS keys and functionality are used by other AWS services, and you can use them to protect data in your AWS environment.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) – AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) – Systems Manager Automation simplifies common maintenance and deployment tasks for Amazon EC2 instances and other AWS resources.

**Other services**
+ [jq](https://stedolan.github.io/jq/download/) – jq is a lightweight and flexible command-line JSON processor. You use this tool to extract key information from the AWS CLI output.

**Code**
+ The code for this pattern is available in the GitHub [Automatically remediate unencrypted EBS Volumes using customer KMS keys](https://github.com/aws-samples/aws-system-manager-automation-unencrypted-to-encrypted-resources/tree/main/ebs) repository.

## Epics
<a name="automatically-encrypt-existing-and-new-amazon-ebs-volumes-epics"></a>

### Automate remediation of unencrypted volumes
<a name="automate-remediation-of-unencrypted-volumes"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download scripts and CloudFormation templates. | Download the shell script, JSON file, and CloudFormation templates from the GitHub [Automatically remediate unencrypted EBS Volumes using customer KMS keys ](https://github.com/aws-samples/aws-system-manager-automation-unencrypted-to-encrypted-resources/tree/main/ebs)repository. | AWS administrator, General AWS |
| Identify the administrator for the AWS KMS key. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-encrypt-existing-and-new-amazon-ebs-volumes.html) | AWS administrator, General AWS |
| Deploy the Stack1 CloudFormation template. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-encrypt-existing-and-new-amazon-ebs-volumes.html)For more information about deploying a CloudFormation template, see [Working with AWS CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) in the CloudFormation documentation. | AWS administrator, General AWS |
| Deploy the Stack2 CloudFormation template. | In CloudFormation, deploy the `Stack2.yaml` template. Note the following deployment details:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-encrypt-existing-and-new-amazon-ebs-volumes.html) | AWS administrator, General AWS |
| Create an unencrypted volume for testing. | Create an EC2 instance with an unencrypted EBS volume. For instructions, see [Create an Amazon EBS volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-volume.html) in the Amazon EC2 documentation. The instance type does not matter, and access to the instance is not needed. You can create a t2.micro instance to stay in the free tier, and you don’t need to create a key pair. | AWS administrator, General AWS |
| Test the AWS Config rule. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-encrypt-existing-and-new-amazon-ebs-volumes.html)You can view the remediation progress and status in Systems Manager as follows:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-encrypt-existing-and-new-amazon-ebs-volumes.html) | AWS administrator, General AWS |
| Configure additional accounts or AWS Regions. | As needed for your use case, repeat this epic for any additional accounts or AWS Regions. | AWS administrator, General AWS |

### Enable account-level encryption of EBS volumes
<a name="enable-account-level-encryption-of-ebs-volumes"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the enable script. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-encrypt-existing-and-new-amazon-ebs-volumes.html) | AWS administrator, General AWS, bash |
| Confirm the settings are updated. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-encrypt-existing-and-new-amazon-ebs-volumes.html) | AWS administrator, General AWS |
| Configure additional accounts or AWS Regions. | As needed for your use case, repeat this epic for any additional accounts or AWS Regions. | AWS administrator, General AWS |

### Prevent creation of unencrypted instances
<a name="prevent-creation-of-unencrypted-instances"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a service control policy. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-encrypt-existing-and-new-amazon-ebs-volumes.html) | AWS administrator, General AWS |

## Related resources
<a name="automatically-encrypt-existing-and-new-amazon-ebs-volumes-resources"></a>

**AWS service documentation**
+ [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [Amazon EC2](https://docs.aws.amazon.com/ec2/?id=docs_gateway)
+ [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
+ [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)

**Other resources**
+ [jq manual](https://stedolan.github.io/jq/manual/) (jq website)
+ [jq download](https://github.com/stedolan/jq) (GitHub)
