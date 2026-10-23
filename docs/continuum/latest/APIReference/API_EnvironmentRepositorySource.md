---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_EnvironmentRepositorySource.html
---

# EnvironmentRepositorySource
<a name="API_EnvironmentRepositorySource"></a>

One repository selected from a previously-created integration.

## Contents
<a name="API_EnvironmentRepositorySource_Contents"></a>

 ** integrationId **   <a name="continuum-Type-EnvironmentRepositorySource-integrationId"></a>
The identifier of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** repository **   <a name="continuum-Type-EnvironmentRepositorySource-repository"></a>
The repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+`
Required: Yes

 ** defaultBranch **   <a name="continuum-Type-EnvironmentRepositorySource-defaultBranch"></a>
The default Branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_EnvironmentRepositorySource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/EnvironmentRepositorySource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/EnvironmentRepositorySource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/EnvironmentRepositorySource)
