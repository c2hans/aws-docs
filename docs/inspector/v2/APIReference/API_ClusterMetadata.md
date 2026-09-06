---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ClusterMetadata.html
---

# ClusterMetadata
<a name="API_ClusterMetadata"></a>

The metadata for a cluster.

## Contents
<a name="API_ClusterMetadata_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsEcsMetadataDetails **   <a name="inspector2-Type-ClusterMetadata-awsEcsMetadataDetails"></a>
The details for an Amazon ECS cluster in the cluster metadata.
Type: [AwsEcsMetadataDetails](API_AwsEcsMetadataDetails.md) object
Required: No

 ** awsEksMetadataDetails **   <a name="inspector2-Type-ClusterMetadata-awsEksMetadataDetails"></a>
The details for an Amazon EKS cluster in the cluster metadata.
Type: [AwsEksMetadataDetails](API_AwsEksMetadataDetails.md) object
Required: No

## See Also
<a name="API_ClusterMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ClusterMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ClusterMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ClusterMetadata)
