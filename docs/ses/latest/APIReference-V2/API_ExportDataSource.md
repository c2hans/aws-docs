---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ExportDataSource.html
---

# ExportDataSource
<a name="API_ExportDataSource"></a>

An object that contains details about the data source of the export job. It can only contain one of `MetricsDataSource` or `MessageInsightsDataSource` object.

## Contents
<a name="API_ExportDataSource_Contents"></a>

 ** MessageInsightsDataSource **   <a name="SES-Type-ExportDataSource-MessageInsightsDataSource"></a>
An object that contains filters applied when performing the Message Insights export.
Type: [MessageInsightsDataSource](API_MessageInsightsDataSource.md) object
Required: No

 ** MetricsDataSource **   <a name="SES-Type-ExportDataSource-MetricsDataSource"></a>
An object that contains details about the data source for the metrics export.
Type: [MetricsDataSource](API_MetricsDataSource.md) object
Required: No

## See Also
<a name="API_ExportDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ExportDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ExportDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ExportDataSource)
