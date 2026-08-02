---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_DataSetImportConfig.html
---

# DataSetImportConfig
<a name="API_DataSetImportConfig"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Identifies one or more data sets you want to import with the [CreateDataSetImportTask](API_CreateDataSetImportTask.md) operation.

## Contents
<a name="API_DataSetImportConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** dataSets **   <a name="m2-Type-DataSetImportConfig-dataSets"></a>
The data sets.
Type: Array of [DataSetImportItem](API_DataSetImportItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** s3Location **   <a name="m2-Type-DataSetImportConfig-s3Location"></a>
The Amazon S3 location of the data sets.
Type: String
Pattern: `\S{1,2000}`
Required: No

## See Also
<a name="API_DataSetImportConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/DataSetImportConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/DataSetImportConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/DataSetImportConfig)
