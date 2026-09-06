---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateApplication.html
---

# UpdateApplication
<a name="API_UpdateApplication"></a>

Updates application properties.

## Request Syntax
<a name="API_UpdateApplication_RequestSyntax"></a>

```
{
   "ApplicationArn": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "PortalOptions": {
      "SignInOptions": {
         "ApplicationUrl": "{{string}}",
         "Origin": "{{string}}"
      }
   },
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationArn](#API_UpdateApplication_RequestSyntax) **   <a name="singlesignon-UpdateApplication-request-ApplicationArn"></a>
Specifies the ARN of the application. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: Yes

 ** [Description](#API_UpdateApplication_RequestSyntax) **   <a name="singlesignon-UpdateApplication-request-Description"></a>
The description of the [Application](API_Application.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Name](#API_UpdateApplication_RequestSyntax) **   <a name="singlesignon-UpdateApplication-request-Name"></a>
Specifies the updated name for the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\S\s]*`
Required: No

 ** [PortalOptions](#API_UpdateApplication_RequestSyntax) **   <a name="singlesignon-UpdateApplication-request-PortalOptions"></a>
A structure that describes the options for the portal associated with an application.
Type: [UpdateApplicationPortalOptions](API_UpdateApplicationPortalOptions.md) object
Required: No

 ** [Status](#API_UpdateApplication_RequestSyntax) **   <a name="singlesignon-UpdateApplication-request-Status"></a>
Specifies whether the application is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## Response Elements
<a name="API_UpdateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateApplication_Errors"></a>

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
<a name="API_UpdateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/UpdateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/UpdateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/UpdateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/UpdateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/UpdateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/UpdateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/UpdateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/UpdateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/UpdateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/UpdateApplication)
