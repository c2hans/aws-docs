---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-ibm-z-os-by-installing-aws-cli.html
---

# Access AWS services from IBM z/OS by installing the AWS CLI
<a name="access-aws-services-from-ibm-z-os-by-installing-aws-cli"></a>

*Souma Ghosh, Paulo Vitor Pereira, and Phil de Valence, Amazon Web Services*

## Summary
<a name="access-aws-services-from-ibm-z-os-by-installing-aws-cli-summary"></a>

The [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/) is an open source tool for managing multiple AWS services by using commands in a command line shell. With minimal configuration, you can run commands from command line sessions such as the command prompt, terminal, and bash shell to implement functionality that's equivalent to that provided by the browser-based AWS Management Console.

All AWS infrastructure as a service (IaaS) administration, management, and access functions in the AWS Management Console are available in the AWS API and AWS CLI. You can install the AWS CLI on an IBM z/OS mainframe to directly access, manage, and interact with AWS services from z/OS. The AWS CLI enables users and applications to perform various tasks, such as:
+ Transferring files or datasets between z/OS and Amazon Simple Storage Service (Amazon S3) object storage and viewing content of buckets
+ Starting and stopping different AWS resources; for example, starting a batch job in an AWS Mainframe Modernization environment
+ Calling an AWS Lambda function to implement common business logic
+ Integrating with artificial intelligence and machine learning (AI/ML) and analytics services

This pattern describes how to install, configure, and use the AWS CLI on z/OS. You can install it globally, so it's available to all z/OS users, or at a user level. The pattern also details how to use the AWS CLI in an interactive command line session from z/OS Unix System Services (USS) or as a batch job.

## Prerequisites and limitations
<a name="access-aws-services-from-ibm-z-os-by-installing-aws-cli-prereqs"></a>

**Prerequisites**
+ **Network communication from z/OS to AWS**

  By default, the AWS CLI sends requests to AWS services by using HTTPS on TCP port 443. To use the AWS CLI successfully, you must be able to make outbound connections on TCP port 443. You can use any of the following z/OS USS commands (some of these might not be installed in your environment) to test network connectivity from z/OS to AWS:

  ```
  ping amazonaws.com
  dig amazonaws.com
  traceroute amazonaws.com
  curl -k https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-welcome.html
  ```
+ **AWS credentials**

  In order to communicate with AWS Cloud services from z/OS, the AWS CLI requires you to configure some credentials with privileges to access the target AWS account. For programmatic commands to AWS, you can use access keys, which consist of an access key ID and secret access key. If you don't have access keys, you can create them from the AWS Management Console. As a best practice, do not use the access keys for the AWS account root user for any task unless the root user is required. Instead, [create a new administrator IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) and [prepare for least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#LeastPrivilege)** **to set up the user with access keys. After you create the user, you can [create an access key ID and secret access key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) for this user.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-ibm-z-os-by-installing-aws-cli.html)
