---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_ImageTagDetail.html
---

# ImageTagDetail
<a name="API_ImageTagDetail"></a>

An object that represents the image tag details for an image.

## Contents
<a name="API_ImageTagDetail_Contents"></a>

 ** createdAt **   <a name="ecrpublic-Type-ImageTagDetail-createdAt"></a>
The time stamp that indicates when the image tag was created.
Type: Timestamp
Required: No

 ** imageDetail **   <a name="ecrpublic-Type-ImageTagDetail-imageDetail"></a>
An object that describes the details of an image.
Type: [ReferencedImageDetail](API_ReferencedImageDetail.md) object
Required: No

 ** imageTag **   <a name="ecrpublic-Type-ImageTagDetail-imageTag"></a>
The tag that's associated with the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## See Also
<a name="API_ImageTagDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/ImageTagDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/ImageTagDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/ImageTagDetail)
