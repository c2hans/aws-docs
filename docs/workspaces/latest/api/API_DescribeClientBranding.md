---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeClientBranding.html
---

# DescribeClientBranding
<a name="API_DescribeClientBranding"></a>

Describes the specified client branding. Client branding allows you to customize the log in page of various device types for your users. You can add your company logo, the support email address, support link, link to reset password, and a custom message for users trying to sign in.

**Note**
Only device types that have branding information configured will be shown in the response.

## Request Syntax
<a name="API_DescribeClientBranding_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeClientBranding_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ResourceId](#API_DescribeClientBranding_RequestSyntax) **   <a name="WorkSpaces-DescribeClientBranding-request-ResourceId"></a>
The directory identifier of the WorkSpace for which you want to view client branding information.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

## Response Syntax
<a name="API_DescribeClientBranding_ResponseSyntax"></a>

```
{
   "DeviceTypeAndroid": {
      "ForgotPasswordLink": "string",
      "LoginMessage": {
         "string" : "string"
      },
      "LogoUrl": "string",
      "SupportEmail": "string",
      "SupportLink": "string"
   },
   "DeviceTypeIos": {
      "ForgotPasswordLink": "string",
      "LoginMessage": {
         "string" : "string"
      },
      "Logo2xUrl": "string",
      "Logo3xUrl": "string",
      "LogoUrl": "string",
      "SupportEmail": "string",
      "SupportLink": "string"
   },
   "DeviceTypeLinux": {
      "ForgotPasswordLink": "string",
      "LoginMessage": {
         "string" : "string"
      },
      "LogoUrl": "string",
      "SupportEmail": "string",
      "SupportLink": "string"
   },
   "DeviceTypeOsx": {
      "ForgotPasswordLink": "string",
      "LoginMessage": {
         "string" : "string"
      },
      "LogoUrl": "string",
      "SupportEmail": "string",
      "SupportLink": "string"
   },
   "DeviceTypeWeb": {
      "ForgotPasswordLink": "string",
      "LoginMessage": {
         "string" : "string"
      },
      "LogoUrl": "string",
      "SupportEmail": "string",
      "SupportLink": "string"
   },
   "DeviceTypeWindows": {
      "ForgotPasswordLink": "string",
      "LoginMessage": {
         "string" : "string"
      },
      "LogoUrl": "string",
      "SupportEmail": "string",
      "SupportLink": "string"
   }
}
```

## Response Elements
<a name="API_DescribeClientBranding_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeviceTypeAndroid](#API_DescribeClientBranding_ResponseSyntax) **   <a name="WorkSpaces-DescribeClientBranding-response-DeviceTypeAndroid"></a>
The branding information for Android devices.
Type: [DefaultClientBrandingAttributes](API_DefaultClientBrandingAttributes.md) object

 ** [DeviceTypeIos](#API_DescribeClientBranding_ResponseSyntax) **   <a name="WorkSpaces-DescribeClientBranding-response-DeviceTypeIos"></a>
The branding information for iOS devices.
Type: [IosClientBrandingAttributes](API_IosClientBrandingAttributes.md) object

 ** [DeviceTypeLinux](#API_DescribeClientBranding_ResponseSyntax) **   <a name="WorkSpaces-DescribeClientBranding-response-DeviceTypeLinux"></a>
The branding information for Linux devices.
Type: [DefaultClientBrandingAttributes](API_DefaultClientBrandingAttributes.md) object

 ** [DeviceTypeOsx](#API_DescribeClientBranding_ResponseSyntax) **   <a name="WorkSpaces-DescribeClientBranding-response-DeviceTypeOsx"></a>
The branding information for macOS devices.
Type: [DefaultClientBrandingAttributes](API_DefaultClientBrandingAttributes.md) object

 ** [DeviceTypeWeb](#API_DescribeClientBranding_ResponseSyntax) **   <a name="WorkSpaces-DescribeClientBranding-response-DeviceTypeWeb"></a>
The branding information for Web access.
Type: [DefaultClientBrandingAttributes](API_DefaultClientBrandingAttributes.md) object

 ** [DeviceTypeWindows](#API_DescribeClientBranding_ResponseSyntax) **   <a name="WorkSpaces-DescribeClientBranding-response-DeviceTypeWindows"></a>
The branding information for Windows devices.
Type: [DefaultClientBrandingAttributes](API_DefaultClientBrandingAttributes.md) object

## Errors
<a name="API_DescribeClientBranding_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeClientBranding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeClientBranding)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeClientBranding)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeClientBranding)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeClientBranding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeClientBranding)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeClientBranding)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeClientBranding)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeClientBranding)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeClientBranding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeClientBranding)
