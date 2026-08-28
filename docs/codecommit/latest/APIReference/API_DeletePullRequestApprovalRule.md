---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DeletePullRequestApprovalRule.html
---

# DeletePullRequestApprovalRule
<a name="API_DeletePullRequestApprovalRule"></a>

Deletes an approval rule from a specified pull request. Approval rules can be deleted from a pull request only if the pull request is open, and if the approval rule was created specifically for a pull request and not generated from an approval rule template associated with the repository where the pull request was created. You cannot delete an approval rule from a merged or closed pull request.

## Request Syntax
<a name="API_DeletePullRequestApprovalRule_RequestSyntax"></a>

```
{
   "approvalRuleName": "{{string}}",
   "pullRequestId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeletePullRequestApprovalRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [approvalRuleName](#API_DeletePullRequestApprovalRule_RequestSyntax) **   <a name="CodeCommit-DeletePullRequestApprovalRule-request-approvalRuleName"></a>
The name of the approval rule you want to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [pullRequestId](#API_DeletePullRequestApprovalRule_RequestSyntax) **   <a name="CodeCommit-DeletePullRequestApprovalRule-request-pullRequestId"></a>
The system-generated ID of the pull request that contains the approval rule you want to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeletePullRequestApprovalRule_ResponseSyntax"></a>

```
{
   "approvalRuleId": "string"
}
```

## Response Elements
<a name="API_DeletePullRequestApprovalRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvalRuleId](#API_DeletePullRequestApprovalRule_ResponseSyntax) **   <a name="CodeCommit-DeletePullRequestApprovalRule-response-approvalRuleId"></a>
The ID of the deleted approval rule.
If the approval rule was deleted in an earlier API call, the response is 200 OK without content.
Type: String

## Errors
<a name="API_DeletePullRequestApprovalRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApprovalRuleNameRequiredException **
An approval rule name is required, but was not specified.
HTTP Status Code: 400

 ** CannotDeleteApprovalRuleFromTemplateException **
The approval rule cannot be deleted from the pull request because it was created by an approval rule template and applied to the pull request automatically.
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

 ** InvalidApprovalRuleNameException **
The name for the approval rule is not valid.
HTTP Status Code: 400

 ** InvalidPullRequestIdException **
The pull request ID is not valid. Make sure that you have provided the full ID and that the pull request is in the specified repository, and then try again.
HTTP Status Code: 400

 ** PullRequestAlreadyClosedException **
The pull request status cannot be updated because it is already closed.
HTTP Status Code: 400

 ** PullRequestDoesNotExistException **
The pull request ID could not be found. Make sure that you have specified the correct repository name and pull request ID, and then try again.
HTTP Status Code: 400

 ** PullRequestIdRequiredException **
A pull request ID is required, but none was provided.
HTTP Status Code: 400

## Examples
<a name="API_DeletePullRequestApprovalRule_Examples"></a>

### Example
<a name="API_DeletePullRequestApprovalRule_Example_1"></a>

This example illustrates one usage of DeletePullRequestApprovalRule.

#### Sample Request
<a name="API_DeletePullRequestApprovalRule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 31
X-Amz-Target: CodeCommit_20150413.DeletePullRequestApprovalRule
X-Amz-Date: 20191021T225354Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "pullRequestId": "15",
  "approvalRuleName": "My Approval Rule"
}
```

#### Sample Response
<a name="API_DeletePullRequestApprovalRule_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 55
Date: Mon, 21 Oct 2019 22:53:56 GMT

{
    "approvalRuleId": "077d8e8a8-EXAMPLE"
}
```

## See Also
<a name="API_DeletePullRequestApprovalRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/DeletePullRequestApprovalRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/DeletePullRequestApprovalRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/DeletePullRequestApprovalRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/DeletePullRequestApprovalRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/DeletePullRequestApprovalRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/DeletePullRequestApprovalRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/DeletePullRequestApprovalRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/DeletePullRequestApprovalRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/DeletePullRequestApprovalRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/DeletePullRequestApprovalRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
