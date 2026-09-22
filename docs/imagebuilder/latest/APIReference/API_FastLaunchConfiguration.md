---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_FastLaunchConfiguration.html
---

# FastLaunchConfiguration
<a name="API_FastLaunchConfiguration"></a>

Defines and configures EC2 Fast Launch for output Windows AMIs.

## Contents
<a name="API_FastLaunchConfiguration_Contents"></a>

 ** enabled **   <a name="imagebuilder-Type-FastLaunchConfiguration-enabled"></a>
Specifies whether to enable Windows fast launch on the output AMI during distribution. A value of `false` means Image Builder takes no fast-launch action for this configuration.
Type: Boolean
Required: Yes

 ** accountId **   <a name="imagebuilder-Type-FastLaunchConfiguration-accountId"></a>
The owner account ID for the fast-launch enabled Windows AMI.
Type: String
Pattern: `^[0-9]{12}$`
Required: No

 ** launchTemplate **   <a name="imagebuilder-Type-FastLaunchConfiguration-launchTemplate"></a>
The launch template that the fast-launch enabled Windows AMI uses when it launches Windows instances to create pre-provisioned snapshots.
Type: [FastLaunchLaunchTemplateSpecification](API_FastLaunchLaunchTemplateSpecification.md) object
Required: No

 ** maxParallelLaunches **   <a name="imagebuilder-Type-FastLaunchConfiguration-maxParallelLaunches"></a>
The maximum number of parallel instances that are launched for creating resources.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** snapshotConfiguration **   <a name="imagebuilder-Type-FastLaunchConfiguration-snapshotConfiguration"></a>
Configuration settings for managing the number of snapshots that are created from pre-provisioned instances for the Windows AMI when Windows fast launch is enabled.
Type: [FastLaunchSnapshotConfiguration](API_FastLaunchSnapshotConfiguration.md) object
Required: No

## See Also
<a name="API_FastLaunchConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/FastLaunchConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/FastLaunchConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/FastLaunchConfiguration)
