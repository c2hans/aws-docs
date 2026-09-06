---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsEcrContainerAggregationResponse.html
---

# AwsEcrContainerAggregationResponse
<a name="API_AwsEcrContainerAggregationResponse"></a>

An aggregation of information about Amazon ECR containers.

## Contents
<a name="API_AwsEcrContainerAggregationResponse_Contents"></a>

 ** resourceId **   <a name="inspector2-Type-AwsEcrContainerAggregationResponse-resourceId"></a>
The resource ID of the container.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** accountId **   <a name="inspector2-Type-AwsEcrContainerAggregationResponse-accountId"></a>
The AWS account ID of the account that owns the container.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** architecture **   <a name="inspector2-Type-AwsEcrContainerAggregationResponse-architecture"></a>
The architecture of the container.
Type: String
Required: No

 ** imageSha **   <a name="inspector2-Type-AwsEcrContainerAggregationResponse-imageSha"></a>
The SHA value of the container image.
Type: String
Required: No

 ** imageTags **   <a name="inspector2-Type-AwsEcrContainerAggregationResponse-imageTags"></a>
The container image stags.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** inUseCount **   <a name="inspector2-Type-AwsEcrContainerAggregationResponse-inUseCount"></a>
The number of Amazon ECS tasks or Amazon EKS pods where the Amazon ECR container image is in use.
Type: Long
Required: No

 ** lastInUseAt **   <a name="inspector2-Type-AwsEcrContainerAggregationResponse-lastInUseAt"></a>
The last time an Amazon ECR image was used in an Amazon ECS task or Amazon EKS pod.
Type: Timestamp
Required: No

 ** repository **   <a name="inspector2-Type-AwsEcrContainerAggregationResponse-repository"></a>
The container repository.
Type: String
Required: No

 ** severityCounts **   <a name="inspector2-Type-AwsEcrContainerAggregationResponse-severityCounts"></a>
The number of finding by severity.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_AwsEcrContainerAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AwsEcrContainerAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AwsEcrContainerAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AwsEcrContainerAggregationResponse)
