---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateAccountSettings.html
---

# UpdateAccountSettings
<a name="API_UpdateAccountSettings"></a>

Update the OpenSearch Serverless settings for the current AWS account. For more information, see [Managing capacity limits for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-scaling.html).

## Request Syntax
<a name="API_UpdateAccountSettings_RequestSyntax"></a>

```
{
   "capacityLimits": {
      "maxIndexingCapacityInOCU": {{number}},
      "maxSearchCapacityInOCU": {{number}}
   }
}
```

## Request Parameters
<a name="API_UpdateAccountSettings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [capacityLimits](#API_UpdateAccountSettings_RequestSyntax) **   <a name="opensearchserverless-UpdateAccountSettings-request-capacityLimits"></a>
The maximum capacity limits for all OpenSearch Serverless collections, in OpenSearch Compute Units (OCUs). These limits are used to scale your collections based on the current workload. For more information, see [Managing capacity limits for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-scaling.html).
Type: [CapacityLimits](API_CapacityLimits.md) object
Required: No

## Response Syntax
<a name="API_UpdateAccountSettings_ResponseSyntax"></a>

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
<a name="API_UpdateAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountSettingsDetail](#API_UpdateAccountSettings_ResponseSyntax) **   <a name="opensearchserverless-UpdateAccountSettings-response-accountSettingsDetail"></a>
OpenSearch Serverless-related settings for the current AWS account.
Type: [AccountSettingsDetail](API_AccountSettingsDetail.md) object

## Errors
<a name="API_UpdateAccountSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Thrown when you attempt to create more resources than the service allows based on service quotas.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/UpdateAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/UpdateAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/UpdateAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/UpdateAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/UpdateAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/UpdateAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/UpdateAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/UpdateAccountSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/UpdateAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/UpdateAccountSettings)
