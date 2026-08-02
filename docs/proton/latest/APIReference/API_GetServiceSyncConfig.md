---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_GetServiceSyncConfig.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# GetServiceSyncConfig
<a name="API_GetServiceSyncConfig"></a>

Get detailed information for the service sync configuration.

## Request Syntax
<a name="API_GetServiceSyncConfig_RequestSyntax"></a>

```
{
   "serviceName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetServiceSyncConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [serviceName](#API_GetServiceSyncConfig_RequestSyntax) **   <a name="proton-GetServiceSyncConfig-request-serviceName"></a>
The name of the service that you want to get the service sync configuration for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## Response Syntax
<a name="API_GetServiceSyncConfig_ResponseSyntax"></a>

```
{
   "serviceSyncConfig": {
      "branch": "string",
      "filePath": "string",
      "repositoryName": "string",
      "repositoryProvider": "string",
      "serviceName": "string"
   }
}
```

## Response Elements
<a name="API_GetServiceSyncConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceSyncConfig](#API_GetServiceSyncConfig_ResponseSyntax) **   <a name="proton-GetServiceSyncConfig-response-serviceSyncConfig"></a>
The detailed data of the requested service sync configuration.
Type: [ServiceSyncConfig](API_ServiceSyncConfig.md) object

## Errors
<a name="API_GetServiceSyncConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource *wasn't* found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_GetServiceSyncConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/GetServiceSyncConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/GetServiceSyncConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/GetServiceSyncConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/GetServiceSyncConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/GetServiceSyncConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/GetServiceSyncConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/GetServiceSyncConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/GetServiceSyncConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/GetServiceSyncConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/GetServiceSyncConfig)
