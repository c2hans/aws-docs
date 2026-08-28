---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CommitDiffSourceCodeType.html
---

# CommitDiffSourceCodeType
<a name="API_CommitDiffSourceCodeType"></a>

A type of [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) that specifies the commit diff for a pull request on an associated repository. The `SourceCommit` and `DestinationCommit` fields are required to do a pull request code review.

## Contents
<a name="API_CommitDiffSourceCodeType_Contents"></a>

 ** DestinationCommit **   <a name="reviewer-Type-CommitDiffSourceCodeType-DestinationCommit"></a>
The SHA of the destination commit used to generate a commit diff. This field is required for a pull request code review.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `\S+`
Required: Yes

 ** SourceCommit **   <a name="reviewer-Type-CommitDiffSourceCodeType-SourceCommit"></a>
The SHA of the source commit used to generate a commit diff. This field is required for a pull request code review.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `\S+`
Required: Yes

 ** MergeBaseCommit **   <a name="reviewer-Type-CommitDiffSourceCodeType-MergeBaseCommit"></a>
The SHA of the merge base of a commit.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `\S+`
Required: No

## See Also
<a name="API_CommitDiffSourceCodeType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/CommitDiffSourceCodeType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/CommitDiffSourceCodeType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/CommitDiffSourceCodeType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
