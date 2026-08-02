---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_PutDataCatalogEncryptionSettings.html
---

# PutDataCatalogEncryptionSettings
<a name="API_PutDataCatalogEncryptionSettings"></a>

Sets the security configuration for a specified catalog. After the configuration has been set, the specified encryption is applied to every catalog write thereafter.

## Request Syntax
<a name="API_PutDataCatalogEncryptionSettings_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DataCatalogEncryptionSettings": {
      "ConnectionPasswordEncryption": {
         "AwsKmsKeyId": "{{string}}",
         "ReturnConnectionPasswordEncrypted": {{boolean}}
      },
      "EncryptionAtRest": {
         "CatalogEncryptionMode": "{{string}}",
         "CatalogEncryptionServiceRole": "{{string}}",
         "SseAwsKmsKeyId": "{{string}}"
      }
   }
}
```

## Request Parameters
<a name="API_PutDataCatalogEncryptionSettings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_PutDataCatalogEncryptionSettings_RequestSyntax) **   <a name="Glue-PutDataCatalogEncryptionSettings-request-CatalogId"></a>
The ID of the Data Catalog to set the security configuration for. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DataCatalogEncryptionSettings](#API_PutDataCatalogEncryptionSettings_RequestSyntax) **   <a name="Glue-PutDataCatalogEncryptionSettings-request-DataCatalogEncryptionSettings"></a>
The security configuration to set.
Type: [DataCatalogEncryptionSettings](API_DataCatalogEncryptionSettings.md) object
Required: Yes

## Response Elements
<a name="API_PutDataCatalogEncryptionSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutDataCatalogEncryptionSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_PutDataCatalogEncryptionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/PutDataCatalogEncryptionSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/PutDataCatalogEncryptionSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/PutDataCatalogEncryptionSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/PutDataCatalogEncryptionSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/PutDataCatalogEncryptionSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/PutDataCatalogEncryptionSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/PutDataCatalogEncryptionSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/PutDataCatalogEncryptionSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/PutDataCatalogEncryptionSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/PutDataCatalogEncryptionSettings)
