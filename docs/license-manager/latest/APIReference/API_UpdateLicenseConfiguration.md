---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_UpdateLicenseConfiguration.html
---

# UpdateLicenseConfiguration
<a name="API_UpdateLicenseConfiguration"></a>

Modifies the attributes of an existing license configuration.

## Request Syntax
<a name="API_UpdateLicenseConfiguration_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "DisassociateWhenNotFound": {{boolean}},
   "LicenseConfigurationArn": "{{string}}",
   "LicenseConfigurationStatus": "{{string}}",
   "LicenseCount": {{number}},
   "LicenseCountHardLimit": {{boolean}},
   "LicenseExpiry": {{number}},
   "LicenseRules": [ "{{string}}" ],
   "Name": "{{string}}",
   "ProductInformationList": [
      {
         "ProductInformationFilterList": [
            {
               "ProductInformationFilterComparator": "{{string}}",
               "ProductInformationFilterName": "{{string}}",
               "ProductInformationFilterValue": [ "{{string}}" ]
            }
         ],
         "ResourceType": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateLicenseConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-UpdateLicenseConfiguration-request-Description"></a>
New description of the license configuration.
Type: String
Required: No

 ** [DisassociateWhenNotFound](#API_UpdateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-UpdateLicenseConfiguration-request-DisassociateWhenNotFound"></a>
When true, disassociates a resource when software is uninstalled.
Type: Boolean
Required: No

 ** [LicenseConfigurationArn](#API_UpdateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-UpdateLicenseConfiguration-request-LicenseConfigurationArn"></a>
Amazon Resource Name (ARN) of the license configuration.
Type: String
Required: Yes

 ** [LicenseConfigurationStatus](#API_UpdateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-UpdateLicenseConfiguration-request-LicenseConfigurationStatus"></a>
New status of the license configuration.
Type: String
Valid Values: `AVAILABLE | DISABLED`
Required: No

 ** [LicenseCount](#API_UpdateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-UpdateLicenseConfiguration-request-LicenseCount"></a>
New number of licenses managed by the license configuration.
Type: Long
Required: No

 ** [LicenseCountHardLimit](#API_UpdateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-UpdateLicenseConfiguration-request-LicenseCountHardLimit"></a>
New hard limit of the number of available licenses.
Type: Boolean
Required: No

 ** [LicenseExpiry](#API_UpdateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-UpdateLicenseConfiguration-request-LicenseExpiry"></a>
License configuration expiry time.
Type: Long
Required: No

 ** [LicenseRules](#API_UpdateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-UpdateLicenseConfiguration-request-LicenseRules"></a>
New license rule. The only rule that you can add after you create a license configuration is licenseAffinityToHost.
Type: Array of strings
Required: No

 ** [Name](#API_UpdateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-UpdateLicenseConfiguration-request-Name"></a>
New name of the license configuration.
Type: String
Required: No

 ** [ProductInformationList](#API_UpdateLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-UpdateLicenseConfiguration-request-ProductInformationList"></a>
New product information.
Type: Array of [ProductInformation](API_ProductInformation.md) objects
Required: No

## Response Elements
<a name="API_UpdateLicenseConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLicenseConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** ConflictException **
There was a conflict processing the request. Try your request again.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more parameter values are not valid.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** ResourceLimitExceededException **
Your resource limits have been exceeded.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## See Also
<a name="API_UpdateLicenseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/UpdateLicenseConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/UpdateLicenseConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/UpdateLicenseConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/UpdateLicenseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/UpdateLicenseConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/UpdateLicenseConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/UpdateLicenseConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/UpdateLicenseConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/UpdateLicenseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/UpdateLicenseConfiguration)
