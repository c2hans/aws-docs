---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_UpdateApprovalRuleTemplateDescription.html
---

# UpdateApprovalRuleTemplateDescription
<a name="API_UpdateApprovalRuleTemplateDescription"></a>

Updates the description for a specified approval rule template.

## Request Syntax
<a name="API_UpdateApprovalRuleTemplateDescription_RequestSyntax"></a>

```
{
   "approvalRuleTemplateDescription": "{{string}}",
   "approvalRuleTemplateName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateApprovalRuleTemplateDescription_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [approvalRuleTemplateDescription](#API_UpdateApprovalRuleTemplateDescription_RequestSyntax) **   <a name="CodeCommit-UpdateApprovalRuleTemplateDescription-request-approvalRuleTemplateDescription"></a>
The updated description of the approval rule template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** [approvalRuleTemplateName](#API_UpdateApprovalRuleTemplateDescription_RequestSyntax) **   <a name="CodeCommit-UpdateApprovalRuleTemplateDescription-request-approvalRuleTemplateName"></a>
The name of the template for which you want to update the description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_UpdateApprovalRuleTemplateDescription_ResponseSyntax"></a>

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
<a name="API_UpdateApprovalRuleTemplateDescription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvalRuleTemplate](#API_UpdateApprovalRuleTemplateDescription_ResponseSyntax) **   <a name="CodeCommit-UpdateApprovalRuleTemplateDescription-response-approvalRuleTemplate"></a>
The structure and content of the updated approval rule template.
Type: [ApprovalRuleTemplate](API_ApprovalRuleTemplate.md) object

## Errors
<a name="API_UpdateApprovalRuleTemplateDescription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApprovalRuleTemplateDoesNotExistException **
The specified approval rule template does not exist. Verify that the name is correct and that you are signed in to the AWS Region where the template was created, and then try again.
HTTP Status Code: 400

 ** ApprovalRuleTemplateNameRequiredException **
An approval rule template name is required, but was not specified.
HTTP Status Code: 400

 ** InvalidApprovalRuleTemplateDescriptionException **
The description for the approval rule template is not valid because it exceeds the maximum characters allowed for a description. For more information about limits in AWS CodeCommit, see [Quotas](https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html) in the * AWS CodeCommit User Guide*.
HTTP Status Code: 400

 ** InvalidApprovalRuleTemplateNameException **
The name of the approval rule template is not valid. Template names must be between 1 and 100 valid characters in length. For more information about limits in AWS CodeCommit, see [Quotas](https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html) in the * AWS CodeCommit User Guide*.
HTTP Status Code: 400

## Examples
<a name="API_UpdateApprovalRuleTemplateDescription_Examples"></a>

### Example
<a name="API_UpdateApprovalRuleTemplateDescription_Example_1"></a>

This example illustrates one usage of UpdateApprovalRuleTemplateDescription.

#### Sample Request
<a name="API_UpdateApprovalRuleTemplateDescription_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: CodeCommit_20150413.UpdateApprovalRuleTemplateDescription
X-Amz-Date: 20191021T132023Z
User-Agent: aws-cli/1.11.187 Python/2.7.9 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20171025/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "approvalRuleTemplateName": "1-approver-rule-for-all-pull-requests",
   "approvalRuleTemplateDescription": "Requires 1 approval for all pull requests from the CodeCommitReview pool"
}
```

#### Sample Response
<a name="API_UpdateApprovalRuleTemplateDescription_Example_1_Response"></a>

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
<a name="API_UpdateApprovalRuleTemplateDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/UpdateApprovalRuleTemplateDescription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/UpdateApprovalRuleTemplateDescription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/UpdateApprovalRuleTemplateDescription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/UpdateApprovalRuleTemplateDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/UpdateApprovalRuleTemplateDescription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/UpdateApprovalRuleTemplateDescription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/UpdateApprovalRuleTemplateDescription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/UpdateApprovalRuleTemplateDescription)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/UpdateApprovalRuleTemplateDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/UpdateApprovalRuleTemplateDescription)
