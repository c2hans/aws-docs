---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_RepositorySyncDefinition.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# RepositorySyncDefinition
<a name="API_RepositorySyncDefinition"></a>

A repository sync definition.

## Contents
<a name="API_RepositorySyncDefinition_Contents"></a>

 ** branch **   <a name="proton-Type-RepositorySyncDefinition-branch"></a>
The repository branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** directory **   <a name="proton-Type-RepositorySyncDefinition-directory"></a>
The directory in the repository.
Type: String
Required: Yes

 ** parent **   <a name="proton-Type-RepositorySyncDefinition-parent"></a>
The resource that is synced from.
Type: String
Required: Yes

 ** target **   <a name="proton-Type-RepositorySyncDefinition-target"></a>
The resource that is synced to.
Type: String
Required: Yes

## See Also
<a name="API_RepositorySyncDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/RepositorySyncDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/RepositorySyncDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/RepositorySyncDefinition)
