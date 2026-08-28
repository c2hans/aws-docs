---
source_url: https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Management
<a name="management"></a>

## Automation
<a name="automation"></a>

 Oracle database creation and deployment can be automated using AWS CloudFormation templates.

## Oracle AMIs
<a name="oracle-amis"></a>

 An Amazon Machine Image (AMI) provides the information required to launch an instance, which is a virtual server in the cloud. You specify an AMI when you launch an instance, and you can launch as many instances from an AMI as you require.

 Oracle periodically provides official AMIs for some Oracle products on AWS, including Oracle Database. However, Oracle-provided database AMIs that are available might not always be the latest version. Oracle-supplied AMIs are based on the Oracle Linux operating system.

 You are not required to use an Oracle-provided AMI to install and use Oracle Database on Amazon EC2. You can start an Amazon EC2 instance with an operating system AMI, and then download and install Oracle Database software from the Oracle website, just as you would with a physical server.

 After you have the first environment set up with all the necessary Oracle software, you can create your own custom AMI for subsequent installations. You can also directly launch AMIs from [AWS Marketplace](https://aws.amazon.com/marketplace). You should closely scrutinize any community AMIs provided by third parties for security and reliability before using them. AWS is not responsible or liable for their security or reliability.

## AWS Systems Manager
<a name="aws-systems-manager"></a>

 AWS Systems Manager AWS Systems Manager is a collection of capabilities that helps you automate management tasks such as systems inventory, applying operational patches, automatic creation of AMIs, and configuring operating systems and applications at scale. Systems Manager uses an SSM (System State Management) Agent to collect inventory, state information within the EC2 instance, and run patch commands. Patch Manager integrates with AWS Identity and Access Management (IAM), AWS CloudTrail, and Amazon CloudWatch Events to provide a secure patching experience that includes event notifications and the ability to audit usage.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
