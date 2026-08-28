---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_BatchDisassociateApprovalRuleTemplateFromRepositoriesError.html
---

# BatchDisassociateApprovalRuleTemplateFromRepositoriesError
<a name="API_BatchDisassociateApprovalRuleTemplateFromRepositoriesError"></a>

Returns information about errors in a BatchDisassociateApprovalRuleTemplateFromRepositories operation.

## Contents
<a name="API_BatchDisassociateApprovalRuleTemplateFromRepositoriesError_Contents"></a>

 ** errorCode **   <a name="CodeCommit-Type-BatchDisassociateApprovalRuleTemplateFromRepositoriesError-errorCode"></a>
An error code that specifies whether the repository name was not valid or not found.
Type: String
Required: No

 ** errorMessage **   <a name="CodeCommit-Type-BatchDisassociateApprovalRuleTemplateFromRepositoriesError-errorMessage"></a>
An error message that provides details about why the repository name was either not found or not valid.
Type: String
Required: No

 ** repositoryName **   <a name="CodeCommit-Type-BatchDisassociateApprovalRuleTemplateFromRepositoriesError-repositoryName"></a>
The name of the repository where the association with the template was not able to be removed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: No

## See Also
<a name="API_BatchDisassociateApprovalRuleTemplateFromRepositoriesError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/BatchDisassociateApprovalRuleTemplateFromRepositoriesError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/BatchDisassociateApprovalRuleTemplateFromRepositoriesError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/BatchDisassociateApprovalRuleTemplateFromRepositoriesError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
