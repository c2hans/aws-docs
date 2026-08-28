---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_CreateIdentityCenterApplication.html
---

# CreateIdentityCenterApplication
<a name="API_CreateIdentityCenterApplication"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

 Creates the WorkMail application in IAM Identity Center that can be used later in the WorkMail - IdC integration. For more information, see PutIdentityProviderConfiguration. This action does not affect the authentication settings for any WorkMail organizations.

## Request Syntax
<a name="API_CreateIdentityCenterApplication_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "InstanceArn": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateIdentityCenterApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateIdentityCenterApplication_RequestSyntax) **   <a name="workmail-CreateIdentityCenterApplication-request-ClientToken"></a>
 The idempotency token associated with the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7e]+`
Required: No

 ** [InstanceArn](#API_CreateIdentityCenterApplication_RequestSyntax) **   <a name="workmail-CreateIdentityCenterApplication-request-InstanceArn"></a>
 The Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1124.
Pattern: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$`
Required: Yes

 ** [Name](#API_CreateIdentityCenterApplication_RequestSyntax) **   <a name="workmail-CreateIdentityCenterApplication-request-Name"></a>
 The name of the IAM Identity Center application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `^[\w+=,.@-]+$`
Required: Yes

## Response Syntax
<a name="API_CreateIdentityCenterApplication_ResponseSyntax"></a>

```
{
   "ApplicationArn": "string"
}
```

## Response Elements
<a name="API_CreateIdentityCenterApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationArn](#API_CreateIdentityCenterApplication_ResponseSyntax) **   <a name="workmail-CreateIdentityCenterApplication-response-ApplicationArn"></a>
 The Amazon Resource Name (ARN) of the application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}$`

## Errors
<a name="API_CreateIdentityCenterApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

## See Also
<a name="API_CreateIdentityCenterApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/CreateIdentityCenterApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/CreateIdentityCenterApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/CreateIdentityCenterApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/CreateIdentityCenterApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/CreateIdentityCenterApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/CreateIdentityCenterApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/CreateIdentityCenterApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/CreateIdentityCenterApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/CreateIdentityCenterApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/CreateIdentityCenterApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
