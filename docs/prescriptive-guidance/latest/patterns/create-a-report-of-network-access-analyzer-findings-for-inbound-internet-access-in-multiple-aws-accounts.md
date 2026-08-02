---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html
---

# Create a report of Network Access Analyzer findings for inbound internet access in multiple AWS accounts
<a name="create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts"></a>

*Mike Virgilio, Amazon Web Services*

## Summary
<a name="create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts-summary"></a>

Unintentional inbound internet access to AWS resources can pose risks to an organization’s data perimeter. [Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html) is an Amazon Virtual Private Cloud (Amazon VPC) feature that helps you identify unintended network access to your resources on Amazon Web Services (AWS). You can use Network Access Analyzer to specify your network access requirements and to identify potential network paths that do not meet your specified requirements. You can use Network Access Analyzer to do the following:

1. Identify AWS resources that are accessible to the internet through internet gateways.

1. Validate that your virtual private clouds (VPCs) are appropriately segmented, such as isolating production and development environments and separating transactional workloads.

Network Access Analyzer analyzes end-to-end network reachability conditions and not just a single component. To determine whether a resource is internet accessible, Network Access Analyzer evaluates the internet gateway, VPC route tables, network access control lists (ACLs), public IP addresses on elastic network interfaces, and security groups. If any of these components prevent internet access, Network Access Analyzer doesn’t generate a finding. For example, if an Amazon Elastic Compute Cloud (Amazon EC2) instance has an open security group that allows traffic from `0/0` but the instance is in a private subnet that isn’t routable from any internet gateway, then Network Access Analyzer wouldn’t generate a finding. This provides high-fidelity results so that you can identify resources that are truly accessible from the internet.

