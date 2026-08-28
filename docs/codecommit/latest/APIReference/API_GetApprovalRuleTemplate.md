---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetApprovalRuleTemplate.html
---

# GetApprovalRuleTemplate
<a name="API_GetApprovalRuleTemplate"></a>

Returns information about a specified approval rule template.

## Request Syntax
<a name="API_GetApprovalRuleTemplate_RequestSyntax"></a>

```
{
   "approvalRuleTemplateName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetApprovalRuleTemplate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [approvalRuleTemplateName](#API_GetApprovalRuleTemplate_RequestSyntax) **   <a name="CodeCommit-GetApprovalRuleTemplate-request-approvalRuleTemplateName"></a>
The name of the approval rule template for which you want to get information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_GetApprovalRuleTemplate_ResponseSyntax"></a>

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
<a name="API_GetApprovalRuleTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvalRuleTemplate](#API_GetApprovalRuleTemplate_ResponseSyntax) **   <a name="CodeCommit-GetApprovalRuleTemplate-response-approvalRuleTemplate"></a>
The content and structure of the approval rule template.
Type: [ApprovalRuleTemplate](API_ApprovalRuleTemplate.md) object

## Errors
<a name="API_GetApprovalRuleTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApprovalRuleTemplateDoesNotExistException **
The specified approval rule template does not exist. Verify that the name is correct and that you are signed in to the AWS Region where the template was created, and then try again.
HTTP Status Code: 400

 ** ApprovalRuleTemplateNameRequiredException **
An approval rule template name is required, but was not specified.
HTTP Status Code: 400

 ** InvalidApprovalRuleTemplateNameException **
The name of the approval rule template is not valid. Template names must be between 1 and 100 valid characters in length. For more information about limits in AWS CodeCommit, see [Quotas](https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html) in the * AWS CodeCommit User Guide*.
HTTP Status Code: 400

## Examples
<a name="API_GetApprovalRuleTemplate_Examples"></a>

### Example
<a name="API_GetApprovalRuleTemplate_Example_1"></a>

This example illustrates one usage of GetApprovalRuleTemplate.

#### Sample Request
<a name="API_GetApprovalRuleTemplate_Example_1_Request"></a>

```
POST / HTTP/1.1
    Host: codecommit.us-east-1.amazonaws.com
    Accept-Encoding: identity
    Content-Length: 124
    X-Amz-Target: CodeCommit_20150413.GetApprovalRuleTemplate
    X-Amz-Date: 20191021T223055Z
    User-Agent: aws-cli/1.15.9 Python/2.7.11 Darwin/16.7.0 botocore/1.10.9
    Content-Type: application/x-amz-json-1.1
    Authorization: AWS4-HMAC-SHA256 Credential=AKIAEXAMPLE/20180914/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature==8d9b5998EXAMPLE
{
   "approvalRuleTemplateName": "1-approver-rule-for-all-pull-requests"
}
```

#### Sample Response
<a name="API_GetApprovalRuleTemplate_Example_1_Response"></a>

```
HTTP/1.1 200 OK
    x-amzn-RequestId: d8ad1d21-EXAMPLE
    Content-Type: application/x-amz-json-1.1
    Content-Length: 2267
    Date: Mon, 21 Oct 2019 22:30:56 GMT
    Connection: keep-alive

{
    "approvalRuleTemplate": {
        "approvalRuleTemplateContent": "{\"Version\": \"2018-11-08\",\"DestinationReferences\": [\"refs/heads/main\"],\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}",
        "ruleContentSha256": "621181bbEXAMPLE",
        "lastModifiedDate": 1571356106.936,
        "creationDate": 1571356106.936,
        "approvalRuleTemplateName": "1-approver-rule-for-all-pull-requests",
        "lastModifiedUser": "arn:aws:iam::123456789012:user/Li_Juan",
        "approvalRuleTemplateId": "a29abb15-EXAMPLE",
        "approvalRuleTemplateDescription": "All pull requests must be approved by one developer on the team."
    }
}
```

## See Also
<a name="API_GetApprovalRuleTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/GetApprovalRuleTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/GetApprovalRuleTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/GetApprovalRuleTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/GetApprovalRuleTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/GetApprovalRuleTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/GetApprovalRuleTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/GetApprovalRuleTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/GetApprovalRuleTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/GetApprovalRuleTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/GetApprovalRuleTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
