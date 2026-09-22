---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_TargetContainerRepository.html
---

# TargetContainerRepository
<a name="API_TargetContainerRepository"></a>

The container repository where the output container image is stored.

## Contents
<a name="API_TargetContainerRepository_Contents"></a>

 ** repositoryName **   <a name="imagebuilder-Type-TargetContainerRepository-repositoryName"></a>
The name of the container repository where the output container image is stored. Provide the repository name only (a namespace path such as `team-a/my-repo` is allowed, but not the registry hostname).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** service **   <a name="imagebuilder-Type-TargetContainerRepository-service"></a>
Specifies the service in which this image was registered.
Type: String
Valid Values: `ECR`
Required: Yes

## See Also
<a name="API_TargetContainerRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/TargetContainerRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/TargetContainerRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/TargetContainerRepository)
