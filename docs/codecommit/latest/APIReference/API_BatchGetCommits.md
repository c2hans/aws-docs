---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_BatchGetCommits.html
---

# BatchGetCommits
<a name="API_BatchGetCommits"></a>

Returns information about the contents of one or more commits in a repository.

## Request Syntax
<a name="API_BatchGetCommits_RequestSyntax"></a>

```
{
   "commitIds": [ "{{string}}" ],
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchGetCommits_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [commitIds](#API_BatchGetCommits_RequestSyntax) **   <a name="CodeCommit-BatchGetCommits-request-commitIds"></a>
The full commit IDs of the commits to get information about.
You must supply the full SHA IDs of each commit. You cannot use shortened SHA IDs.
Type: Array of strings
Required: Yes

 ** [repositoryName](#API_BatchGetCommits_RequestSyntax) **   <a name="CodeCommit-BatchGetCommits-request-repositoryName"></a>
The name of the repository that contains the commits.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_BatchGetCommits_ResponseSyntax"></a>

```
{
   "commits": [
      {
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
      }
   ],
   "errors": [
      {
         "commitId": "string",
         "errorCode": "string",
         "errorMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetCommits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commits](#API_BatchGetCommits_ResponseSyntax) **   <a name="CodeCommit-BatchGetCommits-response-commits"></a>
An array of commit data type objects, each of which contains information about a specified commit.
Type: Array of [Commit](API_Commit.md) objects

 ** [errors](#API_BatchGetCommits_ResponseSyntax) **   <a name="CodeCommit-BatchGetCommits-response-errors"></a>
Returns any commit IDs for which information could not be found. For example, if one of the commit IDs was a shortened SHA ID or that commit was not found in the specified repository, the ID returns an error object with more information.
Type: Array of [BatchGetCommitsError](API_BatchGetCommitsError.md) objects

## Errors
<a name="API_BatchGetCommits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CommitIdsLimitExceededException **
The maximum number of allowed commit IDs in a batch request is 100. Verify that your batch requests contains no more than 100 commit IDs, and then try again.
HTTP Status Code: 400

 ** CommitIdsListRequiredException **
A list of commit IDs is required, but was either not specified or the list was empty.
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
<a name="API_BatchGetCommits_Examples"></a>

### Example
<a name="API_BatchGetCommits_Example_1"></a>

This example illustrates one usage of BatchGetCommits.

#### Sample Request
<a name="API_BatchGetCommits_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 105
X-Amz-Target: CodeCommit_20150413.BatchGetCommits
X-Amz-Date: 20190724T201222Z
User-Agent: aws-cli/1.11.187 Python/3.4.9 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo",
  "commitIds": [
    317f8570EXAMPLE,
    4c925148EXAMPLE
  ]
}
```

#### Sample Response
<a name="API_BatchGetCommits_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 1218
Date: Wed, 24 Jul 2019 20:12:13 GMT

{
    "commits": [
      {
        "additionalData": "",
        "committer": {
            "date": "1508280564 -0800",
            "name": "Mary Major",
            "email": "mary_major@example.com"
        },
        "author": {
            "date": "1508280564 -0800",
            "name": "Mary Major",
            "email": "mary_major@example.com"
        },
        "commitId": "317f8570EXAMPLE",
        "treeId": "1f330709EXAMPLE",
        "parents": [
            "6e147360EXAMPLE"
        ],
        "message": "Change variable name and add new response element"
    },
    {
        "additionalData": "",
        "committer": {
            "date": "1508280542 -0800",
            "name": "Li Juan",
            "email": "li_juan@example.com"
        },
        "author": {
            "date": "1508280542 -0800",
            "name": "Li Juan",
            "email": "li_juan@example.com"
        },
        "commitId": "4c925148EXAMPLE",
        "treeId": "1f330709EXAMPLE",
        "parents": [
            "317f8570EXAMPLE"
        ],
        "message": "Added new class"
    }
}
```

## See Also
<a name="API_BatchGetCommits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/BatchGetCommits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/BatchGetCommits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/BatchGetCommits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/BatchGetCommits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/BatchGetCommits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/BatchGetCommits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/BatchGetCommits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/BatchGetCommits)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/BatchGetCommits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/BatchGetCommits)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
