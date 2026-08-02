---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_BatchGetRepositoriesError.html
---

# BatchGetRepositoriesError
<a name="API_BatchGetRepositoriesError"></a>

Returns information about errors in a BatchGetRepositories operation.

## Contents
<a name="API_BatchGetRepositoriesError_Contents"></a>

 ** errorCode **   <a name="CodeCommit-Type-BatchGetRepositoriesError-errorCode"></a>
An error code that specifies the type of failure.
Type: String
Valid Values: `EncryptionIntegrityChecksFailedException | EncryptionKeyAccessDeniedException | EncryptionKeyDisabledException | EncryptionKeyNotFoundException | EncryptionKeyUnavailableException | RepositoryDoesNotExistException`
Required: No

 ** errorMessage **   <a name="CodeCommit-Type-BatchGetRepositoriesError-errorMessage"></a>
An error message that provides detail about why the repository either was not found or was not in a valid state.
Type: String
Required: No

 ** repositoryId **   <a name="CodeCommit-Type-BatchGetRepositoriesError-repositoryId"></a>
The ID of a repository that either could not be found or was not in a valid state.
Type: String
Required: No

 ** repositoryName **   <a name="CodeCommit-Type-BatchGetRepositoriesError-repositoryName"></a>
The name of a repository that either could not be found or was not in a valid state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: No

## See Also
<a name="API_BatchGetRepositoriesError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/BatchGetRepositoriesError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/BatchGetRepositoriesError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/BatchGetRepositoriesError)
