---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-consolidated-report-of-prowler-security-findings-from-multiple-aws-accounts.html
---

# Create a consolidated report of Prowler security findings from multiple AWS accounts
<a name="create-a-consolidated-report-of-prowler-security-findings-from-multiple-aws-accounts"></a>

*Mike Virgilio, Jay Durga, and Andrea Di Fabio, Amazon Web Services*

## Summary
<a name="create-a-consolidated-report-of-prowler-security-findings-from-multiple-aws-accounts-summary"></a>

[Prowler](https://github.com/prowler-cloud/prowler) (GitHub) is an open-source command line tool that can help you assess, audit, and monitor your Amazon Web Services (AWS) accounts for adherence to security best practices. In this pattern, you deploy Prowler in a centralized AWS account in your organization, managed by AWS Organizations, and then use Prowler to perform a security assessment of all of the accounts in the organization.

While there are many methods to deploy and utilize Prowler for an assessment, this solution has been designed for rapid deployment, full analysis of all accounts in the organization or defined target accounts, and accessible reporting of the security findings. In this solution, when Prowler completes the security assessment of all accounts in the organization, it consolidates the results. It also filters out any expected error messages, such as errors related to restrictions that prevent Prowler from scanning Amazon Simple Storage Service (Amazon S3) buckets in accounts provisioned through AWS Control Tower. The filtered, consolidated results are reported in a Microsoft Excel template that is included with this pattern. You can use this report to identify potential improvements for the security controls in your organization.

This solution was designed with the following in mind:
+ The AWS CloudFormation templates reduce the effort required to deploy the AWS resources in this pattern.
+ You can adjust the parameters in the CloudFormation templates and **prowler\_scan.sh** script at the time of deployment to customize the templates for your environment.
+ Prowler assessment and reporting speeds are optimized through parallel processing of AWS accounts, aggregated results, consolidated reporting with recommended remediations, and automatically generated visualizations.
+ The user doesn’t need to monitor the scan progress. When the assessment is complete, the user is notified through an Amazon Simple Notification Service (Amazon SNS) topic so that they can retrieve the report.
+ The report template helps you read and assess only the relevant results for your entire organization.

## Prerequisites and limitations
<a name="create-a-consolidated-report-of-prowler-security-findings-from-multiple-aws-accounts-prereqs"></a>

**Prerequisites**
+ An AWS account for hosting security services and tools, managed as a member account of an organization in AWS Organizations. In this pattern, this account is referred to as the *security account*.
+ In the security account, you must have a private subnet with outbound internet access. For instructions, see [VPC with servers in private subnets and NAT](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html) in the Amazon Virtual Private Cloud (Amazon VPC) documentation. You can establish internet access by using an [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) that is provisioned in a public subnet.
+ Access to the AWS Organizations management account or an account that has delegated administrator permissions for CloudFormation. For instructions, see [Register a delegated administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the CloudFormation documentation.
+ Enable trusted access between AWS Organizations and CloudFormation. For instructions, see [Enable trusted access with AWS Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.html) in the CloudFormation documentation.

**Limitations**
+ The target AWS accounts must be managed as an organization in AWS Organizations. If you are not using AWS Organizations, you can update the **IAM-ProwlerExecRole.yaml** CloudFormation template and the **prowler\_scan.sh** script for your environment. Instead, you provide a list of AWS account IDs and Regions where you want to run the script.
+ The CloudFormation template is designed to deploy the Amazon Elastic Compute Cloud (Amazon EC2) instance in a private subnet that has outbound internet access. The AWS Systems Manager Agent (SSM Agent) requires outbound access to reach the AWS Systems Manager service endpoint, and you need outbound access to clone the code repository and install dependencies. If you want to use a public subnet, you must modify the **prowler-resources.yaml** template to associate an [Elastic IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) with the EC2 instance.

**Product versions**
+ Prowler version 4.0 or later

## Architecture
<a name="create-a-consolidated-report-of-prowler-security-findings-from-multiple-aws-accounts-architecture"></a>

![Architecture diagram with Prowler deployed in a centralized security account.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/81ba9037-9958-4e4a-95b7-d68896075a5b/images/4a3c281c-f108-4e35-9683-72783ceb3336.png)

The diagram shows the following process:

1. Using Session Manager, a capability of AWS Systems Manager, the user authenticates to the EC2 instance and runs the **prowler\_scan.sh** script. This shell script performs steps 2–8.

1. The EC2 instance assumes the `ProwlerEC2Role` IAM role, which grants permissions to access the S3 bucket and to assume the `ProwlerExecRole` IAM roles in the other accounts in the organization.

1. The EC2 instance assumes the `ProwlerExecRole` IAM role in the organization’s management account and generates a list of the accounts in the organization.

1. The EC2 instance assumes the `ProwlerExecRole` IAM role in the organization’s member accounts (called *workload accounts* in the architecture diagram) and performs a security assessment in each account. The findings are stored as CSV and HTML files on the EC2 instance.
**Note**
 HTML files are an output of the Prowler assessment. Due to the nature of HTML, they aren’t concatenated, processed, or used directly in this pattern. However, these might be useful for individual account report review.

1. The EC2 instance processes all of the CSV files to remove known, expected errors and consolidates the remaining findings into a single CSV file.

1. The EC2 instance packages the individual account results and aggregated results into a zip file.

1. The EC2 instance uploads the zip file to the S3 bucket.

1. An EventBridge rule detects the file upload and uses an Amazon SNS topic to send an email to the user notifying them that the assessment is complete.

1. The user downloads the zip file from the S3 bucket. The user imports the results into the Excel template and reviews the results.

## Tools
<a name="create-a-consolidated-report-of-prowler-security-findings-from-multiple-aws-accounts-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale. This pattern uses Session Manger, a capability of Systems Manager.

**Other tools**
+ [Prowler](https://github.com/prowler-cloud/prowler/#requirements-and-installation) is an open-source command-line tool that helps you assess, audit, and monitor your accounts for adherence to AWS security best practices and other security frameworks and standards.

**Code repository**

The code for this pattern is available in the GitHub [Multi-Account Security Assessment via Prowler](https://github.com/aws-samples/multi-account-security-assessment-via-prowler) repository. The code repository contains the following files:
+ **prowler\_scan.sh** – This bash script is used to start a Prowler security assessment of multiple AWS accounts, in parallel. As defined in the **Prowler-resources.yaml** CloudFormationtemplate, this script is automatically deployed to the `usr/local/prowler` folder on the EC2 instance.
+ **Prowler-Resources.yaml** – You use this CloudFormation template to create a stack in the security account in the organization. This template deploys all of the required resources for this account in order to support the solution. This stack must be deployed before the **IAM-ProwlerExecRole.yaml** template. We do not recommend that you deploy these resources in an account that hosts critical production workloads.
**Note**
If this stack is deleted and redeployed, you must rebuild the `ProwlerExecRole` stack set in order to rebuild the cross-account dependencies between the IAM roles.
+ **IAM-ProwlerExecRole.yaml** – You use this CloudFormation template to create a stack set that deploys the `ProwlerExecRole` IAM role in all accounts in the organization, including the management account.
+ **prowler-report-template.xlsm** – You use this Excel template to process the Prowler findings. The pivot tables in the report provide search capabilities, charts, and consolidated findings.

## Epics
<a name="create-a-consolidated-report-of-prowler-security-findings-from-multiple-aws-accounts-epics"></a>

### Prepare for deployment
<a name="prepare-for-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the code repository. | 1. In a command-line interface, change your working directory to the location where you want to store the sample files.<br />2. Enter the following command:<br />`git clone https://github.com/aws-samples/multi-account-security-assessment-via-prowler.git` | AWS DevOps |
| Review the templates. | 1. In the cloned repository, open the **Prowler-Resources.yaml** and **IAM-ProwlerExecRole.yaml** files.<br />2. Review the resources created by these templates and adjust the templates as needed for your environment. For more information, see [Working with templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) in the CloudFormation documentation.<br />3. Save and close the **Prowler-Resources.yaml** and **IAM-ProwlerExecRole.yaml** files. | AWS DevOps |

### Create the CloudFormation stacks
<a name="create-the-cfnshort-stacks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Provision resources in the security account. | Using the **prowler-resources.yaml** template, you create a CloudFormation stack that deploys all of the required resources in the security account. For instructions, see [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the CloudFormation documentation. Note the following when deploying this template:1. On the **Specify template** page, choose **Template is ready**, and then upload the **prowler-resources.yaml **file.<br />2. On the **Specify stack details** page, in the **Stack name** box, enter `Prowler-Resources`.<br />3. In the **Parameters** section, enter the following:`VPCId` – Select a VPC in the account.`SubnetId` ­–­ Select a private subnet that has internet access.<br />*Note:* If you select a public subnet, the EC2 instance won’t be assigned a public IP address because the CloudFormation template, by default, doesn’t provision and attach an Elastic IP address.`InstanceType` – Select an instance size based on the number of parallel assessments:For 10, choose `r6i.large`.For 12, choose `r6i.xlarge`.For 14–18, choose `r6i.2xlarge`.`InstanceImageId` – Leave the default for Amazon Linux.`KeyPairName` – If you’re using SSH for access, specify the name of an existing key pair.`PermittedSSHInbound` – If you’re using SSH for access, specify a permitted CIDR block. If you’re not using SSH, keep the default value of `127.0.0.1`.`BucketName` – The default value is `prowler-output-<accountID>-<region>`. You can modify this as needed. If you specify a custom value, the account ID and Region are automatically appended to the specified value.`EmailAddress` – Specify an email address for an Amazon SNS notification when Prowler completes the assessment and uploads the .zip file to the S3 bucket.<br />*Note:* The SNS subscription configuration must be confirmed prior to Prowler completing the assessment or a notification will not be sent.`IAMProwlerEC2Role` – Keep the default unless your naming conventions require a different name for this IAM role.`IAMProwlerExecRole` – Keep the default unless another name will be used when deploying the **IAM-ProwlerExecRole.yaml** file.`Parallelism` – Specify the number of parallel assessments to perform. Make sure that the value in the `InstanceType` parameter supports this number of parallel assessments.`FindingOutput` – If you want to exclude pass results, select `FailOnly`. This significantly reduces the output size and focuses on the checks that might need to be resolved. If you want to include pass results, select `FailAndPass`.<br />4. On the **Review** page, select **The following resource(s) require capabilities: [AWS::IAM::Role]**, and then choose **Create Stack**.<br />5. After the stack has been successfully created, in the CloudFormation console, on the **Outputs** tab, copy the `ProwlerEC2Role` Amazon Resource Name (ARN). You use this ARN later when deploying the **IAM-ProwlerExecRole.yaml** file. | AWS DevOps |
| Provision the IAM role in the member accounts. | In the AWS Organizations management account or an account with delegated administrator permissions for CloudFormation, use the **IAM-ProwlerExecRole.yaml** template to create a CloudFormation stack set. The stack set deploys the `ProwlerExecRole` IAM role in all member accounts in the organization. For instructions, see [Create a stack set with service-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html#stacksets-orgs-associate-stackset-with-org) in the CloudFormation documentation. Note the following when deploying this template:1. Under **Prepare template**, choose **Template is ready**, and then upload the **IAM-ProwlerExecRole.yaml** file.<br />2. On the **Specify StackSet details** page, name the stack set `IAM-ProwlerExecRole`.<br />3. In the **Parameters** section, enter the following:`AuthorizedARN` – Enter the `ProwlerEC2Role` ARN, which you copied when you created the `Prowler-Resources` stack.`ProwlerExecRoleName` – Keep the default value of `ProwlerExecRole` unless another name was used when deploying the **Prowler-Resources.yaml** file.<br />4. Under **Permissions**, choose **Service-managed permissions**.<br />5. On the **Set deployment options** page, under **Deployment targets**, choose **Deploy to organization** and accept all defaults.<br />*Note:* If you want the stacks deployed to all member accounts simultaneously, set **Maximum concurrent accounts** and **Failure tolerance** to a high value, such as `100`.<br />6. Under **Deployment regions**, choose the AWS Region where the EC2 instance for Prowler is deployed. Because IAM resources are global and not Regional, this deploys the IAM role in all active Regions.<br />7. On the **Review** page, select **I acknowledge that AWS CloudFormation might create IAM resources with custom names**, and then choose **Create StackSet**.<br />8. Monitor the **Stack instances** tab (for individual account status) and the **Operations** tab (for overall status) to determine when the deployment is complete. | AWS DevOps |
| Provision the IAM role in the management account. | Using the **IAM-ProwlerExecRole.yaml** template, you create a CloudFormation stack that deploys the `ProwlerExecRole` IAM role in the management account of the organization. The stack set you created previously doesn’t deploy the IAM role in the management account. For instructions, see [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the CloudFormation documentation. Note the following when deploying this template:1. On the **Specify template** page, choose **Template is ready**, and then upload the **IAM-ProwlerExecRole.yaml** file.<br />2. On the **Specify stack details** page, in the **Stack name** box, enter `IAM-ProwlerExecRole`.<br />3. In the **Parameters** section, enter the following:`AuthorizedARN` – Enter the `ProwlerEC2Role` ARN, which you copied when you created the `Prowler-Resources` stack.`ProwlerExecRoleName` – Keep the default value of `ProwlerExecRole` unless another name was used when deploying the **Prowler-Resources.yaml** file.<br />4. On the **Review** page, select **The following resource(s) require capabilities: [AWS::IAM::Role]**, and then choose **Create Stack**. | AWS DevOps |

### Perform the Prowler security assessment
<a name="perform-the-prowler-security-assessment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the scan. | 1. Sign in to the security account in the organization.<br />2. Using Session Manager, connect to the EC2 instance for Prowler that you previously provisioned. For instructions, see [Connect to your Linux instance using Session Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/session-manager.html). If you’re unable to connect, see the [Troubleshooting](#create-a-consolidated-report-of-prowler-security-findings-from-multiple-aws-accounts-troubleshooting) section of this pattern.<br />3. Navigate to `usr/local/prowler`, and then open the **prowler\_scan.sh** file.<br />4. Review and modify the adjustable parameters and variables in this script as needed for your environment. For more information about customization options, see the comments at the beginning of the script.<br />For example, instead of getting a list of all member accounts in the organization from the management account, you can modify the script to specify the AWS account IDs or AWS Regions that you want to scan, or you can reference an external file that contains these parameters.<br />5. Save and close the **prowler\_scan.sh** file.<br />6. Enter the following commands. This runs the **prowler\_scan.sh** script.<pre>sudo -i<br />screen<br />cd /usr/local/prowler<br />./prowler_scan.sh</pre><br />Note the following:The screen command permits the script to continue running in the event that the connection times out or you lose console access.After the scan starts, you can force a screen detach by pressing **Ctrl\+A D**. The screen detaches, and you can close the instance connection and allow the assessment to proceed.To resume a detached session, connect to the instance, enter `sudo -i` then enter `screen -r`.To monitor progress of the individual account assessments, you can navigate to the `usr/local/prowler` directory and enter the command `tail -f output/stdout-<account-id>`.<br />7. Wait for Prowler to complete scans in all accounts. The script assesses multiple accounts at the same time. When the assessment is complete in all accounts, you receive a notification if you specified an email address when you deployed the **Prowler-Resources.yaml** file. | AWS administrator |
| Retrieve the Prowler findings. | 1. Download the `prowler-output-<assessDate>.zip` file from the `prowler-output-<accountID>-<region>` bucket. For instructions, see [Downloading an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html) in the Amazon S3 documentation.<br />2. Delete all objects in the bucket, including the file you downloaded. This is a best practice for cost optimization and to make sure that you can delete the `Prowler-Resources` CloudFormation stack at any time. For instructions, see [Deleting objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjects.html) in the Amazon S3 documentation. | General AWS |
| Stop the EC2 instance. | To prevent billing while the instance is idle, stop the EC2 instance that runs Prowler. For instructions, see [Stop and start your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html#starting-stopping-instances) in the Amazon EC2 documentation. | AWS DevOps |

### Create a report of the findings
<a name="create-a-report-of-the-findings"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Import the findings. | 1. In Excel, open the **prowler-report-template.xlsx** file, and then choose the **Prowler CSV** worksheet.<br />2. Delete all of the sample data, including the header row. If you are asked whether to delete the query associated with the data being removed, choose **No**. Deleting the query can affect the functionality of the pivot tables in the Excel template.<br />3. Extract the contents of the zip file you download from the S3 bucket.<br />4. In Excel, open the **prowler-fullorgresults-accessdeniedfiltered.txt**. We recommended that you use this file because the most common, non-actionable errors have already been removed, such as `Access Denied` errors related to attempted scans of AWS Control Tower resources. If you want the unfiltered findings, open the **prowler-fullorgresults.txt** file instead.<br />5. Select column A.<br />6. If you’re using Windows, enter **Ctrl\+C**, or if you’re using MacOS, enter **Cmd\+C**. This copies all of the data to the clipboard.<br />7. In the Excel report template, on the **Prowler CSV** worksheet, select cell A1.<br />8. If you’re using Windows, enter **Ctrl\+V**, or if you’re using MacOS, enter **Cmd\+V**. This pastes the findings into the report.<br />9. Confirm all of the cells containing pasted data are selected. If not, select column A.<br />10. On the **Data** tab, choose **Text to Columns**.<br />11. In the wizard, do the following:For step 1, choose **Delimited**.For step 2, for **Delimiters**, choose **Semicolon**. In the **Data preview** pane, confirm that the data is being separated into columns.For step 3, choose **Finish**.<br />12. Confirm that the text data is delimited across multiple columns.<br />13. Save the Excel report with a new name.<br />14. Search and delete any `Access Denied` errors in the findings. For instructions about how to remove these programmatically, see *Programmatically removing errors* in the [Additional information](#create-a-consolidated-report-of-prowler-security-findings-from-multiple-aws-accounts-additional) section. | General AWS |
| Finalize the report. | 1. Choose the **Findings** worksheet, and then select cell A17. This cell is the header of the pivot table.<br />2. In the ribbon, under **PivotTable Tools**, choose **Analyze**, and then under **Refresh**, choose **Refresh All**. This updates the pivot tables with the new data set.<br />3. By default, Excel does not properly display AWS account numbers. To fix the number formatting, do the following:On the **Findings** worksheet, open the context (right-click) menu for column A, and then choose **Format Cells**.Choose **Number**, and in **Decimal places**, enter `0`.Choose **OK**.<br />*Note: *If an AWS account number starts with one or more zeros, Excel automatically removes the zeros. If you see an account number that is less than 12 digits in the report, the missing digits are zeros at the beginning of the number.<br />4. (Optional) You can collapse fields to make the findings easier to read. Do the following:On the **Findings** worksheet, if you move the cursor to the line between rows 18 and 19 (the space between the critical header and the first finding), the cursor icon changes to a small arrow pointing down.Click to select all finding fields.Open the context (right-click) menu, find **Expand/Collapse**, and then choose **Collapse**.<br />5. For details about the assessment, review the **Findings**, **Severity**, and **Pass Fail** worksheets. | General AWS |

### (Optional) Update Prowler or the resources in the code repository
<a name="optional-update-prowler-or-the-resources-in-the-code-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update Prowler. | If you want to update Prowler to the latest version, do the following:1. Connect to the EC2 instance for Prowler by using Session Manager. For instructions, see [Connect to your Linux instance using Session Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/session-manager.html).<br />2. Enter the following command.<pre>sudo -i<br />pip3 install --upgrade prowler</pre> | General AWS |
| Update the prowler\_scan.sh script. | If you want to update the **prowler\_scan.sh** script to the latest version in the repo, do the following:1. Connect to the EC2 instance for Prowler by using Session Manager. For instructions, see [Connect to your Linux instance using Session Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/session-manager.html).<br />2. Enter the following command.<pre>sudo -i</pre><br />3. Navigate to the Prowler script directory.<pre>cd /usr/local/prowler</pre><br />4. Enter the following command to stash the local script so that you can merge custom changes into the newest version.<pre>git stash</pre><br />5. Enter the following command to get the latest version of the script.<pre>git pull</pre><br />6. Enter the following command to merge the custom script with the latest version of the script.<pre>git stash pop</pre>You might receive warnings related to any locally generated files that are not in the GitHub repo, such as finding reports. You can ignore these as long as the **prowler\_scan.sh** shows that the locally stashed changes are merged back in. | General AWS |

### (Optional) Clean up
<a name="optional-clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete all deployed resources. | You can leave the resources deployed in the accounts. If you shut down the EC2 instance when it is not in use and keep the S3 bucket empty, this reduces the costs of maintaining the resources for future scans.<br />If you want to deprovision all resources, do the following:1. Delete the `IAM-ProwlerExecRole` stack provisioned in the management account. For instructions, see [Deleting a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-cli-deleting-stack.html) in the CloudFormation documentation.<br />2. Delete the `IAM-ProwlerExecRole` stack set provisioned in the organization’s management account or in the delegated administrator account. For instructions, see [Delete a stack set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-delete.html) in the CloudFormation documentation.<br />3. Delete all objects in the `prowler-output` S3 bucket. For instructions, see [Deleting objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjects.html) in the Amazon S3 documentation.<br />4. Delete the `Prowler-Resources` stack provisioned in the security account. For instructions, see [Deleting a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-cli-deleting-stack.html) in the CloudFormation documentation. | AWS DevOps |

## Troubleshooting
<a name="create-a-consolidated-report-of-prowler-security-findings-from-multiple-aws-accounts-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Unable to connect to the EC2 instance by using Session Manager. | The SSM Agent must be able to communicate with the Systems Manager endpoint. Do the following:1. Validate the subnet where the EC2 instance is deployed has internet access.<br />2. Reboot the EC2 instance. |
| When deploying the stack set, the CloudFormation console prompts you to `Enable trusted access with AWS Organizations to use service-managed permissions`. | This indicates that trusted access has not been enabled between AWS Organizations and CloudFormation. Trusted access is required to deploy the service-managed stack set. Choose the button to enable trusted access. For more information, see [Enable trusted access](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.html) in the CloudFormation documentation. |

## Related resources
<a name="create-a-consolidated-report-of-prowler-security-findings-from-multiple-aws-accounts-resources"></a>

**AWS documentation**
+ [Implementing security controls on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/introduction.html) (AWS Prescriptive Guidance)

**Other resources**
+ [Prowler](https://github.com/prowler-cloud/prowler) (GitHub)

## Additional information
<a name="create-a-consolidated-report-of-prowler-security-findings-from-multiple-aws-accounts-additional"></a>

**Programmatically removing errors**

If the results contain `Access Denied` errors, you should remove them from the findings. These errors are typically due to external influencing permissions that prevent Prowler from assessing a particular resource. For example, some checks fail when reviewing S3 buckets provisioned through AWS Control Tower. You can programmatically extract these results and save the filtered results as a new file.

The following commands remove rows that contain a single text string (a pattern) and then output the results to a new file.
+ For Linux or MacOS (Grep)

  ```
  grep -v -i "Access Denied getting bucket" myoutput.csv > myoutput_modified.csv
  ```
+ For Windows (PowerShell)

  ```
  Select-String -Path myoutput.csv -Pattern 'Access Denied getting bucket' -NotMatch > myoutput_modified.csv
  ```

The following commands removes rows that match more than one text string and then output the results to a new file.
+ For Linux or MacOS (Uses an escaped pipe between strings)

  ```
  grep -v -i 'Access Denied getting bucket\|Access Denied Trying to Get' myoutput.csv > myoutput_modified.csv
  ```
+ For Windows (Uses a comma between strings)

  ```
  Select-String -Path myoutput.csv -Pattern 'Access Denied getting bucket', 'Access Denied Trying to Get' -NotMatch > myoutput_modified.csv
  ```

**Report examples**

The following image is an example of the **Findings** worksheet in the report of consolidated Prowler findings.

![Example of the Findings tab in the report of Prowler scan results](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/81ba9037-9958-4e4a-95b7-d68896075a5b/images/70311fc4-b919-4848-b200-40b35ce81826.png)

The following image is an example of the **Pass Fail** worksheet in the report of consolidated Prowler findings. (By default, pass results are excluded from the output.)

![Example of the Pass Fail tab in the report of Prowler scan results](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/81ba9037-9958-4e4a-95b7-d68896075a5b/images/4823e2be-4d5e-4676-9fa3-d47b065dc6d8.png)

The following image is an example of the **Severity** worksheet in the report of consolidated Prowler findings.

![Example of the Severity tab in the report of Prowler scan results](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/81ba9037-9958-4e4a-95b7-d68896075a5b/images/b7cbbff1-bca3-4667-9a1e-cc92e2e4adcd.png)
