---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_RepositoryTrigger.html
---

# RepositoryTrigger
<a name="API_RepositoryTrigger"></a>

Information about a trigger for a repository.

**Note**
If you want to receive notifications about repository events, consider using notifications instead of triggers. For more information, see [Configuring notifications for repository events](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-repository-email.html).

## Contents
<a name="API_RepositoryTrigger_Contents"></a>

 ** destinationArn **   <a name="CodeCommit-Type-RepositoryTrigger-destinationArn"></a>
The ARN of the resource that is the target for a trigger (for example, the ARN of a topic in Amazon SNS).
Type: String
Required: Yes

 ** events **   <a name="CodeCommit-Type-RepositoryTrigger-events"></a>
The repository events that cause the trigger to run actions in another service, such as sending a notification through Amazon SNS.
The valid value "all" cannot be used with any other values.
Type: Array of strings
Valid Values: `all | updateReference | createReference | deleteReference`
Required: Yes

 ** name **   <a name="CodeCommit-Type-RepositoryTrigger-name"></a>
The name of the trigger.
Type: String
Required: Yes

 ** branches **   <a name="CodeCommit-Type-RepositoryTrigger-branches"></a>
The branches to be included in the trigger configuration. If you specify an empty array, the trigger applies to all branches.
Although no content is required in the array, you must include the array itself.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** customData **   <a name="CodeCommit-Type-RepositoryTrigger-customData"></a>
Any custom data associated with the trigger to be included in the information sent to the target of the trigger.
Type: String
Required: No

## See Also
<a name="API_RepositoryTrigger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/RepositoryTrigger)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/RepositoryTrigger)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/RepositoryTrigger)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
