---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/back-up-and-archive-mainframe-data-to-amazon-s3-using-bmc-ami-cloud-data.html
---

# Back up and archive mainframe data to Amazon S3 using BMC AMI Cloud Data
<a name="back-up-and-archive-mainframe-data-to-amazon-s3-using-bmc-ami-cloud-data"></a>

*Santosh Kumar Singh, Gilberto Biondo, and Maggie Li, Amazon Web Services*

*Mikhael Liberman, Model9 Mainframe Software*

## Summary
<a name="back-up-and-archive-mainframe-data-to-amazon-s3-using-bmc-ami-cloud-data-summary"></a>

This pattern demonstrates how to back up and archive mainframe data directly to Amazon Simple Storage Service (Amazon S3), and then recall and restore that data to the mainframe by using BMC AMI Cloud Data (previously known as Model9 Manager). If you are looking for a way to modernize your backup and archive solution as part of a mainframe modernization project or to meet compliance requirements, this pattern can help meet those goals.

Typically, organizations that run core business applications on mainframes use a virtual tape library (VTL) to back up data stores such as files and logs. This method can be expensive because it consumes billable MIPS, and the data stored on tapes outside the mainframe is inaccessible. To avoid these issues, you can use BMC AMI Cloud Data to quickly and cost-effectively transfer operational and historical mainframe data directly to Amazon S3. You can use BMC AMI Cloud Data to back up and archive data over TCP/IP to AWS while taking advantage of IBM z Integrated Information Processor (zIIP) engines to reduce cost, parallelism, and transfer times.

