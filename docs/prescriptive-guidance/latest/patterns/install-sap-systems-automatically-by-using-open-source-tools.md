---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/install-sap-systems-automatically-by-using-open-source-tools.html
---

# Install SAP systems automatically by using open-source tools
<a name="install-sap-systems-automatically-by-using-open-source-tools"></a>

*Guilherme Sesterheim, Amazon Web Services*

## Summary
<a name="install-sap-systems-automatically-by-using-open-source-tools-summary"></a>

This pattern shows how to automate SAP systems installation by using open-source tools to create the following resources:
+ An SAP S/4HANA 1909 database
+ An SAP ABAP Central Services (ASCS) instance
+ An SAP Primary Application Server (PAS) instance

HashiCorp Terraform creates the SAP system’s infrastructure and Ansible configures the operating system (OS) and installs SAP applications. Jenkins runs the installation.

This setup turns SAP systems installation into a repeatable process, which can help increase deployment efficiency and quality.

**Note**
The example code provided in this pattern works for both high-availability (HA) systems and non-HA systems.

## Prerequisites and limitations
<a name="install-sap-systems-automatically-by-using-open-source-tools-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An Amazon Simple Storage Service (Amazon S3) bucket that contains all of your SAP media files
+ An AWS Identity and Access Management (IAM) principal with an [access key and secret key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), and that has the following permissions:
  + **Read only permissions:** Amazon Route 53, AWS Key Management Service (AWS KMS)
  + **Read and write permissions:** Amazon S3, Amazon Elastic Compute Cloud (Amazon EC2), Amazon Elastic File System (Amazon EFS), IAM, Amazon CloudWatch, Amazon DynamoDB
+ A Route 53 [private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html)
+ A subscription to the [Red Hat Enterprise Linux for SAP with HA and Update Services 8.2](https://aws.amazon.com/marketplace/pp/prodview-5grz5a5thx7c2) Amazon Machine Image (AMI) in Amazon Marketplace
+ An [AWS KMS customer managed key](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html#aws-managed-customer-managed-keys)
+ A [Secure Shell (SSH) key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)
+ An [Amazon EC2 security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) that allows SSH connection on port 22 from the hostname where you install Jenkins (the hostname is most likely **localhost**)
+ [Vagrant](https://www.vagrantup.com/) by HashiCorp installed and configured
+ [VirtualBox](https://www.virtualbox.org/) by Oracle installed and configured
+ Familiarity with Git, Terraform, Ansible, and Jenkins

**Limitations**
+ Only SAP S/4HANA 1909 is fully tested for this specific scenario. The example Ansible code in this pattern requires modification if you use another version of SAP HANA.
+ The example procedure in this pattern works for Mac OS and Linux operating systems. Some of the commands can be run only in Unix-based terminals. However, you can achieve a similar result by using different commands and a Windows OS.

**Product versions**
+ SAP S/4HANA 1909
+ Red Hat Enterprise Linux (RHEL) 8.2 or higher versions

## Architecture
<a name="install-sap-systems-automatically-by-using-open-source-tools-architecture"></a>

The following diagram shows an example workflow that uses open-source tools to automate SAP systems installation in an AWS account:

![Example workflow uses open-source tools to automate SAP systems installation in an AWS account.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/aaf11dac-38cc-4e89-be86-51d4409cf238/images/d7902f9d-f1be-461f-b69b-cf3c663c8f2f.png)

The diagram shows the following workflow:

1. Jenkins orchestrates running the SAP system installation by running Terraform and Ansible code.

1. Terraform code builds the SAP system’s infrastructure.

1. Ansible code configures the OS and installs SAP applications.

1. An SAP S/4HANA 1909 database, an ASCS instance, and PAS instance that include all defined prerequisites are installed on an Amazon EC2 instance.

**Note**
The example setup in this pattern automatically creates an Amazon S3 bucket in your AWS account to store the Terraform state file.

**Technology stack**
+ Terraform
+ Ansible
+ Jenkins
+ An SAP S/4HANA 1909 database
+ An SAP ASCS instance
+ An SAP PAS instance
+ Amazon EC2

## Tools
<a name="install-sap-systems-automatically-by-using-open-source-tools-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/?id=docs_gateway) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need, and quickly scale them up or down.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS) ](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)helps you create and control cryptographic keys to protect your data.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**Other tools**
+ [HashiCorp Terraform](https://www.terraform.io/docs) is a command-line interface application that helps you use code to provision and manage cloud infrastructure and resources.
+ [Ansible](https://www.ansible.com/) is an open-source configuration as code (CaC) tool that helps automate applications, configurations, and IT infrastructure.
+ [Jenkins](https://www.jenkins.io/) is an open-source automation server that enables developers to build, test, and deploy their software.

**Code**

The code for this pattern is available in the GitHub [aws-install-sap-with-jenkins-ansible](https://github.com/aws-samples/aws-install-sap-with-jenkins-ansible) repository.

## Epics
<a name="install-sap-systems-automatically-by-using-open-source-tools-epics"></a>

### Configure the prerequisites
<a name="configure-the-prerequisites"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add your SAP media files to an Amazon S3 bucket. | [Create an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) that contains all of your SAP media files.Make sure that you follow the AWS Launch Wizard’s folder hierarchy for **S/4HANA** in the [Launch Wizard documentation](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-software-install-details.html). | Cloud administrator |
| Install VirtualBox. | Install and configure [VirtualBox](https://www.virtualbox.org/) by Oracle. | DevOps engineer |
| Install Vagrant. | Install and configure [Vagrant](https://www.vagrantup.com/) by HashiCorp. | DevOps engineer |
| Configure your AWS account. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/install-sap-systems-automatically-by-using-open-source-tools.html) | General AWS |

### Build and run your SAP installation
<a name="build-and-run-your-sap-installation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the code repository from GitHub. | Clone the [aws-install-sap-with-jenkins-ansible](https://github.com/aws-samples/aws-install-sap-with-jenkins-ansible) repository on GitHub. | DevOps engineer |
| Start the Jenkins service. | Open the Linux terminal. Then, navigate to the local folder that contains the cloned code repository folder and run the following command:<pre>sudo vagrant up</pre>The Jenkins startup takes about 20 minutes. The command returns a **Service is up and running** message when successful. | DevOps engineer |
| Open Jenkins in a web browser and log in. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/install-sap-systems-automatically-by-using-open-source-tools.html) | DevOps engineer |
| Configure your SAP system installation parameters. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/install-sap-systems-automatically-by-using-open-source-tools.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/install-sap-systems-automatically-by-using-open-source-tools.html)You can configure the other nonrequired parameters as needed, based on your use case. For example, you can change the SAP system ID (SID) of the instances, default password, names, and tags for your SAP system. All of the required variables have **(Required)** at the beginning of their names. | AWS systems administrator, DevOps engineer |
| Run you SAP system installation. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/install-sap-systems-automatically-by-using-open-source-tools.html)For information on the pipeline steps, see the **Understanding the pipeline steps** section of [Automating SAP installation with open-source tools](https://aws.amazon.com/blogs/awsforsap/automating-sap-installation-with-open-source-tools/) on the AWS Blog.If an error occurs, move your cursor over the red error box that appears and choose **Logs**. The logs for the pipeline step that errored out appear. Most errors occur because of incorrect parameter settings. | DevOps engineer, AWS systems administrator |

## Related resources
<a name="install-sap-systems-automatically-by-using-open-source-tools-resources"></a>
+ [DevOps for SAP – SAP Installation: From 2 Months to 2 Hours](https://videos.itrevolution.com/watch/707351918/) (DevOps Enterprise Summit Video Library)
