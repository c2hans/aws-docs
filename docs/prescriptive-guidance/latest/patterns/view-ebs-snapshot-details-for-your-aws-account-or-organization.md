---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/view-ebs-snapshot-details-for-your-aws-account-or-organization.html
---

# View EBS snapshot details for your AWS account or organization
<a name="view-ebs-snapshot-details-for-your-aws-account-or-organization"></a>

*Arun Chandapillai and Parag Nagwekar, Amazon Web Services*

## Summary
<a name="view-ebs-snapshot-details-for-your-aws-account-or-organization-summary"></a>

This pattern describes how you can automatically generate an on-demand report of all Amazon Elastic Block Store (Amazon EBS) snapshots in your Amazon Web Services (AWS) account or organizational unit (OU) in AWS Organizations.

Amazon EBS is an easy-to-use, scalable, high-performance block- storage service designed for Amazon Elastic Compute Cloud (Amazon EC2). An EBS volume provides durable and persistent storage that you can attach to your EC2 instances. You can use EBS volumes as primary storage for your data and take a point-in-time backup of your EBS volumes by creating a snapshot. You can use the AWS Management Console or the AWS Command Line Interface (AWS CLI) to view the details of specific EBS snapshots. This pattern provides a programmatic way to retrieve information about all EBS snapshots in your AWS account or OU.

You can use the script provided by this pattern to generate a comma-separated values (CSV) file that has the following information about each snapshot: account ID, snapshot ID, volume ID and size, the date the snapshot was taken, instance ID, and description. If your EBS snapshots are tagged, the report also includes the owner and team attributes.

## Prerequisites and limitations
<a name="view-ebs-snapshot-details-for-your-aws-account-or-organization-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ AWS CLI version 2 [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ AWS Identity and Access Management (IAM) role with the appropriate permissions (access permissions for a specific account or for all accounts in an OU if you’re planning to run the script from AWS Organizations)

## Architecture
<a name="view-ebs-snapshot-details-for-your-aws-account-or-organization-architecture"></a>

The following diagram shows the script workflow that generates an on-demand report of EBS snapshots that are spread across multiple AWS accounts in an OU.

![Generating an on-demand report of EBS snapshots across OUs.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4e8b1812-2731-4f46-8385-0dd4d92f2d03/images/62d10408-7c85-46cf-a6a4-fe87a6e446f2.png)

## Tools
<a name="view-ebs-snapshot-details-for-your-aws-account-or-organization-tools"></a>

**AWS services**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) provides block-level storage volumes for use with EC2 instances.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.

**Code **

