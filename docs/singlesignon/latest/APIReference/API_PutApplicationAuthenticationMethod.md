---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationAuthenticationMethod.html
---

# PutApplicationAuthenticationMethod
<a name="API_PutApplicationAuthenticationMethod"></a>

Adds or updates an authentication method for an application.

## Request Syntax
<a name="API_PutApplicationAuthenticationMethod_RequestSyntax"></a>

```
{
   "ApplicationArn": "{{string}}",
   "AuthenticationMethod": { ... },
   "AuthenticationMethodType": "{{string}}"
}
```

## Request Parameters
<a name="API_PutApplicationAuthenticationMethod_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationArn](#API_PutApplicationAuthenticationMethod_RequestSyntax) **   <a name="singlesignon-PutApplicationAuthenticationMethod-request-ApplicationArn"></a>
Specifies the ARN of the application with the authentication method to add or update.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: Yes

 ** [AuthenticationMethod](#API_PutApplicationAuthenticationMethod_RequestSyntax) **   <a name="singlesignon-PutApplicationAuthenticationMethod-request-AuthenticationMethod"></a>
Specifies a structure that describes the authentication method to add or update. The structure type you provide is determined by the `AuthenticationMethodType` parameter.
Type: [AuthenticationMethod](API_AuthenticationMethod.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [AuthenticationMethodType](#API_PutApplicationAuthenticationMethod_RequestSyntax) **   <a name="singlesignon-PutApplicationAuthenticationMethod-request-AuthenticationMethodType"></a>
Specifies the type of the authentication method that you want to add or update.
Type: String
Valid Values: `IAM`
Required: Yes

## Response Elements
<a name="API_PutApplicationAuthenticationMethod_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutApplicationAuthenticationMethod_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Indicates that a requested resource is not found.
 ** Reason **
The reason for the resource not found exception.
HTTP Status Code: 400

 ** ThrottlingException **
Indicates that the principal has crossed the throttling limits of the API operations.
 ** Reason **
The reason for the throttling exception.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
 ** Reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_PutApplicationAuthenticationMethod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/PutApplicationAuthenticationMethod)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/PutApplicationAuthenticationMethod)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/PutApplicationAuthenticationMethod)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/PutApplicationAuthenticationMethod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/PutApplicationAuthenticationMethod)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/PutApplicationAuthenticationMethod)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/PutApplicationAuthenticationMethod)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/PutApplicationAuthenticationMethod)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/PutApplicationAuthenticationMethod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/PutApplicationAuthenticationMethod)
