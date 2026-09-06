---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_BatchAssociateApprovalRuleTemplateWithRepositoriesError.html
---

# BatchAssociateApprovalRuleTemplateWithRepositoriesError
<a name="API_BatchAssociateApprovalRuleTemplateWithRepositoriesError"></a>

Returns information about errors in a BatchAssociateApprovalRuleTemplateWithRepositories operation.

## Contents
<a name="API_BatchAssociateApprovalRuleTemplateWithRepositoriesError_Contents"></a>

 ** errorCode **   <a name="CodeCommit-Type-BatchAssociateApprovalRuleTemplateWithRepositoriesError-errorCode"></a>
An error code that specifies whether the repository name was not valid or not found.
Type: String
Required: No

 ** errorMessage **   <a name="CodeCommit-Type-BatchAssociateApprovalRuleTemplateWithRepositoriesError-errorMessage"></a>
An error message that provides details about why the repository name was not found or not valid.
Type: String
Required: No

 ** repositoryName **   <a name="CodeCommit-Type-BatchAssociateApprovalRuleTemplateWithRepositoriesError-repositoryName"></a>
The name of the repository where the association was not made.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: No

## See Also
<a name="API_BatchAssociateApprovalRuleTemplateWithRepositoriesError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/BatchAssociateApprovalRuleTemplateWithRepositoriesError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/BatchAssociateApprovalRuleTemplateWithRepositoriesError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/BatchAssociateApprovalRuleTemplateWithRepositoriesError)
