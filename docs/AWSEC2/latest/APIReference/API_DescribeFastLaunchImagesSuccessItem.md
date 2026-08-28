---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFastLaunchImagesSuccessItem.html
---

# DescribeFastLaunchImagesSuccessItem
<a name="API_DescribeFastLaunchImagesSuccessItem"></a>

Describe details about a Windows image with Windows fast launch enabled that meets the requested criteria. Criteria are defined by the `DescribeFastLaunchImages` action filters.

## Contents
<a name="API_DescribeFastLaunchImagesSuccessItem_Contents"></a>

 ** imageId **
The image ID that identifies the Windows fast launch enabled image.
Type: String
Required: No

 ** launchTemplate **
The launch template that the Windows fast launch enabled AMI uses when it launches Windows instances from pre-provisioned snapshots.
Type: [FastLaunchLaunchTemplateSpecificationResponse](API_FastLaunchLaunchTemplateSpecificationResponse.md) object
Required: No

 ** maxParallelLaunches **
The maximum number of instances that Amazon EC2 can launch at the same time to create pre-provisioned snapshots for Windows fast launch.
Type: Integer
Required: No

 ** ownerId **
The owner ID for the Windows fast launch enabled AMI.
Type: String
Required: No

 ** resourceType **
The resource type that Amazon EC2 uses for pre-provisioning the Windows AMI. Supported values include: `snapshot`.
Type: String
Valid Values: `snapshot`
Required: No

 ** snapshotConfiguration **
A group of parameters that are used for pre-provisioning the associated Windows AMI using snapshots.
Type: [FastLaunchSnapshotConfigurationResponse](API_FastLaunchSnapshotConfigurationResponse.md) object
Required: No

 ** state **
The current state of Windows fast launch for the specified Windows AMI.
Type: String
Valid Values: `enabling | enabling-failed | enabled | enabled-failed | disabling | disabling-failed`
Required: No

 ** stateTransitionReason **
The reason that Windows fast launch for the AMI changed to the current state.
Type: String
Required: No

 ** stateTransitionTime **
The time that Windows fast launch for the AMI changed to the current state.
Type: Timestamp
Required: No

## See Also
<a name="API_DescribeFastLaunchImagesSuccessItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeFastLaunchImagesSuccessItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeFastLaunchImagesSuccessItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeFastLaunchImagesSuccessItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
