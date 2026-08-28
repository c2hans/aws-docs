---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_CreateTrustedIdentityPropagationApplicationForConsole.html
---

# CreateTrustedIdentityPropagationApplicationForConsole
<a name="API_CreateTrustedIdentityPropagationApplicationForConsole"></a>

Creates an IAM Identity Center application that represents the AWS Management Console on an IAM Identity Center organization instance. This application supports identity-aware sessions in IAM Identity Center, which enables additional user context to be included in the user's AWS Management Console session.

## Request Syntax
<a name="API_CreateTrustedIdentityPropagationApplicationForConsole_RequestSyntax"></a>

```
{
   "identityCenterInstanceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateTrustedIdentityPropagationApplicationForConsole_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [identityCenterInstanceArn](#API_CreateTrustedIdentityPropagationApplicationForConsole_RequestSyntax) **   <a name="signin-CreateTrustedIdentityPropagationApplicationForConsole-request-identityCenterInstanceArn"></a>
The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

## Response Syntax
<a name="API_CreateTrustedIdentityPropagationApplicationForConsole_ResponseSyntax"></a>

```
{
   "applicationArn": "string"
}
```

## Response Elements
<a name="API_CreateTrustedIdentityPropagationApplicationForConsole_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationArn](#API_CreateTrustedIdentityPropagationApplicationForConsole_ResponseSyntax) **   <a name="signin-CreateTrustedIdentityPropagationApplicationForConsole-response-applicationArn"></a>
Specifies the ARN of the newly created application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::[0-9]{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`

## Errors
<a name="API_CreateTrustedIdentityPropagationApplicationForConsole_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure with an internal server.
HTTP Status Code: 500

 ** SetupFailedException **
The request to set up an IAM Identity Center application that represents the AWS Management Console has failed due to one of the following:
+  `LIMIT_EXCEEDED` - Indicates that the principal has crossed the permitted number of resources that can be created.
+  `RESOURCE_NOT_FOUND` - Indicates that the ARN of an instance of IAM Identity Center is not found.
+  `APPLICATION_ALREADY_EXISTS` - Indicates that an IAM Identity Center application that represents the AWS Management Console already exists.
HTTP Status Code: 400

 ** ThrottlingException **
Indicates that the principal has crossed the throttling limits of the API operations.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
HTTP Status Code: 400

## See Also
<a name="API_CreateTrustedIdentityPropagationApplicationForConsole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signincontrolplane-2022-07-26/CreateTrustedIdentityPropagationApplicationForConsole)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signincontrolplane-2022-07-26/CreateTrustedIdentityPropagationApplicationForConsole)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/CreateTrustedIdentityPropagationApplicationForConsole)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signincontrolplane-2022-07-26/CreateTrustedIdentityPropagationApplicationForConsole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/CreateTrustedIdentityPropagationApplicationForConsole)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signincontrolplane-2022-07-26/CreateTrustedIdentityPropagationApplicationForConsole)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signincontrolplane-2022-07-26/CreateTrustedIdentityPropagationApplicationForConsole)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signincontrolplane-2022-07-26/CreateTrustedIdentityPropagationApplicationForConsole)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signincontrolplane-2022-07-26/CreateTrustedIdentityPropagationApplicationForConsole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/CreateTrustedIdentityPropagationApplicationForConsole)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Sign-In. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
