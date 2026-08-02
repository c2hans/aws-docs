---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html
---

# Monitoring AWS Elemental MediaPackage with Amazon CloudWatch metrics
<a name="monitoring-cloudwatch"></a>

You can monitor MediaPackage using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

------
#### [ MediaPackage console ]

MediaPackage displays metrics throughout the console.

**To view metrics using the MediaPackage console**

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/).

1. Navigate to the appropriate page to view metrics:
   + For metrics on all channel groups, go to the **Channel groups** page.
   + For metrics on all channels and origin endpoints associated with your channel group in the AWS Region, go to the channel group's details page.
   + For metrics on a specific channel and all of its origin endpoints, go to the channel's details page.
   + For metrics on a specific origin endpoint, go to the origin endpoint's details page.

1. (Optional) To refine the metrics view, choose **Open in CloudWatch**.

------
#### [ CloudWatch console ]

Metrics are grouped first by the service namespace, and then by the various dimension combinations within each namespace.

**To view metrics using the CloudWatch console**

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. Under **All metrics**, choose the **AWS/MediaPackage** namespace.

1. Choose the metric dimension to view the metrics (for example, choose `channel` to view metrics per channel).

------
#### [ AWS CLI ]

**To view metrics using the AWS CLI**

At a command prompt, enter the following command:
+

  ```
  aws cloudwatch list-metrics --namespace "AWS/MediaPackage"
  ```

------

## MediaPackage live content metrics
<a name="metrics"></a>

The `AWS/MediaPackage` namespace includes the following metrics for live content. MediaPackage publishes metrics to CloudWatch every minute, if not sooner.

| Metric | Description |
| --- | --- |
| ChannelMQCS | Segment-level quality score as calculated by MediaPackage for the active input to this channel.Units: Numeric<br />Valid statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html)<br />Valid dimensions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
| ChannelMQCSSequence | Aggregated quality score for all segments in the sequence for the active input to this channel, as calculated by MediaPackage.Units: Numeric<br />Valid statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html)<br />Valid dimensions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
| EgressBytes | Number of bytes that MediaPackage successfully sends for each request. If MediaPackage doesn't receive any requests for output in the specified interval, then no data is given.<br />Units: Bytes<br />Valid statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html)<br />Valid dimensions: [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
|  EgressRequestCount  | Number of content requests that MediaPackage receives. If MediaPackage doesn't receive any requests for output in the specified interval, then no data is given.<br />Units: Count<br />Valid statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html)<br />Valid dimensions: [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
|  EgressResponseTime  | The time that it takes MediaPackage to process each output request. If MediaPackage doesn't receive any requests for output in the specified interval, then no data is given.<br />Units: Milliseconds<br />Valid statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html)<br />Valid dimensions: [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
|  IngressBytes  | Number of bytes of content that MediaPackage receives for each input request. If MediaPackage doesn't receive any requests for input in the specified interval, then no data is given.<br />Units: Bytes<br />Valid statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html)<br />Valid dimensions: [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
| IngressMQCS | Segment-level quality score as communicated by AWS Elemental MediaLive for this input.Units: Numeric<br />Valid statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html)<br />Valid dimensions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
| IngressMQCSSequence | Aggregated quality scores for all segments in the sequence, as communicated by AWS Elemental MediaLive.Units: Numeric<br />Valid statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html)<br />Valid dimensions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
|  IngressRequestCount  | Number of input requests that MediaPackage receives. If MediaPackage doesn't receive any requests for input in the specified interval, then no data is given.<br />Units: Count<br />Valid statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html)<br />Valid dimensions: [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
|  IngressResponseTime  | The time that it takes MediaPackage to process each input request. If MediaPackage doesn't receive any requests for input in the specified interval, then no data is given.<br />Units: Milliseconds<br />Valid statistics:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html)<br />Valid dimensions: [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |

## MediaPackage live dimensions
<a name="dimensions"></a>

You can filter the `AWS/MediaPackage` data using the following dimensions.

| Dimension | Description |
| --- | --- |
| No Dimension | Metrics are aggregated and shown for all channels, endpoints, or status codes. |
| `CDNAuthorizationStatus` | Value: `Authorized` or `Unauthorized`<br />Can be used in combination with `ChannelGroup`, `Channel`, `OriginEndpoint`, and `CDNAuthorizationStatusDetails` to show metrics for the CDN authorization requests to the specified endpoint. |
| `CDNAuthorizationStatusDetails` | Value when `CDNAuthorizationStatus` is `Authorized`: `HeaderSecretMatched`<br />Value when `CDNAuthorizationStatus` is `Unauthorized`: `HeaderSecretMismatched`, `MissingCdnAuthHeaderAndConfiguration`, `MissingCdnAuthHeader`, `MissingCdnAuthConfiguration`, `MissingCdnIdentifierSecretArns`, `MissingSecretsRoleArn`, `SecretsManagerInvalidParameterError`, `SecretsManagerInternalServiceError`, `SecretsManagerThrottlingError`, `MediaPackageSecretsValidationError`, or `OtherErrors`.<br />Can be used in combination with `ChannelGroup`, `Channel`, `OriginEndpoint`, and `CDNAuthorizationStatus` to show the CDN authorization request details for the specified endpoint. |
| `Channel` | Metrics are shown only for the specified channel.<br />Value: The auto-generated name of the channel.<br />Can be used alone or with other dimensions: [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
| `ChannelGroup` | Metrics are shown only for the specified channel group.<br />Value: The name of the channel group.<br />Can be used alone or with other dimensions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
| `IngestEndpoint` | Metrics are shown only for the specified ingest endpoint on a channel.<br />Value: The auto-generated GUID of the ingest endpoint.<br />Can be used with the following dimensions: [See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
| `OriginEndpoint` | Metrics are shown for the specified channel and endpoint combination.<br />Value: The auto-generated name of the endpoint.<br />Must be used with the `channel` dimension.  |
| `RequestType` | Metrics are shown only for the specified request type.<br />Value: Either `manifest` or `segment`, signifying the type of content being filtered in the metric.<br />Can be used alone or with other dimensions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
| `StatusCode` | Metrics are shown for the specified status code range. <br />Value: `2xx`, `3xx`, `4xx`, or `5xx`.<br />Can be used alone or with other dimensions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
| `TrackType` | Metrics are shown for the specified track type. <br />Value: `Video`, `Audio`, or `Subtitle`.<br />Can be used alone or with other dimensions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html) |
