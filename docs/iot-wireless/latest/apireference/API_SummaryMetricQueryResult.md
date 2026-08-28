---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_SummaryMetricQueryResult.html
---

# SummaryMetricQueryResult
<a name="API_SummaryMetricQueryResult"></a>

The result of the summary metrics aggregation operation.

## Contents
<a name="API_SummaryMetricQueryResult_Contents"></a>

 ** AggregationPeriod **   <a name="iotwireless-Type-SummaryMetricQueryResult-AggregationPeriod"></a>
The aggregation period of the metric.
Type: String
Valid Values: `OneHour | OneDay | OneWeek`
Required: No

 ** Dimensions **   <a name="iotwireless-Type-SummaryMetricQueryResult-Dimensions"></a>
The dimensions of the metric.
Type: Array of [Dimension](API_Dimension.md) objects
Required: No

 ** EndTimestamp **   <a name="iotwireless-Type-SummaryMetricQueryResult-EndTimestamp"></a>
The end timestamp for the summary metric query.
Type: Timestamp
Required: No

 ** Error **   <a name="iotwireless-Type-SummaryMetricQueryResult-Error"></a>
The error message for the summary metric query result.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** MetricName **   <a name="iotwireless-Type-SummaryMetricQueryResult-MetricName"></a>
The name of the summary metric query result.
Type: String
Length Constraints: Maximum length of 256.
Valid Values: `DeviceRSSI | DeviceSNR | DeviceRoamingRSSI | DeviceRoamingSNR | DeviceUplinkCount | DeviceDownlinkCount | DeviceUplinkLostCount | DeviceUplinkLostRate | DeviceJoinRequestCount | DeviceJoinAcceptCount | DeviceRoamingUplinkCount | DeviceRoamingDownlinkCount | GatewayUpTime | GatewayDownTime | GatewayRSSI | GatewaySNR | GatewayUplinkCount | GatewayDownlinkCount | GatewayJoinRequestCount | GatewayJoinAcceptCount | AwsAccountUplinkCount | AwsAccountDownlinkCount | AwsAccountUplinkLostCount | AwsAccountUplinkLostRate | AwsAccountJoinRequestCount | AwsAccountJoinAcceptCount | AwsAccountRoamingUplinkCount | AwsAccountRoamingDownlinkCount | AwsAccountDeviceCount | AwsAccountGatewayCount | AwsAccountActiveDeviceCount | AwsAccountActiveGatewayCount`
Required: No

 ** QueryId **   <a name="iotwireless-Type-SummaryMetricQueryResult-QueryId"></a>
The ID of the summary metric results query operation.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** QueryStatus **   <a name="iotwireless-Type-SummaryMetricQueryResult-QueryStatus"></a>
The status of the summary metric query result.
Type: String
Valid Values: `Succeeded | Failed`
Required: No

 ** StartTimestamp **   <a name="iotwireless-Type-SummaryMetricQueryResult-StartTimestamp"></a>
The start timestamp for the summary metric query.
Type: Timestamp
Required: No

 ** Timestamps **   <a name="iotwireless-Type-SummaryMetricQueryResult-Timestamps"></a>
The timestamp of each aggregation result.
Type: Array of timestamps
Required: No

 ** Unit **   <a name="iotwireless-Type-SummaryMetricQueryResult-Unit"></a>
The units of measurement to be used for interpreting the aggregation result.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** Values **   <a name="iotwireless-Type-SummaryMetricQueryResult-Values"></a>
The list of aggregated summary metric query results.
Type: Array of [MetricQueryValue](API_MetricQueryValue.md) objects
Required: No

## See Also
<a name="API_SummaryMetricQueryResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/SummaryMetricQueryResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/SummaryMetricQueryResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/SummaryMetricQueryResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
