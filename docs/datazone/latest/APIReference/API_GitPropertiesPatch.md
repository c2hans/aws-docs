---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GitPropertiesPatch.html
---

# GitPropertiesPatch
<a name="API_GitPropertiesPatch"></a>

The properties used to update an existing Git connection, such as the AWS CodeConnections ARN or the default branch.

## Contents
<a name="API_GitPropertiesPatch_Contents"></a>

 ** codeConnectionArn **   <a name="datazone-Type-GitPropertiesPatch-codeConnectionArn"></a>
The ARN of the AWS CodeConnections connection used to connect to the Git repository.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[^:]*:(codeconnections|codestar-connections):[a-z0-9\-]+:\d{12}:connection/[a-f0-9\-]+`
Required: No

 ** defaultBranch **   <a name="datazone-Type-GitPropertiesPatch-defaultBranch"></a>
The default branch of the Git repository.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9._\-/]+`
Required: No

## See Also
<a name="API_GitPropertiesPatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GitPropertiesPatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GitPropertiesPatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GitPropertiesPatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