When you run Network Access Analyzer, you use [Network Access Scopes](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html#concepts) to specify your network access requirements. This solution identifies network paths between an internet gateway and an elastic network interface. In this pattern, you deploy the solution in a centralized AWS account in your organization, managed by AWS Organizations, and it analyzes all of the accounts, in any AWS Region, in the organization.

This solution was designed with the following in mind:
+ The AWS CloudFormation templates reduce the effort required to deploy the AWS resources in this pattern.
+ You can adjust the parameters in the CloudFormation templates and **naa-script.sh** script at the time of deployment to customize them for your environment.
+ Bash scripting automatically provisions and analyzes the Network Access Scopes for multiple accounts, in parallel.
+ A Python script processes the findings, extracts the data, and then consolidates the results. You can choose to review the consolidated report of Network Access Analyzer findings in CSV format or in AWS Security Hub CSPM. An example of the CSV report is available in the [Additional information](#create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts-additional) section of this pattern.
+ You can remediate findings, or you can exclude them from future analyses by adding them to the **naa-exclusions.csv** file.

## Prerequisites and limitations
<a name="create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts-prereqs"></a>

**Prerequisites**
+ An AWS account for hosting security services and tools, managed as a member account of an organization in AWS Organizations. In this pattern, this account is referred to as the security account.
+ In the security account, you must have a private subnet with outbound internet access. For instructions, see [Create a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/create-subnets.html) in the Amazon VPC documentation. You can establish internet access by using an [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) or an [interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html).
+ Access to the AWS Organizations management account or an account that has delegated administrator permissions for CloudFormation. For instructions, see [Register a delegated administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the CloudFormation documentation.
+ Enable trusted access between AWS Organizations and CloudFormation. For instructions, see [Enable trusted access with AWS Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.html) in the CloudFormation documentation.
+ If you’re uploading the findings to Security Hub CSPM, Security Hub CSPM must be enabled in the account and AWS Region where the Amazon EC2 instance is provisioned. For more information, see [Setting up AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html).

**Limitations**
+ Cross-account network paths are not currently analyzed due to limitations of the Network Access Analyzer feature.
+ The target AWS accounts must be managed as an organization in AWS Organizations. If you are not using AWS Organizations, you can update the **naa-execrole.yaml** CloudFormation template and the **naa-script.sh** script for your environment. Instead, you provide a list of AWS account IDs and Regions where you want to run the script.
+ The CloudFormation template is designed to deploy the Amazon EC2 instance in a private subnet that has outbound internet access. The AWS Systems Manager Agent (SSM Agent) requires outbound access to reach the Systems Manager service endpoint, and you need outbound access to clone the code repository and install dependencies. If you want to use a public subnet, you must modify the **naa-resources.yaml** template to associate an [Elastic IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) with the Amazon EC2 instance.

## Architecture
<a name="create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts-architecture"></a>

**Target architecture**

*Option 1: Access findings in an Amazon S3 bucket*

![Architecture diagram of accessing the Network Access Analyzer findings report in an Amazon S3 bucket](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/eda6abba-632a-4e3d-92b9-31848fa6dead/images/d0b08437-e5b0-47a1-abdd-040c67b5da8f.png)

The diagram shows the following process:

1. If you’re manually running the solution, the user authenticates to the Amazon EC2 instance by using Session Manager and then runs the **naa-script.sh** script. This shell script performs steps 2–7.

   If you’re automatically running the solution, the **naa-script.sh** script starts automatically on the schedule you defined in the cron expression. This shell script performs steps 2–7. For more information, see *Automation and scale* at the end of this section.

1. The Amazon EC2 instance downloads the latest **naa-exception.csv** file from the Amazon S3 bucket. This file is used later in the process when the Python script processes the exclusions.

1. The Amazon EC2 instance assumes the `NAAEC2Role` AWS Identity and Access Management (IAM) role, which grants permissions to access the Amazon S3 bucket and to assume the `NAAExecRole` IAM roles in the other accounts in the organization.

1. The Amazon EC2 instance assumes the `NAAExecRole` IAM role in the organization’s management account and generates a list of the accounts in the organization.

1. The Amazon EC2 instance assumes the `NAAExecRole` IAM role in the organization’s member accounts (called *workload accounts* in the architecture diagram) and performs a security assessment in each account. The findings are stored as JSON files on the Amazon EC2 instance.

1. The Amazon EC2 instance uses a Python script to process the JSON files, extract the data fields, and create a CSV report.

1. The Amazon EC2 instance uploads the CSV file to the Amazon S3 bucket.

1. An Amazon EventBridge rule detects the file upload and uses an Amazon SNS topic to send an email that notifies the user that the report is complete.

1. The user downloads the CSV file from the Amazon S3 bucket. The user imports the results into the Excel template and reviews the results.

*Option 2: Access findings in AWS Security Hub CSPM*

![Architecture diagram of accessing the Network Access Analyzer findings through AWS Security Hub](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/eda6abba-632a-4e3d-92b9-31848fa6dead/images/9cb4f059-dfb6-4a33-9f8d-159fe5df0d64.png)

The diagram shows the following process:

1. If you’re manually running the solution, the user authenticates to the Amazon EC2 instance by using Session Manager and then runs the **naa-script.sh** script. This shell script performs steps 2–7.

   If you’re automatically running the solution, the **naa-script.sh** script starts automatically on the schedule you defined in the cron expression. This shell script performs steps 2–7. For more information, see *Automation and scale* at the end of this section.

1. The Amazon EC2 instance downloads the latest **naa-exception.csv** file from the Amazon S3 bucket. This file is used later in the process when the Python script processes the exclusions.

1. The Amazon EC2 instance assumes the `NAAEC2Role` IAM role, which grants permissions to access the Amazon S3 bucket and to assume the `NAAExecRole` IAM roles in the other accounts in the organization.

1. The Amazon EC2 instance assumes the `NAAExecRole` IAM role in the organization’s management account and generates a list of the accounts in the organization.

1. The Amazon EC2 instance assumes the `NAAExecRole` IAM role in the organization’s member accounts (called *workload accounts* in the architecture diagram) and performs a security assessment in each account. The findings are stored as JSON files on the Amazon EC2 instance.

1. The Amazon EC2 instance uses a Python script to process the JSON files and extract the data fields for import into Security Hub CSPM.

1. The Amazon EC2 instance imports the Network Access Analyzer findings to Security Hub CSPM.

1. An Amazon EventBridge rule detects the import and uses an Amazon SNS topic to send an email that notifies the user that the process is complete.

1. The user views the findings in Security Hub CSPM.

**Automation and scale**

You can schedule this solution to run the **naa-script.sh** script automatically on a custom schedule. To set a custom schedule, in the **naa-resources.yaml** CloudFormation template, modify the `CronScheduleExpression` parameter. For example, the default value of `0 0 * * 0` runs the solution at midnight on every Sunday. A value of `0 0 * 1-12 0` would run the solution at midnight on the first Sunday of every month. For more information about using cron expressions, see [Cron and rate expressions](https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-cron-and-rate-expressions.html) in the Systems Manager documentation.

If you want adjust the schedule after the `NAA-Resources` stack has been deployed, you can manually edit the cron schedule in `/etc/cron.d/naa-schedule`.

## Tools
<a name="create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides a comprehensive view of your security state in AWS. It also helps you check your AWS environment against security industry standards and best practices.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale. This pattern uses Session Manager, a capability of Systems Manager.

**Code repository**

The code for this pattern is available in the GitHub [Network Access Analyzer Multi-Account Analysis](https://github.com/aws-samples/network-access-analyzer-multi-account-analysis) repository. The code repository contains the following files:
+ **naa-script.sh** – This bash script is used to start a Network Access Analyzer analysis of multiple AWS accounts, in parallel. As defined in the **naa-resources.yaml** CloudFormation template, this script is automatically deployed to the `/usr/local/naa` folder on the Amazon EC2 instance.
+ **naa-resources.yaml** – You use this CloudFormation template to create a stack in the security account in the organization. This template deploys all of the required resources for this account in order to support the solution. This stack must be deployed before the **naa-execrole.yaml** template.
**Note**
If this stack is deleted and redeployed, you must rebuild the `NAAExecRole` stack set in order to rebuild the cross-account dependencies between the IAM roles.
+ **naa-execrole.yaml** – You use this CloudFormation template to create a stack set that deploys the `NAAExecRole` IAM role in all accounts in the organization, including the management account.
+ **naa-processfindings.py** – The **naa-script.sh **script automatically calls this Python script to process the Network Access Analyzer JSON outputs, exclude any known-good resources in the **naa-exclusions.csv** file, and then either generate a CSV file of the consolidated results or import the results into Security Hub CSPM.

## Epics
<a name="create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts-epics"></a>

### Prepare for deployment
<a name="prepare-for-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the code repository. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html) | AWS DevOps |
| Review the templates. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html) | AWS DevOps |

### Create the CloudFormation stacks
<a name="create-the-cfnshort-stacks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Provision resources in the security account. | Using the **naa-resources.yaml** template, you create a CloudFormation stack that deploys all of the required resources in the security account. For instructions, see [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the CloudFormation documentation. Note the following when deploying this template:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html) | AWS DevOps |
| Provision the IAM role in the member accounts. | In the AWS Organizations management account or an account with delegated administrator permissions for CloudFormation, use the **naa-execrole.yaml** template to create a CloudFormation stack set. The stack set deploys the `NAAExecRole` IAM role in all member accounts in the organization. For instructions, see [Create a stack set with service-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html#stacksets-orgs-associate-stackset-with-org) in the CloudFormation documentation. Note the following when deploying this template:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html) | AWS DevOps |
| Provision the IAM role in the management account. | Using the **naa-execrole.yaml** template, you create a CloudFormation stack that deploys the `NAAExecRole` IAM role in the management account of the organization. The stack set you created previously doesn’t deploy the IAM role in the management account. For instructions, see [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the CloudFormation documentation. Note the following when deploying this template:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html) | AWS DevOps |

### Perform the analysis
<a name="perform-the-analysis"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Customize the shell script. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html) | AWS DevOps |
| Analyze the target accounts. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html) | AWS DevOps |
| Option 1 – Retrieve the results from the Amazon S3 bucket. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html) | AWS DevOps |
| Option 2 – Review the results in Security Hub CSPM. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html) | AWS DevOps |

