---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_CodeRepository.html
---

# CodeRepository
<a name="API_CodeRepository"></a>

Describes a source code repository.

## Contents
<a name="API_CodeRepository_Contents"></a>

 ** RepositoryUrl **   <a name="apprunner-Type-CodeRepository-RepositoryUrl"></a>
The location of the repository that contains the source code.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: Yes

 ** SourceCodeVersion **   <a name="apprunner-Type-CodeRepository-SourceCodeVersion"></a>
The version that should be used within the source code repository.
Type: [SourceCodeVersion](API_SourceCodeVersion.md) object
Required: Yes

 ** CodeConfiguration **   <a name="apprunner-Type-CodeRepository-CodeConfiguration"></a>
Configuration for building and running the service from a source code repository.
 `CodeConfiguration` is required only for `CreateService` request.
Type: [CodeConfiguration](API_CodeConfiguration.md) object
Required: No

 ** SourceDirectory **   <a name="apprunner-Type-CodeRepository-SourceDirectory"></a>
The path of the directory that stores source code and configuration files. The build and start commands also execute from here. The path is absolute from root and, if not specified, defaults to the repository root.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[^\x00]+`
Required: No

## See Also
<a name="API_CodeRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/CodeRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/CodeRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/CodeRepository)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
