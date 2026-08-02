---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_SourceCodeVersion.html
---

# SourceCodeVersion
<a name="API_SourceCodeVersion"></a>

Identifies a version of code that AWS App Runner refers to within a source code repository.

## Contents
<a name="API_SourceCodeVersion_Contents"></a>

 ** Type **   <a name="apprunner-Type-SourceCodeVersion-Type"></a>
The type of version identifier.
For a git-based repository, branches represent versions.
Type: String
Valid Values: `BRANCH`
Required: Yes

 ** Value **   <a name="apprunner-Type-SourceCodeVersion-Value"></a>
A source code version.
For a git-based repository, a branch name maps to a specific version. App Runner uses the most recent commit to the branch.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_SourceCodeVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/SourceCodeVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/SourceCodeVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/SourceCodeVersion)
