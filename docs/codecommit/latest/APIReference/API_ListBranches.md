---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListBranches.html
---

# ListBranches
<a name="API_ListBranches"></a>

Gets information about one or more branches in a repository.

## Request Syntax
<a name="API_ListBranches_RequestSyntax"></a>

```
{
   "nextToken": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListBranches_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [nextToken](#API_ListBranches_RequestSyntax) **   <a name="CodeCommit-ListBranches-request-nextToken"></a>
An enumeration token that allows the operation to batch the results.
Type: String
Required: No

 ** [repositoryName](#API_ListBranches_RequestSyntax) **   <a name="CodeCommit-ListBranches-request-repositoryName"></a>
The name of the repository that contains the branches.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_ListBranches_ResponseSyntax"></a>

```
{
   "branches": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBranches_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [branches](#API_ListBranches_ResponseSyntax) **   <a name="CodeCommit-ListBranches-response-branches"></a>
The list of branch names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [nextToken](#API_ListBranches_ResponseSyntax) **   <a name="CodeCommit-ListBranches-response-nextToken"></a>
An enumeration token that returns the batch of the results.
Type: String

## Errors
<a name="API_ListBranches_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** InvalidContinuationTokenException **
The specified continuation token is not valid.
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
<a name="API_ListBranches_Examples"></a>

### Example
<a name="API_ListBranches_Example_1"></a>

This example illustrates one usage of ListBranches.

#### Sample Request
<a name="API_ListBranches_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 33
X-Amz-Target: CodeCommit_20150413.ListBranches
X-Amz-Date: 20151028T231012Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo"
}
```

#### Sample Response
<a name="API_ListBranches_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 55
Date: Wed, 28 Oct 2015 23:10:15 GMT

{
  "branches":[
    "main",
	"MyNewBranch"
	]
}
```

## See Also
<a name="API_ListBranches_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/ListBranches)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/ListBranches)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ListBranches)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/ListBranches)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ListBranches)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/ListBranches)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/ListBranches)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/ListBranches)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/ListBranches)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ListBranches)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
