---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DatasetItem.html
---

# DatasetItem
<a name="API_DatasetItem"></a>

A dataset to process.

## Contents
<a name="API_DatasetItem_Contents"></a>

 ** datasetId **   <a name="iotsitewise-Type-DatasetItem-datasetId"></a>
The unique identifier for the dataset.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** exportDataTypes **   <a name="iotsitewise-Type-DatasetItem-exportDataTypes"></a>
The optional subset of data types to export. If omitted, all data types are exported.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `VIDEO | TELEMETRY | ANNOTATION`
Required: No

 ** trimSettings **   <a name="iotsitewise-Type-DatasetItem-trimSettings"></a>
The trim settings applied to all items in the dataset. When omitted, the full dataset time range is used.
Type: [TrimSettings](API_TrimSettings.md) object
Required: No

## See Also
<a name="API_DatasetItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DatasetItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DatasetItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DatasetItem)
