---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpstreamRepository.html
---

# UpstreamRepository
<a name="API_UpstreamRepository"></a>

 Information about an upstream repository. A list of `UpstreamRepository` objects is an input parameter to [CreateRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreateRepository.html) and [UpdateRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdateRepository.html).

## Contents
<a name="API_UpstreamRepository_Contents"></a>

 ** repositoryName **   <a name="codeartifact-Type-UpstreamRepository-repositoryName"></a>
 The name of an upstream repository.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## See Also
<a name="API_UpstreamRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/UpstreamRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/UpstreamRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/UpstreamRepository)
