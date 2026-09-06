---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListImagesFilter.html
---

# ListImagesFilter
<a name="API_ListImagesFilter"></a>

An object representing a filter on a [ListImages](API_ListImages.md) operation.

## Contents
<a name="API_ListImagesFilter_Contents"></a>

 ** imageStatus **   <a name="ECR-Type-ListImagesFilter-imageStatus"></a>
The image status with which to filter your [ListImages](API_ListImages.md) results. Valid values are `ACTIVE`, `ARCHIVED`, and `ACTIVATING`. If not specified, only images with `ACTIVE` status are returned.
Type: String
Valid Values: `ACTIVE | ARCHIVED | ACTIVATING | ANY`
Required: No

 ** tagStatus **   <a name="ECR-Type-ListImagesFilter-tagStatus"></a>
The tag status with which to filter your [ListImages](API_ListImages.md) results.
Type: String
Valid Values: `TAGGED | UNTAGGED | ANY`
Required: No

## See Also
<a name="API_ListImagesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ListImagesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ListImagesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ListImagesFilter)
