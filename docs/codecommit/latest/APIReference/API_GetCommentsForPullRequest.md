---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetCommentsForPullRequest.html
---

# GetCommentsForPullRequest
<a name="API_GetCommentsForPullRequest"></a>

Returns comments made on a pull request.

**Note**
Reaction counts might include numbers from user identities who were deleted after the reaction was made. For a count of reactions from active identities, use GetCommentReactions.

## Request Syntax
<a name="API_GetCommentsForPullRequest_RequestSyntax"></a>

```
{
   "afterCommitId": "{{string}}",
   "beforeCommitId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "pullRequestId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCommentsForPullRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [afterCommitId](#API_GetCommentsForPullRequest_RequestSyntax) **   <a name="CodeCommit-GetCommentsForPullRequest-request-afterCommitId"></a>
The full commit ID of the commit in the source branch that was the tip of the branch at the time the comment was made. Requirement is conditional: `afterCommitId` must be specified when `repositoryName` is included.
Type: String
Required: No

 ** [beforeCommitId](#API_GetCommentsForPullRequest_RequestSyntax) **   <a name="CodeCommit-GetCommentsForPullRequest-request-beforeCommitId"></a>
The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was created. Requirement is conditional: `beforeCommitId` must be specified when `repositoryName` is included.
Type: String
Required: No

 ** [maxResults](#API_GetCommentsForPullRequest_RequestSyntax) **   <a name="CodeCommit-GetCommentsForPullRequest-request-maxResults"></a>
A non-zero, non-negative integer used to limit the number of returned results. The default is 100 comments. You can return up to 500 comments with a single request.
Type: Integer
Required: No

 ** [nextToken](#API_GetCommentsForPullRequest_RequestSyntax) **   <a name="CodeCommit-GetCommentsForPullRequest-request-nextToken"></a>
An enumeration token that, when provided in a request, returns the next batch of the results.
Type: String
Required: No

 ** [pullRequestId](#API_GetCommentsForPullRequest_RequestSyntax) **   <a name="CodeCommit-GetCommentsForPullRequest-request-pullRequestId"></a>
The system-generated ID of the pull request. To get this ID, use [ListPullRequests](API_ListPullRequests.md).
Type: String
Required: Yes

 ** [repositoryName](#API_GetCommentsForPullRequest_RequestSyntax) **   <a name="CodeCommit-GetCommentsForPullRequest-request-repositoryName"></a>
The name of the repository that contains the pull request. Requirement is conditional: `repositoryName` must be specified when `beforeCommitId` and `afterCommitId` are included.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: No

## Response Syntax
<a name="API_GetCommentsForPullRequest_ResponseSyntax"></a>

```
{
   "commentsForPullRequestData": [
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
         "pullRequestId": "string",
         "repositoryName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetCommentsForPullRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commentsForPullRequestData](#API_GetCommentsForPullRequest_ResponseSyntax) **   <a name="CodeCommit-GetCommentsForPullRequest-response-commentsForPullRequestData"></a>
An array of comment objects on the pull request.
Type: Array of [CommentsForPullRequest](API_CommentsForPullRequest.md) objects

 ** [nextToken](#API_GetCommentsForPullRequest_ResponseSyntax) **   <a name="CodeCommit-GetCommentsForPullRequest-response-nextToken"></a>
An enumeration token that can be used in a request to return the next batch of the results.
Type: String

## Errors
<a name="API_GetCommentsForPullRequest_Errors"></a>

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

 ** InvalidPullRequestIdException **
The pull request ID is not valid. Make sure that you have provided the full ID and that the pull request is in the specified repository, and then try again.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** PullRequestDoesNotExistException **
The pull request ID could not be found. Make sure that you have specified the correct repository name and pull request ID, and then try again.
HTTP Status Code: 400

 ** PullRequestIdRequiredException **
A pull request ID is required, but none was provided.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

 ** RepositoryNotAssociatedWithPullRequestException **
The repository does not contain any pull requests with that pull request ID. Use GetPullRequest to verify the correct repository name for the pull request ID.
HTTP Status Code: 400

## Examples
<a name="API_GetCommentsForPullRequest_Examples"></a>

### Example
<a name="API_GetCommentsForPullRequest_Example_1"></a>

This example illustrates one usage of GetCommentsForPullRequest.

#### Sample Request
<a name="API_GetCommentsForPullRequest_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 176
X-Amz-Target: CodeCommit_20150413.GetCommentsForPullRequest
X-Amz-Date: 20171025T134323Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/8
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "afterCommitId": "5d036259EXAMPLE",
   "beforeCommitId": "317f8570EXAMPLE",
   "maxResults": 250,
   "nextToken": "exampleToken",
   "pullRequestId": 42,
   "repositoryName": "MyDemoRepo"
}
```

#### Sample Response
<a name="API_GetCommentsForPullRequest_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 2101
Date: Wed, 25 Oct 2017 20:18:13 GMT

{
   "commentsForPullRequestData": [
      {
         "afterBlobId": "1f330709EXAMPLE",
         "afterCommitId": "5d036259EXAMPLE",
         "beforeBlobId": "80906a4cEXAMPLE",
         "beforeCommitId": "317f8570EXAMPLE",
         "comments": [
            {
               "authorArn": "arn:aws:iam::123456789012:user/Saanvi_Sarkar",
               "clientRequestToken": "",
               "commentId": "abcd1234EXAMPLEb5678efgh",
               "content": "These don't appear to be used anywhere. Can we remove them?",
               "creationDate": 1508369622.123,
               "deleted": false,
               "lastModifiedDate": 1508369622.123,
               "callerReactions": [],
               "reactionCounts":
                {
                  "THUMBSUP" : 6,
                  "CONFUSED" : 1
                }
            },
            {
               "authorArn": "arn:aws:iam::123456789012:user/Li_Juan",
               "clientRequestToken": "",
               "commentId": "442b498bEXAMPLE5756813",
               "content": "Good catch. I'll remove them.",
               "creationDate": 1508369829.104,
               "deleted": false,
               "commentId": "abcd1234EXAMPLEb5678efgh",
               "lastModifiedDate": 150836912.273,
               "callerReactions": ["THUMBSUP],
               "reactionCounts":
                {
                  "THUMBSUP" : 14
                }
             }
         ],
         "location": {
            "filePath": "ahs_count.py",
            "filePosition": 367,
            "relativeFileVersion": "AFTER"
         },
         "repositoryName": "MyDemoRepo",
         "pullRequestId": "42"
      }
   ],
   "nextToken": "exampleToken"
}
```

## See Also
<a name="API_GetCommentsForPullRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/GetCommentsForPullRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/GetCommentsForPullRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/GetCommentsForPullRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/GetCommentsForPullRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/GetCommentsForPullRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/GetCommentsForPullRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/GetCommentsForPullRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/GetCommentsForPullRequest)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/GetCommentsForPullRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/GetCommentsForPullRequest)
