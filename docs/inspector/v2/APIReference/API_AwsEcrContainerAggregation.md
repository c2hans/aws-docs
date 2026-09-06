---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsEcrContainerAggregation.html
---

# AwsEcrContainerAggregation
<a name="API_AwsEcrContainerAggregation"></a>

An aggregation of information about Amazon ECR containers.

## Contents
<a name="API_AwsEcrContainerAggregation_Contents"></a>

 ** architectures **   <a name="inspector2-Type-AwsEcrContainerAggregation-architectures"></a>
The architecture of the containers.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** imageShas **   <a name="inspector2-Type-AwsEcrContainerAggregation-imageShas"></a>
The image SHA values.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** imageTags **   <a name="inspector2-Type-AwsEcrContainerAggregation-imageTags"></a>
The image tags.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** inUseCount **   <a name="inspector2-Type-AwsEcrContainerAggregation-inUseCount"></a>
The number of Amazon ECS tasks or Amazon EKS pods where the Amazon ECR container image is in use.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lastInUseAt **   <a name="inspector2-Type-AwsEcrContainerAggregation-lastInUseAt"></a>
The last time an Amazon ECR image was used in an Amazon ECS task or Amazon EKS pod.
Type: Array of [DateFilter](API_DateFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** repositories **   <a name="inspector2-Type-AwsEcrContainerAggregation-repositories"></a>
The container repositories.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceIds **   <a name="inspector2-Type-AwsEcrContainerAggregation-resourceIds"></a>
The container resource IDs.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** sortBy **   <a name="inspector2-Type-AwsEcrContainerAggregation-sortBy"></a>
The value to sort by.
Type: String
Valid Values: `CRITICAL | HIGH | ALL`
Required: No

 ** sortOrder **   <a name="inspector2-Type-AwsEcrContainerAggregation-sortOrder"></a>
The sort order (ascending or descending).
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_AwsEcrContainerAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AwsEcrContainerAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AwsEcrContainerAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AwsEcrContainerAggregation)
