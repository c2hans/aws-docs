---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_SourceAuth.html
---

# SourceAuth
<a name="API_SourceAuth"></a>

Information about the authorization settings for AWS CodeBuild to access the source code to be built.

## Contents
<a name="API_SourceAuth_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** type **   <a name="CodeBuild-Type-SourceAuth-type"></a>
The authorization type to use. Valid options are OAUTH, CODECONNECTIONS, or SECRETS\_MANAGER.
Type: String
Valid Values: `OAUTH | CODECONNECTIONS | SECRETS_MANAGER`
Required: Yes

 ** resource **   <a name="CodeBuild-Type-SourceAuth-resource"></a>
The resource value that applies to the specified authorization type.
Type: String
Required: No

## See Also
<a name="API_SourceAuth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/SourceAuth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/SourceAuth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/SourceAuth)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
