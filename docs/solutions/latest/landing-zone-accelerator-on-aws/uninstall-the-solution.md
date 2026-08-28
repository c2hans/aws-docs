---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

You can uninstall the Landing Zone Accelerator on AWS solution from the AWS Management Console or by using the AWS Command Line Interface. You must manually delete the Amazon S3 buckets and CloudFormation stacks created by this solution. AWS Solutions Implementations don’t automatically delete these resources in case you have stored data to retain.

## Step 1. Delete the Installer and Core pipelines
<a name="delete-the-installer"></a>

### Option 1: Use the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. On the **Stacks** page, select the **AWSAccelerator-InstallerStack** and **AWSAccelerator-PipelineStack** stacks.

1. These stacks will have `TerminationProtection` enabled, which needs to be disabled before deletion. Follow the steps outlined in [Problem: "ValidationError: Stack <stack-name> cannot be deleted while TerminationProtection is enabled"](problem-validationerror.md) error.

1. Choose **Delete** for each stack.

### Option 2: Use the AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, refer to [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following commands.

**Note**
These stacks will have TerminationProtection enabled and need to be disabled prior to deletion. Follow the steps outlined in [Problem: "ValidationError: Stack <stack-name> cannot be deleted while TerminationProtection is enabled"](problem-validationerror.md).

```
$ aws cloudformation delete-stack --stack-name AWSAccelerator-InstallerStack
```

```
$ aws cloudformation delete-stack --stack-name AWSAccelerator-PipelineStack
```

## Step 2. Delete the Amazon S3 buckets
<a name="deleting-the-amazon-s3-buckets"></a>

This solution is configured to retain the solution-created Amazon S3 buckets if you decide to delete the AWS CloudFormation stack to prevent accidental data loss. After uninstalling the solution, you can manually delete the Amazon S3 buckets if you don’t need to retain the data. Follow these steps to delete the Amazon S3 buckets in each account Landing Zone Accelerator on AWS was configured to manage.

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home).

1. Choose **Buckets** from the left navigation pane.

1. Locate the `aws-accelerator-*` Amazon S3 buckets.

1. Select each Amazon S3 bucket and choose **Empty**.

1. Select each Amazon S3 bucket and choose **Delete**.

To delete the Amazon S3 buckets using AWS CLI, run the following command for each bucket:

```
$ aws s3 rb s3://<bucket-name> --force
```

## Step 3. Delete additional CloudFormation stacks
<a name="deleting-the-cloudformation-stacks"></a>

This solution deploys several CloudFormation stacks to each account and AWS Region that’s activated for management by Landing Zone Accelerator on AWS. Each stack deployed by the solution uses the following naming convention:

```
AWSAccelerator-<pipeline action>-<account number>-<region>
```

To successfully delete all stacks without experiencing dependency issues, delete the stacks in the reverse order that they’re deployed. See the [AWSAccelerator-Pipeline](awsaccelerator-pipeline.md) section for a list of actions orchestrated by the pipeline. Complete the following steps to delete each of the stacks:

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. On the **Stacks** page, select this solution’s stack.

1. Choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
