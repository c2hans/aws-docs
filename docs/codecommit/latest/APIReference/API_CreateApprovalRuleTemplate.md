---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_CreateApprovalRuleTemplate.html
---

# CreateApprovalRuleTemplate
<a name="API_CreateApprovalRuleTemplate"></a>

Creates a template for approval rules that can then be associated with one or more repositories in your AWS account. When you associate a template with a repository, AWS CodeCommit creates an approval rule that matches the conditions of the template for all pull requests that meet the conditions of the template. For more information, see [AssociateApprovalRuleTemplateWithRepository](API_AssociateApprovalRuleTemplateWithRepository.md).

## Request Syntax
<a name="API_CreateApprovalRuleTemplate_RequestSyntax"></a>

```
{
   "approvalRuleTemplateContent": "{{string}}",
   "approvalRuleTemplateDescription": "{{string}}",
   "approvalRuleTemplateName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateApprovalRuleTemplate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [approvalRuleTemplateContent](#API_CreateApprovalRuleTemplate_RequestSyntax) **   <a name="CodeCommit-CreateApprovalRuleTemplate-request-approvalRuleTemplateContent"></a>
The content of the approval rule that is created on pull requests in associated repositories. If you specify one or more destination references (branches), approval rules are created in an associated repository only if their destination references (branches) match those specified in the template.
When you create the content of the approval rule template, you can specify approvers in an approval pool in one of two ways:
+  **CodeCommitApprovers**: This option only requires an AWS account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the AWS account *123456789012* and *Mary\_Major*, all of the following are counted as approvals coming from that user:
  + An IAM user in the account (arn:aws:iam::*123456789012*:user/*Mary\_Major*)
  + A federated user identified in IAM as Mary\_Major (arn:aws:sts::*123456789012*:federated-user/*Mary\_Major*)

  This option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of *Mary\_Major* (arn:aws:sts::*123456789012*:assumed-role/CodeCommitReview/*Mary\_Major*) unless you include a wildcard (\*Mary\_Major).
+  **Fully qualified ARN**: This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role.
For more information about IAM ARNs, wildcards, and formats, see [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3000.
Required: Yes

 ** [approvalRuleTemplateDescription](#API_CreateApprovalRuleTemplate_RequestSyntax) **   <a name="CodeCommit-CreateApprovalRuleTemplate-request-approvalRuleTemplateDescription"></a>
The description of the approval rule template. Consider providing a description that explains what this template does and when it might be appropriate to associate it with repositories.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [approvalRuleTemplateName](#API_CreateApprovalRuleTemplate_RequestSyntax) **   <a name="CodeCommit-CreateApprovalRuleTemplate-request-approvalRuleTemplateName"></a>
The name of the approval rule template. Provide descriptive names, because this name is applied to the approval rules created automatically in associated repositories.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_CreateApprovalRuleTemplate_ResponseSyntax"></a>

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
<a name="API_CreateApprovalRuleTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvalRuleTemplate](#API_CreateApprovalRuleTemplate_ResponseSyntax) **   <a name="CodeCommit-CreateApprovalRuleTemplate-response-approvalRuleTemplate"></a>
The content and structure of the created approval rule template.
Type: [ApprovalRuleTemplate](API_ApprovalRuleTemplate.md) object

## Errors
<a name="API_CreateApprovalRuleTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApprovalRuleTemplateContentRequiredException **
The content for the approval rule template is empty. You must provide some content for an approval rule template. The content cannot be null.
HTTP Status Code: 400

 ** ApprovalRuleTemplateNameAlreadyExistsException **
You cannot create an approval rule template with that name because a template with that name already exists in this AWS Region for your AWS account. Approval rule template names must be unique.
HTTP Status Code: 400

 ** ApprovalRuleTemplateNameRequiredException **
An approval rule template name is required, but was not specified.
HTTP Status Code: 400

 ** InvalidApprovalRuleTemplateContentException **
The content of the approval rule template is not valid.
HTTP Status Code: 400

 ** InvalidApprovalRuleTemplateDescriptionException **
The description for the approval rule template is not valid because it exceeds the maximum characters allowed for a description. For more information about limits in AWS CodeCommit, see [Quotas](https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html) in the * AWS CodeCommit User Guide*.
HTTP Status Code: 400

 ** InvalidApprovalRuleTemplateNameException **
The name of the approval rule template is not valid. Template names must be between 1 and 100 valid characters in length. For more information about limits in AWS CodeCommit, see [Quotas](https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html) in the * AWS CodeCommit User Guide*.
HTTP Status Code: 400

 ** NumberOfRuleTemplatesExceededException **
The maximum number of approval rule templates has been exceeded for this AWS Region.
HTTP Status Code: 400

## Examples
<a name="API_CreateApprovalRuleTemplate_Examples"></a>

### Example
<a name="API_CreateApprovalRuleTemplate_Example_1"></a>

This example illustrates one usage of CreateApprovalRuleTemplate.

#### Sample Request
<a name="API_CreateApprovalRuleTemplate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 113
X-Amz-Target: CodeCommit_20150413.CreateApprovalRuleTemplate
X-Amz-Date: 20191021T221237Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
    "approvalRuleTemplateContent": "{\"Version\": \"2018-11-08\",\"DestinationReferences\": [\"refs/heads/main\"],\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}",
    "approvalRuleTemplateDescription": "Requires two developers from the team to approve the pull request if the destination branch is main",
    "approvalRuleTemplateName": "2-approver-rule-for-main"
}
```

#### Sample Response
<a name="API_CreateApprovalRuleTemplate_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Mon, 21 Oct 2019 22:12:40 GMT

{
    "approvalRuleTemplate": {
        "approvalRuleTemplateName": "2-approver-rule-for-main",
        "creationDate": 1571356106.936,
        "approvalRuleTemplateId": "dd8b17fe-EXAMPLE",
        "approvalRuleTemplateContent": "{\"Version\": \"2018-11-08\",\"DestinationReferences\": [\"refs/heads/main\"],\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}",
        "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major",
        "approvalRuleTemplateDescription": "Requires two developers from the team to approve the pull request if the destination branch is main",
        "lastModifiedDate": 1571356106.936,
        "ruleContentSha256": "4711b576EXAMPLE"
    }
}
```

## See Also
<a name="API_CreateApprovalRuleTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/CreateApprovalRuleTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/CreateApprovalRuleTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/CreateApprovalRuleTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/CreateApprovalRuleTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/CreateApprovalRuleTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/CreateApprovalRuleTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/CreateApprovalRuleTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/CreateApprovalRuleTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/CreateApprovalRuleTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/CreateApprovalRuleTemplate)
