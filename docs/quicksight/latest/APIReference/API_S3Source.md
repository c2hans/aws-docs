---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_S3Source.html
---

# S3Source
<a name="API_S3Source"></a>

A physical table type for an S3 data source.

## Contents
<a name="API_S3Source_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSourceArn **   <a name="QS-Type-S3Source-DataSourceArn"></a>
The Amazon Resource Name (ARN) for the data source.
Type: String
Required: Yes

 ** InputColumns **   <a name="QS-Type-S3Source-InputColumns"></a>
A physical table type for an S3 data source.
For files that aren't JSON, only `STRING` data types are supported in input columns.
Type: Array of [InputColumn](API_InputColumn.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2048 items.
Required: Yes

 ** UploadSettings **   <a name="QS-Type-S3Source-UploadSettings"></a>
Information about the format for the S3 source file or files.
Type: [UploadSettings](API_UploadSettings.md) object
Required: No

## See Also
<a name="API_S3Source_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/S3Source)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/S3Source)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/S3Source)
