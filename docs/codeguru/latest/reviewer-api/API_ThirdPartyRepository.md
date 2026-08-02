---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ThirdPartyRepository.html
---

# ThirdPartyRepository
<a name="API_ThirdPartyRepository"></a>

Information about a third-party repository that can be connected to CodeGuru Reviewer.

## Contents
<a name="API_ThirdPartyRepository_Contents"></a>

 ** ConnectionToken **   <a name="reviewer-Type-ThirdPartyRepository-ConnectionToken"></a>
The connection token used to access the third-party repository.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 2048.
Pattern: `\S+`
Required: Yes

 ** Name **   <a name="reviewer-Type-ThirdPartyRepository-Name"></a>
The name of the third-party repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S[\w.-]*$`
Required: Yes

 ** Owner **   <a name="reviewer-Type-ThirdPartyRepository-Owner"></a>
The owner of the third-party repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: Yes

 ** IsEnabled **   <a name="reviewer-Type-ThirdPartyRepository-IsEnabled"></a>
Indicates whether the third-party repository is enabled for code analysis.
Type: Boolean
Required: No

## See Also
<a name="API_ThirdPartyRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/ThirdPartyRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/ThirdPartyRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/ThirdPartyRepository)
