---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-data-from-microsoft-azure-blob-to-amazon-s3-by-using-rclone.html
---

# Migrate data from Microsoft Azure Blob to Amazon S3 by using Rclone
<a name="migrate-data-from-microsoft-azure-blob-to-amazon-s3-by-using-rclone"></a>

*Suhas Basavaraj, Aidan Keane, and Corey Lane, Amazon Web Services*

## Summary
<a name="migrate-data-from-microsoft-azure-blob-to-amazon-s3-by-using-rclone-summary"></a>

This pattern describes how to use [Rclone](https://rclone.org/) to migrate data from Microsoft Azure Blob object storage to an Amazon Simple Storage Service (Amazon S3) bucket. You can use this pattern to perform a one-time migration or an ongoing synchronization of the data. Rclone is a command-line program written in Go and is used to move data across various storage technologies from cloud providers.

## Prerequisites and limitations
<a name="migrate-data-from-microsoft-azure-blob-to-amazon-s3-by-using-rclone-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Data stored in Azure Blob container service

## Architecture
<a name="migrate-data-from-microsoft-azure-blob-to-amazon-s3-by-using-rclone-architecture"></a>

**Source technology stack**
+ Azure Blob storage container

**Target technology stack**
+ Amazon S3 bucket
+ Amazon Elastic Compute Cloud (Amazon EC2) Linux instance

**Architecture**

![Migrating data from Microsoft Azure to Amazon S3](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/6ead815d-7768-4726-b27d-97a70cd21081/images/abe69eee-632f-4ca2-abf6-3223f3f3ec94.png)

## Tools
<a name="migrate-data-from-microsoft-azure-blob-to-amazon-s3-by-using-rclone-tools"></a>
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Rclone](https://rclone.org/) is an open-source command-line program inspired by **rsync**. It is used to manage files across many cloud storage platforms.

## Best practices
<a name="migrate-data-from-microsoft-azure-blob-to-amazon-s3-by-using-rclone-best-practices"></a>

When you migrate data from Azure to Amazon S3, be mindful of these considerations to avoid unnecessary costs or slow transfer speeds:
+ Create your AWS infrastructure in the same geographical Region as the Azure storage account and Blob container—for example, AWS Region `us-east-1` (N. Virginia) and Azure region `East US`.
+ Avoid using NAT Gateway if possible, because it accrues data transfer fees for both ingress and egress bandwidth.
+ Use a [VPC gateway endpoint for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) to increase performance.
+ Consider using an AWS Graviton2 (ARM) processor-based EC2 instance for lower cost and higher performance over Intel x86 instances. Rclone is heavily cross-compiled and provides a precompiled ARM binary.

## Epics
<a name="migrate-data-from-microsoft-azure-blob-to-amazon-s3-by-using-rclone-epics"></a>

### Prepare AWS and Azure cloud resources
<a name="prepare-aws-and-azure-cloud-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare a destination S3 bucket. | [Create a new S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the appropriate AWS Region or choose an existing bucket as the destination for the data you want to migrate. | AWS administrator |
| Create an IAM instance role for Amazon EC2. | [Create a new AWS Identity and Access Management (IAM) role for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#working-with-iam-roles). This role gives your EC2 instance write access to the destination S3 bucket. | AWS administrator |
| Attach a policy to the IAM instance role. | Use the IAM console or AWS Command Line Interface (AWS CLI) to create an inline policy for the EC2 instance role that allows write access permissions to the destination S3 bucket. For an example policy, see the [Additional information](#migrate-data-from-microsoft-azure-blob-to-amazon-s3-by-using-rclone-additional) section. | AWS administrator |
| Launch an EC2 instance. | Launch an Amazon Linux EC2 instance that is configured to use the newly created IAM service role. This instance will also need access to Azure public API endpoints through the internet. Consider using [AWS Graviton-based EC2 instances](https://docs.aws.amazon.com/compute-optimizer/latest/ug/graviton-recommendations.html) to lower costs. Rclone provides ARM-compiled binaries. | AWS administrator |
| Create an Azure AD service principal. | Use the Azure CLI to create an Azure Active Directory (Azure AD) service principal that has read-only access to the source Azure Blob storage container. For instructions, see the [Additional information](#migrate-data-from-microsoft-azure-blob-to-amazon-s3-by-using-rclone-additional) section. Store these credentials on your EC2 instance to the location `~/azure-principal.json`. | Cloud administrator, Azure |

### Install and configure Rclone
<a name="install-and-configure-rclone"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download and install Rclone.  | Download and install the Rclone command-line program. For installation instructions, see the [Rclone installation documentation](https://rclone.org/install/). | General AWS, Cloud administrator |
| Configure Rclone. | Copy the following `rclone.conf` sample file. Replace `AZStorageAccount` with your Azure Storage account name and `us-east-1` with the AWS Region where your S3 bucket is located. Save this file to the location `~/.config/rclone/rclone.conf` on your EC2 instance.<pre>[AZStorageAccount]<br />type = azureblob<br />account = AZStorageAccount<br />service_principal_file = azure-principal.json<br /><br />[s3]<br />type = s3<br />provider = AWS<br />env_auth = true<br />region = us-east-1</pre> | General AWS, Cloud administrator |
| Verify Rclone configuration. | To confirm that Rclone is configured and permissions are working properly, verify that Rclone can parse your configuration file and that objects inside your Azure Blob container and S3 bucket are accessible. See the following for example validation commands.+ List the configured remotes in the configuration file. This will ensure that your configuration file is being parsed correctly. Review the output to make sure that it matches your `rclone.conf` file.<pre>rclone listremotes<br />AZStorageAccount:<br />s3:</pre><br />+ List the Azure Blob containers in the configured account. Replace `AZStorageAccount` with the storage account name that you used in the `rclone.conf` file.<pre>rclone lsd AZStorageAccount:<br />2020-04-29 08:29:26  docs</pre><br />+ List the files in the Azure Blob container. Replace docs in this command with an actual Blob container name in your Azure storage account.<pre>rclone ls AZStorageAccount:docs<br />824884 administrator-en.a4.pdf</pre><br />+ List the buckets in your AWS account.<pre>[root@ip-10-0-20-157 ~]# rclone lsd s3:<br />2022-03-07 01:44:40        DOC-EXAMPLE-BUCKET<br />2022-03-07 01:45:16        DOC-EXAMPLE-BUCKET<br />2022-03-07 02:12:07        DOC-EXAMPLE-BUCKET</pre><br />+ List the files in the S3 bucket.<pre>[root@ip-10-0-20-157 ~]# rclone ls s3:DOC-EXAMPLE-BUCKET<br />template0.yaml<br />template1.yaml</pre> | General AWS, Cloud administrator |

### Migrate data using Rclone
<a name="migrate-data-using-rclone"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate data from your containers. | Run the Rclone [copy](https://rclone.org/commands/rclone_copy/) or [sync](https://rclone.org/commands/rclone_sync/) command.  <br />**Example: copy**<br />This command copies data from the source Azure Blob container to the destination S3 bucket.<pre>rclone copy AZStorageAccount:blob-container s3:DOC-EXAMPLE-BUCKET</pre><br />**Example: sync**<br />This command synchronizes data between the source Azure Blob container and the destination S3 bucket. ** **<pre>rclone sync AZStorageAccount:blob-container s3:DOC-EXAMPLE-BUCKET</pre>When you use the **sync **command, data that isn't present in the source container will be deleted from the destination S3 bucket. | General AWS, Cloud administrator |
| Synchronize your containers.  | After the initial copy is complete, run the Rclone **sync** command for ongoing migration so that only new files that are missing from the destination S3 bucket will be copied. | General AWS, Cloud administrator |
| Verify that data has been migrated successfully.  | To check that data was successfully copied to the destination S3 bucket, run the Rclone [lsd](https://rclone.org/commands/rclone_lsd/) and [ls](https://rclone.org/commands/rclone_ls/) commands. | General AWS, Cloud administrator |

## Related resources
<a name="migrate-data-from-microsoft-azure-blob-to-amazon-s3-by-using-rclone-resources"></a>
+ [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) (AWS documentation)
+ [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) (AWS documentation)
+ [Creating a Microsoft Azure Blob container](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal) (Microsoft Azure documentation)
+ [Rclone commands](https://rclone.org/commands/) (Rclone documentation)

## Additional information
<a name="migrate-data-from-microsoft-azure-blob-to-amazon-s3-by-using-rclone-additional"></a>

**Example role policy for EC2 instances**

This policy gives your EC2 instance read and write access to a specific bucket in your account. If your bucket uses a customer managed key for server-side encryption, the policy might need additional access to AWS Key Management Service (AWS KMS) .

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:DeleteObject",
                "s3:GetObject",
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            "Resource": [
              "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*",
              "arn:aws:s3:::DOC-EXAMPLE-BUCKET"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "arn:aws:s3:::*"
        }
    ]
}
```

**Creating a read-only Azure AD service principal**

An Azure service principal is a security identity that is used by customer applications, services, and automation tools to access specific Azure resources. Think of it as a user identity (login and password or certificate) with a specific role and tightly controlled permissions to access your resources. To create a read-only service principal to follow least privilege permissions and protect data in Azure from accidental deletions, follow these steps:

1. Log in to your Microsoft Azure cloud account portal and launch Cloud Shell in PowerShell or use the Azure Command-Line Interface (CLI) on your workstation.

1. Create a service principal and configure it with [read-only](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-reader) access to your Azure Blob storage account. Save the JSON output of this command to a local file called `azure-principal.json`. The file will be uploaded to your EC2 instance. Replace the placeholder variables that are shown in braces (`{` and `}`) with your Azure subscription ID, resource group name, and storage account name.

   ```
   az ad sp create-for-rbac `
   --name AWS-Rclone-Reader `
   --role "Storage Blob Data Reader" `
   --scopes /subscriptions/{Subscription ID}/resourceGroups/{Resource Group Name}/providers/Microsoft.Storage/storageAccounts/{Storage Account Name}
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