### Remediate and exclude findings
<a name="remediate-and-exclude-findings"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remediate findings. | Remediate any findings that you want to address. For more information and best practices about how to create a perimeter around your AWS identities, resources, and networks, see [Building a data perimeter on AWS](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) (AWS Whitepaper). | AWS DevOps |
| Exclude resources with known-good network paths. | If Network Access Analyzer generates findings for resources that should be accessible from the internet, then you can add these resources to an exclusion list. The next time Network Access Analyzer runs, it won’t generate a finding for that resource.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html) | AWS DevOps |

### (Optional) Update the naa-script.sh script
<a name="optional-update-the-naa-script-sh-script"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the naa-script.sh script. | If you want to update the **naa-script.sh** script to the latest version in the repo, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html) | AWS DevOps |

### (Optional) Clean up
<a name="optional-clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete all deployed resources. | You can leave the resources deployed in the accounts.<br />If you want to deprovision all resources, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html) | AWS DevOps |

## Troubleshooting
<a name="create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Unable to connect to the Amazon EC2 instance by using Session Manager. | The SSM Agent must be able to communicate with the Systems Manager endpoint. Do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts.html) |
| When deploying the stack set, the CloudFormation console prompts you to `Enable trusted access with AWS Organizations to use service-managed permissions`. | This indicates that trusted access has not been enabled between AWS Organizations and CloudFormation. Trusted access is required to deploy the service-managed stack set. Choose the button to enable trusted access. For more information, see [Enable trusted access](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.html) in the CloudFormation documentation. |

