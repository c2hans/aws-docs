---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdateComment.html
---

# UpdateComment
<a name="API_UpdateComment"></a>

Replaces the contents of a comment.

## Request Syntax
<a name="API_UpdateComment_RequestSyntax"></a>

```
{
   "commentId": "{{string}}",
   "content": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateComment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [commentId](#API_UpdateComment_RequestSyntax) **   <a name="CodeCommit-UpdateComment-request-commentId"></a>
The system-generated ID of the comment you want to update. To get this ID, use [GetCommentsForComparedCommit](API_GetCommentsForComparedCommit.md) or [GetCommentsForPullRequest](API_GetCommentsForPullRequest.md).
Type: String
Required: Yes

 ** [content](#API_UpdateComment_RequestSyntax) **   <a name="CodeCommit-UpdateComment-request-content"></a>
The updated content to replace the existing content of the comment.
Type: String
Required: Yes

## Response Syntax
<a name="API_UpdateComment_ResponseSyntax"></a>

```
{
   "comment": {
      "authorArn": "string",
      "callerReactions": [ "string" ],
      "clientRequestToken": "string",
      "commentId": "string",
      "content": "string",
      "creationDate": number,
      "deleted": boolean,
      "inReplyTo": "string",
      "lastModifiedDate": number,
      "reactionCounts": {
         "string" : number
      }
   }
}
```

## Response Elements
<a name="API_UpdateComment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [comment](#API_UpdateComment_ResponseSyntax) **   <a name="CodeCommit-UpdateComment-response-comment"></a>
Information about the updated comment.
Type: [Comment](API_Comment.md) object

## Errors
<a name="API_UpdateComment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CommentContentRequiredException **
The comment is empty. You must provide some content for a comment. The content cannot be null.
HTTP Status Code: 400

 ** CommentContentSizeLimitExceededException **
The comment is too large. Comments are limited to 10,240 characters.
HTTP Status Code: 400

 ** CommentDeletedException **
This comment has already been deleted. You cannot edit or delete a deleted comment.
HTTP Status Code: 400

 ** CommentDoesNotExistException **
No comment exists with the provided ID. Verify that you have used the correct ID, and then try again.
HTTP Status Code: 400

 ** CommentIdRequiredException **
The comment ID is missing or null. A comment ID is required.
HTTP Status Code: 400

 ** CommentNotCreatedByCallerException **
You cannot modify or delete this comment. Only comment authors can modify or delete their comments.
HTTP Status Code: 400

 ** InvalidCommentIdException **
The comment ID is not in a valid format. Make sure that you have provided the full comment ID.
HTTP Status Code: 400

## Examples
<a name="API_UpdateComment_Examples"></a>

### Example
<a name="API_UpdateComment_Example_1"></a>

This example illustrates one usage of UpdateComment.

#### Sample Request
<a name="API_UpdateComment_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.UpdateComment
X-Amz-Date: 20171025T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/8
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "commentId": "442b498bEXAMPLE5756813",
   "content": "Fixed as requested. I'll update the pull request."
}
```

#### Sample Response
<a name="API_UpdateComment_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 847
Date: Wed, 25 Oct 2017 20:20:13 GMT

{
    "comment": {
        "authorArn": "arn:aws:iam::123456789012:user/Li_Juan",
        "clientRequestToken": "",
        "commentId": "442b498bEXAMPLE5756813",
        "content": "Fixed as requested. I'll update the pull request.",
        "creationDate": 1508369929.783,
        "deleted": false,
        "lastModifiedDate": 1508369929.287,
        "callerReactions": [],
        "reactionCounts":
          {
            "THUMBSUP" : 2
          }
    }
 }
```

## See Also
<a name="API_UpdateComment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/UpdateComment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/UpdateComment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/UpdateComment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/UpdateComment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/UpdateComment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/UpdateComment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/UpdateComment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/UpdateComment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/UpdateComment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/UpdateComment)
