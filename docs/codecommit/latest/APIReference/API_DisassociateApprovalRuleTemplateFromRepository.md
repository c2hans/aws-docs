---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_DisassociateApprovalRuleTemplateFromRepository.html
---

# DisassociateApprovalRuleTemplateFromRepository
<a name="API_DisassociateApprovalRuleTemplateFromRepository"></a>

Removes the association between a template and a repository so that approval rules based on the template are not automatically created when pull requests are created in the specified repository. This does not delete any approval rules previously created for pull requests through the template association.

## Request Syntax
<a name="API_DisassociateApprovalRuleTemplateFromRepository_RequestSyntax"></a>

```
{
   "approvalRuleTemplateName": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateApprovalRuleTemplateFromRepository_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [approvalRuleTemplateName](#API_DisassociateApprovalRuleTemplateFromRepository_RequestSyntax) **   <a name="CodeCommit-DisassociateApprovalRuleTemplateFromRepository-request-approvalRuleTemplateName"></a>
The name of the approval rule template to disassociate from a specified repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [repositoryName](#API_DisassociateApprovalRuleTemplateFromRepository_RequestSyntax) **   <a name="CodeCommit-DisassociateApprovalRuleTemplateFromRepository-request-repositoryName"></a>
The name of the repository you want to disassociate from the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Elements
<a name="API_DisassociateApprovalRuleTemplateFromRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateApprovalRuleTemplateFromRepository_Errors"></a>

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

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_DisassociateApprovalRuleTemplateFromRepository_Examples"></a>

### Example
<a name="API_DisassociateApprovalRuleTemplateFromRepository_Example_1"></a>

This example illustrates one usage of DisassociateApprovalRuleTemplateFromRepository.

#### Sample Request
<a name="API_DisassociateApprovalRuleTemplateFromRepository_Example_1_Request"></a>

```
POST / HTTP/1.1
    Host: codecommit.us-east-1.amazonaws.com
    Accept-Encoding: identity
    Content-Length: 124
    X-Amz-Target: CodeCommit_20150413.DisassociateApprovalRuleTemplateFromRepository
    X-Amz-Date: 20191021T223055Z
    User-Agent: aws-cli/1.15.9 Python/2.7.11 Darwin/16.7.0 botocore/1.10.9
    Content-Type: application/x-amz-json-1.1
    Authorization: AWS4-HMAC-SHA256 Credential=AKIAEXAMPLE/20180914/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature==8d9b5998EXAMPLE
{
   "repositoryName": "MyDemoRepo"
   "approvalRuleTemplateName": "1-approver-rule-for-all-pull-requests"
}
```

#### Sample Response
<a name="API_DisassociateApprovalRuleTemplateFromRepository_Example_1_Response"></a>

```
HTTP/1.1 200 OK
    x-amzn-RequestId: d8ad1d21-EXAMPLE
    Content-Type: application/x-amz-json-1.1
    Content-Length: 2267
    Date: Mon, 21 Oct 2019 22:30:56 GMT
```

## See Also
<a name="API_DisassociateApprovalRuleTemplateFromRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/DisassociateApprovalRuleTemplateFromRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/DisassociateApprovalRuleTemplateFromRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/DisassociateApprovalRuleTemplateFromRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/DisassociateApprovalRuleTemplateFromRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/DisassociateApprovalRuleTemplateFromRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/DisassociateApprovalRuleTemplateFromRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/DisassociateApprovalRuleTemplateFromRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/DisassociateApprovalRuleTemplateFromRepository)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/DisassociateApprovalRuleTemplateFromRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/DisassociateApprovalRuleTemplateFromRepository)
