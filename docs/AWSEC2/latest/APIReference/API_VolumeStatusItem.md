---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VolumeStatusItem.html
---

# VolumeStatusItem
<a name="API_VolumeStatusItem"></a>

Describes the volume status.

## Contents
<a name="API_VolumeStatusItem_Contents"></a>

 ** ActionsSet.N **
The details of the operation.
Type: Array of [VolumeStatusAction](API_VolumeStatusAction.md) objects
Required: No

 ** AttachmentStatuses.N **
Information about the instances to which the volume is attached.
Type: Array of [VolumeStatusAttachmentStatus](API_VolumeStatusAttachmentStatus.md) objects
Required: No

 ** availabilityZone **
The Availability Zone of the volume.
Type: String
Required: No

 ** availabilityZoneId **
The ID of the Availability Zone.
Type: String
Required: No

 ** EventsSet.N **
A list of events associated with the volume.
Type: Array of [VolumeStatusEvent](API_VolumeStatusEvent.md) objects
Required: No

 ** initializationStatusDetails **
Information about the volume initialization. It can take up to 5 minutes for the volume initialization information to be updated.
Only available for volumes created from snapshots. Not available for empty volumes created without a snapshot.
For more information, see [ Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html).
Type: [InitializationStatusDetails](API_InitializationStatusDetails.md) object
Required: No

 ** operator **
The service provider that manages the resource.
Type: [OperatorResponse](API_OperatorResponse.md) object
Required: No

 ** outpostArn **
The Amazon Resource Name (ARN) of the Outpost.
Type: String
Required: No

 ** volumeId **
The volume ID.
Type: String
Required: No

 ** volumeStatus **
The volume status.
Type: [VolumeStatusInfo](API_VolumeStatusInfo.md) object
Required: No

## See Also
<a name="API_VolumeStatusItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VolumeStatusItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VolumeStatusItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VolumeStatusItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
