---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_Conflict.html
---

# Conflict
<a name="API_Conflict"></a>

Information about conflicts in a merge operation.

## Contents
<a name="API_Conflict_Contents"></a>

 ** conflictMetadata **   <a name="CodeCommit-Type-Conflict-conflictMetadata"></a>
Metadata about a conflict in a merge operation.
Type: [ConflictMetadata](API_ConflictMetadata.md) object
Required: No

 ** mergeHunks **   <a name="CodeCommit-Type-Conflict-mergeHunks"></a>
A list of hunks that contain the differences between files or lines causing the conflict.
Type: Array of [MergeHunk](API_MergeHunk.md) objects
Required: No

## See Also
<a name="API_Conflict_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/Conflict)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/Conflict)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/Conflict)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