## Related resources
<a name="create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts-resources"></a>
+ [New – Amazon VPC Network Access Analyzer](https://aws.amazon.com/blogs/aws/new-amazon-vpc-network-access-analyzer/) (AWS blog post)
+ [AWS re:Inforce 2022 - Validate effective network access controls on AWS (NIS202)](https://youtu.be/aN2P2zeQek0) (video)
+ [Demo - Organization-wide Internet Ingress Data Path Analysis Using Network Access Analyzer](https://youtu.be/1IFNZWy4iy0) (video)

## Additional information
<a name="create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts-additional"></a>

**Example console output**

The following sample shows the output of generating the list of target accounts and analyzing the target accounts.

```
[root@ip-10-10-43-82 naa]# ./naa-script.sh
download: s3://naa-<account ID>-us-east-1/naa-exclusions.csv to ./naa-exclusions.csv

AWS Management Account: <Management account ID>

AWS Accounts being processed...
<Account ID 1> <Account ID 2> <Account ID 3>

Assessing AWS Account: <Account ID 1>, using Role: NAAExecRole
Assessing AWS Account: <Account ID 2>, using Role: NAAExecRole
Assessing AWS Account: <Account ID 3>, using Role: NAAExecRole
Processing account: <Account ID 1> / Region: us-east-1
Account: <Account ID 1> / Region: us-east-1 – Detecting Network Analyzer scope...
Processing account: <Account ID 2> / Region: us-east-1
Account: <Account ID 2> / Region: us-east-1 – Detecting Network Analyzer scope...
Processing account: <Account ID 3> / Region: us-east-1
Account: <Account ID 3> / Region: us-east-1 – Detecting Network Analyzer scope...
Account: <Account ID 1> / Region: us-east-1 – Network Access Analyzer scope detected.
Account: <Account ID 1> / Region: us-east-1 – Continuing analyses with Scope ID. Accounts with many resources may take up to one hour
Account: <Account ID 2> / Region: us-east-1 – Network Access Analyzer scope detected.
Account: <Account ID 2> / Region: us-east-1 – Continuing analyses with Scope ID. Accounts with many resources may take up to one hour
Account: <Account ID 3> / Region: us-east-1 – Network Access Analyzer scope detected.
Account: <Account ID 3> / Region: us-east-1 – Continuing analyses with Scope ID. Accounts with many resources may take up to one hour
```

**CSV report examples**

The following images are examples of the CSV output.

![Example 1 of the CSV report generated by this solution.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/eda6abba-632a-4e3d-92b9-31848fa6dead/images/55e02e61-054e-4da6-aaae-c9a8b6f4f272.png)

![Example 2 of the CSV report generated by this solution.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/eda6abba-632a-4e3d-92b9-31848fa6dead/images/95f980ad-92c1-4392-92d4-9c742755aab2.png)
