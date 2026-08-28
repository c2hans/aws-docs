---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetMergeOptions.html
---

# GetMergeOptions
<a name="API_GetMergeOptions"></a>

Returns information about the merge options available for merging two specified branches. For details about why a merge option is not available, use GetMergeConflicts or DescribeMergeConflicts.

## Request Syntax
<a name="API_GetMergeOptions_RequestSyntax"></a>

```
{
   "conflictDetailLevel": "{{string}}",
   "conflictResolutionStrategy": "{{string}}",
   "destinationCommitSpecifier": "{{string}}",
   "repositoryName": "{{string}}",
   "sourceCommitSpecifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMergeOptions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [conflictDetailLevel](#API_GetMergeOptions_RequestSyntax) **   <a name="CodeCommit-GetMergeOptions-request-conflictDetailLevel"></a>
The level of conflict detail to use. If unspecified, the default FILE\_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE\_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.
Type: String
Valid Values: `FILE_LEVEL | LINE_LEVEL`
Required: No

 ** [conflictResolutionStrategy](#API_GetMergeOptions_RequestSyntax) **   <a name="CodeCommit-GetMergeOptions-request-conflictResolutionStrategy"></a>
Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.
Type: String
Valid Values: `NONE | ACCEPT_SOURCE | ACCEPT_DESTINATION | AUTOMERGE`
Required: No

 ** [destinationCommitSpecifier](#API_GetMergeOptions_RequestSyntax) **   <a name="CodeCommit-GetMergeOptions-request-destinationCommitSpecifier"></a>
The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).
Type: String
Required: Yes

 ** [repositoryName](#API_GetMergeOptions_RequestSyntax) **   <a name="CodeCommit-GetMergeOptions-request-repositoryName"></a>
The name of the repository that contains the commits about which you want to get merge options.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

 ** [sourceCommitSpecifier](#API_GetMergeOptions_RequestSyntax) **   <a name="CodeCommit-GetMergeOptions-request-sourceCommitSpecifier"></a>
The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).
Type: String
Required: Yes

## Response Syntax
<a name="API_GetMergeOptions_ResponseSyntax"></a>

```
{
   "baseCommitId": "string",
   "destinationCommitId": "string",
   "mergeOptions": [ "string" ],
   "sourceCommitId": "string"
}
```

## Response Elements
<a name="API_GetMergeOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [baseCommitId](#API_GetMergeOptions_ResponseSyntax) **   <a name="CodeCommit-GetMergeOptions-response-baseCommitId"></a>
The commit ID of the merge base.
Type: String

 ** [destinationCommitId](#API_GetMergeOptions_ResponseSyntax) **   <a name="CodeCommit-GetMergeOptions-response-destinationCommitId"></a>
The commit ID of the destination commit specifier that was used in the merge evaluation.
Type: String

 ** [mergeOptions](#API_GetMergeOptions_ResponseSyntax) **   <a name="CodeCommit-GetMergeOptions-response-mergeOptions"></a>
The merge option or strategy used to merge the code.
Type: Array of strings
Valid Values: `FAST_FORWARD_MERGE | SQUASH_MERGE | THREE_WAY_MERGE`

 ** [sourceCommitId](#API_GetMergeOptions_ResponseSyntax) **   <a name="CodeCommit-GetMergeOptions-response-sourceCommitId"></a>
The commit ID of the source commit specifier that was used in the merge evaluation.
Type: String

## Errors
<a name="API_GetMergeOptions_Errors"></a>

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

 ** InvalidConflictDetailLevelException **
The specified conflict detail level is not valid.
HTTP Status Code: 400

 ** InvalidConflictResolutionStrategyException **
The specified conflict resolution strategy is not valid.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** MaximumFileContentToLoadExceededException **
The number of files to load exceeds the allowed limit.
HTTP Status Code: 400

 ** MaximumItemsToCompareExceededException **
The number of items to compare between the source or destination branches and the merge base has exceeded the maximum allowed.
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
<a name="API_GetMergeOptions_Examples"></a>

### Example
<a name="API_GetMergeOptions_Example_1"></a>

This example illustrates one usage of GetMergeOptions.

#### Sample Request
<a name="API_GetMergeOptions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 57
X-Amz-Target: CodeCommit_20150413.GetMergeOptions
X-Amz-Date: 20190428T213222Z
User-Agent: aws-cli/1.16.137 Python/3.6.0 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo",
  "sourceCommitSpecifier": "bugfix-bug1234",
  "destinationCommitSpecifier": "main"
}
```

#### Sample Response
<a name="API_GetMergeOptions_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 167
Date: Sat, 11 Nov 2017 22:59:13 GMT

{
    "mergeOptions": [
        "FAST_FORWARD_MERGE",
        "SQUASH_MERGE",
        "THREE_WAY_MERGE"
    ],
    "sourceCommitId": "18059494EXAMPLE",
    "destinationCommitId": "ffd3311dEXAMPLE",
    "baseCommitId": "ffd3311dEXAMPLE"
}
```

## See Also
<a name="API_GetMergeOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/GetMergeOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/GetMergeOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/GetMergeOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/GetMergeOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/GetMergeOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/GetMergeOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/GetMergeOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/GetMergeOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/GetMergeOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/GetMergeOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
