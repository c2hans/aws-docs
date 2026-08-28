---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ListAssociatedApprovalRuleTemplatesForRepository.html
---

# ListAssociatedApprovalRuleTemplatesForRepository
<a name="API_ListAssociatedApprovalRuleTemplatesForRepository"></a>

Lists all approval rule templates that are associated with a specified repository.

## Request Syntax
<a name="API_ListAssociatedApprovalRuleTemplatesForRepository_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAssociatedApprovalRuleTemplatesForRepository_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListAssociatedApprovalRuleTemplatesForRepository_RequestSyntax) **   <a name="CodeCommit-ListAssociatedApprovalRuleTemplatesForRepository-request-maxResults"></a>
A non-zero, non-negative integer used to limit the number of returned results.
Type: Integer
Required: No

 ** [nextToken](#API_ListAssociatedApprovalRuleTemplatesForRepository_RequestSyntax) **   <a name="CodeCommit-ListAssociatedApprovalRuleTemplatesForRepository-request-nextToken"></a>
An enumeration token that, when provided in a request, returns the next batch of the results.
Type: String
Required: No

 ** [repositoryName](#API_ListAssociatedApprovalRuleTemplatesForRepository_RequestSyntax) **   <a name="CodeCommit-ListAssociatedApprovalRuleTemplatesForRepository-request-repositoryName"></a>
The name of the repository for which you want to list all associated approval rule templates.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_ListAssociatedApprovalRuleTemplatesForRepository_ResponseSyntax"></a>

```
{
   "approvalRuleTemplateNames": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAssociatedApprovalRuleTemplatesForRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvalRuleTemplateNames](#API_ListAssociatedApprovalRuleTemplatesForRepository_ResponseSyntax) **   <a name="CodeCommit-ListAssociatedApprovalRuleTemplatesForRepository-response-approvalRuleTemplateNames"></a>
The names of all approval rule templates associated with the repository.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [nextToken](#API_ListAssociatedApprovalRuleTemplatesForRepository_ResponseSyntax) **   <a name="CodeCommit-ListAssociatedApprovalRuleTemplatesForRepository-response-nextToken"></a>
An enumeration token that allows the operation to batch the next results of the operation.
Type: String

## Errors
<a name="API_ListAssociatedApprovalRuleTemplatesForRepository_Errors"></a>

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

## Examples
<a name="API_ListAssociatedApprovalRuleTemplatesForRepository_Examples"></a>

### Example
<a name="API_ListAssociatedApprovalRuleTemplatesForRepository_Example_1"></a>

This example illustrates one usage of ListAssociatedApprovalRuleTemplatesForRepository.

#### Sample Request
<a name="API_ListAssociatedApprovalRuleTemplatesForRepository_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 33
X-Amz-Target: CodeCommit_20150413.ListAssociatedApprovalRuleTemplatesForRepository
X-Amz-Date: 20191021T231012Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo"
}
```

#### Sample Response
<a name="API_ListAssociatedApprovalRuleTemplatesForRepository_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 55
Date: Mon, 21 Oct 2019 23:10:15 GMT

{
    "approvalRuleTemplateNames": [
        "2-approver-rule-for-main",
        "1-approver-rule-for-all-pull-requests"
    ]
}
```

## See Also
<a name="API_ListAssociatedApprovalRuleTemplatesForRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/ListAssociatedApprovalRuleTemplatesForRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/ListAssociatedApprovalRuleTemplatesForRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ListAssociatedApprovalRuleTemplatesForRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/ListAssociatedApprovalRuleTemplatesForRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ListAssociatedApprovalRuleTemplatesForRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/ListAssociatedApprovalRuleTemplatesForRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/ListAssociatedApprovalRuleTemplatesForRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/ListAssociatedApprovalRuleTemplatesForRepository)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/ListAssociatedApprovalRuleTemplatesForRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ListAssociatedApprovalRuleTemplatesForRepository)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
