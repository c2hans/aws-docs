---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/using-service-linked-roles-media-pipeline.html
---

# Using roles with Amazon Chime SDK media pipelines
<a name="using-service-linked-roles-media-pipeline"></a>

The information in the following sections explains how to create and manage a service-linked role for Amazon Chime SDK Media Pipelines.

**Topics**
+ [Service-linked role permissions for Amazon Chime SDK media pipelines](#slr-permissions)
+ [Creating a service-linked role for Amazon Chime SDK media pipelines](#create-slr)
+ [Editing a service-linked role for Amazon Chime SDK media pipelines](#edit-slr)
+ [Deleting a service-linked role for Amazon Chime SDK media pipelines](#delete-slr)
+ [Supported Regions for Amazon Chime SDK media pipelines service-linked roles](#slr-regions)

## Service-linked role permissions for Amazon Chime SDK media pipelines
<a name="slr-permissions"></a>

The Amazon Chime SDK uses the service-linked role named `AWSServiceRoleForAmazonChimeSDKMediaPipelines` – Allows Amazon Chime SDK media pipelines to access AWS services on your behalf.

The `AWSServiceRoleForAmazonChimeSDKMediaPipelines` service-linked role trusts the following services to assume the role:
+ `mediapipelines.chime.amazonaws.com`

The role allows the Amazon Chime SDK to complete the following actions on the specified resources:
+ Action: `cloudwatch:PutMetricData` on `all AWS resources`
+ Action: `chime:CreateAttendee` on `all AWS resources`
+ Action: `chime:DeleteAttendee` on `all AWS resources`
+ Action: `chime:GetMeeting` on `all AWS resources`
+ Action: `kinesisvideo:CreateStream` on `arn:aws:kinesisvideo:*:{{111122223333}}:stream/ChimeMediaPipelines-*`
+ Action: `kinesisvideo:PutMedia` on `arn:aws:kinesisvideo:*:{{111122223333}}:stream/ChimeMediaPipelines-*`
+ Action: `kinesisvideo:UpdateDataRetention` on `arn:aws:kinesisvideo:*:{{111122223333}}:stream/ChimeMediaPipelines-*`
+ Action: `kinesisvideo:DescribeStream` on `arn:aws:kinesisvideo:*:{{111122223333}}:stream/ChimeMediaPipelines-*`
+ Action: `kinesisvideo:GetDataEndpoint` on `arn:aws:kinesisvideo:*:{{111122223333}}:stream/ChimeMediaPipelines-*`
+ Action: `kinesisvideo:ListStreams` on `arn:aws:kinesisvideo:*:{{111122223333}}:stream/*`

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information about configuring permissions, see [ Service-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

For more information about the `AmazonChimeSDKMediaPipelinesServiceLinkedRolePolicy`, see [AWS managed policy: AmazonChimeSDKMediaPipelinesServiceLinkedRolePolicy](media-pipeline-service-linked-role-policy.md), earlier in this guide.

## Creating a service-linked role for Amazon Chime SDK media pipelines
<a name="create-slr"></a>

You use the IAM console to create a service-linked role with the **Amazon Chime SDK Media Pipelines** use case.

**Note**
You must have IAM administrative permissions to complete these steps. If you don't, contact a system administrator.

**To create the role**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the IAM console, choose **Roles**, then choose **Create role**.

1. Choose the **AWS Service** role type, then choose **Chime**, then choose **Chime SDK Media Pipelines**.

1. Choose **Next**.

1. Choose **Next**.

1. Edit the description as needed, then choose **Create role**.

You can also use the AWS CLI or the AWS API to create a service-linked role named `mediapipelines.chime.amazonaws.com`.

In the AWS CLI, run this command: **aws iam create-service-linked-role --aws-service-name mediapipelines.chime.amazonaws.com**.

For more information, see [Creating a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

## Editing a service-linked role for Amazon Chime SDK media pipelines
<a name="edit-slr"></a>

The Amazon Chime SDK doesn't allow you to edit the `AWSServiceRoleForAmazonChimeSDKMediaPipelines` service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for Amazon Chime SDK media pipelines
<a name="delete-slr"></a>

When you don't need to use a feature or service that requires a service-linked role, we recommend deleting that role. That way you don’t have an unused entity that isn't actively monitored or maintained.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the `AWSServiceRoleForAmazonChimeSDKMediaPipelines` service-linked role. For more information, see [Deleting a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for Amazon Chime SDK media pipelines service-linked roles
<a name="slr-regions"></a>

The Amazon Chime SDK supports using service-linked roles in all of the AWS Regions where the service is available. For more information, see [Amazon Chime endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/chime.html#chime_region).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
