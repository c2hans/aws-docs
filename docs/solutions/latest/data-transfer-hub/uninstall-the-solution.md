---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/uninstall-the-solution.html
---

# Uninstall the Guidance
<a name="uninstall-the-solution"></a>

 You can uninstall the Data Transfer Hub Guidance from the AWS Management Console or by using the AWS Command Line Interface. You must manually stop any active transfer tasks before uninstalling.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1.  Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1.  On the **Stacks** page, select this Guidance's installation stack.

1.  Choose **Delete**.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

 Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, refer to [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
$ aws cloudformation delete-stack --stack-name <installation-stack-name>
```

## Deleting the Amazon S3 buckets
<a name="deleting-the-amazon-s3-buckets"></a>

 This Guidance is configured to retain the Guidance-created Amazon S3 bucket (for deploying in an opt-in Region) if you decide to delete the AWS CloudFormation stack to prevent accidental data loss. After uninstalling the Guidance, you can manually delete this S3 bucket if you do not need to retain the data. Follow these steps to delete the Amazon S3 bucket.

1.  Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home).

1.  Choose **Buckets** from the left navigation pane.

1.  Locate the `<stack-name>` S3 buckets.

1.  Select the S3 bucket and choose **Delete**.

 To delete the S3 bucket using AWS CLI, run the following command:

```
$ aws s3 rb s3://<bucket-name> --force
```