The code for the sample application used in this pattern is available on GitHub, in the [aws-ebs-snapshots-awsorganizations](https://github.com/aws-samples/aws-ebs-snapshots-awsorganizations) repository. Follow the instructions in the next section to use the sample files.

## Epics
<a name="view-ebs-snapshot-details-for-your-aws-account-or-organization-epics"></a>

### Download the script
<a name="download-the-script"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the Python script. | Download the script  [GetSnapshotDetailsAllAccountsOU.py](https://github.com/aws-samples/aws-ebs-snapshots-awsorganizations/blob/main/GetSnapshotDetailsAllAccountsOU.py) from the [GitHub repository](https://github.com/aws-samples/aws-ebs-snapshots-awsorganizations). | General AWS |

### Get EBS snapshot details for an AWS account
<a name="get-ebs-snapshot-details-for-an-aws-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the Python script. | Run the command:<pre>python3 getsnapshotinfo.py --file <output-file>.csv --region <region-name> </pre><br />where `<output-file>` refers to the CSV output file where you want information about the EBS snapshots placed, and `<region-name>` is the AWS Region where the snapshots are stored. For example:<pre>python3 getsnapshotinfo.py --file snapshots.csv --region us-east-1 </pre> | General AWS |

### Get EBS snapshot details for an organization
<a name="get-ebs-snapshot-details-for-an-organization"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the Python script. | Run the command:<pre>python3 getsnapshotinfo.py --file <output-file>.csv --role <IAM-role> --region <region-name> </pre><br />where `<output-file>` refers to the CSV output file where you want information about the EBS snapshots placed, `<IAM-role>` is a role that provides permissions to access AWS Organizations, and `<region-name>` is the AWS Region where the snapshots are stored. For example:<pre>python3 getsnapshotinfo.py --file snapshots.csv --role <IAM role> --region us-west-2</pre> | General AWS |

## Related resources
<a name="view-ebs-snapshot-details-for-your-aws-account-or-organization-resources"></a>
+ [Amazon EBS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)
+ [Amazon EBS actions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-ebs.html)
+ [Amazon EBS API reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ebs/index.html)
+ [Improving Amazon EBS performance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSPerformance.html)
+ [Amazon EBS resources](https://aws.amazon.com/ebs/resources/)
+ [EBS snapshot pricing](https://aws.amazon.com/ebs/pricing/)

## Additional information
<a name="view-ebs-snapshot-details-for-your-aws-account-or-organization-additional"></a>

**EBS snapshot types**

Amazon EBS provides three types of snapshots, based on ownership and access:
+ **Owned by you** –** **By default, only you can create volumes from snapshots that you own.
+ **Public snapshots** – You can share snapshots publicly with all other AWS accounts. To create a public snapshot, you modify the permissions for a snapshot to share it with the AWS accounts that you specify. Users that you will authorize can then use the snapshots you share by creating their own EBS volumes, while your original snapshot remains unaffected. You can also make your unencrypted snapshots available publicly to all AWS users. However, you can't make your encrypted snapshots available publicly for security reasons. Public snapshots pose a significant security risk because of the possibility of exposing personal and sensitive data. We strongly recommend against sharing your EBS snapshots with all AWS accounts. For more information about sharing snapshots, see the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html).
+ **Private snapshots** – You can share snapshots privately with individual AWS accounts that you specify. To share the snapshot privately with specific AWS accounts, follow the [instructions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html#share-unencrypted-snapshot) in the AWS documentation, and choose **Private** for the permissions setting. Users that you have authorized can use the snapshots that you share to create their own EBS volumes, while your original snapshot remains unaffected.

**Overviews and procedures**

The following table provides links to more information about EBS snapshots, including how you can lower EBS volume costs by finding and deleting unused snapshots, and archive rarely accessed snapshots that do not require frequent or fast retrieval.

|
|
| For information about | See |
| --- |--- |
| **Snapshots, their features, and limitations** | [Create Amazon EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-snapshot.html) |
| **How to create a snapshot** | Console: [Create a snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-snapshot.html#ebs-create-snapshot)<br />AWS CLI: [create-snapshot command](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-snapshot.html)<br />For example:<pre>aws ec2 create-snapshot --volume-id vol-1234567890abcdef0 --description " volume snapshot"</pre> |
| **Deleting snapshots (general information)** | [Delete an Amazon EBS snapshot](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-deleting-snapshot.html) |
| **How to delete a snapshot** | Console: [Delete a snapshot](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-deleting-snapshot.html#ebs-delete-snapshot)<br />AWS CLI: [delete-snapshot command](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-snapshot.html)<br />For example:<pre>aws ec2 delete-snapshot --snapshot-id snap-1234567890abcdef0</pre> |
| **Archiving snapshots (general information)** | [Archive Amazon EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/snapshot-archive.html)<br />[Amazon EBS Snapshots Archive](https://aws.amazon.com/blogs/aws/new-amazon-ebs-snapshots-archive/) (blog post) |
| **How to archive a snapshot** | Console: [Archive a snapshot](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/working-with-snapshot-archiving.html#archive-snapshot)<br />AWS CLI: [modify-snapshot-tier command](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-snapshot-tier.html) |
| **How to retrieve an archived snapshot** | Console: [Restore an archived snapshot](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/working-with-snapshot-archiving.html#restore-archived-snapshot)<br />AWS CLI: [restore-snapshot-tier command](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/restore-snapshot-tier.html) |
| **Snapshot pricing** | [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/) |

**FAQ**

**What is the minimum archive period?**

The minimum archive period is 90 days.

**How long would it take to restore an archived snapshot?**

It can take up to 72 hours to restore an archived snapshot from the archive tier to the standard tier, depending on the size of the snapshot.

**Are archived snapshots full snapshots?**

Archived snapshots are always full snapshots.

**Which snapshots can a user archive?**

You can archive only snapshots that you own in your account.

**Can you archive a snapshot of the root device volume of a registered Amazon Machine Image (AMI)?**

No, you can’t archive a snapshot of the root device volume of a registered AMI.

**What are security considerations for sharing a snapshot?**

When you share a snapshot, you are giving others access to all the data on the snapshot. Share snapshots only with people that you trust with your data.

**How do you share a snapshot with another AWS Region?**

Snapshots are constrained to the Region in which they were created. To share a snapshot with another Region, copy the snapshot to that Region and then share the copy.

**Can you share snapshots that are encrypted?**

You can't share snapshots that are encrypted with the default AWS managed key. You can share snapshots that are encrypted with a customer managed key only. When you share an encrypted snapshot, you must also share the customer managed key that was used to encrypt the snapshot.

**What about unencrypted snapshots?**

You can share unencrypted snapshots publicly.
