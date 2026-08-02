---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/move-mainframe-files-directly-to-amazon-s3-using-transfer-family.html
---

# Move mainframe files directly to Amazon S3 using Transfer Family
<a name="move-mainframe-files-directly-to-amazon-s3-using-transfer-family"></a>

*Luis Gustavo Dantas, Amazon Web Services*

## Summary
<a name="move-mainframe-files-directly-to-amazon-s3-using-transfer-family-summary"></a>

As part of the modernization journey, you can face the challenge of transferring files between your on-premises servers and the Amazon Web Services (AWS) Cloud. Transferring data from mainframes can be a significant challenge because mainframes typically can’t access modern data stores like Amazon Simple Storage Service (Amazon S3), Amazon Elastic Block Store (Amazon EBS), or Amazon Elastic File System (Amazon EFS).

Many customers use intermediate staging resources, such as on-premises Linux, Unix, or Windows servers, to transfer files to the AWS Cloud. You can avoid this indirect method by using AWS Transfer Family with the Secure Shell (SSH) File Transfer Protocol (SFTP) to upload mainframe files directly to Amazon S3.

## Prerequisites and limitations
<a name="move-mainframe-files-directly-to-amazon-s3-using-transfer-family-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A virtual private cloud (VPC) with a subnet that’s reachable by your legacy platform
+ A Transfer Family endpoint for your VPC
+ Mainframe Virtual Storage Access Method (VSAM) files converted to sequential, [fixed-length files](https://www.ibm.com/docs/en/zos/2.1.0?topic=reports-converting-vb-fb) (IBM documentation)

**Limitations**
+ SFTP transfers files in binary mode by default, which means that files are uploaded to Amazon S3 with EBCDIC encoding preserved. If your file doesn't contain binary or packed data, then you can use the **sftp **[ascii subcommand](https://www.ibm.com/docs/en/zos/2.3.0?topic=version-what-zos-openssh-supports) (IBM documentation) to convert your files to text during the transfer.
+ You must [unpack mainframe files](https://apg-library.amazonaws.com/content/f5907bfe-7dff-4cd0-8523-57015ad48c4b) (AWS Prescriptive Guidance) that contain packed and binary content to use these files in your target environment.
+ Amazon S3 objects can range in size from a minimum of 0 bytes to a maximum of 5 TB. For more information about Amazon S3 capabilities, see [Amazon S3 FAQs](https://aws.amazon.com/s3/faqs/?nc1=h_ls).

## Architecture
<a name="move-mainframe-files-directly-to-amazon-s3-using-transfer-family-architecture"></a>

**Source technology stack**
+ Job control language (JCL)
+ z/OS Unix shell and ISPF
+ SFTP
+ VSAM and flat files

**Target technology stack**
+ Transfer Family
+ Amazon S3
+ Amazon Virtual Private Cloud (Amazon VPC)

**Target architecture**

The following diagram shows a reference architecture for using Transfer Family with SFTP to upload mainframe files directly to an S3 bucket.

![Using Transfer Family with SFTP to upload mainframe files directly to an S3 bucket](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/1f4fa1fd-b681-41bc-81d8-d556426b14c2/images/110491d5-b58d-4451-8de9-e742756bb192.png)

The diagram shows the following workflow:

1. You use a JCL job to transfer your mainframe files from the legacy mainframe to the AWS Cloud through Direct Connect.

1. Direct Connect enables your network traffic to remain on the AWS global network and bypass the public internet. Direct Connect also enhances the network speed, starting at 50 Mbps and scaling up to 100 Gbps.

1. The VPC endpoint enables connections between your VPC resources and the supported services without using the public internet. Access to Transfer Family and Amazon S3 achieves high availability by taking place through the elastic network interfaces located in two private subnets and Availability Zones.

1. Transfer Family authenticates users and uses SFTP to receive your files from the legacy environment and move them to an S3 bucket.

**Automation and scale**

After the Transfer Family service is in place, you can transfer an unlimited number of files from the mainframe to Amazon S3 by using a JCL job as the SFTP client. You can also automate the file transfer by using a mainframe batch job scheduler to run the SFTP jobs when you’re ready to transfer the mainframe files.

## Tools
<a name="move-mainframe-files-directly-to-amazon-s3-using-transfer-family-tools"></a>
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.
+ [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html) enables you to securely scale your recurring business-to-business file transfers to Amazon S3 and Amazon EFS by using SFTP, FTPS, and FTP protocols.

## Epics
<a name="move-mainframe-files-directly-to-amazon-s3-using-transfer-family-epics"></a>

### Create the S3 bucket and the access policy
<a name="create-the-s3-bucket-and-the-access-policy"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the S3 bucket. | [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) to host the files that you transfer from your legacy environment. | General AWS |
| Create the IAM role and policy. | Transfer Family uses your AWS Identity and Access Management (IAM) role to grant access to the S3 bucket that you created earlier.<br />[Create an IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) that includes the following [IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html):<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Sid": "UserFolderListing",<br />            "Action": [<br />                "s3:ListBucket",<br />                "s3:GetBucketLocation"<br />            ],<br />            "Effect": "Allow",<br />            "Resource": [<br />                "arn:aws:s3:::<your-bucket-name>"<br />            ]<br />        },<br />        {<br />            "Sid": "HomeDirObjectAccess",<br />            "Effect": "Allow",<br />            "Action": [<br />                "s3:PutObject",<br />                "s3:GetObjectAcl",<br />                "s3:GetObject",<br />                "s3:DeleteObjectVersion",<br />                "s3:DeleteObject",<br />                "s3:PutObjectAcl",<br />                "s3:GetObjectVersion"<br />            ],<br />            "Resource": "arn:aws:s3:::<your-bucket-name>/*"<br />        }<br />    ]<br />}</pre>You must choose the Transfer use case when you create the IAM role. | General AWS |

### Define the transfer service
<a name="define-the-transfer-service"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the SFTP server. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/move-mainframe-files-directly-to-amazon-s3-using-transfer-family.html)For more information about how to set up an SFTP server, see [Create an SFTP-enabled server](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-sftp.html) (AWS Transfer Family User Guide). | General AWS |
| Get the server address. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/move-mainframe-files-directly-to-amazon-s3-using-transfer-family.html) | General AWS |
| Create the SFTP client key pair. | Create an SSH key pair for either [Microsoft Windows](https://docs.aws.amazon.com/transfer/latest/userguide/key-management.html#windows-ssh) or [macOS/Linux/UNIX](https://docs.aws.amazon.com/transfer/latest/userguide/key-management.html#macOS-linux-unix-ssh). | General AWS, SSH |
| Create the SFTP user. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/move-mainframe-files-directly-to-amazon-s3-using-transfer-family.html) | General AWS |

### Transfer the mainframe file
<a name="transfer-the-mainframe-file"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Send the SSH private key to the mainframe. | Use SFTP or SCP to send the SSH private key to the legacy environment.<br />SFTP example:<pre>sftp [USERNAME@mainframeIP]<br />[password]<br />cd [/u/USERNAME]<br />put [your-key-pair-file]</pre><br />SCP example:<pre>scp [your-key-pair-file] [USERNAME@MainframeIP]:/[u/USERNAME]</pre><br />Next, store the SSH key in the z/OS Unix file system under the user name that will later run the file transfer batch job (for example, `/u/CONTROLM`). For more information about z/OS Unix shell, see [An introduction to the z/OS shells](https://www.ibm.com/docs/en/zos/2.2.0?topic=shells-introduction-zos) (IBM documentation). | Mainframe, z/OS Unix shell, FTP, SCP |
| Create the JCL SFTP client. | Because mainframes don't have a native SFTP client, you must use the BPXBATCH utility to run the SFTP client from the z/OS Unix shell.<br />In the ISPF editor, create the JCL SFTP client. For example:<pre>//JOBNAM JOB ...<br />//**********************************************************************<br />//SFTP EXEC PGM=BPXBATCH,REGION=0M <br />//STDPARM DD * <br />SH cp "//'MAINFRAME.FILE.NAME'" filename.txt; <br />echo 'put filename.txt' > uplcmd; <br />sftp -b uplcmd -i ssh_private_key_file ssh_username@<transfer service ip or DNS>; <br />//SYSPRINT DD SYSOUT=* <br />//STDOUT DD SYSOUT=* <br />//STDENV DD * <br />//STDERR DD SYSOUT=*</pre>For more information about how to run a command in the z/OS Unix shell, see [The BPXBATCH utility](https://www.ibm.com/docs/en/zos/2.2.0?topic=ispf-bpxbatch-utility) (IBM documentation). For more information about how to create or edit JCL jobs in z/OS, see [What is ISPF?](https://www.ibm.com/docs/en/zos-basic-skills?topic=interfaces-what-is-ispf) and [The ISPF editor](https://www.ibm.com/docs/en/zos-basic-skills?topic=ispf-editor) (IBM documentation). | JCL, Mainframe, z/OS Unix shell |
| Run the JCL SFTP client. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/move-mainframe-files-directly-to-amazon-s3-using-transfer-family.html)For more information about how to check the activity of batch jobs, see [z/OS SDSF User's Guide](https://www.ibm.com/docs/en/zos/2.4.0?topic=sdsf-zos-users-guide) (IBM documentation). | Mainframe, JCL, ISPF |
| Validate the file transfer. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/move-mainframe-files-directly-to-amazon-s3-using-transfer-family.html) | General AWS |
| Automate the JCL SFTP client. | Use job scheduler to automatically trigger the JCL SFTP client.You can use mainframe job schedulers, such as [BMC Control-M](https://www.bmcsoftware.pt/it-solutions/control-m.html) or [CA Workload Automation](https://www.broadcom.com/products/mainframe/workload-automation/ca7), to automate batch jobs for file transfers based on time and other batch job dependencies. | Job scheduler |

## Related resources
<a name="move-mainframe-files-directly-to-amazon-s3-using-transfer-family-resources"></a>
+ [How AWS Transfer Family works](https://docs.aws.amazon.com/transfer/latest/userguide/how-aws-transfer-works.html)
