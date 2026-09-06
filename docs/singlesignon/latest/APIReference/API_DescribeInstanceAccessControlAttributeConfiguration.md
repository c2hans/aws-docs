---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeInstanceAccessControlAttributeConfiguration.html
---

# DescribeInstanceAccessControlAttributeConfiguration
<a name="API_DescribeInstanceAccessControlAttributeConfiguration"></a>

Returns the list of IAM Identity Center identity store attributes that have been configured to work with attributes-based access control (ABAC) for the specified IAM Identity Center instance. This will not return attributes configured and sent by an external identity provider. For more information about ABAC, see [Attribute-Based Access Control](/singlesignon/latest/userguide/abac.html) in the *IAM Identity Center User Guide*.

## Request Syntax
<a name="API_DescribeInstanceAccessControlAttributeConfiguration_RequestSyntax"></a>

```
{
   "InstanceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInstanceAccessControlAttributeConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceArn](#API_DescribeInstanceAccessControlAttributeConfiguration_RequestSyntax) **   <a name="singlesignon-DescribeInstanceAccessControlAttributeConfiguration-request-InstanceArn"></a>
The ARN of the IAM Identity Center instance under which the operation will be executed.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

## Response Syntax
<a name="API_DescribeInstanceAccessControlAttributeConfiguration_ResponseSyntax"></a>

```
{
   "InstanceAccessControlAttributeConfiguration": {
      "AccessControlAttributes": [
         {
            "Key": "string",
            "Value": {
               "Source": [ "string" ]
            }
         }
      ]
   },
   "Status": "string",
   "StatusReason": "string"
}
```

## Response Elements
<a name="API_DescribeInstanceAccessControlAttributeConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceAccessControlAttributeConfiguration](#API_DescribeInstanceAccessControlAttributeConfiguration_ResponseSyntax) **   <a name="singlesignon-DescribeInstanceAccessControlAttributeConfiguration-response-InstanceAccessControlAttributeConfiguration"></a>
Gets the list of IAM Identity Center identity store attributes that have been added to your ABAC configuration.
Type: [InstanceAccessControlAttributeConfiguration](API_InstanceAccessControlAttributeConfiguration.md) object

 ** [Status](#API_DescribeInstanceAccessControlAttributeConfiguration_ResponseSyntax) **   <a name="singlesignon-DescribeInstanceAccessControlAttributeConfiguration-response-Status"></a>
The status of the attribute configuration process.
Type: String
Valid Values: `ENABLED | CREATION_IN_PROGRESS | CREATION_FAILED`

 ** [StatusReason](#API_DescribeInstanceAccessControlAttributeConfiguration_ResponseSyntax) **   <a name="singlesignon-DescribeInstanceAccessControlAttributeConfiguration-response-StatusReason"></a>
Provides more details about the current status of the specified attribute.
Type: String

## Errors
<a name="API_DescribeInstanceAccessControlAttributeConfiguration_Errors"></a>

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
<a name="API_DescribeInstanceAccessControlAttributeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/DescribeInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/DescribeInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/DescribeInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/DescribeInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/DescribeInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/DescribeInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/DescribeInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/DescribeInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/DescribeInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/DescribeInstanceAccessControlAttributeConfiguration)
