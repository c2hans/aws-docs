---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_PutEncryptionConfig.html
---

# PutEncryptionConfig
<a name="API_PutEncryptionConfig"></a>

Updates the encryption configuration for X-Ray data.

## Request Syntax
<a name="API_PutEncryptionConfig_RequestSyntax"></a>

```
POST /PutEncryptionConfig HTTP/1.1
Content-type: application/json

{
   "KeyId": "{{string}}",
   "Type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutEncryptionConfig_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutEncryptionConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [KeyId](#API_PutEncryptionConfig_RequestSyntax) **   <a name="xray-PutEncryptionConfig-request-KeyId"></a>
An AWS KMS key in one of the following formats:
+  **Alias** - The name of the key. For example, `alias/MyKey`.
+  **Key ID** - The KMS key ID of the key. For example, `ae4aa6d49-a4d8-9df9-a475-4ff6d7898456`. AWS X-Ray does not support asymmetric KMS keys.
+  **ARN** - The full Amazon Resource Name of the key ID or alias. For example, `arn:aws:kms:us-east-2:123456789012:key/ae4aa6d49-a4d8-9df9-a475-4ff6d7898456`. Use this format to specify a key in a different account.
Omit this key if you set `Type` to `NONE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3000.
Required: No

 ** [Type](#API_PutEncryptionConfig_RequestSyntax) **   <a name="xray-PutEncryptionConfig-request-Type"></a>
The type of encryption. Set to `KMS` to use your own key for encryption. Set to `NONE` for default encryption.
Type: String
Valid Values: `NONE | KMS`
Required: Yes

## Response Syntax
<a name="API_PutEncryptionConfig_ResponseSyntax"></a>

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
<a name="API_PutEncryptionConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EncryptionConfig](#API_PutEncryptionConfig_ResponseSyntax) **   <a name="xray-PutEncryptionConfig-response-EncryptionConfig"></a>
The new encryption configuration.
Type: [EncryptionConfig](API_EncryptionConfig.md) object

## Errors
<a name="API_PutEncryptionConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_PutEncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/PutEncryptionConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/PutEncryptionConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/PutEncryptionConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/PutEncryptionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/PutEncryptionConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/PutEncryptionConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/PutEncryptionConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/PutEncryptionConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/PutEncryptionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/PutEncryptionConfig)
