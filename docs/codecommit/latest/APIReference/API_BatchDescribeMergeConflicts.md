---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_BatchDescribeMergeConflicts.html
---

# BatchDescribeMergeConflicts
<a name="API_BatchDescribeMergeConflicts"></a>

Returns information about one or more merge conflicts in the attempted merge of two commit specifiers using the squash or three-way merge strategy.

## Request Syntax
<a name="API_BatchDescribeMergeConflicts_RequestSyntax"></a>

```
{
   "conflictDetailLevel": "{{string}}",
   "conflictResolutionStrategy": "{{string}}",
   "destinationCommitSpecifier": "{{string}}",
   "filePaths": [ "{{string}}" ],
   "maxConflictFiles": {{number}},
   "maxMergeHunks": {{number}},
   "mergeOption": "{{string}}",
   "nextToken": "{{string}}",
   "repositoryName": "{{string}}",
   "sourceCommitSpecifier": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchDescribeMergeConflicts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [conflictDetailLevel](#API_BatchDescribeMergeConflicts_RequestSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-request-conflictDetailLevel"></a>
The level of conflict detail to use. If unspecified, the default FILE\_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE\_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.
Type: String
Valid Values: `FILE_LEVEL | LINE_LEVEL`
Required: No

 ** [conflictResolutionStrategy](#API_BatchDescribeMergeConflicts_RequestSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-request-conflictResolutionStrategy"></a>
Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.
Type: String
Valid Values: `NONE | ACCEPT_SOURCE | ACCEPT_DESTINATION | AUTOMERGE`
Required: No

 ** [destinationCommitSpecifier](#API_BatchDescribeMergeConflicts_RequestSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-request-destinationCommitSpecifier"></a>
The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).
Type: String
Required: Yes

 ** [filePaths](#API_BatchDescribeMergeConflicts_RequestSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-request-filePaths"></a>
The path of the target files used to describe the conflicts. If not specified, the default is all conflict files.
Type: Array of strings
Required: No

 ** [maxConflictFiles](#API_BatchDescribeMergeConflicts_RequestSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-request-maxConflictFiles"></a>
The maximum number of files to include in the output.
Type: Integer
Required: No

 ** [maxMergeHunks](#API_BatchDescribeMergeConflicts_RequestSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-request-maxMergeHunks"></a>
The maximum number of merge hunks to include in the output.
Type: Integer
Required: No

 ** [mergeOption](#API_BatchDescribeMergeConflicts_RequestSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-request-mergeOption"></a>
The merge option or strategy you want to use to merge the code.
Type: String
Valid Values: `FAST_FORWARD_MERGE | SQUASH_MERGE | THREE_WAY_MERGE`
Required: Yes

 ** [nextToken](#API_BatchDescribeMergeConflicts_RequestSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-request-nextToken"></a>
An enumeration token that, when provided in a request, returns the next batch of the results.
Type: String
Required: No

 ** [repositoryName](#API_BatchDescribeMergeConflicts_RequestSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-request-repositoryName"></a>
The name of the repository that contains the merge conflicts you want to review.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

 ** [sourceCommitSpecifier](#API_BatchDescribeMergeConflicts_RequestSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-request-sourceCommitSpecifier"></a>
The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).
Type: String
Required: Yes

## Response Syntax
<a name="API_BatchDescribeMergeConflicts_ResponseSyntax"></a>

```
{
   "baseCommitId": "string",
   "conflicts": [
      {
         "conflictMetadata": {
            "contentConflict": boolean,
            "fileModeConflict": boolean,
            "fileModes": {
               "base": "string",
               "destination": "string",
               "source": "string"
            },
            "filePath": "string",
            "fileSizes": {
               "base": number,
               "destination": number,
               "source": number
            },
            "isBinaryFile": {
               "base": boolean,
               "destination": boolean,
               "source": boolean
            },
            "mergeOperations": {
               "destination": "string",
               "source": "string"
            },
            "numberOfConflicts": number,
            "objectTypeConflict": boolean,
            "objectTypes": {
               "base": "string",
               "destination": "string",
               "source": "string"
            }
         },
         "mergeHunks": [
            {
               "base": {
                  "endLine": number,
                  "hunkContent": "string",
                  "startLine": number
               },
               "destination": {
                  "endLine": number,
                  "hunkContent": "string",
                  "startLine": number
               },
               "isConflict": boolean,
               "source": {
                  "endLine": number,
                  "hunkContent": "string",
                  "startLine": number
               }
            }
         ]
      }
   ],
   "destinationCommitId": "string",
   "errors": [
      {
         "exceptionName": "string",
         "filePath": "string",
         "message": "string"
      }
   ],
   "nextToken": "string",
   "sourceCommitId": "string"
}
```

## Response Elements
<a name="API_BatchDescribeMergeConflicts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [baseCommitId](#API_BatchDescribeMergeConflicts_ResponseSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-response-baseCommitId"></a>
The commit ID of the merge base.
Type: String

 ** [conflicts](#API_BatchDescribeMergeConflicts_ResponseSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-response-conflicts"></a>
A list of conflicts for each file, including the conflict metadata and the hunks of the differences between the files.
Type: Array of [Conflict](API_Conflict.md) objects

 ** [destinationCommitId](#API_BatchDescribeMergeConflicts_ResponseSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-response-destinationCommitId"></a>
The commit ID of the destination commit specifier that was used in the merge evaluation.
Type: String

 ** [errors](#API_BatchDescribeMergeConflicts_ResponseSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-response-errors"></a>
A list of any errors returned while describing the merge conflicts for each file.
Type: Array of [BatchDescribeMergeConflictsError](API_BatchDescribeMergeConflictsError.md) objects

 ** [nextToken](#API_BatchDescribeMergeConflicts_ResponseSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-response-nextToken"></a>
An enumeration token that can be used in a request to return the next batch of the results.
Type: String

 ** [sourceCommitId](#API_BatchDescribeMergeConflicts_ResponseSyntax) **   <a name="CodeCommit-BatchDescribeMergeConflicts-response-sourceCommitId"></a>
The commit ID of the source commit specifier that was used in the merge evaluation.
Type: String

## Errors
<a name="API_BatchDescribeMergeConflicts_Errors"></a>

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

 ** InvalidContinuationTokenException **
The specified continuation token is not valid.
HTTP Status Code: 400

 ** InvalidMaxConflictFilesException **
The specified value for the number of conflict files to return is not valid.
HTTP Status Code: 400

 ** InvalidMaxMergeHunksException **
The specified value for the number of merge hunks to return is not valid.
HTTP Status Code: 400

 ** InvalidMergeOptionException **
The specified merge option is not valid for this operation. Not all merge strategies are supported for all operations.
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

 ** MergeOptionRequiredException **
A merge option or stategy is required, and none was provided.
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
<a name="API_BatchDescribeMergeConflicts_Examples"></a>

### Example
<a name="API_BatchDescribeMergeConflicts_Example_1"></a>

This example illustrates one usage of BatchDescribeMergeConflicts.

#### Sample Request
<a name="API_BatchDescribeMergeConflicts_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 226
X-Amz-Target: CodeCommit_20150413.BatchDescribeMergeConflicts
X-Amz-Date: 20190428T213222Z
User-Agent: aws-cli/1.16.137 Python/3.6.0 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo",
  "destinationCommitSpecifier": "bugfix-bug1234",
  "sourceCommitSpecifier": "main",
  "mergeOption": "THREE_WAY_MERGE",
  "conflictDetailLevel" "LINE_LEVEL",
  "conflictResolutionStrategy": "NONE",
  "nextToken": "exampleToken",
}
```

