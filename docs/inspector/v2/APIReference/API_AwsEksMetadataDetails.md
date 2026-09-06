---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsEksMetadataDetails.html
---

# AwsEksMetadataDetails
<a name="API_AwsEksMetadataDetails"></a>

The metadata for an Amazon EKS pod where an Amazon ECR image is in use.

## Contents
<a name="API_AwsEksMetadataDetails_Contents"></a>

 ** namespace **   <a name="inspector2-Type-AwsEksMetadataDetails-namespace"></a>
The namespace for an Amazon EKS cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** workloadInfoList **   <a name="inspector2-Type-AwsEksMetadataDetails-workloadInfoList"></a>
The list of workloads.
Type: Array of [AwsEksWorkloadInfo](API_AwsEksWorkloadInfo.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## See Also
<a name="API_AwsEksMetadataDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AwsEksMetadataDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AwsEksMetadataDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AwsEksMetadataDetails)
