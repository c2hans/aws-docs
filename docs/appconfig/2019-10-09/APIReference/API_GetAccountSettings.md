---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetAccountSettings.html
---

# GetAccountSettings
<a name="API_GetAccountSettings"></a>

Returns information about the status of the `DeletionProtection` parameter.

## Request Syntax
<a name="API_GetAccountSettings_RequestSyntax"></a>

```
GET /settings HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccountSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAccountSettings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccountSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DeletionProtection": {
      "Enabled": boolean,
      "ProtectionPeriodInMinutes": number
   },
   "VendedMetrics": {
      "Enabled": boolean
   }
}
```

## Response Elements
<a name="API_GetAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeletionProtection](#API_GetAccountSettings_ResponseSyntax) **   <a name="appconfig-GetAccountSettings-response-DeletionProtection"></a>
A parameter to configure deletion protection. Deletion protection prevents a user from deleting a configuration profile or an environment if AWS AppConfig has called either [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) or [GetConfiguration](API_GetConfiguration.md) for the configuration profile or from the environment during the specified interval. The default interval for `ProtectionPeriodInMinutes` is 60.
Type: [DeletionProtectionSettings](API_DeletionProtectionSettings.md) object

 ** [VendedMetrics](#API_GetAccountSettings_ResponseSyntax) **   <a name="appconfig-GetAccountSettings-response-VendedMetrics"></a>
The configuration for vended metrics in the account.
Type: [VendedMetricsSettings](API_VendedMetricsSettings.md) object

## Errors
<a name="API_GetAccountSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

## See Also
<a name="API_GetAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/GetAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/GetAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/GetAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/GetAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/GetAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/GetAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/GetAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/GetAccountSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/GetAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/GetAccountSettings)
