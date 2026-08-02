---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListFileCommitHistory.html
---

# ListFileCommitHistory
<a name="API_ListFileCommitHistory"></a>

Retrieves a list of commits and changes to a specified file.

## Request Syntax
<a name="API_ListFileCommitHistory_RequestSyntax"></a>

```
{
   "commitSpecifier": "{{string}}",
   "filePath": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListFileCommitHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [commitSpecifier](#API_ListFileCommitHistory_RequestSyntax) **   <a name="CodeCommit-ListFileCommitHistory-request-commitSpecifier"></a>
The fully quaified reference that identifies the commit that contains the file. For example, you can specify a full commit ID, a tag, a branch name, or a reference such as `refs/heads/main`. If none is provided, the head commit is used.
Type: String
Required: No

 ** [filePath](#API_ListFileCommitHistory_RequestSyntax) **   <a name="CodeCommit-ListFileCommitHistory-request-filePath"></a>
The full path of the file whose history you want to retrieve, including the name of the file.
Type: String
Required: Yes

 ** [maxResults](#API_ListFileCommitHistory_RequestSyntax) **   <a name="CodeCommit-ListFileCommitHistory-request-maxResults"></a>
A non-zero, non-negative integer used to limit the number of returned results.
Type: Integer
Required: No

 ** [nextToken](#API_ListFileCommitHistory_RequestSyntax) **   <a name="CodeCommit-ListFileCommitHistory-request-nextToken"></a>
An enumeration token that allows the operation to batch the results.
Type: String
Required: No

 ** [repositoryName](#API_ListFileCommitHistory_RequestSyntax) **   <a name="CodeCommit-ListFileCommitHistory-request-repositoryName"></a>
The name of the repository that contains the file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_ListFileCommitHistory_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "revisionDag": [
      {
         "blobId": "string",
         "commit": {
            "additionalData": "string",
            "author": {
               "date": "string",
               "email": "string",
               "name": "string"
            },
            "commitId": "string",
            "committer": {
               "date": "string",
               "email": "string",
               "name": "string"
            },
            "message": "string",
            "parents": [ "string" ],
            "treeId": "string"
         },
         "path": "string",
         "revisionChildren": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_ListFileCommitHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListFileCommitHistory_ResponseSyntax) **   <a name="CodeCommit-ListFileCommitHistory-response-nextToken"></a>
An enumeration token that can be used to return the next batch of results.
Type: String

 ** [revisionDag](#API_ListFileCommitHistory_ResponseSyntax) **   <a name="CodeCommit-ListFileCommitHistory-response-revisionDag"></a>
An array of FileVersion objects that form a directed acyclic graph (DAG) of the changes to the file made by the commits that changed the file.
Type: Array of [FileVersion](API_FileVersion.md) objects

## Errors
<a name="API_ListFileCommitHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CommitDoesNotExistException **
The specified commit does not exist or no commit was specified, and the specified repository has no default branch.
HTTP Status Code: 400

 ** CommitRequiredException **
A commit was not specified.
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

 ** InvalidCommitException **
The specified commit is not valid.
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

 ** TipsDivergenceExceededException **
The divergence between the tips of the provided commit specifiers is too great to determine whether there might be any merge conflicts. Locally compare the specifiers using `git diff` or a diff tool.
HTTP Status Code: 400

## Examples
<a name="API_ListFileCommitHistory_Examples"></a>

### Example
<a name="API_ListFileCommitHistory_Example_1"></a>

This example illustrates one usage of ListFileCommitHistory.

#### Sample Request
<a name="API_ListFileCommitHistory_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 54
X-Amz-Target: CodeCommit_20150413.ListFileCommitHistory
X-Amz-Date: 20230816T224020Z
User-Agent: aws-cli/1.29.30 Python/3.6.10 Linux/4.9.184-0.1.ac.235.83.329.metal1.x86_64 botocore/1.15.36
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo",
  "filePath": "README.md"
}
```

#### Sample Response
<a name="API_ListFileCommitHistory_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 300
Date: Wed, 16 Aug 2023 22:40:20 GMT

{
  "revisionDag": [
    { "commit": {…, "commitId": "4f178133EXAMPLE", …}, "blobId": "2eb4af3bEXAMPLE", "filePath": "README.md", "revisionChildren": [] },
    { "commit": {…, "commitId": "317f8570EXAMPLE", …}, "blobId": "bf7fcf28fEXAMPLE", "filePath": "README.md", "revisionChildren": ["4f178133EXAMPLE"] },
  ],
  "nextToken": "exampleToken",
}
```

## See Also
<a name="API_ListFileCommitHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/ListFileCommitHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/ListFileCommitHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ListFileCommitHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/ListFileCommitHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ListFileCommitHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/ListFileCommitHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/ListFileCommitHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/ListFileCommitHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/ListFileCommitHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ListFileCommitHistory)
