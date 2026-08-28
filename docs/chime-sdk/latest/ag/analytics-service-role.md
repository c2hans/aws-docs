---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/analytics-service-role.html
---

# Using the AmazonChimeSDKEvents service-linked role
<a name="analytics-service-role"></a>

The Amazon Chime SDK uses a service-linked role named `AmazonChimeSDKEvents`. The role grants access to the AWS services and resources used or managed by the Amazon Chime SDK, such as the Kinesis firehose used for data streaming.

The `AmazonChimeSDKEvents` service-linked role allows the Amazon Chime SDK to complete `kinesis:PutRecord` and `kinesis:PutRecordBatch` on streams with this format: `arn:aws:firehose:::deliverystream/AmazonChimeSDKEvents-*`.

You must configure permissions to allow an IAM entity such as a user, group, or role to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/) in the *IAM User Guide*.

## Creating the service-linked role
<a name="slr-create"></a>

The service-linked role is part of the Chime SDK Events CloudFormation template in the quick-create link.

You can also use the IAM console to create a service-linked role with the Amazon Chime SDK Events use case. In the AWS CLI or the AWS API, create a service-linked role with the `events.chime.amazonaws.com` service name. For more information, see [Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) in the *IAM User Guide*. If you delete this role, you can repeat this process to create it again.

## Editing the service-linked role
<a name="slr-edit"></a>

After you create a service-linked role, you can only edit its description, and you do that using IAM. For more information, see [Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) in the *IAM User Guide*.

## Deleting the service-linked role
<a name="slr-delete-resources"></a>

As a best practice, delete the `Amazon Chime SDKEvents` role when you no longer need a feature or service that requires it. Otherwise, you have an unused entity that is not actively monitored or maintained.

To manually delete the role, you first delete the resources that the role uses. The following sets of steps explain how to do both tasks.

**Deleting role resources**
You delete resources by deleting the Kinesis firehose used to stream data.

**Note**
Deletions can fail if you try to delete resources while the role uses them. If a deletion fails, wait a few minutes and try the operation again.

**To delete the role resources**
+ Turn off the Kinesis firehose by invoking the following API.

  ```
  aws firehose delete-delivery-stream --delivery-stream-name {{delivery_stream_name}}
  ```

**To delete the service-linked role**
+ Use the IAM console, AWS CLI, or the AWS API to delete the AmazonChimeSDKEvents service-linked role. For more information, see [Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) and [ Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/example_iam_DeleteServiceLinkedRole_section.html) in the *IAM user Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
