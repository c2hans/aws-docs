---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetMergeCommit.html
---

# GetMergeCommit
<a name="API_GetMergeCommit"></a>

Returns information about a specified merge commit.

## Request Syntax
<a name="API_GetMergeCommit_RequestSyntax"></a>

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
<a name="API_GetMergeCommit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [conflictDetailLevel](#API_GetMergeCommit_RequestSyntax) **   <a name="CodeCommit-GetMergeCommit-request-conflictDetailLevel"></a>
The level of conflict detail to use. If unspecified, the default FILE\_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE\_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.
Type: String
Valid Values: `FILE_LEVEL | LINE_LEVEL`
Required: No

 ** [conflictResolutionStrategy](#API_GetMergeCommit_RequestSyntax) **   <a name="CodeCommit-GetMergeCommit-request-conflictResolutionStrategy"></a>
Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.
Type: String
Valid Values: `NONE | ACCEPT_SOURCE | ACCEPT_DESTINATION | AUTOMERGE`
Required: No

 ** [destinationCommitSpecifier](#API_GetMergeCommit_RequestSyntax) **   <a name="CodeCommit-GetMergeCommit-request-destinationCommitSpecifier"></a>
The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).
Type: String
Required: Yes

 ** [repositoryName](#API_GetMergeCommit_RequestSyntax) **   <a name="CodeCommit-GetMergeCommit-request-repositoryName"></a>
The name of the repository that contains the merge commit about which you want to get information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

 ** [sourceCommitSpecifier](#API_GetMergeCommit_RequestSyntax) **   <a name="CodeCommit-GetMergeCommit-request-sourceCommitSpecifier"></a>
The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).
Type: String
Required: Yes

## Response Syntax
<a name="API_GetMergeCommit_ResponseSyntax"></a>

```
{
   "baseCommitId": "string",
   "destinationCommitId": "string",
   "mergedCommitId": "string",
   "sourceCommitId": "string"
}
```

## Response Elements
<a name="API_GetMergeCommit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [baseCommitId](#API_GetMergeCommit_ResponseSyntax) **   <a name="CodeCommit-GetMergeCommit-response-baseCommitId"></a>
The commit ID of the merge base.
Type: String

 ** [destinationCommitId](#API_GetMergeCommit_ResponseSyntax) **   <a name="CodeCommit-GetMergeCommit-response-destinationCommitId"></a>
The commit ID of the destination commit specifier that was used in the merge evaluation.
Type: String

 ** [mergedCommitId](#API_GetMergeCommit_ResponseSyntax) **   <a name="CodeCommit-GetMergeCommit-response-mergedCommitId"></a>
The commit ID for the merge commit created when the source branch was merged into the destination branch. If the fast-forward merge strategy was used, there is no merge commit.
Type: String

 ** [sourceCommitId](#API_GetMergeCommit_ResponseSyntax) **   <a name="CodeCommit-GetMergeCommit-response-sourceCommitId"></a>
The commit ID of the source commit specifier that was used in the merge evaluation.
Type: String

## Errors
<a name="API_GetMergeCommit_Errors"></a>

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

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_GetMergeCommit_Examples"></a>

### Example
<a name="API_GetMergeCommit_Example_1"></a>

This example illustrates one usage of GetMergeCommit.

#### Sample Request
<a name="API_GetMergeCommit_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 165
X-Amz-Target: CodeCommit_20150413.GetMergeCommit
X-Amz-Date: 20190428T213222Z
User-Agent: aws-cli/1.16.137 Python/3.6.0 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo",
  "sourceCommitSpecifier": "bugfix-bug1234",
  "destinationCommitSpecifier": "main",
  "mergeOption": "THREE_WAY_MERGE"
}
```

#### Sample Response
<a name="API_GetMergeCommit_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 220
Date: Sun, 28 Apr 2019 22:43:13 GMT

{
    "sourceCommitId": "c5709475EXAMPLE",
    "destinationCommitId": "317f8570EXAMPLE",
    "baseCommitId": "fb12a539EXAMPLE",
    "mergeCommitId": "ffc4d608eEXAMPLE"
}
```

## See Also
<a name="API_GetMergeCommit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/GetMergeCommit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/GetMergeCommit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/GetMergeCommit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/GetMergeCommit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/GetMergeCommit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/GetMergeCommit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/GetMergeCommit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/GetMergeCommit)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/GetMergeCommit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/GetMergeCommit)
