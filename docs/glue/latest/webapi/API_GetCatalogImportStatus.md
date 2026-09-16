---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetCatalogImportStatus.html
---

# GetCatalogImportStatus
<a name="API_GetCatalogImportStatus"></a>

Retrieves the status of a migration operation.

## Request Syntax
<a name="API_GetCatalogImportStatus_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCatalogImportStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetCatalogImportStatus_RequestSyntax) **   <a name="Glue-GetCatalogImportStatus-request-CatalogId"></a>
The ID of the catalog to migrate. Currently, this should be the AWS account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## Response Syntax
<a name="API_GetCatalogImportStatus_ResponseSyntax"></a>

```
{
   "ImportStatus": {
      "ImportCompleted": boolean,
      "ImportedBy": "string",
      "ImportTime": number
   }
}
```

## Response Elements
<a name="API_GetCatalogImportStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImportStatus](#API_GetCatalogImportStatus_ResponseSyntax) **   <a name="Glue-GetCatalogImportStatus-response-ImportStatus"></a>
The status of the specified catalog migration.
Type: [CatalogImportStatus](API_CatalogImportStatus.md) object

## Errors
<a name="API_GetCatalogImportStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetCatalogImportStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetCatalogImportStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetCatalogImportStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetCatalogImportStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetCatalogImportStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetCatalogImportStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetCatalogImportStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetCatalogImportStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetCatalogImportStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetCatalogImportStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetCatalogImportStatus)
