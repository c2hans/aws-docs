---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PostCommentForComparedCommit.html
---

# PostCommentForComparedCommit
<a name="API_PostCommentForComparedCommit"></a>

Posts a comment on the comparison between two commits.

## Request Syntax
<a name="API_PostCommentForComparedCommit_RequestSyntax"></a>

```
{
   "afterCommitId": "{{string}}",
   "beforeCommitId": "{{string}}",
   "clientRequestToken": "{{string}}",
   "content": "{{string}}",
   "location": {
      "filePath": "{{string}}",
      "filePosition": {{number}},
      "relativeFileVersion": "{{string}}"
   },
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_PostCommentForComparedCommit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [afterCommitId](#API_PostCommentForComparedCommit_RequestSyntax) **   <a name="CodeCommit-PostCommentForComparedCommit-request-afterCommitId"></a>
To establish the directionality of the comparison, the full commit ID of the after commit.
Type: String
Required: Yes

 ** [beforeCommitId](#API_PostCommentForComparedCommit_RequestSyntax) **   <a name="CodeCommit-PostCommentForComparedCommit-request-beforeCommitId"></a>
To establish the directionality of the comparison, the full commit ID of the before commit. Required for commenting on any commit unless that commit is the initial commit.
Type: String
Required: No

 ** [clientRequestToken](#API_PostCommentForComparedCommit_RequestSyntax) **   <a name="CodeCommit-PostCommentForComparedCommit-request-clientRequestToken"></a>
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.
Type: String
Required: No

 ** [content](#API_PostCommentForComparedCommit_RequestSyntax) **   <a name="CodeCommit-PostCommentForComparedCommit-request-content"></a>
The content of the comment you want to make.
Type: String
Required: Yes

 ** [location](#API_PostCommentForComparedCommit_RequestSyntax) **   <a name="CodeCommit-PostCommentForComparedCommit-request-location"></a>
The location of the comparison where you want to comment.
Type: [Location](API_Location.md) object
Required: No

 ** [repositoryName](#API_PostCommentForComparedCommit_RequestSyntax) **   <a name="CodeCommit-PostCommentForComparedCommit-request-repositoryName"></a>
The name of the repository where you want to post a comment on the comparison between commits.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_PostCommentForComparedCommit_ResponseSyntax"></a>

```
{
   "afterBlobId": "string",
   "afterCommitId": "string",
   "beforeBlobId": "string",
   "beforeCommitId": "string",
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
   },
   "location": {
      "filePath": "string",
      "filePosition": number,
      "relativeFileVersion": "string"
   },
   "repositoryName": "string"
}
```

## Response Elements
<a name="API_PostCommentForComparedCommit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [afterBlobId](#API_PostCommentForComparedCommit_ResponseSyntax) **   <a name="CodeCommit-PostCommentForComparedCommit-response-afterBlobId"></a>
In the directionality you established, the blob ID of the after blob.
Type: String

 ** [afterCommitId](#API_PostCommentForComparedCommit_ResponseSyntax) **   <a name="CodeCommit-PostCommentForComparedCommit-response-afterCommitId"></a>
In the directionality you established, the full commit ID of the after commit.
Type: String

 ** [beforeBlobId](#API_PostCommentForComparedCommit_ResponseSyntax) **   <a name="CodeCommit-PostCommentForComparedCommit-response-beforeBlobId"></a>
In the directionality you established, the blob ID of the before blob.
Type: String

 ** [beforeCommitId](#API_PostCommentForComparedCommit_ResponseSyntax) **   <a name="CodeCommit-PostCommentForComparedCommit-response-beforeCommitId"></a>
In the directionality you established, the full commit ID of the before commit.
Type: String

 ** [comment](#API_PostCommentForComparedCommit_ResponseSyntax) **   <a name="CodeCommit-PostCommentForComparedCommit-response-comment"></a>
The content of the comment you posted.
Type: [Comment](API_Comment.md) object

 ** [location](#API_PostCommentForComparedCommit_ResponseSyntax) **   <a name="CodeCommit-PostCommentForComparedCommit-response-location"></a>
The location of the comment in the comparison between the two commits.
Type: [Location](API_Location.md) object

 ** [repositoryName](#API_PostCommentForComparedCommit_ResponseSyntax) **   <a name="CodeCommit-PostCommentForComparedCommit-response-repositoryName"></a>
The name of the repository where you posted a comment on the comparison between commits.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`

