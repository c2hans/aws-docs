---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListImageReferrersFilter.html
---

# ListImageReferrersFilter
<a name="API_ListImageReferrersFilter"></a>

An object representing a filter on a [ListImageReferrers](API_ListImageReferrers.md) operation.

## Contents
<a name="API_ListImageReferrersFilter_Contents"></a>

 ** artifactStatus **   <a name="ECR-Type-ListImageReferrersFilter-artifactStatus"></a>
The artifact status with which to filter your [ListImageReferrers](API_ListImageReferrers.md) results. Valid values are `ACTIVE`, `ARCHIVED`, `ACTIVATING`, or `ANY`. If not specified, only artifacts with `ACTIVE` status are returned.
Type: String
Valid Values: `ACTIVE | ARCHIVED | ACTIVATING | ANY`
Required: No

 ** artifactTypes **   <a name="ECR-Type-ListImageReferrersFilter-artifactTypes"></a>
The artifact types with which to filter your [ListImageReferrers](API_ListImageReferrers.md) results.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_ListImageReferrersFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ListImageReferrersFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ListImageReferrersFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ListImageReferrersFilter)
