---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_SummaryMetricQuery.html
---

# SummaryMetricQuery
<a name="API_SummaryMetricQuery"></a>

The summary metric query object.

## Contents
<a name="API_SummaryMetricQuery_Contents"></a>

 ** AggregationPeriod **   <a name="iotwireless-Type-SummaryMetricQuery-AggregationPeriod"></a>
The aggregation period of the summary metric.
Type: String
Valid Values: `OneHour | OneDay | OneWeek`
Required: No

 ** Dimensions **   <a name="iotwireless-Type-SummaryMetricQuery-Dimensions"></a>
The dimensions of the summary metric.
Type: Array of [Dimension](API_Dimension.md) objects
Required: No

 ** EndTimestamp **   <a name="iotwireless-Type-SummaryMetricQuery-EndTimestamp"></a>
The end timestamp for the summary metric query.
Type: Timestamp
Required: No

 ** MetricName **   <a name="iotwireless-Type-SummaryMetricQuery-MetricName"></a>
The name of the metric.
Type: String
Length Constraints: Maximum length of 256.
Valid Values: `DeviceRSSI | DeviceSNR | DeviceRoamingRSSI | DeviceRoamingSNR | DeviceUplinkCount | DeviceDownlinkCount | DeviceUplinkLostCount | DeviceUplinkLostRate | DeviceJoinRequestCount | DeviceJoinAcceptCount | DeviceRoamingUplinkCount | DeviceRoamingDownlinkCount | GatewayUpTime | GatewayDownTime | GatewayRSSI | GatewaySNR | GatewayUplinkCount | GatewayDownlinkCount | GatewayJoinRequestCount | GatewayJoinAcceptCount | AwsAccountUplinkCount | AwsAccountDownlinkCount | AwsAccountUplinkLostCount | AwsAccountUplinkLostRate | AwsAccountJoinRequestCount | AwsAccountJoinAcceptCount | AwsAccountRoamingUplinkCount | AwsAccountRoamingDownlinkCount | AwsAccountDeviceCount | AwsAccountGatewayCount | AwsAccountActiveDeviceCount | AwsAccountActiveGatewayCount`
Required: No

 ** QueryId **   <a name="iotwireless-Type-SummaryMetricQuery-QueryId"></a>
The id of the summary metric query.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** StartTimestamp **   <a name="iotwireless-Type-SummaryMetricQuery-StartTimestamp"></a>
The start timestamp for the summary metric query.
Type: Timestamp
Required: No

## See Also
<a name="API_SummaryMetricQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/SummaryMetricQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/SummaryMetricQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/SummaryMetricQuery)
