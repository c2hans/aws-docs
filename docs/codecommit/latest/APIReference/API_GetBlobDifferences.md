---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetBlobDifferences.html
---

# GetBlobDifferences
<a name="API_GetBlobDifferences"></a>

Returns a structured, line-level diff between two blob versions in a repository. The diff is returned as an ordered list of hunks, where each hunk represents a contiguous run of changed lines together with any surrounding unchanged context lines.

Results are paginated. Use `MaxResults` and `NextToken` to retrieve additional pages.

For the typical usage workflow, see [GetDifferences](API_GetDifferences.md).

## Request Syntax
<a name="API_GetBlobDifferences_RequestSyntax"></a>

```
{
   "afterBlobId": "{{string}}",
   "beforeBlobId": "{{string}}",
   "contextLines": {{number}},
   "ignoreWhitespace": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetBlobDifferences_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [afterBlobId](#API_GetBlobDifferences_RequestSyntax) **   <a name="CodeCommit-GetBlobDifferences-request-afterBlobId"></a>
The ID of the "after" (destination) blob in the diff. Typically the value of `afterBlob.blobId` from a `Difference` object returned by [GetDifferences](API_GetDifferences.md).
Type: String
Required: Yes

 ** [beforeBlobId](#API_GetBlobDifferences_RequestSyntax) **   <a name="CodeCommit-GetBlobDifferences-request-beforeBlobId"></a>
The ID of the "before" (source) blob in the diff. Typically the value of `beforeBlob.blobId` from a `Difference` object returned by [GetDifferences](API_GetDifferences.md).
If you do not specify a value, the operation returns a diff against an empty before-state. This is equivalent to treating the file as newly added.
Type: String
Required: No

 ** [contextLines](#API_GetBlobDifferences_RequestSyntax) **   <a name="CodeCommit-GetBlobDifferences-request-contextLines"></a>
The number of unchanged lines of context to include before and after each block of changes in a hunk. Valid values are 0 through 20. Defaults to `3`.
Type: Integer
Required: No

 ** [ignoreWhitespace](#API_GetBlobDifferences_RequestSyntax) **   <a name="CodeCommit-GetBlobDifferences-request-ignoreWhitespace"></a>
Specifies whether to ignore whitespace-only changes when computing the diff. When `true`, the operation treats lines that differ only in whitespace as unchanged. Defaults to `false`.
Type: Boolean
Required: No

 ** [MaxResults](#API_GetBlobDifferences_RequestSyntax) **   <a name="CodeCommit-GetBlobDifferences-request-MaxResults"></a>
The maximum number of `DiffHunk` entries to return in a single response page. Defaults to `100`.
Type: Integer
Required: No

 ** [NextToken](#API_GetBlobDifferences_RequestSyntax) **   <a name="CodeCommit-GetBlobDifferences-request-NextToken"></a>
An enumeration token that returns the next batch of results when present in a request.
Type: String
Required: No

 ** [repositoryName](#API_GetBlobDifferences_RequestSyntax) **   <a name="CodeCommit-GetBlobDifferences-request-repositoryName"></a>
The name of the repository that contains the blobs to compare.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_GetBlobDifferences_ResponseSyntax"></a>

```
{
   "afterBlobSize": number,
   "beforeBlobSize": number,
   "hunks": [
      {
         "afterLineCount": number,
         "afterStartLine": number,
         "beforeLineCount": number,
         "beforeStartLine": number,
         "changes": [
            {
               "afterLineNumber": number,
               "beforeLineNumber": number,
               "content": "string",
               "type": "string"
            }
         ]
      }
   ],
   "isBinary": boolean,
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetBlobDifferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [afterBlobSize](#API_GetBlobDifferences_ResponseSyntax) **   <a name="CodeCommit-GetBlobDifferences-response-afterBlobSize"></a>
The size, in bytes, of the blob identified by `afterBlobId`.
Type: Long

 ** [beforeBlobSize](#API_GetBlobDifferences_ResponseSyntax) **   <a name="CodeCommit-GetBlobDifferences-response-beforeBlobSize"></a>
The size, in bytes, of the blob identified by `beforeBlobId`. Returns `0` when you do not specify `beforeBlobId`.
Type: Long

 ** [hunks](#API_GetBlobDifferences_ResponseSyntax) **   <a name="CodeCommit-GetBlobDifferences-response-hunks"></a>
An ordered list of diff hunks. Each hunk represents a contiguous run of changed and adjacent context lines. The list is empty when the blobs are identical or when the content is binary. The list is also empty when a paginated request has already returned all hunks in earlier pages, in which case `NextToken` is also `null`.
Type: Array of [DiffHunk](API_DiffHunk.md) objects
Array Members: Maximum number of 1000 items.

 ** [isBinary](#API_GetBlobDifferences_ResponseSyntax) **   <a name="CodeCommit-GetBlobDifferences-response-isBinary"></a>
Specifies whether the operation treated the diff content as binary. When `true`, the operation does not compute a line-level diff and `hunks` is empty.
Type: Boolean

 ** [NextToken](#API_GetBlobDifferences_ResponseSyntax) **   <a name="CodeCommit-GetBlobDifferences-response-NextToken"></a>
An enumeration token that can be used in a request to return the next batch of `DiffHunk` entries. `null` when the response contains the final page of the diff.
Type: String

## Errors
<a name="API_GetBlobDifferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BlobIdDoesNotExistException **
The specified blob does not exist.
HTTP Status Code: 400

 ** BlobIdRequiredException **
A blob ID is required, but was not specified.
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

 ** FileTooLargeException **
The specified file exceeds the file size limit for AWS CodeCommit. For more information about limits in AWS CodeCommit, see [Quotas](https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html) in the * AWS CodeCommit User Guide*.
HTTP Status Code: 400

 ** InvalidBlobIdException **
The specified blob is not valid.
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

 ** ValidationException **
The specified input is either not valid, or it could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_GetBlobDifferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/GetBlobDifferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/GetBlobDifferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/GetBlobDifferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/GetBlobDifferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/GetBlobDifferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/GetBlobDifferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/GetBlobDifferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/GetBlobDifferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/GetBlobDifferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/GetBlobDifferences)
