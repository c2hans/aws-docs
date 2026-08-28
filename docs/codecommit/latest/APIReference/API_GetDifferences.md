---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetDifferences.html
---

# GetDifferences
<a name="API_GetDifferences"></a>

Returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID, or other fully qualified reference). Results can be limited to a specified path.

For line-level diff details, pass the `beforeBlob.blobId` and `afterBlob.blobId` values from a `Difference` object to [GetBlobDifferences](API_GetBlobDifferences.md).

## Request Syntax
<a name="API_GetDifferences_RequestSyntax"></a>

```
{
   "afterCommitSpecifier": "{{string}}",
   "afterPath": "{{string}}",
   "beforeCommitSpecifier": "{{string}}",
   "beforePath": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDifferences_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [afterCommitSpecifier](#API_GetDifferences_RequestSyntax) **   <a name="CodeCommit-GetDifferences-request-afterCommitSpecifier"></a>
The branch, tag, HEAD, or other fully qualified reference used to identify a commit.
Type: String
Required: Yes

 ** [afterPath](#API_GetDifferences_RequestSyntax) **   <a name="CodeCommit-GetDifferences-request-afterPath"></a>
The file path in which to check differences. Limits the results to this path. Can also be used to specify the changed name of a directory or folder, if it has changed. If not specified, differences are shown for all paths.
Type: String
Required: No

 ** [beforeCommitSpecifier](#API_GetDifferences_RequestSyntax) **   <a name="CodeCommit-GetDifferences-request-beforeCommitSpecifier"></a>
The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, the full commit ID). Optional. If not specified, all changes before the `afterCommitSpecifier` value are shown. If you do not use `beforeCommitSpecifier` in your request, consider limiting the results with `maxResults`.
Type: String
Required: No

 ** [beforePath](#API_GetDifferences_RequestSyntax) **   <a name="CodeCommit-GetDifferences-request-beforePath"></a>
The file path in which to check for differences. Limits the results to this path. Can also be used to specify the previous name of a directory or folder. If `beforePath` and `afterPath` are not specified, differences are shown for all paths.
Type: String
Required: No

 ** [MaxResults](#API_GetDifferences_RequestSyntax) **   <a name="CodeCommit-GetDifferences-request-MaxResults"></a>
A non-zero, non-negative integer used to limit the number of returned results.
Type: Integer
Required: No

 ** [NextToken](#API_GetDifferences_RequestSyntax) **   <a name="CodeCommit-GetDifferences-request-NextToken"></a>
An enumeration token that, when provided in a request, returns the next batch of the results.
Type: String
Required: No

 ** [repositoryName](#API_GetDifferences_RequestSyntax) **   <a name="CodeCommit-GetDifferences-request-repositoryName"></a>
The name of the repository where you want to get differences.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_GetDifferences_ResponseSyntax"></a>

```
{
   "differences": [
      {
         "afterBlob": {
            "blobId": "string",
            "mode": "string",
            "path": "string"
         },
         "beforeBlob": {
            "blobId": "string",
            "mode": "string",
            "path": "string"
         },
         "changeType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetDifferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [differences](#API_GetDifferences_ResponseSyntax) **   <a name="CodeCommit-GetDifferences-response-differences"></a>
A data type object that contains information about the differences, including whether the difference is added, modified, or deleted (A, D, M).
Type: Array of [Difference](API_Difference.md) objects

 ** [NextToken](#API_GetDifferences_ResponseSyntax) **   <a name="CodeCommit-GetDifferences-response-NextToken"></a>
An enumeration token that can be used in a request to return the next batch of the results.
Type: String

## Errors
<a name="API_GetDifferences_Errors"></a>

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

 ** InvalidCommitIdException **
The specified commit ID is not valid.
HTTP Status Code: 400

 ** InvalidContinuationTokenException **
The specified continuation token is not valid.
HTTP Status Code: 400

 ** InvalidMaxResultsException **
The specified number of maximum results is not valid.
HTTP Status Code: 400

 ** InvalidPathException **
The specified path is not valid.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** PathDoesNotExistException **
The specified path does not exist.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_GetDifferences_Examples"></a>

### Example
<a name="API_GetDifferences_Example_1"></a>

This example illustrates one usage of GetDifferences.

#### Sample Request
<a name="API_GetDifferences_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 57
X-Amz-Target: CodeCommit_20150413.GetDifferences
X-Amz-Date: 20170111T224311Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo",
  "beforeCommitSpecifier": "16d097f03EXAMPLE",
  "afterCommitSpecifier": "fac04518EXAMPLE"
  "beforePath": "tmp/example-folder"
  "afterPath": "tmp/renamed-folder",

}
```

#### Sample Response
<a name="API_GetDifferences_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 770
Date: Wed, 11 Jan 2017 22:43:13 GMT

{
    "differences": [
        {
            "afterBlob": {
                "path": "blob.txt",
                "blobId": "2eb4af3bEXAMPLE",
                "mode": "100644"
            },
            "changeType": "M",
            "beforeBlob": {
                "path": "blob.txt",
                "blobId": "bf7fcf28fEXAMPLE",
                "mode": "100644"
            }
        }
    ]
}
```

## See Also
<a name="API_GetDifferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/GetDifferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/GetDifferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/GetDifferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/GetDifferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/GetDifferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/GetDifferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/GetDifferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/GetDifferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/GetDifferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/GetDifferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
