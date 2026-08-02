---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DevEnvironmentRepositorySummary.html
---

# DevEnvironmentRepositorySummary
<a name="API_DevEnvironmentRepositorySummary"></a>

Information about the source repsitory for a Dev Environment.

## Contents
<a name="API_DevEnvironmentRepositorySummary_Contents"></a>

 ** repositoryName **   <a name="codecatalyst-Type-DevEnvironmentRepositorySummary-repositoryName"></a>
The name of the source repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!.*[.]git$)[\w\-.]*`
Required: Yes

 ** branchName **   <a name="codecatalyst-Type-DevEnvironmentRepositorySummary-branchName"></a>
The name of the branch in a source repository cloned into the Dev Environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_DevEnvironmentRepositorySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/DevEnvironmentRepositorySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/DevEnvironmentRepositorySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/DevEnvironmentRepositorySummary)
