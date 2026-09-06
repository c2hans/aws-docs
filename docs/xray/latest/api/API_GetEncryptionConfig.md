---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetEncryptionConfig.html
---

# GetEncryptionConfig
<a name="API_GetEncryptionConfig"></a>

Retrieves the current encryption configuration for X-Ray data.

## Request Syntax
<a name="API_GetEncryptionConfig_RequestSyntax"></a>

```
POST /EncryptionConfig HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEncryptionConfig_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetEncryptionConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEncryptionConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EncryptionConfig": {
      "KeyId": "string",
      "Status": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_GetEncryptionConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EncryptionConfig](#API_GetEncryptionConfig_ResponseSyntax) **   <a name="xray-GetEncryptionConfig-response-EncryptionConfig"></a>
The encryption configuration document.
Type: [EncryptionConfig](API_EncryptionConfig.md) object

## Errors
<a name="API_GetEncryptionConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetEncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetEncryptionConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetEncryptionConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetEncryptionConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetEncryptionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetEncryptionConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetEncryptionConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetEncryptionConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetEncryptionConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetEncryptionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetEncryptionConfig)
