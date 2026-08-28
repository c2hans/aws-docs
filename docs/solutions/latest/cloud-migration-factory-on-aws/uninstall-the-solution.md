---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

You can uninstall the Cloud Migration Factory on AWS solution from the AWS Management Console or by using the AWS Command Line Interface. You must manually empty all the Amazon Simple Storage Service (Amazon S3) buckets created by this solution. AWS Solutions Implementations do not automatically delete S3 buckets in case you have stored data to retain.

## Empty the Amazon S3 buckets
<a name="empty-the-amazon-s3-buckets"></a>

If you decide to delete the AWS CloudFormation stack, this solution is configured to retain the created Amazon S3 bucket (for deploying in an opt-in Region) to prevent accidental data loss. You must manually empty all the S3 buckets before deleting the stack completely. Follow these steps to empty the Amazon S3 bucket.

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home).

1. Choose **Buckets** from the left navigation pane.

1. Locate the `[.replaceable]`<application name>`-{{<environment name>}}-{{<AWS account ID>}}\\\*` S3 buckets.

1. Select each S3 bucket and choose **Empty**.

To delete the S3 bucket using AWS CLI, run the following command:

```
aws s3 rm s3://<bucket-name> --recursive
```

## (Migration Tracker only) Delete Amazon Athena workgroup
<a name="delete-athena-workgroup"></a>

If you deployed the solution with the Migration Tracker, you must delete the Amazon Athena workgroup.

1. Sign in to the [Amazon Athena console](https://console.aws.amazon.com/athena).

1. Select **Administration** from the left navigation pane, then select **Workgroups**.

1. Locate the {{<application name>}}-{{<environment name>}}-workgroup` from the workgroups.

1. From **Actions**, choose **Delete**.

1. Confirm that you want to delete the workgroup.

1. Choose **Delete**.

## Using the AWS Management Console to delete the stack
<a name="using-the-aws-management-console-to-delete-the-stack"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. On the **Stacks** page, select this solution’s installation stack.

1. Choose **Delete**.

## Using AWS Command Line Interface to delete the stack
<a name="using-aws-command-line-interface-to-delete-the-stack"></a>

Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, refer to [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command:

```
aws cloudformation delete-stack --stack-name <installation-stack-name>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
