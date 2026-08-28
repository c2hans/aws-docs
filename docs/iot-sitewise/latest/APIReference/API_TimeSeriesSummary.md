---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TimeSeriesSummary.html
---

# TimeSeriesSummary
<a name="API_TimeSeriesSummary"></a>

Contains a summary of a time series (data stream).

## Contents
<a name="API_TimeSeriesSummary_Contents"></a>

 ** dataType **   <a name="iotsitewise-Type-TimeSeriesSummary-dataType"></a>
The data type of the time series.
If you specify `STRUCT`, you must also specify `dataTypeSpec` to identify the type of the structure for this time series.
Type: String
Valid Values: `STRING | INTEGER | DOUBLE | BOOLEAN | STRUCT | VIDEO | ANNOTATION | JSON`
Required: Yes

 ** timeSeriesArn **   <a name="iotsitewise-Type-TimeSeriesSummary-timeSeriesArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the time series, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:time-series/${TimeSeriesId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: Yes

 ** timeSeriesCreationDate **   <a name="iotsitewise-Type-TimeSeriesSummary-timeSeriesCreationDate"></a>
The date that the time series was created, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** timeSeriesId **   <a name="iotsitewise-Type-TimeSeriesSummary-timeSeriesId"></a>
The ID of the time series.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 73.
Required: Yes

 ** timeSeriesLastUpdateDate **   <a name="iotsitewise-Type-TimeSeriesSummary-timeSeriesLastUpdateDate"></a>
The date that the time series was last updated, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** alias **   <a name="iotsitewise-Type-TimeSeriesSummary-alias"></a>
The alias that identifies the time series.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** assetId **   <a name="iotsitewise-Type-TimeSeriesSummary-assetId"></a>
The ID of the asset in which the asset property was created.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** dataTypeSpec **   <a name="iotsitewise-Type-TimeSeriesSummary-dataTypeSpec"></a>
The data type of the structure for this time series. This parameter is required for time series that have the `STRUCT` data type.
The options for this parameter depend on the type of the composite model in which you created the asset property that is associated with your time series. Use `AWS/ALARM_STATE` for alarm state in alarm composite models.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** propertyId **   <a name="iotsitewise-Type-TimeSeriesSummary-propertyId"></a>
The ID of the asset property, in UUID format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

## See Also
<a name="API_TimeSeriesSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/TimeSeriesSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/TimeSeriesSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/TimeSeriesSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
