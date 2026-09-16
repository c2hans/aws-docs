---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PutCommentReaction.html
---

# PutCommentReaction
<a name="API_PutCommentReaction"></a>

Adds or updates a reaction to a specified comment for the user whose identity is used to make the request. You can only add or update a reaction for yourself. You cannot add, modify, or delete a reaction for another user.

## Request Syntax
<a name="API_PutCommentReaction_RequestSyntax"></a>

```
{
   "commentId": "{{string}}",
   "reactionValue": "{{string}}"
}
```

## Request Parameters
<a name="API_PutCommentReaction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [commentId](#API_PutCommentReaction_RequestSyntax) **   <a name="CodeCommit-PutCommentReaction-request-commentId"></a>
The ID of the comment to which you want to add or update a reaction.
Type: String
Required: Yes

 ** [reactionValue](#API_PutCommentReaction_RequestSyntax) **   <a name="CodeCommit-PutCommentReaction-request-reactionValue"></a>
The emoji reaction you want to add or update. To remove a reaction, provide a value of blank or null. You can also provide the value of none. For information about emoji reaction values supported in AWS CodeCommit, see the [AWS CodeCommit User Guide](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-commit-comment.html#emoji-reaction-table).
Type: String
Required: Yes

## Response Elements
<a name="API_PutCommentReaction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutCommentReaction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CommentDeletedException **
This comment has already been deleted. You cannot edit or delete a deleted comment.
HTTP Status Code: 400

 ** CommentDoesNotExistException **
No comment exists with the provided ID. Verify that you have used the correct ID, and then try again.
HTTP Status Code: 400

 ** CommentIdRequiredException **
The comment ID is missing or null. A comment ID is required.
HTTP Status Code: 400

 ** InvalidCommentIdException **
The comment ID is not in a valid format. Make sure that you have provided the full comment ID.
HTTP Status Code: 400

 ** InvalidReactionValueException **
The value of the reaction is not valid. For more information, see the [AWS CodeCommit User Guide](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html).
HTTP Status Code: 400

 ** ReactionLimitExceededException **
The number of reactions has been exceeded. Reactions are limited to one reaction per user for each individual comment ID.
HTTP Status Code: 400

 ** ReactionValueRequiredException **
A reaction value is required.
HTTP Status Code: 400

## Examples
<a name="API_PutCommentReaction_Examples"></a>

### Example
<a name="API_PutCommentReaction_Example_1"></a>

This example illustrates one usage of PutCommentReaction.

#### Sample Request
<a name="API_PutCommentReaction_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.PutCommentReaction
X-Amz-Date: 20200406T224019Z
User-Agent: aws-cli/1.18.36 Python/3.6.10 Linux/4.9.184-0.1.ac.235.83.329.metal1.x86_64 botocore/1.15.36
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "commentId": "ff30b348EXAMPLE1EXAMPLE",
   "reaction:: ":thumbsup:"
}
```

#### Sample Response
<a name="API_PutCommentReaction_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Mon, 06 Apr 2020 22:40:19 GMT
```

## See Also
<a name="API_PutCommentReaction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/PutCommentReaction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/PutCommentReaction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/PutCommentReaction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/PutCommentReaction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/PutCommentReaction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/PutCommentReaction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/PutCommentReaction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/PutCommentReaction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/PutCommentReaction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/PutCommentReaction)
