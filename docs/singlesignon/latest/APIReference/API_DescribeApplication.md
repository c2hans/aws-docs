---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeApplication.html
---

# DescribeApplication
<a name="API_DescribeApplication"></a>

Retrieves the details of an application associated with an instance of IAM Identity Center.

## Request Syntax
<a name="API_DescribeApplication_RequestSyntax"></a>

```
{
   "ApplicationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationArn](#API_DescribeApplication_RequestSyntax) **   <a name="singlesignon-DescribeApplication-request-ApplicationArn"></a>
Specifies the ARN of the application. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: Yes

## Response Syntax
<a name="API_DescribeApplication_ResponseSyntax"></a>

```
{
   "ApplicationAccount": "string",
   "ApplicationArn": "string",
   "ApplicationProviderArn": "string",
   "CreatedDate": number,
   "CreatedFrom": "string",
   "Description": "string",
   "IdentityStoreArn": "string",
   "InstanceArn": "string",
   "Name": "string",
   "PortalOptions": {
      "SignInOptions": {
         "ApplicationUrl": "string",
         "Origin": "string"
      },
      "Visibility": "string"
   },
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribeApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationAccount](#API_DescribeApplication_ResponseSyntax) **   <a name="singlesignon-DescribeApplication-response-ApplicationAccount"></a>
The account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [ApplicationArn](#API_DescribeApplication_ResponseSyntax) **   <a name="singlesignon-DescribeApplication-response-ApplicationArn"></a>
Specifies the ARN of the application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`

 ** [ApplicationProviderArn](#API_DescribeApplication_ResponseSyntax) **   <a name="singlesignon-DescribeApplication-response-ApplicationProviderArn"></a>
The ARN of the application provider under which the operation will run.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::aws:applicationProvider/[a-zA-Z0-9-/]+`

 ** [CreatedDate](#API_DescribeApplication_ResponseSyntax) **   <a name="singlesignon-DescribeApplication-response-CreatedDate"></a>
The date the application was created.
Type: Timestamp

 ** [CreatedFrom](#API_DescribeApplication_ResponseSyntax) **   <a name="singlesignon-DescribeApplication-response-CreatedFrom"></a>
The AWS Region where the application was created in IAM Identity Center.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([a-z]+-){2,3}\d`

 ** [Description](#API_DescribeApplication_ResponseSyntax) **   <a name="singlesignon-DescribeApplication-response-Description"></a>
The description of the [Application](API_Application.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [IdentityStoreArn](#API_DescribeApplication_ResponseSyntax) **   <a name="singlesignon-DescribeApplication-response-IdentityStoreArn"></a>
The ARN of the identity store that is connected to the instance of IAM Identity Center.
Type: String

 ** [InstanceArn](#API_DescribeApplication_ResponseSyntax) **   <a name="singlesignon-DescribeApplication-response-InstanceArn"></a>
The ARN of the IAM Identity Center application under which the operation will run. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`

 ** [Name](#API_DescribeApplication_ResponseSyntax) **   <a name="singlesignon-DescribeApplication-response-Name"></a>
The application name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\S\s]*`

 ** [PortalOptions](#API_DescribeApplication_ResponseSyntax) **   <a name="singlesignon-DescribeApplication-response-PortalOptions"></a>
A structure that describes the options for the portal associated with an application.
Type: [PortalOptions](API_PortalOptions.md) object

 ** [Status](#API_DescribeApplication_ResponseSyntax) **   <a name="singlesignon-DescribeApplication-response-Status"></a>
Specifies whether the application is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_DescribeApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
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
<a name="API_DescribeApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/DescribeApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/DescribeApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/DescribeApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/DescribeApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/DescribeApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/DescribeApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/DescribeApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/DescribeApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/DescribeApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/DescribeApplication)
