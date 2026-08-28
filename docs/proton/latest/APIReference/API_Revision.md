---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_Revision.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# Revision
<a name="API_Revision"></a>

Revision detail data for a commit and push that activates a sync attempt

## Contents
<a name="API_Revision_Contents"></a>

 ** branch **   <a name="proton-Type-Revision-branch"></a>
The repository branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** directory **   <a name="proton-Type-Revision-directory"></a>
The repository directory changed by a commit and push that activated the sync attempt.
Type: String
Required: Yes

 ** repositoryName **   <a name="proton-Type-Revision-repositoryName"></a>
The repository name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[A-Za-z0-9_.-].*/[A-Za-z0-9_.-].*`
Required: Yes

 ** repositoryProvider **   <a name="proton-Type-Revision-repositoryProvider"></a>
The repository provider.
Type: String
Valid Values: `GITHUB | GITHUB_ENTERPRISE | BITBUCKET`
Required: Yes

 ** sha **   <a name="proton-Type-Revision-sha"></a>
The secure hash algorithm (SHA) hash for the revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_Revision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/Revision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/Revision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/Revision)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
