---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateInstanceAccessControlAttributeConfiguration.html
---

# UpdateInstanceAccessControlAttributeConfiguration
<a name="API_UpdateInstanceAccessControlAttributeConfiguration"></a>

Updates the IAM Identity Center identity store attributes that you can use with the IAM Identity Center instance for attributes-based access control (ABAC). When using an external identity provider as an identity source, you can pass attributes through the SAML assertion as an alternative to configuring attributes from the IAM Identity Center identity store. If a SAML assertion passes any of these attributes, IAM Identity Center replaces the attribute value with the value from the IAM Identity Center identity store. For more information about ABAC, see [Attribute-Based Access Control](/singlesignon/latest/userguide/abac.html) in the *IAM Identity Center User Guide*.

## Request Syntax
<a name="API_UpdateInstanceAccessControlAttributeConfiguration_RequestSyntax"></a>

```
{
   "InstanceAccessControlAttributeConfiguration": {
      "AccessControlAttributes": [
         {
            "Key": "{{string}}",
            "Value": {
               "Source": [ "{{string}}" ]
            }
         }
      ]
   },
   "InstanceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateInstanceAccessControlAttributeConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceAccessControlAttributeConfiguration](#API_UpdateInstanceAccessControlAttributeConfiguration_RequestSyntax) **   <a name="singlesignon-UpdateInstanceAccessControlAttributeConfiguration-request-InstanceAccessControlAttributeConfiguration"></a>
Updates the attributes for your ABAC configuration.
Type: [InstanceAccessControlAttributeConfiguration](API_InstanceAccessControlAttributeConfiguration.md) object
Required: Yes

 ** [InstanceArn](#API_UpdateInstanceAccessControlAttributeConfiguration_RequestSyntax) **   <a name="singlesignon-UpdateInstanceAccessControlAttributeConfiguration-request-InstanceArn"></a>
The ARN of the IAM Identity Center instance under which the operation will be executed.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

## Response Elements
<a name="API_UpdateInstanceAccessControlAttributeConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateInstanceAccessControlAttributeConfiguration_Errors"></a>

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
<a name="API_UpdateInstanceAccessControlAttributeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/UpdateInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/UpdateInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/UpdateInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/UpdateInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/UpdateInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/UpdateInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/UpdateInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/UpdateInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/UpdateInstanceAccessControlAttributeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/UpdateInstanceAccessControlAttributeConfiguration)
