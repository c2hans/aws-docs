---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetLicenseConfiguration.html
---

# GetLicenseConfiguration
<a name="API_GetLicenseConfiguration"></a>

Gets detailed information about the specified license configuration.

## Request Syntax
<a name="API_GetLicenseConfiguration_RequestSyntax"></a>

```
{
   "LicenseConfigurationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetLicenseConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LicenseConfigurationArn](#API_GetLicenseConfiguration_RequestSyntax) **   <a name="licensemanager-GetLicenseConfiguration-request-LicenseConfigurationArn"></a>
Amazon Resource Name (ARN) of the license configuration.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetLicenseConfiguration_ResponseSyntax"></a>

```
{
   "AutomatedDiscoveryInformation": {
      "LastRunTime": number
   },
   "ConsumedLicenses": number,
   "ConsumedLicenseSummaryList": [
      {
         "ConsumedLicenses": number,
         "ResourceType": "string"
      }
   ],
   "Description": "string",
   "DisassociateWhenNotFound": boolean,
   "LicenseConfigurationArn": "string",
   "LicenseConfigurationId": "string",
   "LicenseCount": number,
   "LicenseCountHardLimit": boolean,
   "LicenseCountingType": "string",
   "LicenseExpiry": number,
   "LicenseRules": [ "string" ],
   "ManagedResourceSummaryList": [
      {
         "AssociationCount": number,
         "ResourceType": "string"
      }
   ],
   "Name": "string",
   "OwnerAccountId": "string",
   "ProductInformationList": [
      {
         "ProductInformationFilterList": [
            {
               "ProductInformationFilterComparator": "string",
               "ProductInformationFilterName": "string",
               "ProductInformationFilterValue": [ "string" ]
            }
         ],
         "ResourceType": "string"
      }
   ],
   "Status": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetLicenseConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutomatedDiscoveryInformation](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-AutomatedDiscoveryInformation"></a>
Automated discovery information.
Type: [AutomatedDiscoveryInformation](API_AutomatedDiscoveryInformation.md) object

 ** [ConsumedLicenses](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-ConsumedLicenses"></a>
Number of licenses assigned to resources.
Type: Long

 ** [ConsumedLicenseSummaryList](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-ConsumedLicenseSummaryList"></a>
Summaries of the licenses consumed by resources.
Type: Array of [ConsumedLicenseSummary](API_ConsumedLicenseSummary.md) objects

 ** [Description](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-Description"></a>
Description of the license configuration.
Type: String

 ** [DisassociateWhenNotFound](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-DisassociateWhenNotFound"></a>
When true, disassociates a resource when software is uninstalled.
Type: Boolean

 ** [LicenseConfigurationArn](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-LicenseConfigurationArn"></a>
Amazon Resource Name (ARN) of the license configuration.
Type: String

 ** [LicenseConfigurationId](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-LicenseConfigurationId"></a>
Unique ID for the license configuration.
Type: String

 ** [LicenseCount](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-LicenseCount"></a>
Number of available licenses.
Type: Long

 ** [LicenseCountHardLimit](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-LicenseCountHardLimit"></a>
Sets the number of available licenses as a hard limit.
Type: Boolean

 ** [LicenseCountingType](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-LicenseCountingType"></a>
Dimension for which the licenses are counted.
Type: String
Valid Values: `vCPU | Instance | Core | Socket`

 ** [LicenseExpiry](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-LicenseExpiry"></a>
License Expiry.
Type: Long

 ** [LicenseRules](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-LicenseRules"></a>
License rules.
Type: Array of strings

 ** [ManagedResourceSummaryList](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-ManagedResourceSummaryList"></a>
Summaries of the managed resources.
Type: Array of [ManagedResourceSummary](API_ManagedResourceSummary.md) objects

 ** [Name](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-Name"></a>
Name of the license configuration.
Type: String

 ** [OwnerAccountId](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-OwnerAccountId"></a>
Account ID of the owner of the license configuration.
Type: String

 ** [ProductInformationList](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-ProductInformationList"></a>
Product information.
Type: Array of [ProductInformation](API_ProductInformation.md) objects

 ** [Status](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-Status"></a>
License configuration status.
Type: String

 ** [Tags](#API_GetLicenseConfiguration_ResponseSyntax) **   <a name="licensemanager-GetLicenseConfiguration-response-Tags"></a>
Tags for the license configuration.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_GetLicenseConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more parameter values are not valid.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## See Also
<a name="API_GetLicenseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/GetLicenseConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/GetLicenseConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/GetLicenseConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/GetLicenseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/GetLicenseConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/GetLicenseConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/GetLicenseConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/GetLicenseConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/GetLicenseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/GetLicenseConfiguration)
