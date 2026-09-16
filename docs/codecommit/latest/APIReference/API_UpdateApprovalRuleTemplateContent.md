---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdateApprovalRuleTemplateContent.html
---

# UpdateApprovalRuleTemplateContent
<a name="API_UpdateApprovalRuleTemplateContent"></a>

Updates the content of an approval rule template. You can change the number of required approvals, the membership of the approval rule, and whether an approval pool is defined.

## Request Syntax
<a name="API_UpdateApprovalRuleTemplateContent_RequestSyntax"></a>

```
{
   "approvalRuleTemplateName": "{{string}}",
   "existingRuleContentSha256": "{{string}}",
   "newRuleContent": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateApprovalRuleTemplateContent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [approvalRuleTemplateName](#API_UpdateApprovalRuleTemplateContent_RequestSyntax) **   <a name="CodeCommit-UpdateApprovalRuleTemplateContent-request-approvalRuleTemplateName"></a>
The name of the approval rule template where you want to update the content of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [existingRuleContentSha256](#API_UpdateApprovalRuleTemplateContent_RequestSyntax) **   <a name="CodeCommit-UpdateApprovalRuleTemplateContent-request-existingRuleContentSha256"></a>
The SHA-256 hash signature for the content of the approval rule. You can retrieve this information by using [GetPullRequest](API_GetPullRequest.md).
Type: String
Required: No

 ** [newRuleContent](#API_UpdateApprovalRuleTemplateContent_RequestSyntax) **   <a name="CodeCommit-UpdateApprovalRuleTemplateContent-request-newRuleContent"></a>
The content that replaces the existing content of the rule. Content statements must be complete. You cannot provide only the changes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3000.
Required: Yes

## Response Syntax
<a name="API_UpdateApprovalRuleTemplateContent_ResponseSyntax"></a>

```
{
   "approvalRuleTemplate": {
      "approvalRuleTemplateContent": "string",
      "approvalRuleTemplateDescription": "string",
      "approvalRuleTemplateId": "string",
      "approvalRuleTemplateName": "string",
      "creationDate": number,
      "lastModifiedDate": number,
      "lastModifiedUser": "string",
      "ruleContentSha256": "string"
   }
}
```

## Response Elements
<a name="API_UpdateApprovalRuleTemplateContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvalRuleTemplate](#API_UpdateApprovalRuleTemplateContent_ResponseSyntax) **   <a name="CodeCommit-UpdateApprovalRuleTemplateContent-response-approvalRuleTemplate"></a>
Returns information about an approval rule template.
Type: [ApprovalRuleTemplate](API_ApprovalRuleTemplate.md) object

## Errors
<a name="API_UpdateApprovalRuleTemplateContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApprovalRuleTemplateContentRequiredException **
The content for the approval rule template is empty. You must provide some content for an approval rule template. The content cannot be null.
HTTP Status Code: 400

 ** ApprovalRuleTemplateDoesNotExistException **
The specified approval rule template does not exist. Verify that the name is correct and that you are signed in to the AWS Region where the template was created, and then try again.
HTTP Status Code: 400

 ** ApprovalRuleTemplateNameRequiredException **
An approval rule template name is required, but was not specified.
HTTP Status Code: 400

 ** InvalidApprovalRuleTemplateContentException **
The content of the approval rule template is not valid.
HTTP Status Code: 400

 ** InvalidApprovalRuleTemplateNameException **
The name of the approval rule template is not valid. Template names must be between 1 and 100 valid characters in length. For more information about limits in AWS CodeCommit, see [Quotas](https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html) in the * AWS CodeCommit User Guide*.
HTTP Status Code: 400

 ** InvalidRuleContentSha256Exception **
The SHA-256 hash signature for the rule content is not valid.
HTTP Status Code: 400

## Examples
<a name="API_UpdateApprovalRuleTemplateContent_Examples"></a>

### Example
<a name="API_UpdateApprovalRuleTemplateContent_Example_1"></a>

This example illustrates one usage of UpdateApprovalRuleTemplateContent.

#### Sample Request
<a name="API_UpdateApprovalRuleTemplateContent_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.UpdateApprovalRuleTemplateContent
X-Amz-Date: 20191021T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
    "approvalRuleTemplateName": "1-approver-rule-for-all-pull-requests",
    "newRuleContent": "{\"Version\": \"2018-11-08\",\"DestinationReferences\": [\"refs/heads/main\"],\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}"
}
```

#### Sample Response
<a name="API_UpdateApprovalRuleTemplateContent_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 847
Date: Mon, 21 Oct 2019 20:20:13 GMT

{
    "approvalRuleTemplate": {
        "creationDate": 1571352720.773,
        "approvalRuleTemplateDescription": "Requires 1 approval for all pull requests from the CodeCommitReview pool",
        "lastModifiedDate": 1571358728.41,
        "approvalRuleTemplateId": "41de97b7-EXAMPLE",
        "approvalRuleTemplateContent": "{\"Version\": \"2018-11-08\",\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 1,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}",
        "approvalRuleTemplateName": "1-approver-rule-for-all-pull-requests",
        "ruleContentSha256": "2f6c21a5EXAMPLE",
        "lastModifiedUser": "arn:aws:iam::123456789012:user/Li_Juan"
    }
}
```

## See Also
<a name="API_UpdateApprovalRuleTemplateContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/UpdateApprovalRuleTemplateContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/UpdateApprovalRuleTemplateContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/UpdateApprovalRuleTemplateContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/UpdateApprovalRuleTemplateContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/UpdateApprovalRuleTemplateContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/UpdateApprovalRuleTemplateContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/UpdateApprovalRuleTemplateContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/UpdateApprovalRuleTemplateContent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/UpdateApprovalRuleTemplateContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/UpdateApprovalRuleTemplateContent)