## Errors
<a name="API_PostCommentForComparedCommit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BeforeCommitIdAndAfterCommitIdAreSameException **
The before commit ID and the after commit ID are the same, which is not valid. The before commit ID and the after commit ID must be different commit IDs.
HTTP Status Code: 400

 ** ClientRequestTokenRequiredException **
A client request token is required. A client request token is an unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.
HTTP Status Code: 400

 ** CommentContentRequiredException **
The comment is empty. You must provide some content for a comment. The content cannot be null.
HTTP Status Code: 400

 ** CommentContentSizeLimitExceededException **
The comment is too large. Comments are limited to 10,240 characters.
HTTP Status Code: 400

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

 ** IdempotencyParameterMismatchException **
The client request token is not valid. Either the token is not in a valid format, or the token has been used in a previous request and cannot be reused.
HTTP Status Code: 400

 ** InvalidClientRequestTokenException **
The client request token is not valid.
HTTP Status Code: 400

 ** InvalidCommitIdException **
The specified commit ID is not valid.
HTTP Status Code: 400

 ** InvalidFileLocationException **
The location of the file is not valid. Make sure that you include the file name and extension.
HTTP Status Code: 400

 ** InvalidFilePositionException **
The position is not valid. Make sure that the line number exists in the version of the file you want to comment on.
HTTP Status Code: 400

 ** InvalidPathException **
The specified path is not valid.
HTTP Status Code: 400

 ** InvalidRelativeFileVersionEnumException **
Either the enum is not in a valid format, or the specified file version enum is not valid in respect to the current file version.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** PathDoesNotExistException **
The specified path does not exist.
HTTP Status Code: 400

 ** PathRequiredException **
The folderPath for a location cannot be null.
HTTP Status Code: 400

 ** PathRequiredException **
The folderPath for a location cannot be null.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_PostCommentForComparedCommit_Examples"></a>

### Example
<a name="API_PostCommentForComparedCommit_Example_1"></a>

This example illustrates one usage of PostCommentForComparedCommit.

#### Sample Request
<a name="API_PostCommentForComparedCommit_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.PostCommentForComparedCommit
X-Amz-Date: 20171025T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/8
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "afterCommitId": "317f8570EXAMPLE",
   "beforeCommitId": "6e147360EXAMPLE",
   "clientRequestToken": "123Example",
   "content": "Can you add a test case for this?",
   "location": {
            "filePath": "cl_sample.js",
            "filePosition": 1232,
            "relativeFileVersion": "AFTER"
         },
   "repositoryName": "MyDemoRepo"
}
```

#### Sample Response
<a name="API_PostCommentForComparedCommit_Example_1_Response"></a>

```
{
         "afterBlobId": "1f330709EXAMPLE",
         "afterCommitId": "317f8570EXAMPLE",
         "beforeBlobId": "80906a4cEXAMPLE",
         "beforeCommitId": "6e147360EXAMPLE",
         "comment": {
               "authorArn": "arn:aws:iam::123456789012:user/Li_Juan",
               "clientRequestToken": "",
               "commentId": "553b509bEXAMPLE56198325",
               "content": "Can you add a test case for this?",
               "creationDate": 1508369612.203,
               "deleted": false,
               "commentId": "abc123-EXAMPLE",
               "lastModifiedDate": 1508369612.203,
               "callerReactions": [],
               "reactionCounts": []
             },
             "location": {
               "filePath": "cl_sample.js",
               "filePosition": 1232,
               "relativeFileVersion": "AFTER"
             },
         "repositoryName": "MyDemoRepo"
 }
```

## See Also
<a name="API_PostCommentForComparedCommit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/PostCommentForComparedCommit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/PostCommentForComparedCommit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/PostCommentForComparedCommit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/PostCommentForComparedCommit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/PostCommentForComparedCommit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/PostCommentForComparedCommit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/PostCommentForComparedCommit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/PostCommentForComparedCommit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/PostCommentForComparedCommit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/PostCommentForComparedCommit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
