---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_ImageRepository.html
---

# ImageRepository
<a name="API_ImageRepository"></a>

Describes a source image repository.

## Contents
<a name="API_ImageRepository_Contents"></a>

 ** ImageIdentifier **   <a name="apprunner-Type-ImageRepository-ImageIdentifier"></a>
The identifier of an image.
For an image in Amazon Elastic Container Registry (Amazon ECR), this is an image name. For the image name format, see [Pulling an image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html) in the *Amazon ECR User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `([0-9]{12}.dkr.ecr.[a-z\-]+-[0-9]{1}.amazonaws.com\/((?:[a-z0-9]+(?:[._-][a-z0-9]+)*\/)*[a-z0-9]+(?:[._-][a-z0-9]+)*)(:([\w\d+\-=._:\/@])+|@([\w\d\:]+))?)|(^public\.ecr\.aws\/.+\/((?:[a-z0-9]+(?:[._-][a-z0-9]+)*\/)*[a-z0-9]+(?:[._-][a-z0-9]+)*)(:([\w\d+\-=._:\/@])+|@([\w\d\:]+))?)`
Required: Yes

 ** ImageRepositoryType **   <a name="apprunner-Type-ImageRepository-ImageRepositoryType"></a>
The type of the image repository. This reflects the repository provider and whether the repository is private or public.
Type: String
Valid Values: `ECR | ECR_PUBLIC`
Required: Yes

 ** ImageConfiguration **   <a name="apprunner-Type-ImageRepository-ImageConfiguration"></a>
Configuration for running the identified image.
Type: [ImageConfiguration](API_ImageConfiguration.md) object
Required: No

## See Also
<a name="API_ImageRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/ImageRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/ImageRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/ImageRepository)
