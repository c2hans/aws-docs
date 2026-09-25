---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/uninstall-the-guidance.html
---

# Uninstall the Guidance
<a name="uninstall-the-guidance"></a>

You can uninstall the Guidance from the AWS Management Console or by using the AWS CLI. You must manually delete the transit gateway, Amazon S3 buckets, and global network created by this Guidance. AWS solutions don’t automatically delete these resources, in case you have stored data that you want to retain.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. On the **Stacks** page, select the installation stack.

1. Choose **Delete**.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

Determine whether the AWS CLI is available in your environment. For installation instructions, see [What is the AWS Command Line Interface?](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
$ aws cloudformation delete-stack --stack-name <installation-stack-name>
```

## Manually delete resources
<a name="manually-delete-resources"></a>

We configured this Guidance to retain specific resources to prevent accidental data loss if you decide to delete the CloudFormation stack. After uninstalling, you can manually delete these resources if you don’t need to retain the data. Refer to these guides to delete the following resources:
+  [Delete a transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#delete-tgw)
+  [Delete Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html)
+  [Delete an AWS Network Manager global network](https://docs.aws.amazon.com/vpc/latest/tgw/global-networks.html#global-networks-deleting)
