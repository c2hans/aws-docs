---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetServiceSettings.html
---

# GetServiceSettings
<a name="API_GetServiceSettings"></a>

Gets the License Manager settings for the current Region.

## Response Syntax
<a name="API_GetServiceSettings_ResponseSyntax"></a>

```
{
   "CrossRegionDiscoveryHomeRegion": "string",
   "CrossRegionDiscoverySourceRegions": [ "string" ],
   "EnableCrossAccountsDiscovery": boolean,
   "LicenseManagerResourceShareArn": "string",
   "OrganizationConfiguration": {
      "EnableIntegration": boolean
   },
   "S3BucketArn": "string",
   "ServiceStatus": {
      "CrossAccountDiscovery": {
         "Message": "string"
      },
      "CrossRegionDiscovery": {
         "Message": {
            "string" : {
               "Status": "string"
            }
         }
      }
   },
   "SnsTopicArn": "string"
}
```

## Response Elements
<a name="API_GetServiceSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CrossRegionDiscoveryHomeRegion](#API_GetServiceSettings_ResponseSyntax) **   <a name="licensemanager-GetServiceSettings-response-CrossRegionDiscoveryHomeRegion"></a>
Cross region discovery home region.
Type: String

 ** [CrossRegionDiscoverySourceRegions](#API_GetServiceSettings_ResponseSyntax) **   <a name="licensemanager-GetServiceSettings-response-CrossRegionDiscoverySourceRegions"></a>
Cross region discovery source regions.
Type: Array of strings

 ** [EnableCrossAccountsDiscovery](#API_GetServiceSettings_ResponseSyntax) **   <a name="licensemanager-GetServiceSettings-response-EnableCrossAccountsDiscovery"></a>
Indicates whether cross-account discovery is enabled.
Type: Boolean

 ** [LicenseManagerResourceShareArn](#API_GetServiceSettings_ResponseSyntax) **   <a name="licensemanager-GetServiceSettings-response-LicenseManagerResourceShareArn"></a>
Amazon Resource Name (ARN) of the resource share. The License Manager management account provides member accounts with access to this share.
Type: String

 ** [OrganizationConfiguration](#API_GetServiceSettings_ResponseSyntax) **   <a name="licensemanager-GetServiceSettings-response-OrganizationConfiguration"></a>
Indicates whether AWS Organizations is integrated with License Manager for cross-account discovery.
Type: [OrganizationConfiguration](API_OrganizationConfiguration.md) object

 ** [S3BucketArn](#API_GetServiceSettings_ResponseSyntax) **   <a name="licensemanager-GetServiceSettings-response-S3BucketArn"></a>
Regional S3 bucket path for storing reports, license trail event data, discovery data, and so on.
Type: String

 ** [ServiceStatus](#API_GetServiceSettings_ResponseSyntax) **   <a name="licensemanager-GetServiceSettings-response-ServiceStatus"></a>
Service status.
Type: [ServiceStatus](API_ServiceStatus.md) object

 ** [SnsTopicArn](#API_GetServiceSettings_ResponseSyntax) **   <a name="licensemanager-GetServiceSettings-response-SnsTopicArn"></a>
SNS topic configured to receive notifications from License Manager.
Type: String

## Errors
<a name="API_GetServiceSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## See Also
<a name="API_GetServiceSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/GetServiceSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/GetServiceSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/GetServiceSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/GetServiceSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/GetServiceSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/GetServiceSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/GetServiceSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/GetServiceSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/GetServiceSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/GetServiceSettings)
