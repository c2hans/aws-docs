---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetComment.html
---

# GetComment
<a name="API_GetComment"></a>

Returns the content of a comment made on a change, file, or commit in a repository.

**Note**
Reaction counts might include numbers from user identities who were deleted after the reaction was made. For a count of reactions from active identities, use GetCommentReactions.

## Request Syntax
<a name="API_GetComment_RequestSyntax"></a>

```
{
   "commentId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetComment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [commentId](#API_GetComment_RequestSyntax) **   <a name="CodeCommit-GetComment-request-commentId"></a>
The unique, system-generated ID of the comment. To get this ID, use [GetCommentsForComparedCommit](API_GetCommentsForComparedCommit.md) or [GetCommentsForPullRequest](API_GetCommentsForPullRequest.md).
Type: String
Required: Yes

## Response Syntax
<a name="API_GetComment_ResponseSyntax"></a>

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
<a name="API_GetComment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [comment](#API_GetComment_ResponseSyntax) **   <a name="CodeCommit-GetComment-response-comment"></a>
The contents of the comment.
Type: [Comment](API_Comment.md) object

## Errors
<a name="API_GetComment_Errors"></a>

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

 ** EncryptionIntegrityChecksFailedException **
An encryption integrity check failed.
HTTP Status Code: 500

 ** EncryptionKeyAccessDeniedException **
An encryption key could not be accessed.
HTTP Status Code: 400

 ** EncryptionKeyDisabledException **
The encryption key is disabled.
HTTP Status Code: 400

 ** EncryptionKeyNotFoundException **
No encryption key was found.
HTTP Status Code: 400

 ** EncryptionKeyUnavailableException **
The encryption key is not available.
HTTP Status Code: 400

 ** InvalidCommentIdException **
The comment ID is not in a valid format. Make sure that you have provided the full comment ID.
HTTP Status Code: 400

## Examples
<a name="API_GetComment_Examples"></a>

### Example
<a name="API_GetComment_Example_1"></a>

This example illustrates one usage of GetComment.

#### Sample Request
<a name="API_GetComment_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.GetComment
X-Amz-Date: 20171025T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/8
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "commentId": "ff30b348EXAMPLEb9aa670f"
}
```

#### Sample Response
<a name="API_GetComment_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 847
Date: Wed, 25 Oct 2017 20:18:13 GMT

{
   "comment": {
      "authorArn": "arn:aws:iam::123456789012:user/Li_Juan",
      "clientRequestToken": "123Example",
      "commentId": "ff30b348EXAMPLEb9aa670f",
      "content": "Whoops - I meant to add this comment to the line, but I don't see how to delete it.",
      "creationDate": 1508369768.142,
      "deleted": false,
      "commentId": "",
      "lastModifiedDate": 1508369842.278,
      "reactionCounts":{
         "THUMBSUP": 20,
         "THUMBSDOWN": 2,
         "SMILE": 5,
         "ANGRY": 7
        }
   }
}
```

## See Also
<a name="API_GetComment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/GetComment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/GetComment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/GetComment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/GetComment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/GetComment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/GetComment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/GetComment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/GetComment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/GetComment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/GetComment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
