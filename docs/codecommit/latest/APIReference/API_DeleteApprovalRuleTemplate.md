---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DeleteApprovalRuleTemplate.html
---

# DeleteApprovalRuleTemplate
<a name="API_DeleteApprovalRuleTemplate"></a>

Deletes a specified approval rule template. Deleting a template does not remove approval rules on pull requests already created with the template.

## Request Syntax
<a name="API_DeleteApprovalRuleTemplate_RequestSyntax"></a>

```
{
   "approvalRuleTemplateName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteApprovalRuleTemplate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [approvalRuleTemplateName](#API_DeleteApprovalRuleTemplate_RequestSyntax) **   <a name="CodeCommit-DeleteApprovalRuleTemplate-request-approvalRuleTemplateName"></a>
The name of the approval rule template to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_DeleteApprovalRuleTemplate_ResponseSyntax"></a>

```
{
   "approvalRuleTemplateId": "string"
}
```

## Response Elements
<a name="API_DeleteApprovalRuleTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvalRuleTemplateId](#API_DeleteApprovalRuleTemplate_ResponseSyntax) **   <a name="CodeCommit-DeleteApprovalRuleTemplate-response-approvalRuleTemplateId"></a>
The system-generated ID of the deleted approval rule template. If the template has been previously deleted, the only response is a 200 OK.
Type: String

## Errors
<a name="API_DeleteApprovalRuleTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApprovalRuleTemplateInUseException **
The approval rule template is associated with one or more repositories. You cannot delete a template that is associated with a repository. Remove all associations, and then try again.
HTTP Status Code: 400

 ** ApprovalRuleTemplateNameRequiredException **
An approval rule template name is required, but was not specified.
HTTP Status Code: 400

 ** InvalidApprovalRuleTemplateNameException **
The name of the approval rule template is not valid. Template names must be between 1 and 100 valid characters in length. For more information about limits in AWS CodeCommit, see [Quotas](https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html) in the * AWS CodeCommit User Guide*.
HTTP Status Code: 400

## Examples
<a name="API_DeleteApprovalRuleTemplate_Examples"></a>

### Example
<a name="API_DeleteApprovalRuleTemplate_Example_1"></a>

This example illustrates one usage of DeleteApprovalRuleTemplate.

#### Sample Request
<a name="API_DeleteApprovalRuleTemplate_Example_1_Request"></a>

```
HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 57
X-Amz-Target: CodeCommit_20150413.DeleteApprovalRuleTemplate
X-Amz-Date: 20191021T224659Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "approvalRuleTemplateName": "1-approver-for-all-pull-requests"
}
```

#### Sample Response
<a name="API_DeleteApprovalRuleTemplate_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 48
Date: Mon, 21 Oct 2019 22:47:03 GMT

{
    "approvalRuleTemplateId": "41de97b7-EXAMPLE"
}
```

## See Also
<a name="API_DeleteApprovalRuleTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/DeleteApprovalRuleTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/DeleteApprovalRuleTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/DeleteApprovalRuleTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/DeleteApprovalRuleTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/DeleteApprovalRuleTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/DeleteApprovalRuleTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/DeleteApprovalRuleTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/DeleteApprovalRuleTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/DeleteApprovalRuleTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/DeleteApprovalRuleTemplate)
