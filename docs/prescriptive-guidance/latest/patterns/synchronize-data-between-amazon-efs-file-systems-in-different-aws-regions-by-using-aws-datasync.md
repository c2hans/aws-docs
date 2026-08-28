---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/synchronize-data-between-amazon-efs-file-systems-in-different-aws-regions-by-using-aws-datasync.html
---

# Synchronize data between Amazon EFS file systems in different AWS Regions by using AWS DataSync
<a name="synchronize-data-between-amazon-efs-file-systems-in-different-aws-regions-by-using-aws-datasync"></a>

*Sarat Chandra Pothula and Aditya Ambati, Amazon Web Services*

## Summary
<a name="synchronize-data-between-amazon-efs-file-systems-in-different-aws-regions-by-using-aws-datasync-summary"></a>

This solution provides a robust framework for efficient and secure data synchronization between Amazon Elastic File System (Amazon EFS) instances in different AWS Regions. This approach is scalable and provides controlled, cross-Region data replication. This solution can enhance your disaster recovery and data redundancy strategies.

By using the AWS Cloud Development Kit (AWS CDK), this pattern uses as an infrastructure as code (IaC) approach to deploy the solution resources. The AWS CDK application deploys the essential AWS DataSync, Amazon EFS, Amazon Virtual Private Cloud (Amazon VPC), and Amazon Elastic Compute Cloud (Amazon EC2) resources. This IaC provides a repeatable and version-controlled deployment process that is fully aligned with AWS best practices.

