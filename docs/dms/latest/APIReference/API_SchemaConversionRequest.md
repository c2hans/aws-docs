---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_SchemaConversionRequest.html
---

# SchemaConversionRequest
<a name="API_SchemaConversionRequest"></a>

Provides information about a schema conversion action.

## Contents
<a name="API_SchemaConversionRequest_Contents"></a>

 ** Error **   <a name="DMS-Type-SchemaConversionRequest-Error"></a>
Provides error information about a project.
Type: [ErrorDetails](API_ErrorDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** ExportSqlDetails **   <a name="DMS-Type-SchemaConversionRequest-ExportSqlDetails"></a>
The Amazon S3 location of the ZIP archive that contains the exported data definition language (DDL) scripts.
 AWS DMS populates this field only for the `DescribeMetadataModelExportsAsScript` operation.
Type: [ExportSqlDetails](API_ExportSqlDetails.md) object
Required: No

 ** MigrationProjectArn **   <a name="DMS-Type-SchemaConversionRequest-MigrationProjectArn"></a>
The migration project ARN.
Type: String
Required: No

 ** Progress **   <a name="DMS-Type-SchemaConversionRequest-Progress"></a>
Provides information about the progress of the schema conversion operation.
Type: [Progress](API_Progress.md) object
Required: No

 ** RequestIdentifier **   <a name="DMS-Type-SchemaConversionRequest-RequestIdentifier"></a>
The identifier for the schema conversion action.
Type: String
Required: No

 ** Status **   <a name="DMS-Type-SchemaConversionRequest-Status"></a>
The schema conversion operation status. Possible values:
+  `RECEIVED` – The operation is received but not yet queued for processing.
+  `IN_PROGRESS` – The operation is queued or actively running.
+  `SUCCESS` – The operation completed successfully.
+  `FAILED` – The operation did not complete.
+  `CANCELING` – The operation is being canceled. The operation might still succeed or fail before cancellation takes effect.
+  `CANCELED` – The operation was canceled before completion.
Type: String
Required: No

## See Also
<a name="API_SchemaConversionRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/SchemaConversionRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/SchemaConversionRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/SchemaConversionRequest)
