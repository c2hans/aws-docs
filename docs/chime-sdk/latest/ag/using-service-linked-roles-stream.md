---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/using-service-linked-roles-stream.html
---

# Using the Amazon Chime SDK Voice Connector service linked role policy
<a name="using-service-linked-roles-stream"></a>

The information in the following sections explains how to:
+ Use the Amazon Chime SDK Voice Connector service linked role policy to stream Amazon Chime SDK Voice Connector media to Kinesis.
+ Synthesize speech with Amazon Polly and the [Speak](https://docs.aws.amazon.com/chime-sdk/latest/dg/speak.html) and [SpeakAndGetDigits](https://docs.aws.amazon.com/chime-sdk/latest/dg/speak-and-get-digits.html) actions.

**Topics**
+ [Service-linked role permissions for Amazon Chime SDK Voice Connectors](#service-linked-role-permissions-stream)
+ [Creating a service-linked role for Amazon Chime SDK Voice Connectors](#create-service-linked-role-stream)
+ [Editing a service-linked role for Amazon Chime SDK Voice Connectors](#edit-service-linked-role-stream)
+ [Deleting a service-linked role for Amazon Chime SDK Voice Connectors](#delete-service-linked-role-stream)
+ [Supported Regions for Amazon Chime SDK service-linked roles](#slr-regions-stream)

## Service-linked role permissions for Amazon Chime SDK Voice Connectors
<a name="service-linked-role-permissions-stream"></a>

Amazon Chime SDK Voice Connectors use the service-linked role named **AWSServiceRoleForAmazonChimeVoiceConnector** – Allows Amazon Chime SDK Voice Connectors to call AWS services on your behalf. For more information about how to start media streaming for your Amazon Chime SDK Voice Connector, see [Streaming Amazon Chime SDK Voice Connector media to Kinesis](start-kinesis-vc.md).

The AWSServiceRoleForAmazonChimeVoiceConnector service-linked role trusts the following services to assume the role:
+ `voiceconnector.chime.amazonaws.com`

The [AmazonChimeVoiceConnectorServiceLinkedRolePolicy](cvc-linked-role-policy.md) allows the Amazon Chime SDK to complete the following actions on the specified resources:
+ Action: `chime:GetVoiceConnector*` on `all AWS resources`
+ Action: `kinesisvideo:*` on `arn:aws:kinesisvideo:us-east-1:{{111122223333}}:stream/ChimeVoiceConnector-*`
+ Action: `polly:SynthesizeSpeech` on `all AWS resources`
+ Action: `chime:CreateMediaInsightsPipeline` on `all AWS resources`
+ Action: `chime:GetMediaInsightsPipelineConfiguration` on `all AWS resources`
+ Action: `kinesisvideo:CreateStream` on `arn:aws:kinesisvideo:us-east-1:{{111122223333}}:stream/ChimeMediaPipelines-*`
+ Action: `kinesisvideo:PutMedia` on `arn:aws:kinesisvideo:us-east-1:{{111122223333}}:stream/ChimeMediaPipelines-*`
+ Action: `kinesisvideo:UpdateDataRetention` on `arn:aws:kinesisvideo:us-east-1:{{111122223333}}:stream/ChimeMediaPipelines-*`
+ Action: `kinesisvideo:DescribeStream` on `arn:aws:kinesisvideo:us-east-1:{{111122223333}}:stream/ChimeMediaPipelines-*`
+ Action: `kinesisvideo:GetDataEndpoint` on `arn:aws:kinesisvideo:us-east-1:{{111122223333}}:stream/ChimeMediaPipelines-*`
+ Action: `kinesisvideo:ListStreams` on `arn:aws:kinesisvideo:us-east-1:{{111122223333}}:stream/*`

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for Amazon Chime SDK Voice Connectors
<a name="create-service-linked-role-stream"></a>

You don't need to manually create a service-linked role. When you start Kinesis media streaming for your Amazon Chime SDK Voice Connector, or create or update an Amazon Chime SDK SIP media application in the AWS Management Console, the AWS CLI, or the AWS API, Amazon Chime creates the service-linked role for you.

You can also use the IAM console to create a service-linked role with the **Chime Voice Connector** use case. In the AWS CLI or the AWS API, create a service-linked role with the `voiceconnector.chime.amazonaws.com` service name. For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

## Editing a service-linked role for Amazon Chime SDK Voice Connectors
<a name="edit-service-linked-role-stream"></a>

The Amazon Chime SDK does not allow you to edit the AWSServiceRoleForAmazonChimeVoiceConnector service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for Amazon Chime SDK Voice Connectors
<a name="delete-service-linked-role-stream"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up your service-linked role before you can manually delete it.

### Cleaning up a service-linked role
<a name="service-linked-role-review-before-delete-stream"></a>

Before you can use IAM to delete a service-linked role, you must first delete any resources used by the role.

**Note**
If the Amazon Chime SDK service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To delete Amazon Chime SDK resources used by the AWSServiceRoleForAmazonChimeVoiceConnector (console)**
+ Stop media streaming for all the Amazon Chime SDK Voice Connectors in your Amazon Chime SDK account.

  1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

  1. In the navigation pane, under **SIP Trunking**, choose **Voice connectors**.

  1. Choose the name of the Amazon Chime SDK Voice Connector.

  1. Choose the **Streaming** tab.

  1. Under **Send to Kinesis Video Streams**, choose **Stop**.

  1. Choose **Save**.

**To delete Amazon Chime SDK resources used by the AWSServiceRoleForAmazonChimeVoiceConnector (AWS CLI)**
+ Use the `delete-voice-connector-streaming-configuration` command in the AWS CLI to stop media streaming for all Amazon Chime SDK Voice Connectors in your account.

  ```
  aws chime delete-voice-connector-streaming-configuration --voice-connector-id {{abcdef1ghij2klmno3pqr4}}
  ```

**To delete Amazon Chime SDK resources used by the AWSServiceRoleForAmazonChimeVoiceConnector (API)**
+ Use the [DeleteVoiceConnectorStreamingConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_voice-chime_DeleteVoiceConnectorStreamingConfiguration.html) API to stop media streaming for all Amazon Chime SDK Voice Connectors in your account.

### Manually delete the service-linked role
<a name="slr-manual-delete-stream"></a>

Use the IAM console, the AWS CLI, or the AWS API operation to delete the AWSServiceRoleForAmazonChimeVoiceConnector service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for Amazon Chime SDK service-linked roles
<a name="slr-regions-stream"></a>

Amazon Chime SDK supports using service-linked roles in all of the AWS Regions where the service is available. For more information, see [Amazon Chime endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/chime.html#chime_region).
