---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_ListTrustedIdentityPropagationApplicationsForConsole.html
---

# ListTrustedIdentityPropagationApplicationsForConsole
<a name="API_ListTrustedIdentityPropagationApplicationsForConsole"></a>

Lists an IAM Identity Center application that represents the AWS Management Console.

## Request Syntax
<a name="API_ListTrustedIdentityPropagationApplicationsForConsole_RequestSyntax"></a>

```
{
   "identityCenterInstanceArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTrustedIdentityPropagationApplicationsForConsole_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [identityCenterInstanceArn](#API_ListTrustedIdentityPropagationApplicationsForConsole_RequestSyntax) **   <a name="signin-ListTrustedIdentityPropagationApplicationsForConsole-request-identityCenterInstanceArn"></a>
The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

 ** [maxResults](#API_ListTrustedIdentityPropagationApplicationsForConsole_RequestSyntax) **   <a name="signin-ListTrustedIdentityPropagationApplicationsForConsole-request-maxResults"></a>
The maximum number of results to display for the instance.
Type: Integer
Valid Range: Fixed value of 1.
Required: No

 ** [nextToken](#API_ListTrustedIdentityPropagationApplicationsForConsole_RequestSyntax) **   <a name="signin-ListTrustedIdentityPropagationApplicationsForConsole-request-nextToken"></a>
Specifies that you want to receive the next page of results. Initially the value is null. Valid only if you received a `NextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `NextToken` response to request the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/_]*`
Required: No

## Response Syntax
<a name="API_ListTrustedIdentityPropagationApplicationsForConsole_ResponseSyntax"></a>

```
{
   "applicationArns": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListTrustedIdentityPropagationApplicationsForConsole_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationArns](#API_ListTrustedIdentityPropagationApplicationsForConsole_ResponseSyntax) **   <a name="signin-ListTrustedIdentityPropagationApplicationsForConsole-response-applicationArns"></a>
Specifies the ARNs for all of your IAM Identity Center applications that represent the AWS Management Console.
Type: Array of strings
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::[0-9]{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`

 ** [nextToken](#API_ListTrustedIdentityPropagationApplicationsForConsole_ResponseSyntax) **   <a name="signin-ListTrustedIdentityPropagationApplicationsForConsole-response-nextToken"></a>
If present, this value indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. This indicates that this is the last page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/_]*`

## Errors
<a name="API_ListTrustedIdentityPropagationApplicationsForConsole_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure with an internal server.
HTTP Status Code: 500

 ** ThrottlingException **
Indicates that the principal has crossed the throttling limits of the API operations.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
HTTP Status Code: 400

## See Also
<a name="API_ListTrustedIdentityPropagationApplicationsForConsole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signincontrolplane-2022-07-26/ListTrustedIdentityPropagationApplicationsForConsole)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signincontrolplane-2022-07-26/ListTrustedIdentityPropagationApplicationsForConsole)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/ListTrustedIdentityPropagationApplicationsForConsole)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signincontrolplane-2022-07-26/ListTrustedIdentityPropagationApplicationsForConsole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/ListTrustedIdentityPropagationApplicationsForConsole)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signincontrolplane-2022-07-26/ListTrustedIdentityPropagationApplicationsForConsole)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signincontrolplane-2022-07-26/ListTrustedIdentityPropagationApplicationsForConsole)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signincontrolplane-2022-07-26/ListTrustedIdentityPropagationApplicationsForConsole)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/signincontrolplane-2022-07-26/ListTrustedIdentityPropagationApplicationsForConsole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/ListTrustedIdentityPropagationApplicationsForConsole)
