---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ContainerImageMetadata.html
---

# ContainerImageMetadata
<a name="API_ContainerImageMetadata"></a>

Contains metadata about a container image associated with a covered resource.

## Contents
<a name="API_ContainerImageMetadata_Contents"></a>

 ** imagePulledAt **   <a name="inspector2-Type-ContainerImageMetadata-imagePulledAt"></a>
The date and time the container image was pulled.
Type: Timestamp
Required: No

 ** imageTags **   <a name="inspector2-Type-ContainerImageMetadata-imageTags"></a>
The tags attached to the container image.
Type: Array of strings
Required: No

 ** inUseCount **   <a name="inspector2-Type-ContainerImageMetadata-inUseCount"></a>
The number of times the container image is in use.
Type: Long
Required: No

 ** lastInUseAt **   <a name="inspector2-Type-ContainerImageMetadata-lastInUseAt"></a>
The last time the container image was in use.
Type: Timestamp
Required: No

## See Also
<a name="API_ContainerImageMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ContainerImageMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ContainerImageMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ContainerImageMetadata)
