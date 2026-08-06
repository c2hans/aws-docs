---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/clean-up-aft-resources-safely-after-state-file-loss.html
---

# Clean up AWS Account Factory for Terraform (AFT) resources safely after state file loss
<a name="clean-up-aft-resources-safely-after-state-file-loss"></a>

*Gokendra Malviya, Amazon Web Services*

## Summary
<a name="clean-up-aft-resources-safely-after-state-file-loss-summary"></a>

When you use AWS Account Factory for Terraform (AFT) to manage your AWS Control Tower environment, AFT generates a Terraform state file to track the state and configuration of the resources created by Terraform. Losing the Terraform state file can create significant challenges for resource management and cleanup. This pattern provides a systematic approach to safely identify and remove AFT-related resources while maintaining the integrity of your AWS Control Tower environment.

The process is designed to ensure proper removal of all AFT components, even without the original state file reference. This process provides a clear path to successfully re-establish and reconfigure AFT in your environment, to help ensure minimal disruption to your AWS Control Tower operations.

For more information about AFT, see the [AWS Control Tower documentation](https://docs.aws.amazon.com/controltower/latest/userguide/taf-account-provisioning.html).

## Prerequisites and limitations
<a name="clean-up-aft-resources-safely-after-state-file-loss-prereqs"></a>

**Prerequisites**
+ A thorough understanding of [AFT architecture](https://docs.aws.amazon.com/controltower/latest/userguide/aft-architecture.html).
+ Administrator access to the following accounts:
  + AFT Management account
  + AWS Control Tower Management account
  + Log Archive account
  + Audit account
+ Verification that no service control policies (SCPs) contain restrictions or limitations that would block the deletion of AFT-related resources.

**Limitations**
+ This process can clean up resources effectively, but it cannot recover lost state files, and some resources might require manual identification.
+ The duration of the cleanup process depends on your environment's complexity and might take several hours.
+ This pattern has been tested with AFT version 1.12.2 and deletes the following resources. If you're using a different version of AFT, you might have to delete additional resources.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/clean-up-aft-resources-safely-after-state-file-loss.html)

**Important**
The resources that are deleted by the steps in this pattern cannot be recovered. Before you follow these steps, verify the resource names carefully and make sure that they were created by AFT.

## Architecture
<a name="clean-up-aft-resources-safely-after-state-file-loss-architecture"></a>

The following diagram shows the AFT components and high-level workflow. AFT sets up a Terraform pipeline that helps you provision and customize your accounts in AWS Control Tower. AFT follows a GitOps model to automate the processes of account provisioning in AWS Control Tower. You create a Terraform file for an account request and commit it to a repository, which provides the input that triggers the AFT workflow for account provisioning. After account provisioning is complete, AFT can run additional customization steps automatically.

![AFT components and high-level workflow.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/1342c0a6-4b07-46df-a063-ceab2e2f83c8/images/3e0cae87-20ef-4fcc-aacf-bb450844ac56.png)

In this architecture:
+ **AWS Control Tower Management account** is an AWS account that's dedicated to the AWS Control Tower service. This is also typically referred to as the *AWS payer account* or *AWS Organizations Management account*.
+ **AFT Management account** is an AWS account that's dedicated to AFT management operations. This is different from your organization's management account.
+ **Vended account** is an AWS account that contains all the baseline components and controls that you selected. AFT uses AWS Control Tower to vend a new account.

For additional information about this architecture, see [Introduction to AFT](https://catalog.workshops.aws/control-tower/en-US/customization/aft) in the AWS Control Tower workshop.

## Tools
<a name="clean-up-aft-resources-safely-after-state-file-loss-tools"></a>

**AWS services**
+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) helps you set up and govern an AWS multi-account environment, following prescriptive best practices.
+ [AWS Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/taf-account-provisioning.html) sets up a Terraform pipeline to help you provision and customize accounts and resources in AWS Control Tower.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) helps you centrally manage and govern your environment as you grow and scale your AWS resources. Using Organizations, you can create accounts and allocate resources, group accounts to organize your workflows, apply policies for governance, and simplify billing by using a single payment method for all your accounts.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them. This pattern requires IAM roles and permissions.

**Other tools**
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.

## Best practices
<a name="clean-up-aft-resources-safely-after-state-file-loss-best-practices"></a>
+ For AWS Control Tower, see [Best practices for AWS Control Tower administrators](https://docs.aws.amazon.com/controltower/latest/userguide/best-practices.html) in the AWS Control Tower documentation.
+ For IAM, see [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Epics
<a name="clean-up-aft-resources-safely-after-state-file-loss-epics"></a>

### Delete AFT resources in the AFT Management account
<a name="delete-aft-resources-in-the-aft-management-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete resources that are identified by the AFT tag. | 1. Sign in to the AFT management account with administrator permissions.<br />2. Open the [AWS Resource Groups console](https://console.aws.amazon.com/resource-groups/).<br />3. Select the Region where AWS Control Tower has been deployed.<br />4. In the navigation pane, choose **Tag Editor**.<br />5. For **Resource types**, choose **All supported resource types**.<br />6. For **Tags**, type **managed\_by** as the tag key and **AFT** as the tag value.<br />7. Choose **Search resources**.<br />This search displays all resources that were created by AFT.<br />8. Identify the resource names and delete them by using the corresponding service consoles. For example, to delete Parameter Store resources:Open the [AWS Systems Manager console](https://console.aws.amazon.com/systems-manager/).In the navigation pane, choose **Parameter Store**.In the search box, click to display the dropdown, choose **Name**, choose **equals**, and then type **/aft**.Delete the parameters in batches of 10. (This is the maximum number you can delete at the same time.)<br />For AFT version 1.12.2, there will be approximately 62 Parameter Store resources to delete. All parameter names will start with **/aft**.<br />However, not all resources can be identified by AWS Resource Groups. In the following steps, you will find and delete the remaining resources. | AWS administrator, AWS DevOps, DevOps engineer |
| Delete IAM roles. | 1. Sign in to the AFT management account with administrator permissions.<br />2. Open the [IAM console](https://console.aws.amazon.com/iam/).<br />3. Delete these roles in the order listed (the order is important because of dependencies):`aft-*``AWSAFTAdmin``AWSAFTExecution``AWSAFTService``codebuild_trigger_role` | AWS administrator, AWS DevOps, DevOps engineer |
| Delete the AWS Backup backup vault. | 1. Open the [AWS Backup console](https://console.aws.amazon.com/backup/).<br />2. Locate the backup vault named `aws_backup_vault`.<br />3. Confirm that the vault doesn't contain any active backups.<br />4. Delete `aws_backup_vault`. | AWS administrator, AWS DevOps, DevOps engineer |
| Delete Amazon CloudWatch resources. | 1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).<br />2. Delete the following resources in the order listed:Event bus: Delete `aws_cloudwatch_event_bus`.Logs: Search for the prefix **AFT** and delete all related log groups.Query definitions: Delete the following queries:`Customization Logs by Account ID``Customization Logs by Customization Request ID` | AWS administrator, AWS DevOps, DevOps engineer |
| Delete AWS KMS resources. | 1. Switch to the secondary Region, which serves as the backend for state tracking of AFT's own state.<br />2. Open the [AWS KMS console](https://console.aws.amazon.com/kms/).<br />3. Delete the alias named **AFT**. | AWS administrator, AWS DevOps, DevOps engineer |

### Delete AFT resources in the Log Archive account
<a name="delete-aft-resources-in-the-log-archive-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete S3 buckets. | 1. Sign in to the Log Archive account with administrator permissions.<br />2. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/).<br />3. Empty the following buckets:`aws-aft-logs-471112509802-us-east-1``aws-aft-s3-access-logs-471112509802-us-east-1`<br />(Replace `111122223333` with your account ID.)<br />4. Delete the two buckets. | AWS administrator, AWS DevOps, DevOps engineer |
| Delete IAM roles. | 1. Open the [IAM console](https://console.aws.amazon.com/iam/).<br />2. Verify that the following roles aren't being used by any active services:`AWSAFTService``AWSAFTExecution`<br />3. Delete the two roles. | AWS administrator, AWS DevOps, DevOps engineer |

### Delete AFT resources in the Audit account
<a name="delete-aft-resources-in-the-audit-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete IAM roles. | 1. Sign in to the Audit account with administrator permissions.<br />2. Open the [IAM console](https://console.aws.amazon.com/iam/).<br />3. Verify that the following roles aren't being used by any active services:`AWSAFTService``AWSAFTExecution`<br />4. Delete the two roles. | AWS administrator, AWS DevOps, DevOps engineer |

### Delete AFT resources in the AWS Control Tower Management account
<a name="delete-aft-resources-in-the-ctower-management-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete IAM roles. | 1. Sign in to the AWS Control Tower Management account with administrator permissions.<br />2. Open the [IAM console](https://console.aws.amazon.com/iam/).<br />3. Verify that the following roles aren't being used by any active services:`AWSAFTService``AWSAFTExecution``aft-control-tower-events-rule`<br />4. Delete the three roles. | AWS administrator, AWS DevOps, DevOps engineer |
| Delete EventBridge rules. | 1. Open the [Amazon EventBridge console](https://console.aws.amazon.com/events/).<br />2. In the left navigation pane, choose **Rules**.<br />3. Find and select the rule named `aft-capture-ct-events`.<br />4. Choose **Delete** and confirm the deletion when prompted. | AWS administrator, AWS DevOps, DevOps engineer |

## Troubleshooting
<a name="clean-up-aft-resources-safely-after-state-file-loss-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Detaching the internet gateway was unsuccessful. | While you're deleting resources that are identified by the **AFT** tag, if you encounter this issue when you detach or delete the internet gateway, you first have to delete VPC endpoints:1. Sign in to the AFT Management account, and then open the [Amazon VPC console](https://console.aws.amazon.com/vpc/).<br />2. In the navigation pane, in the **Filter by VPC** list, choose the VPC named **aft-management-vpc**.<br />3. In the navigation pane, choose **Endpoints**.<br />4. Select the endpoints that are associated with the VPC **aft-management-vpc**.Double-check the VPC ID column before deletion to avoid removing the wrong endpoints.Be careful to delete only the endpoints that are associated with the AFT VPC.<br />5. Choose **Actions**, **Delete VPC endpoints**.<br />6. In the confirmation dialog box, type **delete** and then choose **Delete**.<br />7. Wait for the endpoint status to change to **Deleted**.<br />Deletion might take a few minutes to complete. |
| You're unable to find the specified CloudWatch queries. | If you are unable to find the CloudWatch queries that were created by AFT, follow these steps:1. Sign in to the AFT Management account, and then open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).<br />2. In the navigation pane, under **Logs**, choose **Logs Insights**.<br />3. In the upper-right corner, choose the **Saved and sample queries** icon.<br />You should now be able to see AFT queries. For a screenshot, see the [Additional information](#clean-up-aft-resources-safely-after-state-file-loss-additional) section.<br />4. Select the following queries, and then choose **Actions**, **Delete** to remove them.`Customization Logs by Account ID``Customization Logs by Customization Request ID` |

## Related resources
<a name="clean-up-aft-resources-safely-after-state-file-loss-resources"></a>
+ AFT:
  + [GitHub Repository](https://github.com/aws-ia/terraform-aws-control_tower_account_factory)
  + [Workshop](https://catalog.workshops.aws/control-tower/en-US/customization/aft)
  + [Documentation](https://docs.aws.amazon.com/controltower/latest/userguide/aft-getting-started.html)
+ [AWS Control Tower documentation](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html)

## Additional information
<a name="clean-up-aft-resources-safely-after-state-file-loss-additional"></a>

To view AFT queries on the CloudWatch Logs Insights dashboard, choose the **Saved and sample queries** icon from the upper-right corner, as illustrated in the following screenshot:

![Accessing AFT queries on the CloudWatch Logs Insights dashboard.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/1342c0a6-4b07-46df-a063-ceab2e2f83c8/images/255d4032-738b-4600-9084-9684d2e9a328.png)
