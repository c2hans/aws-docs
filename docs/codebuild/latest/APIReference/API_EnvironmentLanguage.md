---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_EnvironmentLanguage.html
---

# EnvironmentLanguage
<a name="API_EnvironmentLanguage"></a>

A set of Docker images that are related by programming language and are managed by AWS CodeBuild.

## Contents
<a name="API_EnvironmentLanguage_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** images **   <a name="CodeBuild-Type-EnvironmentLanguage-images"></a>
The list of Docker images that are related by the specified programming language.
Type: Array of [EnvironmentImage](API_EnvironmentImage.md) objects
Required: No

 ** language **   <a name="CodeBuild-Type-EnvironmentLanguage-language"></a>
The programming language for the Docker images.
Type: String
Valid Values: `JAVA | PYTHON | NODE_JS | RUBY | GOLANG | DOCKER | ANDROID | DOTNET | BASE | PHP`
Required: No

## See Also
<a name="API_EnvironmentLanguage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/EnvironmentLanguage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/EnvironmentLanguage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/EnvironmentLanguage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
