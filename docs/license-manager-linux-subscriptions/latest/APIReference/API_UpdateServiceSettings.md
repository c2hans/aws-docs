---
source_url: https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_UpdateServiceSettings.html
---

# UpdateServiceSettings
<a name="API_UpdateServiceSettings"></a>

Updates the service settings for Linux subscriptions.

## Request Syntax
<a name="API_UpdateServiceSettings_RequestSyntax"></a>

```
POST /subscription/UpdateServiceSettings HTTP/1.1
Content-type: application/json

{
   "AllowUpdate": {{boolean}},
   "LinuxSubscriptionsDiscovery": "{{string}}",
   "LinuxSubscriptionsDiscoverySettings": {
      "OrganizationIntegration": "{{string}}",
      "SourceRegions": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_UpdateServiceSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateServiceSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AllowUpdate](#API_UpdateServiceSettings_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-UpdateServiceSettings-request-AllowUpdate"></a>
Describes if updates are allowed to the service settings for Linux subscriptions. If you allow updates, you can aggregate Linux subscription data in more than one home Region.
Type: Boolean
Required: No

 ** [LinuxSubscriptionsDiscovery](#API_UpdateServiceSettings_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-UpdateServiceSettings-request-LinuxSubscriptionsDiscovery"></a>
Describes if the discovery of Linux subscriptions is enabled.
Type: String
Valid Values: `Enabled | Disabled`
Required: Yes

 ** [LinuxSubscriptionsDiscoverySettings](#API_UpdateServiceSettings_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-UpdateServiceSettings-request-LinuxSubscriptionsDiscoverySettings"></a>
The settings defined for Linux subscriptions discovery. The settings include if AWS Organizations integration has been enabled, and which Regions data will be aggregated from.
Type: [LinuxSubscriptionsDiscoverySettings](API_LinuxSubscriptionsDiscoverySettings.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateServiceSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "HomeRegions": [ "string" ],
   "LinuxSubscriptionsDiscovery": "string",
   "LinuxSubscriptionsDiscoverySettings": {
      "OrganizationIntegration": "string",
      "SourceRegions": [ "string" ]
   },
   "Status": "string",
   "StatusMessage": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_UpdateServiceSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HomeRegions](#API_UpdateServiceSettings_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-UpdateServiceSettings-response-HomeRegions"></a>
The Region in which License Manager displays the aggregated data for Linux subscriptions.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [LinuxSubscriptionsDiscovery](#API_UpdateServiceSettings_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-UpdateServiceSettings-response-LinuxSubscriptionsDiscovery"></a>
Lists if discovery has been enabled for Linux subscriptions.
Type: String
Valid Values: `Enabled | Disabled`

 ** [LinuxSubscriptionsDiscoverySettings](#API_UpdateServiceSettings_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-UpdateServiceSettings-response-LinuxSubscriptionsDiscoverySettings"></a>
The settings defined for Linux subscriptions discovery. The settings include if AWS Organizations integration has been enabled, and which Regions data will be aggregated from.
Type: [LinuxSubscriptionsDiscoverySettings](API_LinuxSubscriptionsDiscoverySettings.md) object

 ** [Status](#API_UpdateServiceSettings_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-UpdateServiceSettings-response-Status"></a>
Indicates the status of Linux subscriptions settings being applied.
Type: String
Valid Values: `InProgress | Completed | Successful | Failed`

 ** [StatusMessage](#API_UpdateServiceSettings_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-UpdateServiceSettings-response-StatusMessage"></a>
A message which details the Linux subscriptions service settings current status.
Type: String to string map

## Errors
<a name="API_UpdateServiceSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An exception occurred with the service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_UpdateServiceSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-linux-subscriptions-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-linux-subscriptions-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-linux-subscriptions-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-linux-subscriptions-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-linux-subscriptions-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-linux-subscriptions-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-linux-subscriptions-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-linux-subscriptions-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-linux-subscriptions-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-linux-subscriptions-2018-05-10/UpdateServiceSettings)
