---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DiffHunk.html
---

# DiffHunk
<a name="API_DiffHunk"></a>

A contiguous run of changed lines from a blob diff, together with any surrounding unchanged context lines. Hunks are returned in order from the start of the file to the end. Adjacent or overlapping hunks are merged into a single hunk in the response.

## Contents
<a name="API_DiffHunk_Contents"></a>

 ** afterLineCount **   <a name="CodeCommit-Type-DiffHunk-afterLineCount"></a>
The number of lines from the after blob covered by this hunk, including any context lines.
Type: Integer
Required: No

 ** afterStartLine **   <a name="CodeCommit-Type-DiffHunk-afterStartLine"></a>
The 1-based line number in the after blob where this hunk begins. When the hunk consists entirely of deletions, `afterLineCount` is `0`.
Type: Integer
Required: No

 ** beforeLineCount **   <a name="CodeCommit-Type-DiffHunk-beforeLineCount"></a>
The number of lines from the before blob covered by this hunk, including any context lines.
Type: Integer
Required: No

 ** beforeStartLine **   <a name="CodeCommit-Type-DiffHunk-beforeStartLine"></a>
The 1-based line number in the before blob where this hunk begins. When the hunk consists entirely of additions, `beforeLineCount` is `0`.
Type: Integer
Required: No

 ** changes **   <a name="CodeCommit-Type-DiffHunk-changes"></a>
An ordered list of line-level changes that make up this hunk. Each entry indicates whether the line is unchanged context, an addition, or a deletion.
Type: Array of [DiffChange](API_DiffChange.md) objects
Array Members: Maximum number of 25000 items.
Required: No

## See Also
<a name="API_DiffHunk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/DiffHunk)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/DiffHunk)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/DiffHunk)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
