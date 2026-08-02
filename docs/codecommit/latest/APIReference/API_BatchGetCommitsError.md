---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_BatchGetCommitsError.html
---

# BatchGetCommitsError
<a name="API_BatchGetCommitsError"></a>

Returns information about errors in a BatchGetCommits operation.

## Contents
<a name="API_BatchGetCommitsError_Contents"></a>

 ** commitId **   <a name="CodeCommit-Type-BatchGetCommitsError-commitId"></a>
A commit ID that either could not be found or was not in a valid format.
Type: String
Required: No

 ** errorCode **   <a name="CodeCommit-Type-BatchGetCommitsError-errorCode"></a>
An error code that specifies whether the commit ID was not valid or not found.
Type: String
Required: No

 ** errorMessage **   <a name="CodeCommit-Type-BatchGetCommitsError-errorMessage"></a>
An error message that provides detail about why the commit ID either was not found or was not valid.
Type: String
Required: No

## See Also
<a name="API_BatchGetCommitsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/BatchGetCommitsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/BatchGetCommitsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/BatchGetCommitsError)
