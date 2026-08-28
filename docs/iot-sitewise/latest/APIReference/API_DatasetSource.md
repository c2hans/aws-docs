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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
