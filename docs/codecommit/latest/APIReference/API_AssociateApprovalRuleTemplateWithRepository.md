---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_AssociateApprovalRuleTemplateWithRepository.html
---

# AssociateApprovalRuleTemplateWithRepository
<a name="API_AssociateApprovalRuleTemplateWithRepository"></a>

Creates an association between an approval rule template and a specified repository. Then, the next time a pull request is created in the repository where the destination reference (if specified) matches the destination reference (branch) for the pull request, an approval rule that matches the template conditions is automatically created for that pull request. If no destination references are specified in the template, an approval rule that matches the template contents is created for all pull requests in that repository.

## Request Syntax
<a name="API_AssociateApprovalRuleTemplateWithRepository_RequestSyntax"></a>

```
{
   "approvalRuleTemplateName": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateApprovalRuleTemplateWithRepository_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [approvalRuleTemplateName](#API_AssociateApprovalRuleTemplateWithRepository_RequestSyntax) **   <a name="CodeCommit-AssociateApprovalRuleTemplateWithRepository-request-approvalRuleTemplateName"></a>
The name for the approval rule template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [repositoryName](#API_AssociateApprovalRuleTemplateWithRepository_RequestSyntax) **   <a name="CodeCommit-AssociateApprovalRuleTemplateWithRepository-request-repositoryName"></a>
The name of the repository that you want to associate with the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Elements
<a name="API_AssociateApprovalRuleTemplateWithRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateApprovalRuleTemplateWithRepository_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApprovalRuleTemplateDoesNotExistException **
The specified approval rule template does not exist. Verify that the name is correct and that you are signed in to the AWS Region where the template was created, and then try again.
HTTP Status Code: 400

 ** ApprovalRuleTemplateNameRequiredException **
An approval rule template name is required, but was not specified.
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

 ** InvalidApprovalRuleTemplateNameException **
The name of the approval rule template is not valid. Template names must be between 1 and 100 valid characters in length. For more information about limits in AWS CodeCommit, see [Quotas](https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html) in the * AWS CodeCommit User Guide*.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** MaximumRuleTemplatesAssociatedWithRepositoryException **
The maximum number of approval rule templates for a repository has been exceeded. You cannot associate more than 25 approval rule templates with a repository.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_AssociateApprovalRuleTemplateWithRepository_Examples"></a>

### Example
<a name="API_AssociateApprovalRuleTemplateWithRepository_Example_1"></a>

This example illustrates one usage of AssociateApprovalRuleTemplateWithRepository.

#### Sample Request
<a name="API_AssociateApprovalRuleTemplateWithRepository_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 226
X-Amz-Target: CodeCommit_20150413.AssociateApprovalRuleTemplateWithRepository
X-Amz-Date: 20191021T213222Z
User-Agent: aws-cli/1.16.137 Python/3.6.0 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "repositoryName": "MyDemoRepo",
  "approvalRuleTemplateName": "2-approver-rule-for-main"
}
```

#### Sample Response
<a name="API_AssociateApprovalRuleTemplateWithRepository_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 1681
Date: Mon, 21 Oxr 2019 22:43:13 GMT
```

## See Also
<a name="API_AssociateApprovalRuleTemplateWithRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/AssociateApprovalRuleTemplateWithRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/AssociateApprovalRuleTemplateWithRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/AssociateApprovalRuleTemplateWithRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/AssociateApprovalRuleTemplateWithRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/AssociateApprovalRuleTemplateWithRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/AssociateApprovalRuleTemplateWithRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/AssociateApprovalRuleTemplateWithRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/AssociateApprovalRuleTemplateWithRepository)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/AssociateApprovalRuleTemplateWithRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/AssociateApprovalRuleTemplateWithRepository)
