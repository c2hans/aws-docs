---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GitPropertiesInput.html
---

# GitPropertiesInput
<a name="API_GitPropertiesInput"></a>

Contains the Git connection properties that you specify when creating a Git connection.

## Contents
<a name="API_GitPropertiesInput_Contents"></a>

 ** codeConnectionArn **   <a name="datazone-Type-GitPropertiesInput-codeConnectionArn"></a>
The ARN of the AWS CodeConnections connection used to connect to the Git repository.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[^:]*:(codeconnections|codestar-connections):[a-z0-9\-]+:\d{12}:connection/[a-f0-9\-]+`
Required: Yes

 ** defaultBranch **   <a name="datazone-Type-GitPropertiesInput-defaultBranch"></a>
The default branch of the Git repository.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9._\-/]+`
Required: Yes

 ** repositoryId **   <a name="datazone-Type-GitPropertiesInput-repositoryId"></a>
The ID of the Git repository. This is the owner and repository name, for example, owner/repo-name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9._\-]+(/[a-zA-Z0-9._\-]+)+`
Required: Yes

## See Also
<a name="API_GitPropertiesInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GitPropertiesInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GitPropertiesInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GitPropertiesInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
