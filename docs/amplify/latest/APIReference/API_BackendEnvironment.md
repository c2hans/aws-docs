---
source_url: https://docs.aws.amazon.com/amplify/latest/APIReference/API_BackendEnvironment.html
---

# BackendEnvironment
<a name="API_BackendEnvironment"></a>

Describes the backend environment associated with a `Branch` of a Gen 1 Amplify app. Amplify Gen 1 applications are created using Amplify Studio or the Amplify command line interface (CLI).

## Contents
<a name="API_BackendEnvironment_Contents"></a>

 ** backendEnvironmentArn **   <a name="amplify-Type-BackendEnvironment-backendEnvironmentArn"></a>
The Amazon Resource Name (ARN) for a backend environment that is part of an Amplify app.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `(?s).*`
Required: Yes

 ** createTime **   <a name="amplify-Type-BackendEnvironment-createTime"></a>
The creation date and time for a backend environment that is part of an Amplify app.
Type: Timestamp
Required: Yes

 ** environmentName **   <a name="amplify-Type-BackendEnvironment-environmentName"></a>
The name for a backend environment that is part of an Amplify app.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?s).+`
Required: Yes

 ** updateTime **   <a name="amplify-Type-BackendEnvironment-updateTime"></a>
The last updated date and time for a backend environment that is part of an Amplify app.
Type: Timestamp
Required: Yes

 ** deploymentArtifacts **   <a name="amplify-Type-BackendEnvironment-deploymentArtifacts"></a>
The name of deployment artifacts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(?s).+`
Required: No

 ** stackName **   <a name="amplify-Type-BackendEnvironment-stackName"></a>
The AWS CloudFormation stack name of a backend environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?s).+`
Required: No

## See Also
<a name="API_BackendEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/BackendEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/BackendEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/BackendEnvironment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amplify. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
