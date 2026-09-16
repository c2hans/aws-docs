---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteClientBranding.html
---

# DeleteClientBranding
<a name="API_DeleteClientBranding"></a>

Deletes customized client branding. Client branding allows you to customize your WorkSpace's client login portal. You can tailor your login portal company logo, the support email address, support link, link to reset password, and a custom message for users trying to sign in.

After you delete your customized client branding, your login portal reverts to the default client branding.

## Request Syntax
<a name="API_DeleteClientBranding_RequestSyntax"></a>

```
{
   "Platforms": [ "{{string}}" ],
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteClientBranding_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Platforms](#API_DeleteClientBranding_RequestSyntax) **   <a name="WorkSpaces-DeleteClientBranding-request-Platforms"></a>
The device type for which you want to delete client branding.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Valid Values: `DeviceTypeWindows | DeviceTypeOsx | DeviceTypeAndroid | DeviceTypeIos | DeviceTypeLinux | DeviceTypeWeb`
Required: Yes

 ** [ResourceId](#API_DeleteClientBranding_RequestSyntax) **   <a name="WorkSpaces-DeleteClientBranding-request-ResourceId"></a>
The directory identifier of the WorkSpace for which you want to delete client branding.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

## Response Elements
<a name="API_DeleteClientBranding_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteClientBranding_Errors"></a>

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
<a name="API_DeleteClientBranding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DeleteClientBranding)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DeleteClientBranding)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DeleteClientBranding)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DeleteClientBranding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DeleteClientBranding)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DeleteClientBranding)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DeleteClientBranding)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DeleteClientBranding)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DeleteClientBranding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DeleteClientBranding)