+ **IBM Python for z/OS**

  The AWS CLI requires Python 3.8 or later. IBM has enabled Python to run on z/OS with [IBM Open Enterprise Python for z/OS](https://www.ibm.com/products/open-enterprise-python-zos). IBM Open Enterprise Python is available at no charge through Shopz SMP/E, or you can download the PAX file from the [IBM website](https://www.ibm.com/account/reg/signup?formid=urx-49465). For instructions, see the [installation and configuration documentation](https://www.ibm.com/docs/en/python-zos) for IBM Open Enterprise Python for z/OS.

**Limitations**
+ The installation instructions provided in this pattern are applicable to **AWS CLI version 1 only**. The latest version of the AWS CLI is version 2. However, this pattern uses the older version because the installation methods are different for version 2, and the binary executables available for version 2 aren't compatible with the z/OS system.

**Product versions**
+ AWS CLI version 1
+ Python 3.8 or later

## Architecture
<a name="access-aws-services-from-ibm-z-os-by-installing-aws-cli-architecture"></a>

**Technology stack**
+ Mainframe running z/OS
+ Mainframe z/OS UNIX System Services (USS)
+ Mainframe Open MVS (OMVS) – z/OS UNIX shell environment command interface
+ Mainframe disk, such as a direct-access storage device (DASD)
+ AWS CLI

**Target architecture**

The following diagram shows an AWS CLI deployment on IBM z/OS. You can invoke the AWS CLI from an interactive user session, such as SSH, and telnet sessions. You can also invoke it from a batch job by using job control language (JCL), or from any program that can call a z/OS Unix shell command.

![AWS CLI on an IBM z/OS mainframe accessing AWS services.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4e3188d8-287f-4ced-8c29-80a01cbbdf50/images/c3883500-bd00-4c56-982a-26d5e0b8b093.png)

The AWS CLI communicates with AWS service endpoints over a TCP/IP network. This network connection can happen over the internet or through a private AWS Direct Connect connection from the customer data center to AWS Cloud data centers. The communication is authenticated with AWS credentials and encrypted.

**Automation and scale**

You can explore the capabilities of an AWS service with the AWS CLI and develop USS shell scripts to manage your AWS resources from z/OS. You can also run AWS CLI commands and shell scripts from the z/OS batch environment, and you can automate batch jobs to run on a specific schedule by integrating with mainframe schedulers. AWS CLI commands or scripts can be coded inside parameters (PARMs) and procedures (PROCs), and can be scaled by following the standard approach of calling the PARM or PROC from different batch jobs with different parameters.

## Tools
<a name="access-aws-services-from-ibm-z-os-by-installing-aws-cli-tools"></a>
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command-line shell.

## Best practices
<a name="access-aws-services-from-ibm-z-os-by-installing-aws-cli-best-practices"></a>
+ For security reasons, restrict the access permissions to the USS directory where the AWS access key details are stored. Allow access to only the users or programs that use the AWS CLI.
+ Do not use the AWS account root user access keys for any task. Instead, [create a new administrator IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) for yourself and set it up with access keys.

|
|
| IAM users have long-term credentials that present a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed. |
| --- |

## Epics
<a name="access-aws-services-from-ibm-z-os-by-installing-aws-cli-epics"></a>

### Install AWS CLI version 1 on z/OS USS
<a name="install-cli-version-1-on-z-os-uss"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install Python 3.8 or later. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-ibm-z-os-by-installing-aws-cli.html) | Mainframe z/OS administrator |
| Set USS environment variables. | Add environment variables to the profile. You can add these either to the `/u/cliuser/.profile` file for an individual user (`cliuser`) or to the `/etc/profile` file for all users.This pattern assumes that Python has been installed in the `/u/awscli/python` directory. If your installation directory is different, update the code accordingly.<pre># Python configuration<br />export BPXKAUTOCVT='ON'<br />export CEERUNOPTS='FILETAG(AUTOCVT,AUTOTAG) POSIX(ON)'<br />export TAGREDIR_ERR=txt<br />export TAGREDIR_IN=txt<br />export TAGREDIR_OUT=txt<br /><br /># AWS CLI configuration<br />export PATH=/u/cliuser/python/bin:$PATH<br />export PYTHONPATH=/u/cliuser/python:$PYTHONPATH</pre> | Mainframe z/OS administrator |
| Test the Python installation. | Run the **python** command:<pre>python --version</pre><br />The output should confirm that you have Python 3.8 or later installed correctly. | Mainframe z/OS administrator |
| Verify or install **pip**. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-ibm-z-os-by-installing-aws-cli.html) | Mainframe z/OS administrator |
| Install AWS CLI version 1. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-ibm-z-os-by-installing-aws-cli.html) | Mainframe z/OS administrator |

### Configure AWS CLI access from z/OS
<a name="configure-cli-access-from-z-os"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the AWS access keys, default Region, and output. | The [AWS CLI documentation](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html) describes different options for setting up AWS access. You can choose a configuration according to your organization's standards. This example uses the short-term credential configuration.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-ibm-z-os-by-installing-aws-cli.html) | AWS administrator, Mainframe z/OS administrator, Mainframe z/OS developer |
| Test the AWS CLI. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-ibm-z-os-by-installing-aws-cli.html) | Mainframe z/OS administrator, Mainframe z/OS developer |

