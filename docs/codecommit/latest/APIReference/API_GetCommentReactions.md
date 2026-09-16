---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetCommentReactions.html
---

# GetCommentReactions
<a name="API_GetCommentReactions"></a>

Returns information about reactions to a specified comment ID. Reactions from users who have been deleted will not be included in the count.

## Request Syntax
<a name="API_GetCommentReactions_RequestSyntax"></a>

```
{
   "commentId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "reactionUserArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCommentReactions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [commentId](#API_GetCommentReactions_RequestSyntax) **   <a name="CodeCommit-GetCommentReactions-request-commentId"></a>
The ID of the comment for which you want to get reactions information.
Type: String
Required: Yes

 ** [maxResults](#API_GetCommentReactions_RequestSyntax) **   <a name="CodeCommit-GetCommentReactions-request-maxResults"></a>
A non-zero, non-negative integer used to limit the number of returned results. The default is the same as the allowed maximum, 1,000.
Type: Integer
Required: No

 ** [nextToken](#API_GetCommentReactions_RequestSyntax) **   <a name="CodeCommit-GetCommentReactions-request-nextToken"></a>
An enumeration token that, when provided in a request, returns the next batch of the results.
Type: String
Required: No

 ** [reactionUserArn](#API_GetCommentReactions_RequestSyntax) **   <a name="CodeCommit-GetCommentReactions-request-reactionUserArn"></a>
Optional. The Amazon Resource Name (ARN) of the user or identity for which you want to get reaction information.
Type: String
Required: No

## Response Syntax
<a name="API_GetCommentReactions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "reactionsForComment": [
      {
         "reaction": {
            "emoji": "string",
            "shortCode": "string",
            "unicode": "string"
         },
         "reactionsFromDeletedUsersCount": number,
         "reactionUsers": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_GetCommentReactions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetCommentReactions_ResponseSyntax) **   <a name="CodeCommit-GetCommentReactions-response-nextToken"></a>
An enumeration token that can be used in a request to return the next batch of the results.
Type: String

 ** [reactionsForComment](#API_GetCommentReactions_ResponseSyntax) **   <a name="CodeCommit-GetCommentReactions-response-reactionsForComment"></a>
An array of reactions to the specified comment.
Type: Array of [ReactionForComment](API_ReactionForComment.md) objects

## Errors
<a name="API_GetCommentReactions_Errors"></a>

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

 ** InvalidContinuationTokenException **
The specified continuation token is not valid.
HTTP Status Code: 400

 ** InvalidMaxResultsException **
The specified number of maximum results is not valid.
HTTP Status Code: 400

 ** InvalidReactionUserArnException **
The Amazon Resource Name (ARN) of the user or identity is not valid.
HTTP Status Code: 400

## Examples
<a name="API_GetCommentReactions_Examples"></a>

### Example
<a name="API_GetCommentReactions_Example_1"></a>

This example illustrates one usage of GetCommentReactions.

#### Sample Request
<a name="API_GetCommentReactions_Example_1_Request"></a>

```
POST / HTTP/1.1
    Host: codecommit.us-east-1.amazonaws.com
    Accept-Encoding: identity
    Content-Length: 124
    X-Amz-Target: CodeCommit_20150413.GetCommentReactions
    X-Amz-Date: 20200406T223055Z
    User-Agent: aws-cli/1.18.36 Python/3.6.10 Linux/4.9.184-0.1.ac.235.83.329.metal1.x86_64 botocore/1.15.36
    Content-Type: application/x-amz-json-1.1
    Authorization: AWS4-HMAC-SHA256 Credential=AKIAEXAMPLE/20180914/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature==8d9b5998EXAMPLE
{
   "commentId": "ff30b348EXAMPLE1EXAMPLE"
}
```

#### Sample Response
<a name="API_GetCommentReactions_Example_1_Response"></a>

```
HTTP/1.1 200 OK
    x-amzn-RequestId: d8ad1d21-EXAMPLE
    Content-Type: application/x-amz-json-1.1
    Content-Length: 2267
    Date: Mon, 6 Apr 2020 22:30:56 GMT
    Connection: keep-alive

{
    "reactionsForComment": {
        [
           {
                "reaction": {
                    "emoji:"👍",
                    "shortCode": "thumbsup",
                    "unicode": "U+1F44D"
                },
                "users": [
                    "arn:aws:iam::123456789012:user/Li_Juan",
                    "arn:aws:iam::123456789012:user/Mary_Major",
                    "arn:aws:iam::123456789012:user/Jorge_Souza"
                ]
            },
            {
                "reaction": {
                    "emoji": "👎",
                    "shortCode": "thumbsdown",
                    "unicode": "U+1F44E"
                },
                "users": [
                    "arn:aws:iam::123456789012:user/Nikhil_Jayashankar"
                ]
            },
            {
                "reaction": {
                    "emoji": "😕",
                    "shortCode": "confused",
                    "unicode": "U+1F615"
                },
                "users": [
                    "arn:aws:iam::123456789012:user/Saanvi_Sarkar"
                ]
            }
        ]
    }
}
```

## See Also
<a name="API_GetCommentReactions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/GetCommentReactions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/GetCommentReactions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/GetCommentReactions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/GetCommentReactions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/GetCommentReactions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/GetCommentReactions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/GetCommentReactions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/GetCommentReactions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/GetCommentReactions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/GetCommentReactions)
