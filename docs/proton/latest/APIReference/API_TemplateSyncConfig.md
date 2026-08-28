---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_TemplateSyncConfig.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# TemplateSyncConfig
<a name="API_TemplateSyncConfig"></a>

The detail data for a template sync configuration.

## Contents
<a name="API_TemplateSyncConfig_Contents"></a>

 ** branch **   <a name="proton-Type-TemplateSyncConfig-branch"></a>
The repository branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** repositoryName **   <a name="proton-Type-TemplateSyncConfig-repositoryName"></a>
The repository name (for example, `myrepos/myrepo`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[A-Za-z0-9_.-].*/[A-Za-z0-9_.-].*`
Required: Yes

 ** repositoryProvider **   <a name="proton-Type-TemplateSyncConfig-repositoryProvider"></a>
The repository provider.
Type: String
Valid Values: `GITHUB | GITHUB_ENTERPRISE | BITBUCKET`
Required: Yes

 ** templateName **   <a name="proton-Type-TemplateSyncConfig-templateName"></a>
The template name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** templateType **   <a name="proton-Type-TemplateSyncConfig-templateType"></a>
The template type.
Type: String
Valid Values: `ENVIRONMENT | SERVICE`
Required: Yes

 ** subdirectory **   <a name="proton-Type-TemplateSyncConfig-subdirectory"></a>
A subdirectory path to your template bundle version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_TemplateSyncConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/TemplateSyncConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/TemplateSyncConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/TemplateSyncConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
