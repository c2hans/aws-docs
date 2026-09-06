---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-roles-for-ec2.html
---

# Using IAM roles to authenticate applications deployed to Amazon EC2
<a name="access-iam-roles-for-ec2"></a>

This example covers setting up an AWS Identity and Access Management role with Amazon S3 access to use in your application deployed to an Amazon Elastic Compute Cloud instance.

In order to run your AWS SDK application on an Amazon Elastic Compute Cloud instance, create an IAM role, and then give your Amazon EC2 instance access to that role. For more information, see [IAM Roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) in the *Amazon EC2 User Guide* .

## Create an IAM role
<a name="createRoleForEc2"></a>

The AWS SDK application that you develop likely accesses at least one AWS service to perform actions. Create an IAM role that grants the required permissions necessary for your application to run.

 This procedure creates a role that grants read-only access to Amazon S3 as an example. Many of the AWS SDK guides have "getting started" tutorials that read from Amazon S3.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, select **Roles**, then select **Create role**.

1. For **Select trusted entity**, under **Trusted entity type**, choose **AWS service**.

1. Under **Use case**, choose **Amazon EC2**, then select **Next**.

1. For **Add permissions**, select the checkbox for **Amazon S3 Read Only Access** from the policy list, then select **Next**.

1. Enter a name for the role, then select **Create role**. *Remember this name because you'll need it when you create your Amazon EC2 instance.*

## Launch an Amazon EC2 instance and specify your IAM role
<a name="launchAndSpecify"></a>

You can create and launch an Amazon EC2 instance using your IAM role by doing the following:
+ Follow [Quickly launch an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html#liw-quickly-launch-instance) in the *Amazon EC2 User Guide*. However, prior to the final submission step, also do the following:
  + Under **Advanced details**, for **IAM Instance profile**, choose the role that you created in the previous step.

 With this IAM and Amazon EC2 setup, you can deploy your application to the Amazon EC2 instance and your application will have read access to the Amazon S3 service.

## Connect to the EC2 instance
<a name="net-dg-hosm-connect"></a>

Connect to the Amazon EC2 instance so that you can transfer your application to it and then run the application. You'll need the file that contains the private portion of the key pair you used under **Key pair (login)** when you created your instance; that is, the PEM file.

You can do this by following the guidance for your instance type: [Connect to your Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html) or [Connect to your Windows instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connecting_to_windows_instance.html). When you connect, do so in such a way that you can transfer files from your development machine to your instance.

**Note**
On Linux or macOS terminal, you can use the secure copy command to copy your application. To use `scp` with a key pair, you can use the following command: `scp -i {{path/to/key}} {{file/to/copy}} {{ec2-user@ec2-xx-xx-xxx-xxx.compute.amazonaws.com}}:~` .
For more information for Windows, see [Transfer files to Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instanceWindowsFileTransfer.html).

If you're using an AWS Toolkit, you can often also connect to the instance by using the Toolkit. For more information, see the specific user guide for the Toolkit you use.

## Run your application on the EC2 instance
<a name="net-dg-hosm-run-the-app"></a>

1. Copy your application files from your local drive to your Amazon EC2 instance.

1. Start the application and verify that it runs with the same results as on your development machine.

1. (Optional) Verify that the application uses the credentials provided by the IAM role.

   1. Sign in to the AWS Management Console and open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

   1. Select the instance.

   1. Choose **Actions**, **Security**, and then choose **Modify IAM role**.

   1.  For **IAM role**, detach the IAM role by choosing **No IAM Role**.

   1.  Choose **Update IAM role**.

   1. Run the application again and confirm that it returns an authorization error.
