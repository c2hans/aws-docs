---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DatasetSource.html
---

# DatasetSource
<a name="API_DatasetSource"></a>

The data source for the dataset.

## Contents
<a name="API_DatasetSource_Contents"></a>

 ** sourceFormat **   <a name="iotsitewise-Type-DatasetSource-sourceFormat"></a>
The format of the dataset source associated with the dataset.
Type: String
Valid Values: `KNOWLEDGE_BASE | TIMESERIES`
Required: Yes

 ** sourceType **   <a name="iotsitewise-Type-DatasetSource-sourceType"></a>
The type of data source for the dataset.
Type: String
Valid Values: `KENDRA | SITEWISE`
Required: Yes

 ** sourceDetail **   <a name="iotsitewise-Type-DatasetSource-sourceDetail"></a>
The details of the dataset source associated with the dataset.
Type: [SourceDetail](API_SourceDetail.md) object
Required: No

## See Also
<a name="API_DatasetSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DatasetSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DatasetSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DatasetSource)
