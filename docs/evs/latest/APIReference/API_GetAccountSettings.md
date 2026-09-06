---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_GetAccountSettings.html
---

# GetAccountSettings
<a name="API_GetAccountSettings"></a>

Returns the configured EVS settings for your AWS account in the specified AWS Region. If no settings have been set, an empty list is returned.

## Response Syntax
<a name="API_GetAccountSettings_ResponseSyntax"></a>

```
{
   "settings": [
      {
         "name": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [settings](#API_GetAccountSettings_ResponseSyntax) **   <a name="evs-GetAccountSettings-response-settings"></a>
A list of regional account-level EVS settings for the account. EVS settings that have never been explicitly set are omitted from the response.
Type: Array of [AccountSetting](API_AccountSetting.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_GetAccountSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [InternalServerException](API_InternalServerException.md)
An internal server error occurred. Retry your request.
 ** message **
Describes the error encountered.
HTTP Status Code: 500

 [ThrottlingException](API_ThrottlingException.md)
The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.
 ** message **
Describes the error encountered.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 400

 [ValidationException](API_ValidationException.md)
The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.
 ** fieldList **
A list of fields that didn't validate.
 ** message **
Describes the error encountered.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_GetAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/GetAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/GetAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/GetAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/GetAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/GetAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/GetAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/GetAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/GetAccountSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/GetAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/GetAccountSettings)
