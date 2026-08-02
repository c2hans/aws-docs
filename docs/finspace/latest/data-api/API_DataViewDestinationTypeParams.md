---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_DataViewDestinationTypeParams.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# DataViewDestinationTypeParams
<a name="API_DataViewDestinationTypeParams"></a>

Structure for the Dataview destination type parameters.

## Contents
<a name="API_DataViewDestinationTypeParams_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** destinationType **   <a name="finspace-Type-DataViewDestinationTypeParams-destinationType"></a>
Destination type for a Dataview.
+  `GLUE_TABLE` – Glue table destination type.
+  `S3` – S3 destination type.
Type: String
Required: Yes

 ** s3DestinationExportFileFormat **   <a name="finspace-Type-DataViewDestinationTypeParams-s3DestinationExportFileFormat"></a>
Dataview export file format.
+  `PARQUET` – Parquet export file format.
+  `DELIMITED_TEXT` – Delimited text export file format.
Type: String
Valid Values: `PARQUET | DELIMITED_TEXT`
Required: No

 ** s3DestinationExportFileFormatOptions **   <a name="finspace-Type-DataViewDestinationTypeParams-s3DestinationExportFileFormatOptions"></a>
Format Options for S3 Destination type.
Here is an example of how you could specify the `s3DestinationExportFileFormatOptions`
 ` { "header": "true", "delimiter": ",", "compression": "gzip" }`
Type: String to string map
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]*\S[\s\S]*`
Value Length Constraints: Maximum length of 1000.
Value Pattern: `[\s\S]*\S[\s\S]*`
Required: No

## See Also
<a name="API_DataViewDestinationTypeParams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/DataViewDestinationTypeParams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/DataViewDestinationTypeParams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/DataViewDestinationTypeParams)
