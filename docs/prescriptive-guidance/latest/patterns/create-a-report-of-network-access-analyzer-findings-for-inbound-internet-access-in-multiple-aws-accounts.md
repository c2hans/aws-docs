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
| Clone the code repository. | 1. In a command-line interface, change your working directory to the location where you want to store the sample files.<br />2. Enter the following command:<br />`git clone https://github.com/aws-samples/network-access-analyzer-multi-account-analysis.git` | AWS DevOps |
| Review the templates. | 1. In the cloned repository, open the **naa-resources.yaml** and **naa-execrole.yaml** files.<br />2. Review the resources created by these templates and adjust the templates as needed for your environment. For more information, see [Working with templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) in the CloudFormation documentation.<br />3. Save and close the **naa-resources.yaml** and **naa-execrole.yaml** files. | AWS DevOps |

### Create the CloudFormation stacks
<a name="create-the-cfnshort-stacks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Provision resources in the security account. | Using the **naa-resources.yaml** template, you create a CloudFormation stack that deploys all of the required resources in the security account. For instructions, see [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the CloudFormation documentation. Note the following when deploying this template:1. On the **Specify template** page, choose **Template is ready**, and then upload the **naa-resources.yaml** file.<br />2. On the **Specify stack details** page, in the **Stack name** box, enter `NAA-Resources`.<br />3. In the **Parameters** section, enter the following:`VPCId` – Select a VPC in the account.`SubnetId` ­–­ Select a private subnet that has internet access.If you select a public subnet, the Amazon EC2 instance might not be assigned a public IP address because the CloudFormation template, by default, doesn’t provision and attach an Elastic IP address.`InstanceType` – Leave the default instance type.`InstanceImageId` – Leave the default.`KeyPairName` – If you’re using SSH for access, specify the name of an existing key pair.`PermittedSSHInbound` – If you’re using SSH for access, specify a permitted CIDR block. If you’re not using SSH, keep the default value of `127.0.0.1`.`BucketName` – The default value is `naa-<accountID>-<region>`. You can modify this as needed. If you specify a custom value, the account ID and Region are automatically appended to the specified value.`EmailAddress` – Specify an email address for an Amazon SNS notification when the analysis is complete.The Amazon SNS subscription configuration must be confirmed prior to completion of the analysis, or a notification will not be sent.`NAAEC2Role` – Keep the default unless your naming conventions require a different name for this IAM role.`NAAExecRole` – Keep the default unless another name will be used when deploying the **naa-execrole.yaml**`Parallelism` – Specify the number of parallel assessments to perform.`Regions` – Specify the AWS Regions you want to analyze.`ScopeNameValue` – Specify the tag that will be assigned to the scope. This tag is used to determine the Network Access Scope.`ExclusionFile` – Specify the exclusion file name. Entries in this file will be excluded from findings.`FindingsToCSV` – Specify whether findings should be output to CSV. Accepted values are `true` and `false`.`FindingsToSecurityHub` – Specify whether findings should be imported into Security Hub CSPM. Accepted values are `true` and `false`.`EmailNotificationsForSecurityHub` – Specify whether importing findings into Security Hub CSPM should generate email notifications. Accepted values are `true` and `false`.`ScheduledAnalysis` – If you want the solution to run automatically on a schedule, enter `true`, and then customize the schedule in the `CronScheduleExpression` parameter. If you do not want to run the solution automatically, enter `false`.`CronScheduleExpression` – If you’re running the solution automatically, enter a cron expression to define the schedule. For more information, see *Automation and scale* in the [Architecture](#create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts-architecture) section of this pattern.1. On the **Review** page, select **The following resource(s) require capabilities: [AWS::IAM::Role]**, and then choose **Create Stack**.<br />2. After the stack has been successfully created, in the CloudFormation console, on the **Outputs** tab, copy the `NAAEC2Role` Amazon Resource Name (ARN). You use this ARN later when deploying the **naa-execrole.yaml** file. | AWS DevOps |
| Provision the IAM role in the member accounts. | In the AWS Organizations management account or an account with delegated administrator permissions for CloudFormation, use the **naa-execrole.yaml** template to create a CloudFormation stack set. The stack set deploys the `NAAExecRole` IAM role in all member accounts in the organization. For instructions, see [Create a stack set with service-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html#stacksets-orgs-associate-stackset-with-org) in the CloudFormation documentation. Note the following when deploying this template:1. Under **Prepare template**, choose **Template is ready**, and then upload the **naa-execrole.yaml** file.<br />2. On the **Specify StackSet details** page, name the stack set `NAA-ExecRole`.<br />3. In the **Parameters** section, enter the following:`AuthorizedARN` – Enter the `NAAEC2Role` ARN, which you copied when you created the `NAA-Resources` stack.`NAARoleName` – Keep the default value of `NAAExecRole` unless another name was used when deploying the **naa-resources.yaml** file.<br />4. Under **Permissions**, choose **Service-managed permissions**.<br />5. On the **Set deployment options** page, under **Deployment targets**, choose **Deploy to organization** and accept all defaults.If you want the stacks deployed to all member accounts simultaneously, set **Maximum concurrent accounts** and **Failure tolerance** to a high value, such as `100`.<br />6. Under **Deployment regions**, choose the Region where the Amazon EC2 instance for Network Access Analyzer is deployed. Because IAM resources are global and not Regional, this deploys the IAM role in all active Regions.<br />7. On the **Review** page, select **I acknowledge that AWS CloudFormation might create IAM resources with custom names**, and then choose **Create StackSet**.<br />8. Monitor the **Stack instances** tab (for individual account status) and the **Operations** tab (for overall status) to determine when the deployment is complete. | AWS DevOps |
| Provision the IAM role in the management account. | Using the **naa-execrole.yaml** template, you create a CloudFormation stack that deploys the `NAAExecRole` IAM role in the management account of the organization. The stack set you created previously doesn’t deploy the IAM role in the management account. For instructions, see [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the CloudFormation documentation. Note the following when deploying this template:1. On the **Specify template** page, choose **Template is ready**, and then upload the **naa-execrole.yaml** file.<br />2. On the **Specify stack details** page, in the **Stack name** box, enter `NAA-ExecRole`.<br />3. In the **Parameters** section, enter the following:`AuthorizedARN` – Enter the `NAAEC2Role` ARN, which you copied when you created the `NAA-Resources` stack.`NAARoleName` – Keep the default value of `NAAExecRole` unless another name was used when deploying the **naa-resources.yaml** file.<br />4. On the **Review** page, select **The following resource(s) require capabilities: [AWS::IAM::Role]**, and then choose **Create Stack**. | AWS DevOps |

### Perform the analysis
<a name="perform-the-analysis"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Customize the shell script. | 1. Sign in to the security account in the organization.<br />2. Using Session Manager, connect to the Amazon EC2 instance for Network Access Analyzer that you previously provisioned. For instructions, see [Connect to your Linux instance using Session Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/session-manager.html). If you’re unable to connect, see the [Troubleshooting](#create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts-troubleshooting) section of this pattern.<br />3. Enter the following commands to open the **naa-script.sh** file for editing:<pre>sudo -i<br />cd /usr/local/naa<br />vi naa-script.sh</pre><br />4. Review and modify the adjustable parameters and variables in this script as needed for your environment. For more information about customization options, see the comments at the beginning of the script.<br />For example, instead of getting a list of all member accounts in the organization from the management account, you can modify the script to specify the AWS account IDs or AWS Regions that you want to scan, or you can reference an external file that contains these parameters.<br />5. Save and close the **naa-script.sh** file. | AWS DevOps |
| Analyze the target accounts. | 1. Enter the following commands. This runs the **naa-script.sh** script:<pre>sudo -i<br />cd /usr/local/naa<br />screen<br />./naa-script.sh</pre><br />Note the following:The `screen` command permits the script to continue running in the event that the connection times out or you lose console access.After the scan starts, you can force a screen detach by pressing **Ctrl\+A D**. The screen detaches, and you can close the instance connection while the analysis proceeds.To resume a detached session, connect to the instance, enter `sudo -i` then enter `screen -r`.<br />2. Monitor the output for any errors to make sure that the script is working properly. For a sample output, see the [Additional information](#create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts-additional) section of this pattern.<br />3. Wait for the analysis to complete. If you configured email notifications, you receive an email when the results have been uploaded to the Amazon S3 bucket or imported into Security Hub CSPM. | AWS DevOps |
| Option 1 – Retrieve the results from the Amazon S3 bucket. | 1. Download the CSV file from the `naa-<accountID>-<region>` bucket. For instructions, see [Downloading an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html) in the Amazon S3 documentation.<br />2. Delete the CSV file from the Amazon S3 bucket. This is a best practice for cost optimization. For instructions, see [Deleting objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjects.html) in the Amazon S3 documentation. | AWS DevOps |
| Option 2 – Review the results in Security Hub CSPM. | 1. Open the [Security Hub CSPM console](https://console.aws.amazon.com/securityhub/).<br />2. Choose **Findings** from the navigation pane.<br />3. Review the Network Access Analyzer findings. For instructions, see [Viewing finding lists and details](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-viewing.html) in the Security Hub CSPM documentation.You can search findings by adding a **Title starts with** filter and entering `Network Access Analyzer`. | AWS DevOps |

### Remediate and exclude findings
<a name="remediate-and-exclude-findings"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remediate findings. | Remediate any findings that you want to address. For more information and best practices about how to create a perimeter around your AWS identities, resources, and networks, see [Building a data perimeter on AWS](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) (AWS Whitepaper). | AWS DevOps |
| Exclude resources with known-good network paths. | If Network Access Analyzer generates findings for resources that should be accessible from the internet, then you can add these resources to an exclusion list. The next time Network Access Analyzer runs, it won’t generate a finding for that resource.1. Navigate to `/usr/local/naa`, and then open the **naa-script.sh** script. Make note of the value of the `S3_EXCLUSION_FILE` variable.<br />2. If the value of the `S3_EXCLUSION_FILE` variable is `true`, download the **naa-exclusions.csv** file from the `naa-<accountID>-<region>` bucket. For instructions, see [Downloading an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html) in the Amazon S3 documentation.<br />If the value of the `S3_EXCLUSION_FILE` variable is `false`, navigate to `/usr/local/naa` and then open the **naa-exclusions.csv** file.If the value of the `S3_EXCLUSION_FILE` variable is `false`, the script uses a local version of the exclusions file. If you later change the value to `true`, then the script overwrites the local version with the file in the Amazon S3 bucket.<br />3. In the **naa-exclusions.csv** file, enter the resources that you want to exclude. Enter one resource in each line, and use the following format.<br />`<resource_id>,<secgroup_id>,<sgrule_cidr>,<sgrule_portrange>,<sgrule_protocol>`<br />The following is an example resource.<br />`eni-1111aaaaa2222bbbb,sg-3333ccccc4444dddd,0.0.0.0/0,80 to 80,tcp`<br />4. Save and close the **naa-exclusions.csv** file.<br />5. If you downloaded the **naa-exclusions.csv** file from the Amazon S3 bucket, upload the new version. For instructions, see [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) in the Amazon S3 documentation. | AWS DevOps |

### (Optional) Update the naa-script.sh script
<a name="optional-update-the-naa-script-sh-script"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the naa-script.sh script. | If you want to update the **naa-script.sh** script to the latest version in the repo, do the following:1. Connect to the Amazon EC2 instance by using Session Manager. For instructions, see [Connect to your Linux instance using Session Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/session-manager.html).<br />2. Enter the following command:<pre>sudo -i</pre><br />3. Navigate to the **naa-script.sh** script directory:<pre>cd /usr/local/naa</pre><br />4. Enter the following command to stash the local script so that you can merge custom changes into the newest version:<pre>git stash</pre><br />5. Enter the following command to get the latest version of the script:<pre>git pull</pre><br />6. Enter the following command to merge the custom script with the latest version of the script:<pre>git stash pop</pre> | AWS DevOps |

### (Optional) Clean up
<a name="optional-clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete all deployed resources. | You can leave the resources deployed in the accounts.<br />If you want to deprovision all resources, do the following:1. Delete the `NAA-ExecRole` stack provisioned in the management account. For instructions, see [Deleting a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-cli-deleting-stack.html) in the CloudFormation documentation.<br />2. Delete the `NAA-ExecRole` stack set provisioned in the organization’s management account or in the delegated administrator account. For instructions, see [Delete a stack set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-delete.html) in the CloudFormation documentation.<br />3. Delete all objects in the `naa-<accountID>-<region>` Amazon S3 bucket. For instructions, see [Deleting objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjects.html) in the Amazon S3 documentation.<br />4. Delete the `NAA-Resources` stack provisioned in the security account. For instructions, see [Deleting a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-cli-deleting-stack.html) in the CloudFormation documentation. | AWS DevOps |

## Troubleshooting
<a name="create-a-report-of-network-access-analyzer-findings-for-inbound-internet-access-in-multiple-aws-accounts-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Unable to connect to the Amazon EC2 instance by using Session Manager. | The SSM Agent must be able to communicate with the Systems Manager endpoint. Do the following:1. Validate the subnet where the Amazon EC2 instance is deployed has internet access.<br />2. Reboot the Amazon EC2 instance. |
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
