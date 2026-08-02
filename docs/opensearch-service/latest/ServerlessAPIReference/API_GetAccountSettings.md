---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetAccountSettings.html
---

# GetAccountSettings
<a name="API_GetAccountSettings"></a>

Returns account-level settings related to OpenSearch Serverless.

## Response Syntax
<a name="API_GetAccountSettings_ResponseSyntax"></a>

```
{
   "accountSettingsDetail": {
      "capacityLimits": {
         "maxIndexingCapacityInOCU": number,
         "maxSearchCapacityInOCU": number
      }
   }
}
```

## Response Elements
<a name="API_GetAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountSettingsDetail](#API_GetAccountSettings_ResponseSyntax) **   <a name="opensearchserverless-GetAccountSettings-response-accountSettingsDetail"></a>
OpenSearch Serverless-related details for the current account.
Type: [AccountSettingsDetail](API_AccountSettingsDetail.md) object

## Errors
<a name="API_GetAccountSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_GetAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/GetAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/GetAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/GetAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/GetAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/GetAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/GetAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/GetAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/GetAccountSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/GetAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/GetAccountSettings)
