---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ListSourceRepositoryBranchesItem.html
---

# ListSourceRepositoryBranchesItem
<a name="API_ListSourceRepositoryBranchesItem"></a>

Information about a branch of a source repository returned in a list of branches.

## Contents
<a name="API_ListSourceRepositoryBranchesItem_Contents"></a>

 ** headCommitId **   <a name="codecatalyst-Type-ListSourceRepositoryBranchesItem-headCommitId"></a>
The commit ID of the tip of the branch at the time of the request, also known as the head commit.
Type: String
Required: No

 ** lastUpdatedTime **   <a name="codecatalyst-Type-ListSourceRepositoryBranchesItem-lastUpdatedTime"></a>
The time the branch was last updated, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp
Required: No

 ** name **   <a name="codecatalyst-Type-ListSourceRepositoryBranchesItem-name"></a>
The name of the branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** ref **   <a name="codecatalyst-Type-ListSourceRepositoryBranchesItem-ref"></a>
The Git reference name of the branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_ListSourceRepositoryBranchesItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/ListSourceRepositoryBranchesItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/ListSourceRepositoryBranchesItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/ListSourceRepositoryBranchesItem)