## Prerequisites and limitations
<a name="synchronize-data-between-amazon-efs-file-systems-in-different-aws-regions-by-using-aws-datasync-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ AWS Command Line Interface (AWS CLI) version 2.9.11 or later, [installed](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ AWS CDK version 2.114.1 or later, [installed](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_install) and [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_bootstrap)
+ NodeJS version 20.8.0 or later, [installed](https://nodejs.org/en/download)

**Limitations**
+ The solution inherits limitations from DataSync and Amazon EFS, such as data transfer rates, size limitations, and regional availability. For more information, see [AWS DataSync quotas](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-limits.html) and [Amazon EFS quotas](https://docs.aws.amazon.com/efs/latest/ug/limits.html).
+ This solution supports Amazon EFS only. DataSync supports [other AWS services](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html), such as Amazon Simple Storage Service (Amazon S3) and Amazon FSx for Lustre. However, this solution requires modification to synchronize data with these other services.

## Architecture
<a name="synchronize-data-between-amazon-efs-file-systems-in-different-aws-regions-by-using-aws-datasync-architecture"></a>

![Architecture diagram for replicating data to an EFS file system in a different Region](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e28ba6c2-ab8b-4812-932e-f038106d5496/images/18b35ae9-a22e-43e7-b7a3-30e40321c44e.png)

This solution deploys the following AWS CDK stacks:
+ **Amazon VPC stack** –­ This stack sets up virtual private cloud (VPC) resources, including subnets, an internet gateway, and a NAT gateway in both the primary and secondary AWS Regions.
+ **Amazon EFS stack** – This stack deploys Amazon EFS file systems into the primary and secondary Regions and connects them to their respective VPCs.
+ **Amazon EC2 stack** – This stack launches EC2 instances in the primary and secondary Regions. These instances are configured to mount the Amazon EFS file system, which allows them to access the shared storage.
+ **DataSync location stack** – This stack uses a custom construct called `DataSyncLocationConstruct` to create DataSync location resources in the primary and secondary Regions. These resources define endpoints for data synchronization.
+ **DataSync task stack** – This stack uses a custom construct called `DataSyncTaskConstruct` to create a DataSync task in the primary Region. This task is configured to synchronize data between the primary and secondary Regions by using the DataSync source and destination locations.

## Tools
<a name="synchronize-data-between-amazon-efs-file-systems-in-different-aws-regions-by-using-aws-datasync-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) is an online data transfer and discovery service that helps you move files or object data to, from, and between AWS storage services.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) helps you create and configure shared file systems in the AWS Cloud.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**Code repository**

The code for this pattern is available in the GitHub [Amazon EFS Cross-Region DataSync Project](https://github.com/aws-samples/aws-efs-crossregion-datasync/tree/main) repository.

## Best practices
<a name="synchronize-data-between-amazon-efs-file-systems-in-different-aws-regions-by-using-aws-datasync-best-practices"></a>

Follow the best practices described in [Best practices for using the AWS CDK in TypeScript to create IaC projects](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/introduction.html).

## Epics
<a name="synchronize-data-between-amazon-efs-file-systems-in-different-aws-regions-by-using-aws-datasync-epics"></a>

### Deploy the AWS CDK app
<a name="deploy-the-aws-cdk-app"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the project repository. | Enter the following command to clone the [Amazon EFS Cross-Region DataSync Project](https://github.com/aws-samples/aws-efs-crossregion-datasync/tree/main) repository.<pre>git clone https://github.com/aws-samples/aws-efs-crossregion-datasync.git</pre> | AWS DevOps |
| Install the npm dependencies. | Enter the following command.<pre>npm ci</pre> | AWS DevOps |
| Choose the primary and secondary Regions. | In the cloned repository, navigate to the `src/infa` directory. In the `Launcher.ts` file, update the `PRIMARY_AWS_REGION` and `SECONDARY_AWS_REGION` values. Use the corresponding [Region codes](https://docs.aws.amazon.com/general/latest/gr/datasync.html#datasync-region).<pre>const primaryRegion = { account: account, region: '<PRIMARY_AWS_REGION>' };<br />const secondaryRegion = { account: account, region: '<SECONDARY_AWS_REGION>' };</pre> | AWS DevOps |
| Bootstrap the environment. | Enter the following command to bootstrap the AWS account and AWS Region that you want to use.<pre>cdk bootstrap <aws_account>/<aws_region></pre><br />For more information, see [Bootstrapping](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) in the AWS CDK documentation. | AWS DevOps |
| List the AWS CDK stacks. | Enter the following command to view a list of the AWS CDK stacks in the app.<pre>cdk ls</pre> | AWS DevOps |
| Synthesize the AWS CDK stacks. | Enter the following command to produce an AWS CloudFormation template for each stack defined in the AWS CDK app.<pre>cdk synth</pre> | AWS DevOps |
| Deploy the AWS CDK app. | Enter the following command to deploy all of the stacks to your AWS account, without requiring manual approval for any changes.<pre>cdk deploy --all --require-approval never</pre> | AWS DevOps |

### Validate the deployment
<a name="validate-the-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Log in to the EC2 instance in the primary Region. | 1. Using Session Manager, a capability of AWS Systems Manager, log in to the EC2 instance in the primary Region. For instructions, see [Connect to your Linux instance with AWS Systems Manager Session Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/session-manager-to-linux.html).<br />2. Change directories to the Amazon EFS mount path.<pre>cd /mnt/efs</pre> | AWS DevOps |
| Create a temporary file. | Enter the following command to create a temporary file in the Amazon EFS mount path.<pre>sudo dd if=/dev/zero \<br />of=tmptst.dat \<br />bs=1G \<br />seek=5 \<br />count=0<br /><br />ls -lrt tmptst.dat</pre> | AWS DevOps |
| Start the DataSync task. | Enter the following command to replicate the temporary file from the primary Region to the secondary Region, where `<ARN-task>` is the Amazon Resource Name (ARN) of your DataSync task.<pre>aws datasync start-task-execution \<br />    --task-arn <ARN-task></pre><br />The command returns the ARN of the task execution in the following format.<br />`arn:aws:datasync:<region>:<account-ID>:task/task-execution/<exec-ID>` | AWS DevOps |
| Check the status of the data transfer. | Enter the following command to describe the DataSync execution task, where `<ARN-task-execution>` is the ARN of the task execution.<pre>aws datasync describe-task-execution \<br />    --task-execution-arn <ARN-task-execution></pre><br />The DataSync task is complete when `PrepareStatus`, `TransferStatus`, and `VerifyStatus` all have the value `SUCCESS`. | AWS DevOps |
| Log in to the EC2 instance in the secondary Region. | 1. Using Session Manager, a capability of AWS Systems Manager, log in to the EC2 instance in the secondary Region. For instructions, see [Connect to your Linux instance with AWS Systems Manager Session Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/session-manager-to-linux.html).<br />2. Change directories to the Amazon EFS mount path.<pre>cd /mnt/efs</pre> | AWS DevOps |
| Validate the replication. | Enter the following command to verify that the temporary file exists in the Amazon EFS file system.<pre>ls -lrt<br />tmptst.dat</pre> | AWS DevOps |

## Related resources
<a name="synchronize-data-between-amazon-efs-file-systems-in-different-aws-regions-by-using-aws-datasync-resources"></a>

**AWS documentation**
+ [AWS CDK API Reference](https://docs.aws.amazon.com/cdk/api/v2/python/modules.html)
+ [Configuring AWS DataSync transfers with Amazon EFS](https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html)
+ [Troubleshooting issues with AWS DataSync transfers](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html)

**Other AWS resources**
+ [AWS DataSync FAQs](https://aws.amazon.com/datasync/faqs/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
