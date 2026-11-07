---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetDataCatalogExportConfiguration.html
---

# GetDataCatalogExportConfiguration
<a name="API_GetDataCatalogExportConfiguration"></a>

Retrieves the current export configuration for the AWS Glue Data Catalog. The export configuration controls whether catalog metadata is exported to S3 Tables.

## Response Syntax
<a name="API_GetDataCatalogExportConfiguration_ResponseSyntax"></a>

```
{
   "CreatedAt": number,
   "EncryptionConfiguration": {
      "KmsKeyArn": "string",
      "SseAlgorithm": "string"
   },
   "ExportSetting": "string",
   "S3TableBucketArn": "string",
   "Status": "string",
   "UpdatedAt": number
}
```

## Response Elements
<a name="API_GetDataCatalogExportConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_GetDataCatalogExportConfiguration_ResponseSyntax) **   <a name="Glue-GetDataCatalogExportConfiguration-response-CreatedAt"></a>
The timestamp at which the export configuration was created.
Type: Timestamp

 ** [EncryptionConfiguration](#API_GetDataCatalogExportConfiguration_ResponseSyntax) **   <a name="Glue-GetDataCatalogExportConfiguration-response-EncryptionConfiguration"></a>
The encryption configuration for the exported data.
Type: [ExportEncryptionConfiguration](API_ExportEncryptionConfiguration.md) object

 ** [ExportSetting](#API_GetDataCatalogExportConfiguration_ResponseSyntax) **   <a name="Glue-GetDataCatalogExportConfiguration-response-ExportSetting"></a>
The export setting for the data catalog. Valid values are `ENABLED` and `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [S3TableBucketArn](#API_GetDataCatalogExportConfiguration_ResponseSyntax) **   <a name="Glue-GetDataCatalogExportConfiguration-response-S3TableBucketArn"></a>
The ARN of the S3 Tables bucket where catalog metadata is exported.
Type: String

 ** [Status](#API_GetDataCatalogExportConfiguration_ResponseSyntax) **   <a name="Glue-GetDataCatalogExportConfiguration-response-Status"></a>
The current status of the export. Valid values are `ENABLING`, `ENABLED`, `DISABLING`, `DISABLED`, and `FAILED`.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | FAILED`

 ** [UpdatedAt](#API_GetDataCatalogExportConfiguration_ResponseSyntax) **   <a name="Glue-GetDataCatalogExportConfiguration-response-UpdatedAt"></a>
The timestamp at which the export configuration was last updated.
Type: Timestamp

## Errors
<a name="API_GetDataCatalogExportConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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

 ** ThrottlingException **
The throttling threshhold was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetDataCatalogExportConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetDataCatalogExportConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetDataCatalogExportConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetDataCatalogExportConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetDataCatalogExportConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetDataCatalogExportConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetDataCatalogExportConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetDataCatalogExportConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetDataCatalogExportConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetDataCatalogExportConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetDataCatalogExportConfiguration)
