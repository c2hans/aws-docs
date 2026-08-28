---
source_url: https://docs.aws.amazon.com/amplify/latest/APIReference/API_AutoBranchCreationConfig.html
---

# AutoBranchCreationConfig
<a name="API_AutoBranchCreationConfig"></a>

Describes the automated branch creation configuration.

## Contents
<a name="API_AutoBranchCreationConfig_Contents"></a>

 ** basicAuthCredentials **   <a name="amplify-Type-AutoBranchCreationConfig-basicAuthCredentials"></a>
The basic authorization credentials for the autocreated branch. You must base64-encode the authorization credentials and provide them in the format `user:password`.
Type: String
Length Constraints: Maximum length of 2000.
Pattern: `(?s).*`
Required: No

 ** buildSpec **   <a name="amplify-Type-AutoBranchCreationConfig-buildSpec"></a>
The build specification (build spec) for the autocreated branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25000.
Pattern: `(?s).+`
Required: No

 ** enableAutoBuild **   <a name="amplify-Type-AutoBranchCreationConfig-enableAutoBuild"></a>
Enables auto building for the autocreated branch.
Type: Boolean
Required: No

 ** enableBasicAuth **   <a name="amplify-Type-AutoBranchCreationConfig-enableBasicAuth"></a>
Enables basic authorization for the autocreated branch.
Type: Boolean
Required: No

 ** enablePerformanceMode **   <a name="amplify-Type-AutoBranchCreationConfig-enablePerformanceMode"></a>
Enables performance mode for the branch.
Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.
Type: Boolean
Required: No

 ** enablePullRequestPreview **   <a name="amplify-Type-AutoBranchCreationConfig-enablePullRequestPreview"></a>
Enables pull request previews for the autocreated branch.
Type: Boolean
Required: No

 ** environmentVariables **   <a name="amplify-Type-AutoBranchCreationConfig-environmentVariables"></a>
The environment variables for the autocreated branch.
Type: String to string map
Key Length Constraints: Maximum length of 255.
Key Pattern: `(?s).*`
Value Length Constraints: Maximum length of 5500.
Value Pattern: `(?s).*`
Required: No

 ** framework **   <a name="amplify-Type-AutoBranchCreationConfig-framework"></a>
The framework for the autocreated branch.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `(?s).*`
Required: No

 ** pullRequestEnvironmentName **   <a name="amplify-Type-AutoBranchCreationConfig-pullRequestEnvironmentName"></a>
The Amplify environment name for the pull request.
Type: String
Length Constraints: Maximum length of 20.
Pattern: `(?s).*`
Required: No

 ** stage **   <a name="amplify-Type-AutoBranchCreationConfig-stage"></a>
Describes the current stage for the autocreated branch.
Type: String
Valid Values: `PRODUCTION | BETA | DEVELOPMENT | EXPERIMENTAL | PULL_REQUEST`
Required: No

## See Also
<a name="API_AutoBranchCreationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/AutoBranchCreationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/AutoBranchCreationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/AutoBranchCreationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amplify. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
