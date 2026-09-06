---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ReactionForComment.html
---

# ReactionForComment
<a name="API_ReactionForComment"></a>

Information about the reaction values provided by users on a comment.

## Contents
<a name="API_ReactionForComment_Contents"></a>

 ** reaction **   <a name="CodeCommit-Type-ReactionForComment-reaction"></a>
The reaction for a specified comment.
Type: [ReactionValueFormats](API_ReactionValueFormats.md) object
Required: No

 ** reactionsFromDeletedUsersCount **   <a name="CodeCommit-Type-ReactionForComment-reactionsFromDeletedUsersCount"></a>
A numerical count of users who reacted with the specified emoji whose identities have been subsequently deleted from IAM. While these IAM users or roles no longer exist, the reactions might still appear in total reaction counts.
Type: Integer
Required: No

 ** reactionUsers **   <a name="CodeCommit-Type-ReactionForComment-reactionUsers"></a>
The Amazon Resource Names (ARNs) of users who have provided reactions to the comment.
Type: Array of strings
Required: No

## See Also
<a name="API_ReactionForComment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ReactionForComment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ReactionForComment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ReactionForComment)