## Prerequisites and limitations
<a name="back-up-and-archive-mainframe-data-to-amazon-s3-using-bmc-ami-cloud-data-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ BMC AMI Cloud Data with a valid license key
+ TCP/IP connectivity between the mainframe and AWS
+ An AWS Identity and Access Management (IAM) role for read/write access to an S3 bucket
+ Mainframe security product (RACF) access in place to run BMC AMI Cloud processes
+ A BMC AMI Cloud z/OS agent (Java version 8 64-bit SR5 FP16 or later) that has available network ports, firewall rules permitting access to S3 buckets, and a dedicated z/FS file system
+ [Requirements](https://docs.bmc.com/docs/cdacv27/management-server-requirements-1245343255.html) met for the BMC AMI Cloud management server

**Limitations**
+ BMC AMI Cloud Data stores its operational data in a PostgreSQL database that runs as a Docker container on the same Amazon Elastic Compute Cloud (Amazon EC2) instance as the management server. Amazon Relational Database Service (Amazon RDS) is not currently supported as a backend for BMC AMI Cloud Data. For more information about the latest product updates, see [What's New?](https://docs.bmc.com/docs/cdacv27/what-s-new-1245343246.html) in the BMC documentation.
+ This pattern backs up and archives z/OS mainframe data only. BMC AMI Cloud Data backs up and archives only mainframe files.
+ This pattern doesn’t convert data into standard open formats such as JSON or CSV. Use an additional transformation service such as [BMC AMI Cloud Analytics](https://www.bmc.com/it-solutions/bmc-ami-cloud-analytics.html) (previously known as Model9 Gravity) to convert the data into standard open formats. Cloud-native applications and data analytics tools can access the data after it's is written to the cloud.

**Product versions**
+ BMC AMI Cloud Data version 2.x

## Architecture
<a name="back-up-and-archive-mainframe-data-to-amazon-s3-using-bmc-ami-cloud-data-architecture"></a>

**Source technology stack**
+ Mainframe running z/OS
+ Mainframe files such as datasets and z/OS UNIX System Services (USS) files
+ Mainframe disk, such as a direct-access storage device (DASD)
+ Mainframe tape (virtual or physical tape library)

**Target technology stack**
+ Amazon S3
+ Amazon EC2 instance in a virtual private cloud (VPC)
+ AWS Direct Connect
+ Amazon Elastic File System (Amazon EFS)

**Target architecture**

The following diagram shows a reference architecture where BMC AMI Cloud Data software agents on a mainframe drive the legacy data backup and archive processes that store the data in Amazon S3.

![BMC AMI Cloud Data software agents on a mainframe driving legacy data backup and archive processes](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/bde3b029-184e-4eb0-933b-f8caf6cc40ab/images/a24cd6c1-b131-49ea-8238-f3aea5ab8134.png)

The diagram shows the following workflow:

1. BMC AMI Cloud Data software agents run on mainframe logical partitions (LPARs). The software agents read and write mainframe data from DASD or tape directly to Amazon S3 over TCP/IP.

1. AWS Direct Connect sets up a physical, isolated connection between the on-premises network and AWS. For enhanced security, run a site-to-site VPN on top of Direct Connect to encrypt data in transit.

1. The S3 bucket stores mainframe files as object storage data, and BMC AMI Cloud Data agents directly communicate with the S3 buckets. Certificates are used for HTTPS encryption of all communications between the agent and Amazon S3. Amazon S3 data encryption is used to encrypt and protect the data at rest.

1. BMC AMI Cloud Data management servers run as Docker containers on EC2 instances. The instances communicate with agents running on mainframe LPARs and S3 buckets.

1. Amazon EFS is mounted on both active and passive EC2 instances to share the Network File System (NFS) storage. This is to make sure that metadata related to a policy created on the management server isn't lost in the event of a failover. In the event of a failover by the active server, the passive server can be accessed without any data loss. If the passive server fails, the active server can be accessed without any data loss.

## Tools
<a name="back-up-and-archive-mainframe-data-to-amazon-s3-using-bmc-ami-cloud-data-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) helps you create and configure shared file systems in the AWS Cloud.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve nearly any amount of data.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.
+ [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) links your internal network to a AWS Direct Connect location over a standard Ethernet fiber-optic cable. With this connection, you can create virtual interfaces directly to public AWS services while bypassing internet service providers in your network path.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.

**BMC tools**
+ [BMC AMI Cloud management server](https://docs.bmc.com/docs/cdacv27/bmc-ami-cloud-overview-1245343249.html) is a GUI application that runs as a Docker container on an Amazon Linux Amazon Machine Image (AMI) for Amazon EC2. The management server provides the functionality to manage BMC AMI Cloud activities such as reporting, creating and managing policies, running archives, and performing backups, recalls, and restores.
+ [BMC AMI Cloud agent](https://docs.bmc.com/docs/cdacv27/bmc-ami-cloud-overview-1245343249.html) runs on an on-premises mainframe LPAR that reads and writes files directly to object storage by using TCP/IP. A started task runs on a mainframe LPAR and is responsible for reading and writing backup and archive data to and from Amazon S3.
+ [BMC AMI Cloud Mainframe Command Line Interface (M9CLI)](https://docs.bmc.com/docs/cdacv27/command-line-interface-cli-reference-1245343519.html) provides you with a set of commands to perform BMC AMI Cloud actions directly from TSO/E or in batch operations, without the dependency on the management server.

## Epics
<a name="back-up-and-archive-mainframe-data-to-amazon-s3-using-bmc-ami-cloud-data-epics"></a>

### Create an S3 bucket and IAM policy
<a name="create-an-s3-bucket-and-iam-policy"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket. | [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) to store the files and volumes that you want to back up and archive from your mainframe environment. | General AWS |
| Create an IAM policy. | All BMC AMI Cloud management servers and agents require access to the S3 bucket that you created in the previous step.<br />To grant the required access, create the following IAM policy:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Sid": "Listfolder",<br />            "Action": [<br />                "s3:ListBucket",<br />                "s3:GetBucketLocation",<br />                "s3:ListBucketVersions"<br />            ],<br />            "Effect": "Allow",<br />            "Resource": [<br />                "arn:aws:s3:::<Bucket Name>"<br />            ]<br />        },<br />        {<br />            "Sid": "Objectaccess",<br />            "Effect": "Allow",<br />            "Action": [<br />                "s3:PutObject",<br />                "s3:GetObjectAcl",<br />                "s3:GetObject",<br />                "s3:DeleteObjectVersion",<br />                "s3:DeleteObject",<br />                "s3:PutObjectAcl",<br />                "s3:GetObjectVersion"<br />            ],<br />            "Resource": [<br />                "arn:aws:s3:::<Bucket Name>/*"<br />            ]<br />        }<br />    ]<br />}</pre> | General AWS |

### Get the BMC AMI Cloud software license and download the software
<a name="get-the-bmc-ami-cloud-software-license-and-download-the-software"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Get a BMC AMI Cloud software license. | To get a software license key, contact the [BMC AMI Cloud team](https://www.bmc.com/it-solutions/bmc-ami-cloud.html?vd=model9-io). The output of the z/OS `D M=CPU` command is required for generating a license. | Build lead |
| Download the BMC AMI Cloud software and license key. | Obtain the installation files and license key by following the instructions in the [BMC documentation](https://docs.bmc.com/docs/cdacv27/preparing-to-install-the-bmc-ami-cloud-agent-1245343285.html). | Mainframe infrastructure administrator |

### Install the BMC AMI Cloud software agent on the mainframe
<a name="install-the-bmc-ami-cloud-software-agent-on-the-mainframe"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the BMC AMI Cloud software agent. | 1. Before you start the installation process, verify that [minimum software and hardware requirements](https://docs.bmc.com/docs/cdacv27/z-os-agent-requirements-1245343256.html) for the agent have been met.<br />2. To install the agent, follow the instructions in the [BMC documentation](https://docs.bmc.com/docs/cdacv27/performing-the-bmc-ami-cloud-agent-installation-1245343287.html).<br />3. After the agent starts running on the mainframe LPAR, check for the `ZM91000I MODEL9 BACKUP AGENT INITIALIZED` message in the spool. Verify that the connectivity is successfully established between the agent and the S3 bucket by looking for the `Object store connectivity has been established successfully` message in the agent’s STDOUT. | Mainframe infrastructure administrator |

### Set up a BMC AMI Cloud management server on an EC2 instance
<a name="set-up-a-bmc-ami-cloud-management-server-on-an-ec2-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create Amazon EC2 Linux 2 instances. | Launch two Amazon EC2 Linux 2 instances in different Availability Zones by following the instructions from [Step 1: Launch an instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html#ec2-launch-instance) in the Amazon EC2 documentation.<br />The instance must meet the following recommended hardware and software requirements:+ CPU – Minimum 4 cores<br />+ RAM – Minimum 8 GB<br />+ Drive – 40 GB<br />+ Recommended EC2 instance – C5.xlarge<br />+ OS – Linux<br />+ Software – Docker, unzip, vi/VIM<br />+ Network bandwidth – Minimum 1 GB<br />For more information, see the [BMC documentation](https://docs.bmc.com/docs/cdacv27/preparing-to-install-the-management-server-on-linux-1245343268.html). | Cloud architect, Cloud administrator |
| Create an Amazon EFS file system. | Create an Amazon EFS file system by following the instructions from [Step 1: Create your Amazon EFS file system](https://docs.aws.amazon.com/efs/latest/ug/gs-step-two-create-efs-resources.html) in the Amazon EFS documentation.<br />When creating the file system, do the following:+ Choose the Standard storage class.<br />+ Choose the same VPC that you used to launch your EC2 instances. | Cloud administrator, Cloud architect |
| Install Docker and configure the management server. | **Connect to your EC2 instances:**<br />Connect to your EC2 instances by following the instructions from [Connect to your Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html) in the Amazon EC2 documentation.<br />**Configure your EC2 instances:**<br />For each EC2 instance, do the following:1. To install Docker, run the command:<pre> sudo yum install docker </pre><br />2. To start Docker, run the command:<pre> sudo service docker start </pre><br />3. To validate the status of Docker, run the command:<pre> sudo service docker status </pre><br />4. In the `/etc/selinux`** **folder, change the `config` file to `SELINUX=permissive`.<br />5. Upload the `model9-v2.x.y_build_build-id-server.zip` and `VerificationScripts.zip` files (that you downloaded earlier) to a temporary folder in one of the EC2 instances (for example, into the `/var/tmp` folder in your instance).<br />6. To go to the `tmp` folder, run the command:<pre> cd/var/tmp </pre><br />7. To unzip the verification script, run the command:<pre> unzip VerificationScripts.zip </pre><br />8. To change the directory, run the command:<pre> cd /var/tmp/sysutils/PrereqsScripts </pre><br />9. To run the verification script, run the command:<pre> ./M9VerifyPrereqs.sh </pre><br />10. After the verification script prompts for the input, enter the Amazon S3 URL and port number. Then, enter the z/OS IP/DNS and port number. The script runs a check to confirm that EC2 instance can connect with the S3 bucket and agent that’s running on the mainframe. If a connection is established, a success message is displayed. | Cloud architect, Cloud administrator |
| Install the management server software. | 1. Create a folder and subfolder in the root directory (for example, `/data/model9`) in the EC2 instance that you plan to make the active server.<br />2. To install the `amazon-efs-utils` package and to mount the Amazon EFS file system created earlier, run the following commands:<pre>sudo yum install -y amazon-efs-utils<br />sudo mount -t efs -o tls <File System ID>:/ /data/model9</pre><br />3. To update the EC2 instance’s `/etc/fstab` file with an entry for the Amazon EFS file system (so that Amazon EFS is automatically remounted when Amazon EC2 reboots), run the command:<pre> <Amazon-EFS-file-system-id>:/ /data/model9 efs defaults,_netdev 0 0 </pre><br />4. To define the path to the BMC AMI Cloud installation files and the target installation location, run the following commands to export variables:<pre>export MODEL9_HOME=/data/model9<br />export M9INSTALL=/var/tmp</pre>We recommend that you add these EXPORT commands to your `.bashrc` script.<br />5. To change the directory, run the `cd $MODEL9_HOME` command, and then create another subdirectory by running the `mkdir diag` command.<br />6. To unzip the installation file, run the command:<pre>unzip $M9INSTALL/model9-<v2.x.y>_build_<build-id>-server.zip </pre>Replace `x.y` (the version) and `build-id` with your values.<br />7. To deploy the application, run the following commands:<pre>docker load -i $MODEL9_HOME/model9-<v2.x.y>_build_<build-id>.docker<br />docker load -i $MODEL9_HOME/postgres-12.10-x86.docker.gz</pre>Replace `v2.x.y` (the version) and `build-id` with your values.<br />8. In the `$MODEL9_HOME/conf` folder, update the `model9-local.yml`** **file.Some of the parameters have default values and others can be updated as necessary. For more information, see the instructions in the `model9-local.yml` file.<br />9. Create a file called** **`$MODEL9_HOME/conf`, and then add the following parameters to the file:<pre>TZ=America/New_York<br />EXTRA_JVM_ARGS=-Xmx2048m</pre><br />10. To create a Docker network bridge, run the command:<pre>docker network create -d bridge model9network</pre><br />11. To start the PostgreSQL database container for BMC AMI Cloud, run the following command:<pre>docker run -p 127.0.0.1:5432:5432 \<br />-v $MODEL9_HOME/db/data:/var/lib/postgresql/data:z \<br />--name model9db --restart unless-stopped \<br />--network model9network \<br />-e POSTGRES_PASSWORD=model9 -e POSTGRES_DB=model9 -d postgres:12.10</pre><br />12. After the PostgreSQL container starts running, run the following command to start the application server:<pre>docker run -d -p 0.0.0.0:443:443 -p 0.0.0.0:80:80 \<br />--sysctl net.ipv4.tcp_keepalive_time=600 \<br />--sysctl net.ipv4.tcp_keepalive_intvl=30 \<br />--sysctl net.ipv4.tcp_keepalive_probes=10 \<br />-v $MODEL9_HOME:/model9:z -h $(hostname) --restart unless-stopped \<br />--env-file $MODEL9_HOME/conf/model9.env \<br />--network model9network \<br />--name model9-v2.x.y model9:<v2.x.y>.<build-id></pre>Replace `v2.x.y` (the version) and `build-id` with your values.<br />13. To check the health status of both containers, run the command:<pre>docker ps -a</pre><br />14. To install a management server on the passive EC2 instances, repeat steps 1–4, 7, and 10–13.To troubleshoot issues, go to the logs stored in the `/data/model9/logs/`** **folder. For more information, see the [BMC documentation](https://docs.bmc.com/docs/cdacv27/performing-the-management-server-installation-on-linux-1245343272.html). | Cloud architect, Cloud administrator |

### Add an agent and define a backup or archive policy on the BMC AMI Cloud management server
<a name="add-an-agent-and-define-a-backup-or-archive-policy-on-the-bmc-ami-cloud-management-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add a new agent. | Before you add a new agent, confirm the following:+ A BMC AMI Cloud agent is running on the mainframe LPAR and has been initialized completely. Identify the agent by looking for the `ZM91000I MODEL9 BACKUP AGENT INITIALIZED` initialization message in the spool.<br />+ A Docker container for the management server is fully initialized and running.<br />You must create an agent on the management server before you define any backup and archive policies. To create the agent, do the following:1. Use a web browser to access the management server that’s deployed on your Amazon EC2 machine, and then log in with your mainframe credentials.<br />2. Choose the **AGENTS **tab, and then choose **ADD NEW AGENT**.<br />3. For **Name**, enter the agent name.<br />4. For **Hostname/IP Address**, enter the host name or IP address of your mainframe.<br />5. For** Port**, enter your port number.<br />6. Choose **TEST CONNECTION**. You can see a **success** message if the connectivity is successfully established.<br />7. Choose **CREATE**.<br />After the agent is created, you'll see the **connected** status against the object storage and mainframe agent in a new window that appears in the table. | Mainframe storage administrator or developer |
| Create a backup or archive policy. | 1. Choose **POLICIES**.<br />2. Choose **CREATE POLICY**.<br />3. On the **CREATE A NEW POLICY **page, enter your policy specifications. For more information about the available specifications, see [Creating a new policy](https://docs.bmc.com/docs/cdacv27/creating-a-new-policy-1245343388.html) in the BMC documentation.<br />4. Choose **FINISH**.<br />5. The new policy is now listed as a table. To see this table, choose the **POLICIES **tab. | Mainframe storage administrator or developer |

### Run the backup or archive policy from the management server
<a name="run-the-backup-or-archive-policy-from-the-management-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the backup or archive policy. | Run the data backup or archive policy that you created earlier from the management server either manually or automatically (based on a schedule). To run the policy manually:1. Choose the **POLICIES **tab from the navigation menu.<br />2. On the right side of the table for the policy that you want to run, choose the three-dot menu.<br />3. Choose **Run Now**.<br />4. In the pop-up confirmation window, choose **YES, RUN POLICY NOW**.<br />5. After the policy runs, verify the run status in the policy activity section.<br />6. For the policy that ran, choose the three-dot menu, and then choose **View Run Log **to see the logs.<br />7. To verify that the backup was created, check the S3 bucket. | Mainframe storage administrator or developer |
| Restore the backup or archive policy. | 1. On the navigation menu, choose the **POLICIES **tab.<br />2. Choose the policy to run your restore process on. This will list all the backup or archive activities that ran in the past for that specific policy.<br />3. To select the backups that you want to restore, choose the **Date-time **column. The `file/Volume/Storage`** **group name shows the run details of the policy.<br />4. On the right side of the table, choose the three-dot menu, and then choose **RESTORE**.<br />5. In the pop-up window, enter your target name, volume, and storage group, and then choose **RESTORE**.<br />6. Enter your mainframe credentials, and then choose **RESTORE **again.<br />7. To verify that the restore was successful, check the logs or the mainframe. | Mainframe storage administrator or developer |

### Run the backup or archive policy from the mainframe
<a name="run-the-backup-or-archive-policy-from-the-mainframe"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the backup or archive policy by using M9CLI. | Use the M9CLI to perform backup and restore processes from TSO/E, REXX, or through JCLs without setting up rules on the BMC AMI Cloud management server.<br />**Using TSO/E:**<br />If you use TSO/E, make sure that `M9CLI REXX` is concatenated to `TSO`. To back up a dataset through TSO/E, use the `TSO M9CLI BACKDSN <DSNAME>` command.For more information about M9CLI commands, see [CLI reference ](https://docs.bmc.com/docs/cdacv27/command-line-interface-cli-reference-1245343519.html)in the BMC documentation.<br />**Using JCLs:**<br />To run the backup and archive policy by using JCLs, run the `M9CLI` command.<br />**Using batch operations:**<br />The following example shows you how to archive a dataset by running the `M9CLI` command in batch:<pre>//JOBNAME JOB …<br />//M9CLI EXEC PGM=IKJEFT01<br />//STEPLIB DD DISP=SHR,DSN=<MODEL9 LOADLIB><br />//SYSEXEC DD DISP=SHR,DSN=<MODEL9 EXEC LIB><br />//SYSTSPRT DD SYSOUT=*<br />//SYSPRINT DD SYSOUT=*<br />//SYSTSIN DD TSO M9CLI ARCHIVE <br /> M9CLI ARCHIVE <DSNNAME OR DSN PATTERN>   <br />/</pre> | Mainframe storage administrator or developer |
| Run the backup or archive policy in JCL batch. | BMC AMI Cloud provides a sample JCL routine called **M9SAPIJ**. You can customize **M9SAPIJ** to run a specific policy created on the management server with a JCL. This job can also be part of a batch scheduler for running backup and restore processes automatically.<br />The batch job expects the following mandatory values:+ Management server IP address/host name<br />+ Port number<br />+ Policy ID or policy name (which is created on the management server)You can also change other values by following the instructions on the sample job. | Mainframe storage administrator or developer |

## Related resources
<a name="back-up-and-archive-mainframe-data-to-amazon-s3-using-bmc-ami-cloud-data-resources"></a>
+ [Mainframe Modernization with AWS](https://aws.amazon.com/mainframe/) (AWS documentation)
+ [How Cloud Backup for Mainframes Cuts Costs with Model9 and AWS](https://aws.amazon.com/blogs/apn/how-cloud-backup-for-mainframes-cuts-costs-with-model9-and-aws/) (AWS Partner Network Blog)
+ [How to Enable Mainframe Data Analytics on AWS Using Model9](https://aws.amazon.com/blogs/apn/how-to-enable-mainframe-data-analytics-on-aws-using-model9/) (AWS Partner Network Blog)
+ [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/?nc=sn&loc=4&dn=2) (AWS documentation)
+ [BMC AMI Cloud documentation](https://docs.bmc.com/docs/cdacv27/getting-started-1245343248.html) (BMC website)
