---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BuildStatusConfig.html
---

# BuildStatusConfig
<a name="API_BuildStatusConfig"></a>

Contains information that defines how the AWS CodeBuild build project reports the build status to the source provider.

## Contents
<a name="API_BuildStatusConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** context **   <a name="CodeBuild-Type-BuildStatusConfig-context"></a>
Specifies the context of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.
Bitbucket
This parameter is used for the `name` parameter in the Bitbucket commit status. For more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build) in the Bitbucket API documentation.
GitHub/GitHub Enterprise Server
This parameter is used for the `context` parameter in the GitHub commit status. For more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status) in the GitHub developer guide.
Type: String
Required: No

 ** targetUrl **   <a name="CodeBuild-Type-BuildStatusConfig-targetUrl"></a>
Specifies the target url of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.
Bitbucket
This parameter is used for the `url` parameter in the Bitbucket commit status. For more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build) in the Bitbucket API documentation.
GitHub/GitHub Enterprise Server
This parameter is used for the `target_url` parameter in the GitHub commit status. For more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status) in the GitHub developer guide.
Type: String
Required: No

## See Also
<a name="API_BuildStatusConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BuildStatusConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BuildStatusConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BuildStatusConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
