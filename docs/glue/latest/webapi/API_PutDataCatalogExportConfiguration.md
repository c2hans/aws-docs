---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_PutDataCatalogExportConfiguration.html
---

# PutDataCatalogExportConfiguration
<a name="API_PutDataCatalogExportConfiguration"></a>

Creates or updates the export configuration for the AWS Glue Data Catalog. Use this operation to enable or disable the export of catalog metadata to S3 Tables.

## Request Syntax
<a name="API_PutDataCatalogExportConfiguration_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "EncryptionConfiguration": {
      "KmsKeyArn": "{{string}}",
      "SseAlgorithm": "{{string}}"
   },
   "ExportSetting": "{{string}}"
}
```

## Request Parameters
<a name="API_PutDataCatalogExportConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_PutDataCatalogExportConfiguration_RequestSyntax) **   <a name="Glue-PutDataCatalogExportConfiguration-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [EncryptionConfiguration](#API_PutDataCatalogExportConfiguration_RequestSyntax) **   <a name="Glue-PutDataCatalogExportConfiguration-request-EncryptionConfiguration"></a>
The encryption configuration for the exported data. If not specified, the default encryption settings are used.
Type: [ExportEncryptionConfiguration](API_ExportEncryptionConfiguration.md) object
Required: No

 ** [ExportSetting](#API_PutDataCatalogExportConfiguration_RequestSyntax) **   <a name="Glue-PutDataCatalogExportConfiguration-request-ExportSetting"></a>
The export setting for the data catalog. Specify `ENABLED` to start exporting catalog metadata to S3 Tables, or `DISABLED` to stop exporting. This field is required.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## Response Syntax
<a name="API_PutDataCatalogExportConfiguration_ResponseSyntax"></a>

```
{
   "EncryptionConfiguration": {
      "KmsKeyArn": "string",
      "SseAlgorithm": "string"
   },
   "ExportSetting": "string"
}
```

## Response Elements
<a name="API_PutDataCatalogExportConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EncryptionConfiguration](#API_PutDataCatalogExportConfiguration_ResponseSyntax) **   <a name="Glue-PutDataCatalogExportConfiguration-response-EncryptionConfiguration"></a>
The encryption configuration for the exported data.
Type: [ExportEncryptionConfiguration](API_ExportEncryptionConfiguration.md) object

 ** [ExportSetting](#API_PutDataCatalogExportConfiguration_ResponseSyntax) **   <a name="Glue-PutDataCatalogExportConfiguration-response-ExportSetting"></a>
The export setting for the data catalog.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_PutDataCatalogExportConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConflictException **
The `CreatePartitions` API was called on a table that has indexes enabled.
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
<a name="API_PutDataCatalogExportConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/PutDataCatalogExportConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/PutDataCatalogExportConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/PutDataCatalogExportConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/PutDataCatalogExportConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/PutDataCatalogExportConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/PutDataCatalogExportConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/PutDataCatalogExportConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/PutDataCatalogExportConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/PutDataCatalogExportConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/PutDataCatalogExportConfiguration)