### Option 1 ‒ Transfer data from USS to Amazon S3 interactively from a USS session
<a name="option-1-transfer-data-from-uss-to-s3-interactively-from-a-uss-session"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download and transfer the sample CSV file. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-ibm-z-os-by-installing-aws-cli.html) | App developer, Mainframe z/OS developer |
| Create an S3 bucket and upload the CSV file. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-ibm-z-os-by-installing-aws-cli.html) | App developer, Mainframe z/OS developer |
| View the S3 bucket and uploaded file. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-ibm-z-os-by-installing-aws-cli.html)For more information about uploading objects, see [Getting started with Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) in the Amazon S3 documentation. | General AWS |
| Run a SQL query on an Amazon Athena table. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-ibm-z-os-by-installing-aws-cli.html)The output of the SQL query will display the contents of your CSV file. | General AWS, App developer |

### Option 2 ‒ Transfer data from USS to Amazon S3 by using batch JCL
<a name="option-2-transfer-data-from-uss-to-s3-by-using-batch-jcl"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload the sample file. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-ibm-z-os-by-installing-aws-cli.html) | Mainframe z/OS developer |
| Create batch JCL. | Code the batch JCL as follows to create the destination S3 bucket, upload the dataset, and list the bucket content. Make sure to replace the directory name, file names, and bucket name to your own values.<pre>//AWSCLICP JOB ACTINFO1,'IBMUSER',CLASS=A,MSGCLASS=H,MSGLEVEL=(1,1), <br />// NOTIFY=&SYSUID,TIME=1440 <br />//*---------------------------------------------------------<br />//* Sample job for AWS CLI <br />//*--------------------------------------------------------- <br />//USSCMD EXEC PGM=BPXBATCH<br />//STDERR  DD SYSOUT=*<br />//STDOUT  DD SYSOUT=*<br />//STDENV  DD *<br /> export PATH=/u/cliuser/python/bin:$PATH<br />//STDPARM DD *<br />SH<br /> export _BPXK_AUTOCVT=ON;<br /> aws s3 mb s3://DOC-EXAMPLE-BUCKET2;<br /> cp "//'USER.DATA.FIXED'" /tmp/tmpfile;<br /> aws s3 cp /tmp/tmpfile s3://DOC-EXAMPLE-BUCKET2/USER.DATA.FIXED; <br /> rm /tmp/tmpfile;<br /> aws s3 ls s3://DOC-EXAMPLE-BUCKET2;<br />/*</pre> | Mainframe z/OS developer |
| Submit the batch JCL job. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-ibm-z-os-by-installing-aws-cli.html) | Mainframe z/OS developer |
| View the dataset uploaded to the S3 bucket. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-aws-services-from-ibm-z-os-by-installing-aws-cli.html) | General AWS |

## Related resources
<a name="access-aws-services-from-ibm-z-os-by-installing-aws-cli-resources"></a>
+ [AWS CLI version 1 documentation](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-welcome.html)
+ [AWS Mainframe Modernization CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/m2/)
+ [AWS Mainframe Modernization](https://aws.amazon.com/mainframe-modernization/)

## Additional information
<a name="access-aws-services-from-ibm-z-os-by-installing-aws-cli-additional"></a>

**USER.DATA.FIXED in ISPF option 3.4 (dataset list utility)**

![Viewing the contents of the dataset in z/OS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4e3188d8-287f-4ced-8c29-80a01cbbdf50/images/96c25145-3d4d-4007-99f6-5eeb9e88642d.png)

**SYSOUT of the submitted batch job**

![Standard output from job log.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4e3188d8-287f-4ced-8c29-80a01cbbdf50/images/03fffbd2-7d2b-43b2-bf14-736b3d150e38.png)

## Attachments
<a name="attachments-4e3188d8-287f-4ced-8c29-80a01cbbdf50"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/4e3188d8-287f-4ced-8c29-80a01cbbdf50/attachments/attachment.zip)
