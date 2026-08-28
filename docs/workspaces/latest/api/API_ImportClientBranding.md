---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ImportClientBranding.html
---

# ImportClientBranding
<a name="API_ImportClientBranding"></a>

Imports client branding. Client branding allows you to customize your WorkSpace's client login portal. You can tailor your login portal company logo, the support email address, support link, link to reset password, and a custom message for users trying to sign in.

After you import client branding, the default branding experience for the specified platform type is replaced with the imported experience

**Note**
You must specify at least one platform type when importing client branding.
You can import up to 6 MB of data with each request. If your request exceeds this limit, you can import client branding for different platform types using separate requests.
In each platform type, the `SupportEmail` and `SupportLink` parameters are mutually exclusive. You can specify only one parameter for each platform type, but not both.
Imported data can take up to a minute to appear in the WorkSpaces client.

## Request Syntax
<a name="API_ImportClientBranding_RequestSyntax"></a>

```
{
   "DeviceTypeAndroid": {
      "ForgotPasswordLink": "{{string}}",
      "LoginMessage": {
         "{{string}}" : "{{string}}"
      },
      "Logo": {{blob}},
      "SupportEmail": "{{string}}",
      "SupportLink": "{{string}}"
   },
   "DeviceTypeIos": {
      "ForgotPasswordLink": "{{string}}",
      "LoginMessage": {
         "{{string}}" : "{{string}}"
      },
      "Logo": {{blob}},
      "Logo2x": {{blob}},
      "Logo3x": {{blob}},
      "SupportEmail": "{{string}}",
      "SupportLink": "{{string}}"
   },
   "DeviceTypeLinux": {
      "ForgotPasswordLink": "{{string}}",
      "LoginMessage": {
         "{{string}}" : "{{string}}"
      },
      "Logo": {{blob}},
      "SupportEmail": "{{string}}",
      "SupportLink": "{{string}}"
   },
   "DeviceTypeOsx": {
      "ForgotPasswordLink": "{{string}}",
      "LoginMessage": {
         "{{string}}" : "{{string}}"
      },
      "Logo": {{blob}},
      "SupportEmail": "{{string}}",
      "SupportLink": "{{string}}"
   },
   "DeviceTypeWeb": {
      "ForgotPasswordLink": "{{string}}",
      "LoginMessage": {
         "{{string}}" : "{{string}}"
      },
      "Logo": {{blob}},
      "SupportEmail": "{{string}}",
      "SupportLink": "{{string}}"
   },
   "DeviceTypeWindows": {
      "ForgotPasswordLink": "{{string}}",
      "LoginMessage": {
         "{{string}}" : "{{string}}"
      },
      "Logo": {{blob}},
      "SupportEmail": "{{string}}",
      "SupportLink": "{{string}}"
   },
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_ImportClientBranding_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DeviceTypeAndroid](#API_ImportClientBranding_RequestSyntax) **   <a name="WorkSpaces-ImportClientBranding-request-DeviceTypeAndroid"></a>
The branding information to import for Android devices.
Type: [DefaultImportClientBrandingAttributes](API_DefaultImportClientBrandingAttributes.md) object
Required: No

 ** [DeviceTypeIos](#API_ImportClientBranding_RequestSyntax) **   <a name="WorkSpaces-ImportClientBranding-request-DeviceTypeIos"></a>
The branding information to import for iOS devices.
Type: [IosImportClientBrandingAttributes](API_IosImportClientBrandingAttributes.md) object
Required: No

 ** [DeviceTypeLinux](#API_ImportClientBranding_RequestSyntax) **   <a name="WorkSpaces-ImportClientBranding-request-DeviceTypeLinux"></a>
The branding information to import for Linux devices.
Type: [DefaultImportClientBrandingAttributes](API_DefaultImportClientBrandingAttributes.md) object
Required: No

 ** [DeviceTypeOsx](#API_ImportClientBranding_RequestSyntax) **   <a name="WorkSpaces-ImportClientBranding-request-DeviceTypeOsx"></a>
The branding information to import for macOS devices.
Type: [DefaultImportClientBrandingAttributes](API_DefaultImportClientBrandingAttributes.md) object
Required: No

 ** [DeviceTypeWeb](#API_ImportClientBranding_RequestSyntax) **   <a name="WorkSpaces-ImportClientBranding-request-DeviceTypeWeb"></a>
The branding information to import for web access.
Type: [DefaultImportClientBrandingAttributes](API_DefaultImportClientBrandingAttributes.md) object
Required: No

 ** [DeviceTypeWindows](#API_ImportClientBranding_RequestSyntax) **   <a name="WorkSpaces-ImportClientBranding-request-DeviceTypeWindows"></a>
The branding information to import for Windows devices.
Type: [DefaultImportClientBrandingAttributes](API_DefaultImportClientBrandingAttributes.md) object
Required: No

 ** [ResourceId](#API_ImportClientBranding_RequestSyntax) **   <a name="WorkSpaces-ImportClientBranding-request-ResourceId"></a>
The directory identifier of the WorkSpace for which you want to import client branding.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

## Response Syntax
<a name="API_ImportClientBranding_ResponseSyntax"></a>

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
<a name="API_ImportClientBranding_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeviceTypeAndroid](#API_ImportClientBranding_ResponseSyntax) **   <a name="WorkSpaces-ImportClientBranding-response-DeviceTypeAndroid"></a>
The branding information configured for Android devices.
Type: [DefaultClientBrandingAttributes](API_DefaultClientBrandingAttributes.md) object

 ** [DeviceTypeIos](#API_ImportClientBranding_ResponseSyntax) **   <a name="WorkSpaces-ImportClientBranding-response-DeviceTypeIos"></a>
The branding information configured for iOS devices.
Type: [IosClientBrandingAttributes](API_IosClientBrandingAttributes.md) object

 ** [DeviceTypeLinux](#API_ImportClientBranding_ResponseSyntax) **   <a name="WorkSpaces-ImportClientBranding-response-DeviceTypeLinux"></a>
The branding information configured for Linux devices.
Type: [DefaultClientBrandingAttributes](API_DefaultClientBrandingAttributes.md) object

 ** [DeviceTypeOsx](#API_ImportClientBranding_ResponseSyntax) **   <a name="WorkSpaces-ImportClientBranding-response-DeviceTypeOsx"></a>
The branding information configured for macOS devices.
Type: [DefaultClientBrandingAttributes](API_DefaultClientBrandingAttributes.md) object

 ** [DeviceTypeWeb](#API_ImportClientBranding_ResponseSyntax) **   <a name="WorkSpaces-ImportClientBranding-response-DeviceTypeWeb"></a>
The branding information configured for web access.
Type: [DefaultClientBrandingAttributes](API_DefaultClientBrandingAttributes.md) object

 ** [DeviceTypeWindows](#API_ImportClientBranding_ResponseSyntax) **   <a name="WorkSpaces-ImportClientBranding-response-DeviceTypeWindows"></a>
The branding information configured for Windows devices.
Type: [DefaultClientBrandingAttributes](API_DefaultClientBrandingAttributes.md) object

## Errors
<a name="API_ImportClientBranding_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceLimitExceededException **
Your resource limits have been exceeded.
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
<a name="API_ImportClientBranding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/ImportClientBranding)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/ImportClientBranding)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ImportClientBranding)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/ImportClientBranding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ImportClientBranding)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/ImportClientBranding)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/ImportClientBranding)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/ImportClientBranding)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/ImportClientBranding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ImportClientBranding)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
