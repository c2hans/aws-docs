---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PullRequestMergedStateChangedEventMetadata.html
---

# PullRequestMergedStateChangedEventMetadata
<a name="API_PullRequestMergedStateChangedEventMetadata"></a>

Returns information about the change in the merge state for a pull request event.

## Contents
<a name="API_PullRequestMergedStateChangedEventMetadata_Contents"></a>

 ** destinationReference **   <a name="CodeCommit-Type-PullRequestMergedStateChangedEventMetadata-destinationReference"></a>
The name of the branch that the pull request is merged into.
Type: String
Required: No

 ** mergeMetadata **   <a name="CodeCommit-Type-PullRequestMergedStateChangedEventMetadata-mergeMetadata"></a>
Information about the merge state change event.
Type: [MergeMetadata](API_MergeMetadata.md) object
Required: No

 ** repositoryName **   <a name="CodeCommit-Type-PullRequestMergedStateChangedEventMetadata-repositoryName"></a>
The name of the repository where the pull request was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: No

## See Also
<a name="API_PullRequestMergedStateChangedEventMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/PullRequestMergedStateChangedEventMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/PullRequestMergedStateChangedEventMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/PullRequestMergedStateChangedEventMetadata)
