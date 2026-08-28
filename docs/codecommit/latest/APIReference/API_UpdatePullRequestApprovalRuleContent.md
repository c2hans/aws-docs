---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdatePullRequestApprovalRuleContent.html
---

# UpdatePullRequestApprovalRuleContent
<a name="API_UpdatePullRequestApprovalRuleContent"></a>

Updates the structure of an approval rule created specifically for a pull request. For example, you can change the number of required approvers and the approval pool for approvers.

## Request Syntax
<a name="API_UpdatePullRequestApprovalRuleContent_RequestSyntax"></a>

```
{
   "approvalRuleName": "{{string}}",
   "existingRuleContentSha256": "{{string}}",
   "newRuleContent": "{{string}}",
   "pullRequestId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdatePullRequestApprovalRuleContent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [approvalRuleName](#API_UpdatePullRequestApprovalRuleContent_RequestSyntax) **   <a name="CodeCommit-UpdatePullRequestApprovalRuleContent-request-approvalRuleName"></a>
The name of the approval rule you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [existingRuleContentSha256](#API_UpdatePullRequestApprovalRuleContent_RequestSyntax) **   <a name="CodeCommit-UpdatePullRequestApprovalRuleContent-request-existingRuleContentSha256"></a>
The SHA-256 hash signature for the content of the approval rule. You can retrieve this information by using [GetPullRequest](API_GetPullRequest.md).
Type: String
Required: No

 ** [newRuleContent](#API_UpdatePullRequestApprovalRuleContent_RequestSyntax) **   <a name="CodeCommit-UpdatePullRequestApprovalRuleContent-request-newRuleContent"></a>
The updated content for the approval rule.
When you update the content of the approval rule, you can specify approvers in an approval pool in one of two ways:
+  **CodeCommitApprovers**: This option only requires an AWS account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the AWS account *123456789012* and *Mary\_Major*, all of the following are counted as approvals coming from that user:
  + An IAM user in the account (arn:aws:iam::*123456789012*:user/*Mary\_Major*)
  + A federated user identified in IAM as Mary\_Major (arn:aws:sts::*123456789012*:federated-user/*Mary\_Major*)

  This option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of *Mary\_Major* (arn:aws:sts::*123456789012*:assumed-role/CodeCommitReview/*Mary\_Major*) unless you include a wildcard (\*Mary\_Major).
+  **Fully qualified ARN**: This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role.
For more information about IAM ARNs, wildcards, and formats, see [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3000.
Required: Yes

 ** [pullRequestId](#API_UpdatePullRequestApprovalRuleContent_RequestSyntax) **   <a name="CodeCommit-UpdatePullRequestApprovalRuleContent-request-pullRequestId"></a>
The system-generated ID of the pull request.
Type: String
Required: Yes

## Response Syntax
<a name="API_UpdatePullRequestApprovalRuleContent_ResponseSyntax"></a>

```
{
   "approvalRule": {
      "approvalRuleContent": "string",
      "approvalRuleId": "string",
      "approvalRuleName": "string",
      "creationDate": number,
      "lastModifiedDate": number,
      "lastModifiedUser": "string",
      "originApprovalRuleTemplate": {
         "approvalRuleTemplateId": "string",
         "approvalRuleTemplateName": "string"
      },
      "ruleContentSha256": "string"
   }
}
```

## Response Elements
<a name="API_UpdatePullRequestApprovalRuleContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvalRule](#API_UpdatePullRequestApprovalRuleContent_ResponseSyntax) **   <a name="CodeCommit-UpdatePullRequestApprovalRuleContent-response-approvalRule"></a>
Information about the updated approval rule.
Type: [ApprovalRule](API_ApprovalRule.md) object

## Errors
<a name="API_UpdatePullRequestApprovalRuleContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApprovalRuleContentRequiredException **
The content for the approval rule is empty. You must provide some content for an approval rule. The content cannot be null.
HTTP Status Code: 400

 ** ApprovalRuleDoesNotExistException **
The specified approval rule does not exist.
HTTP Status Code: 400

 ** ApprovalRuleNameRequiredException **
An approval rule name is required, but was not specified.
HTTP Status Code: 400

 ** CannotModifyApprovalRuleFromTemplateException **
The approval rule cannot be modified for the pull request because it was created by an approval rule template and applied to the pull request automatically.
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

 ** InvalidApprovalRuleContentException **
The content for the approval rule is not valid.
HTTP Status Code: 400

 ** InvalidApprovalRuleNameException **
The name for the approval rule is not valid.
HTTP Status Code: 400

 ** InvalidPullRequestIdException **
The pull request ID is not valid. Make sure that you have provided the full ID and that the pull request is in the specified repository, and then try again.
HTTP Status Code: 400

 ** InvalidRuleContentSha256Exception **
The SHA-256 hash signature for the rule content is not valid.
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
<a name="API_UpdatePullRequestApprovalRuleContent_Examples"></a>

### Example
<a name="API_UpdatePullRequestApprovalRuleContent_Example_1"></a>

This example illustrates one usage of UpdatePullRequestApprovalRuleContent.

#### Sample Request
<a name="API_UpdatePullRequestApprovalRuleContent_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.UpdatePullRequestApprovalRuleContent
X-Amz-Date: 20191025T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/8
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "pullRequestId": "27",
   "approvalRuleName": "Require two approvers from approval rule",
   "approvalRuleContent": "{Version: 2018-11-08, Statements: [{Type: \"Approvers\", NumberOfApprovalsNeeded: 2, ApprovalPoolMembers:[\"CodeCommitApprovers:123456789012:user/Jorge_Souza", \"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*"]}]}}"
}
```

#### Sample Response
<a name="API_UpdatePullRequestApprovalRuleContent_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 847
Date: Fri, 25 Oct 2019 20:20:13 GMT

{
    "approvalRule": {
        "approvalRuleName": "Require two approvers from approval pool",
        "lastModifiedDate": 1570752871.932,
        "ruleContentSha256": "7c44e6ebEXAMPLE",
        "creationDate": 1570752871.932,
        "approvalRuleId": "bal37823-EXAMPLE",
        "originApprovalRuleTemplate": {},
        "approvalRuleContent": "{Version: 2018-11-08, Statements: [{Type: \"Approvers\", NumberOfApprovalsNeeded: 2, ApprovalPoolMembers:[\"CodeCommitApprovers:123456789012:user/Jorge_Souza", \"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*"]}]}}",
        "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major"
    }
}
```

## See Also
<a name="API_UpdatePullRequestApprovalRuleContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/UpdatePullRequestApprovalRuleContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/UpdatePullRequestApprovalRuleContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/UpdatePullRequestApprovalRuleContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/UpdatePullRequestApprovalRuleContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/UpdatePullRequestApprovalRuleContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/UpdatePullRequestApprovalRuleContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/UpdatePullRequestApprovalRuleContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/UpdatePullRequestApprovalRuleContent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/UpdatePullRequestApprovalRuleContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/UpdatePullRequestApprovalRuleContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
