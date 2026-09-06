---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateAccountSettings.html
---

# UpdateAccountSettings
<a name="API_UpdateAccountSettings"></a>

Updates the value of the `DeletionProtection` parameter.

## Request Syntax
<a name="API_UpdateAccountSettings_RequestSyntax"></a>

```
PATCH /settings HTTP/1.1
Content-type: application/json

{
   "DeletionProtection": {
      "Enabled": {{boolean}},
      "ProtectionPeriodInMinutes": {{number}}
   },
   "VendedMetrics": {
      "Enabled": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateAccountSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateAccountSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DeletionProtection](#API_UpdateAccountSettings_RequestSyntax) **   <a name="appconfig-UpdateAccountSettings-request-DeletionProtection"></a>
A parameter to configure deletion protection. Deletion protection prevents a user from deleting a configuration profile or an environment if AWS AppConfig has called either [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) or [GetConfiguration](API_GetConfiguration.md) for the configuration profile or from the environment during the specified interval. The default interval for `ProtectionPeriodInMinutes` is 60.
Type: [DeletionProtectionSettings](API_DeletionProtectionSettings.md) object
Required: No

 ** [VendedMetrics](#API_UpdateAccountSettings_RequestSyntax) **   <a name="appconfig-UpdateAccountSettings-request-VendedMetrics"></a>
The configuration for vended metrics in the account.
Type: [VendedMetricsSettings](API_VendedMetricsSettings.md) object
Required: No

## Response Syntax
<a name="API_UpdateAccountSettings_ResponseSyntax"></a>

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
<a name="API_UpdateAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeletionProtection](#API_UpdateAccountSettings_ResponseSyntax) **   <a name="appconfig-UpdateAccountSettings-response-DeletionProtection"></a>
A parameter to configure deletion protection. Deletion protection prevents a user from deleting a configuration profile or an environment if AWS AppConfig has called either [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) or [GetConfiguration](API_GetConfiguration.md) for the configuration profile or from the environment during the specified interval. The default interval for `ProtectionPeriodInMinutes` is 60.
Type: [DeletionProtectionSettings](API_DeletionProtectionSettings.md) object

 ** [VendedMetrics](#API_UpdateAccountSettings_ResponseSyntax) **   <a name="appconfig-UpdateAccountSettings-response-VendedMetrics"></a>
The configuration for vended metrics in the account.
Type: [VendedMetricsSettings](API_VendedMetricsSettings.md) object

## Errors
<a name="API_UpdateAccountSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

## Examples
<a name="API_UpdateAccountSettings_Examples"></a>

### Example
<a name="API_UpdateAccountSettings_Example_1"></a>

This example illustrates one usage of UpdateAccountSettings.

#### Sample Request
<a name="API_UpdateAccountSettings_Example_1_Request"></a>

```
PATCH /settings HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Type: application/json
User-Agent: aws-cli/2.17.58 md/awscrt#0.21.2 ua/2.0 os/windows#10 md/arch#amd64 lang/python#3.12.6 md/pyimpl#CPython cfg/retry-mode#standard md/installer#exe md/prompt#off md/command#appconfig.update-account-settings
X-Amz-Date: 20241001T190010Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20241001/us-east-1/appconfig/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 41

{"DeletionProtection": {"Enabled": true}}
```

#### Sample Response
<a name="API_UpdateAccountSettings_Example_1_Response"></a>

```
{
	"DeletionProtection": {
		"Enabled": true,
		"ProtectionPeriodInMinutes": 60
	}
}
```

## See Also
<a name="API_UpdateAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/UpdateAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/UpdateAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/UpdateAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/UpdateAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/UpdateAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/UpdateAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/UpdateAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/UpdateAccountSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/UpdateAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/UpdateAccountSettings)
