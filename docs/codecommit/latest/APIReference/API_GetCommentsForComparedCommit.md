---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetCommentsForComparedCommit.html
---

# GetCommentsForComparedCommit
<a name="API_GetCommentsForComparedCommit"></a>

Returns information about comments made on the comparison between two commits.

**Note**
Reaction counts might include numbers from user identities who were deleted after the reaction was made. For a count of reactions from active identities, use GetCommentReactions.

## Request Syntax
<a name="API_GetCommentsForComparedCommit_RequestSyntax"></a>

```
{
   "afterCommitId": "{{string}}",
   "beforeCommitId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCommentsForComparedCommit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [afterCommitId](#API_GetCommentsForComparedCommit_RequestSyntax) **   <a name="CodeCommit-GetCommentsForComparedCommit-request-afterCommitId"></a>
To establish the directionality of the comparison, the full commit ID of the after commit.
Type: String
Required: Yes

 ** [beforeCommitId](#API_GetCommentsForComparedCommit_RequestSyntax) **   <a name="CodeCommit-GetCommentsForComparedCommit-request-beforeCommitId"></a>
To establish the directionality of the comparison, the full commit ID of the before commit.
Type: String
Required: No

 ** [maxResults](#API_GetCommentsForComparedCommit_RequestSyntax) **   <a name="CodeCommit-GetCommentsForComparedCommit-request-maxResults"></a>
A non-zero, non-negative integer used to limit the number of returned results. The default is 100 comments, but you can configure up to 500.
Type: Integer
Required: No

 ** [nextToken](#API_GetCommentsForComparedCommit_RequestSyntax) **   <a name="CodeCommit-GetCommentsForComparedCommit-request-nextToken"></a>
An enumeration token that when provided in a request, returns the next batch of the results.
Type: String
Required: No

 ** [repositoryName](#API_GetCommentsForComparedCommit_RequestSyntax) **   <a name="CodeCommit-GetCommentsForComparedCommit-request-repositoryName"></a>
The name of the repository where you want to compare commits.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_GetCommentsForComparedCommit_ResponseSyntax"></a>

```
{
   "commentsForComparedCommitData": [
      {
         "afterBlobId": "string",
         "afterCommitId": "string",
         "beforeBlobId": "string",
         "beforeCommitId": "string",
         "comments": [
            {
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
         ],
         "location": {
            "filePath": "string",
            "filePosition": number,
            "relativeFileVersion": "string"
         },
         "repositoryName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetCommentsForComparedCommit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commentsForComparedCommitData](#API_GetCommentsForComparedCommit_ResponseSyntax) **   <a name="CodeCommit-GetCommentsForComparedCommit-response-commentsForComparedCommitData"></a>
A list of comment objects on the compared commit.
Type: Array of [CommentsForComparedCommit](API_CommentsForComparedCommit.md) objects

 ** [nextToken](#API_GetCommentsForComparedCommit_ResponseSyntax) **   <a name="CodeCommit-GetCommentsForComparedCommit-response-nextToken"></a>
An enumeration token that can be used in a request to return the next batch of the results.
Type: String

## Errors
<a name="API_GetCommentsForComparedCommit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CommitDoesNotExistException **
The specified commit does not exist or no commit was specified, and the specified repository has no default branch.
HTTP Status Code: 400

 ** CommitIdRequiredException **
A commit ID was not specified.
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

 ** InvalidCommitIdException **
The specified commit ID is not valid.
HTTP Status Code: 400

 ** InvalidContinuationTokenException **
The specified continuation token is not valid.
HTTP Status Code: 400

 ** InvalidMaxResultsException **
The specified number of maximum results is not valid.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_GetCommentsForComparedCommit_Examples"></a>

### Example
<a name="API_GetCommentsForComparedCommit_Example_1"></a>

This example illustrates one usage of GetCommentsForComparedCommit.

#### Sample Request
<a name="API_GetCommentsForComparedCommit_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 176
X-Amz-Target: CodeCommit_20150413.GetCommentsForComparedCommit
X-Amz-Date: 20171025T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/8
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "afterCommitId": "317f8570EXAMPLE",
   "beforeCommitId": "6e147360EXAMPLE",
   "maxResults": 250,
   "nextToken": "exampleToken",
   "repositoryName": "MyDemoRepo"
}
```

#### Sample Response
<a name="API_GetCommentsForComparedCommit_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 2101
Date: Wed, 25 Oct 2017 20:18:13 GMT

{
   "commentsForComparedCommitData": [
      {
         "afterBlobId": "1f330709EXAMPLE",
         "afterCommitId": "317f8570EXAMPLE",
         "beforeBlobId": "80906a4cEXAMPLE",
         "beforeCommitId": "6e147360EXAMPLE",
         "comments": [
            {
               "authorArn": "arn:aws:iam::123456789012:user/Li_Juan",
               "clientRequestToken": "123Example",
               "commentId": "ff30b348EXAMPLEb9aa670f",
               "content": "Whoops - I meant to add this comment to the line, not the file, but I don't see how to delete it.",
               "creationDate": 1508369768.142,
               "deleted": false,
               "lastModifiedDate": 1508369842.278,
               "callerReactions": [],
               "reactionCounts":
                {
                  "THUMBSUP" : 1
                }
            },
            {
               "authorArn": "arn:aws:iam::123456789012:user/Li_Juan",
               "clientRequestToken": "123Example",
               "commentId": "553b509bEXAMPLE56198325",
               "content": "Can you add a test case for this?",
               "creationDate": 1508369612.240,
               "deleted": false,
               "commentId": "456def-EXAMPLE",
               "lastModifiedDate": 1508369612.240,
               "callerReactions": ["THUMBSUP"]
               "reactionCounts":
                {
                  "THUMBSUP" : 10,
                  "THUMBSDOWN" : 1,
                  "SMILE" : 2,
                  "HEART" : 2
                }
             }
         ],
         "location": {
            "filePath": "cl_sample.js",
            "filePosition": 1232,
            "relativeFileVersion": "after"
         },
         "repositoryName": "MyDemoRepo"
      }
   ],
   "nextToken": "exampleToken"
}
```

## See Also
<a name="API_GetCommentsForComparedCommit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/GetCommentsForComparedCommit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/GetCommentsForComparedCommit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/GetCommentsForComparedCommit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/GetCommentsForComparedCommit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/GetCommentsForComparedCommit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/GetCommentsForComparedCommit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/GetCommentsForComparedCommit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/GetCommentsForComparedCommit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/GetCommentsForComparedCommit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/GetCommentsForComparedCommit)