#### Sample Response
<a name="API_BatchDescribeMergeConflicts_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 1681
Date: Sun, 28 Apr 2019 22:43:13 GMT

{
       "conflicts":[
        {
            "conflictMetadata": {
               "filePath": "file1.py",
               "fileSizes": {
                 "source": 123,
                 "destination": 125,
                 "base": 124
            },
            "fileModes": {
                "source": "EXECUTABLE",
                "destination": "EXECUTABLE",
                "base": "EXECUTABLE"
                },
            "numberOfConflicts", 4,
            "isBinaryFile": {
                "source": false,
                "destination": false,
                "base": false
            },
            "contentConflict": true,
            "fileModeConflict": false,
            "mergeOperations": {
                "source": "M",
                "destination": "M"
            }
        }
    "mergeHunks":[
        {
            "mergeHunk": {
                "isConflict": true
                "source": {
                    "startLine": 123,
                    "endLine": 123,
                    "hunkContent" "JzCQbIVyEXAMPLE="
                }
                "destination": {
                    "startLine": 125,
                    "endLine": 125,
                    "hunkContent" "BytPbuMiEXAMPLE="
                }
                "base": {
                    "startLine": 124,
                    "endLine": 124,
                    "hunkContent" "MnKCdITaEXAMPLE="
                }
            }
        }
    ]
    "errors":
    "sourceCommitId": "c5709475EXAMPLE",
    "destinationCommitId": "317f8570EXAMPLE",
    "baseCommitId": "fb12a539EXAMPLE",
    "nextToken": "exampleToken"
}
```

## See Also
<a name="API_BatchDescribeMergeConflicts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/BatchDescribeMergeConflicts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/BatchDescribeMergeConflicts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/BatchDescribeMergeConflicts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/BatchDescribeMergeConflicts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/BatchDescribeMergeConflicts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/BatchDescribeMergeConflicts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/BatchDescribeMergeConflicts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/BatchDescribeMergeConflicts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/BatchDescribeMergeConflicts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/BatchDescribeMergeConflicts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
