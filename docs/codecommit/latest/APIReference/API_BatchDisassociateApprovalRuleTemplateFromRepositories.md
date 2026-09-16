---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_BatchDisassociateApprovalRuleTemplateFromRepositories.html
---

# BatchDisassociateApprovalRuleTemplateFromRepositories
<a name="API_BatchDisassociateApprovalRuleTemplateFromRepositories"></a>

Removes the association between an approval rule template and one or more specified repositories.

## Request Syntax
<a name="API_BatchDisassociateApprovalRuleTemplateFromRepositories_RequestSyntax"></a>

```
{
   "approvalRuleTemplateName": "{{string}}",
   "repositoryNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchDisassociateApprovalRuleTemplateFromRepositories_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [approvalRuleTemplateName](#API_BatchDisassociateApprovalRuleTemplateFromRepositories_RequestSyntax) **   <a name="CodeCommit-BatchDisassociateApprovalRuleTemplateFromRepositories-request-approvalRuleTemplateName"></a>
The name of the template that you want to disassociate from one or more repositories.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [repositoryNames](#API_BatchDisassociateApprovalRuleTemplateFromRepositories_RequestSyntax) **   <a name="CodeCommit-BatchDisassociateApprovalRuleTemplateFromRepositories-request-repositoryNames"></a>
The repository names that you want to disassociate from the approval rule template.
The length constraint limit is for each string in the array. The array itself can be empty.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

## Response Syntax
<a name="API_BatchDisassociateApprovalRuleTemplateFromRepositories_ResponseSyntax"></a>

```
{
   "disassociatedRepositoryNames": [ "string" ],
   "errors": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "repositoryName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDisassociateApprovalRuleTemplateFromRepositories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [disassociatedRepositoryNames](#API_BatchDisassociateApprovalRuleTemplateFromRepositories_ResponseSyntax) **   <a name="CodeCommit-BatchDisassociateApprovalRuleTemplateFromRepositories-response-disassociatedRepositoryNames"></a>
A list of repository names that have had their association with the template removed.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`

 ** [errors](#API_BatchDisassociateApprovalRuleTemplateFromRepositories_ResponseSyntax) **   <a name="CodeCommit-BatchDisassociateApprovalRuleTemplateFromRepositories-response-errors"></a>
A list of any errors that might have occurred while attempting to remove the association between the template and the repositories.
Type: Array of [BatchDisassociateApprovalRuleTemplateFromRepositoriesError](API_BatchDisassociateApprovalRuleTemplateFromRepositoriesError.md) objects

## Errors
<a name="API_BatchDisassociateApprovalRuleTemplateFromRepositories_Errors"></a>

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

 ** MaximumRepositoryNamesExceededException **
The maximum number of allowed repository names was exceeded. Currently, this number is 100.
HTTP Status Code: 400

 ** RepositoryNamesRequiredException **
At least one repository name object is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_BatchDisassociateApprovalRuleTemplateFromRepositories_Examples"></a>

### Example
<a name="API_BatchDisassociateApprovalRuleTemplateFromRepositories_Example_1"></a>

This example illustrates one usage of BatchDisassociateApprovalRuleTemplateFromRepositories.

#### Sample Request
<a name="API_BatchDisassociateApprovalRuleTemplateFromRepositories_Example_1_Request"></a>

```
>POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 226
X-Amz-Target: CodeCommit_20150413.BatchDisassociateApprovalRuleTemplateFromRepositories
X-Amz-Date: 20191021T213222Z
User-Agent: aws-cli/1.16.137 Python/3.6.0 Windows/10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
    "approvalRuleTemplateName": "2-approver-rule-for-main",
    "repositoryNames": [
        "MyDemoRepo",
        "MyOtherDemoRepo"
    ]
}
```

#### Sample Response
<a name="API_BatchDisassociateApprovalRuleTemplateFromRepositories_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 1681
Date: Mon, 21 Oxr 2019 22:43:13 GMT

    "disassociatedRepositoryNames": [
        "MyDemoRepo",
        "MyOtherDemoRepo"
    ],
    "errors": []
}
```

## See Also
<a name="API_BatchDisassociateApprovalRuleTemplateFromRepositories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/BatchDisassociateApprovalRuleTemplateFromRepositories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/BatchDisassociateApprovalRuleTemplateFromRepositories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/BatchDisassociateApprovalRuleTemplateFromRepositories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/BatchDisassociateApprovalRuleTemplateFromRepositories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/BatchDisassociateApprovalRuleTemplateFromRepositories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/BatchDisassociateApprovalRuleTemplateFromRepositories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/BatchDisassociateApprovalRuleTemplateFromRepositories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/BatchDisassociateApprovalRuleTemplateFromRepositories)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/BatchDisassociateApprovalRuleTemplateFromRepositories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/BatchDisassociateApprovalRuleTemplateFromRepositories)
