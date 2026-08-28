---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_Comment.html
---

# Comment
<a name="API_Comment"></a>

Returns information about a specific comment.

## Contents
<a name="API_Comment_Contents"></a>

 ** authorArn **   <a name="CodeCommit-Type-Comment-authorArn"></a>
The Amazon Resource Name (ARN) of the person who posted the comment.
Type: String
Required: No

 ** callerReactions **   <a name="CodeCommit-Type-Comment-callerReactions"></a>
The emoji reactions to a comment, if any, submitted by the user whose credentials are associated with the call to the API.
Type: Array of strings
Required: No

 ** clientRequestToken **   <a name="CodeCommit-Type-Comment-clientRequestToken"></a>
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.
Type: String
Required: No

 ** commentId **   <a name="CodeCommit-Type-Comment-commentId"></a>
The system-generated comment ID.
Type: String
Required: No

 ** content **   <a name="CodeCommit-Type-Comment-content"></a>
The content of the comment.
Type: String
Required: No

 ** creationDate **   <a name="CodeCommit-Type-Comment-creationDate"></a>
The date and time the comment was created, in timestamp format.
Type: Timestamp
Required: No

 ** deleted **   <a name="CodeCommit-Type-Comment-deleted"></a>
A Boolean value indicating whether the comment has been deleted.
Type: Boolean
Required: No

 ** inReplyTo **   <a name="CodeCommit-Type-Comment-inReplyTo"></a>
The ID of the comment for which this comment is a reply, if any.
Type: String
Required: No

 ** lastModifiedDate **   <a name="CodeCommit-Type-Comment-lastModifiedDate"></a>
The date and time the comment was most recently modified, in timestamp format.
Type: Timestamp
Required: No

 ** reactionCounts **   <a name="CodeCommit-Type-Comment-reactionCounts"></a>
A string to integer map that represents the number of individual users who have responded to a comment with the specified reactions.
Type: String to integer map
Required: No

## See Also
<a name="API_Comment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/Comment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/Comment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/Comment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
