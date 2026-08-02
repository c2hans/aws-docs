---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_EcrContainerImageMetadata.html
---

# EcrContainerImageMetadata
<a name="API_EcrContainerImageMetadata"></a>

Information on the Amazon ECR image metadata associated with a finding.

## Contents
<a name="API_EcrContainerImageMetadata_Contents"></a>

 ** imagePulledAt **   <a name="inspector2-Type-EcrContainerImageMetadata-imagePulledAt"></a>
The date an image was last pulled at.
Type: Timestamp
Required: No

 ** inUseCount **   <a name="inspector2-Type-EcrContainerImageMetadata-inUseCount"></a>
The number of Amazon ECS tasks or Amazon EKS pods where the Amazon ECR container image is in use.
Type: Long
Required: No

 ** lastInUseAt **   <a name="inspector2-Type-EcrContainerImageMetadata-lastInUseAt"></a>
The last time an Amazon ECR image was used in an Amazon ECS task or Amazon EKS pod.
Type: Timestamp
Required: No

 ** tags **   <a name="inspector2-Type-EcrContainerImageMetadata-tags"></a>
Tags associated with the Amazon ECR image metadata.
Type: Array of strings
Required: No

## See Also
<a name="API_EcrContainerImageMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/EcrContainerImageMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/EcrContainerImageMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/EcrContainerImageMetadata)
