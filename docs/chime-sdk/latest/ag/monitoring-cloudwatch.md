---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/monitoring-cloudwatch.html
---

# Monitoring the Amazon Chime SDK with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can use CloudWatch to monitor the Amazon Chime SDK. CloudWatch collects raw data and processes it into readable, near real-time metrics. Those statistics are kept for 15 months, so that you can access historical information and gain a better perspective about how your web application or service is performing. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

## CloudWatch metrics for the Amazon Chime SDK
<a name="cw-metrics"></a>

The Amazon Chime SDK sends the following metrics to CloudWatch The Amazon Chime SDK sends the metrics once per minute for the duration of a call, and it sends all of the metrics listed here.

The `AWS/ChimeVoiceConnector` namespace includes the following metrics for phone numbers assigned to your AWS account, and to Amazon Chime SDK Voice Connectors.

**Note**
The SDK sends packet-loss values once per minute for the duration of a call. The loss values accumulate for the duration of the call. For example, if a packet loss occurs at 11:01, that loss value carries forward for the remaining minutes of the call. At the end of the call, you receive a single packet-loss metric.

| Metric | Description |
| --- | --- |
| `SmaActiveCallCount` | The number of active concurrent Sip Media Application calls.<br />Units: Count |
| `VoiceConnectorActiveCallCount` | The number of active concurrent Voice Connector calls.<br />Units: Count |
| `InboundCallAttempts` | The number of inbound calls attempted.<br />Units: Count |
| `InboundCallFailures` | The number of inbound call failures.<br />Units: Count |
| `InboundCallsAnswered` | The number of inbound calls that are answered.<br />Units: Count |
| `InboundCallsActive` | The number of inbound calls that are currently active.<br />Units: Count |
| `OutboundCallAttempts` | The number of outbound calls attempted.<br />Units: Count |
| `OutboundCallFailures` | The number of outbound call failures.<br />Units: Count |
| `OutboundCallsAnswered` | The number of outbound calls that are answered.<br />Units: Count |
| `OutboundCallsActive` | The number of outbound calls that are currently active.<br />Units: Count |
| `Throttles` | The number of times your account is throttled when attempting to make a call.<br />Units: Count |
| `Sip1xxCodes` | The number of SIP messages with 1xx-level status codes.<br />Units: Count |
| `Sip2xxCodes` | The number of SIP messages with 2xx-level status codes.<br />Units: Count |
| `Sip3xxCodes` | The number of SIP messages with 3xx-level status codes.<br />Units: Count |
| `Sip4xxCodes` | The number of SIP messages with 4xx-level status codes.<br />Units: Count |
| `Sip5xxCodes` | The number of SIP messages with 5xx-level status codes.<br />Units: Count |
| `Sip6xxCodes` | The number of SIP messages with 6xx-level status codes.<br />Units: Count |
| `CustomerToVcRtpPackets` | The number of RTP packets sent from the customer to the Amazon Chime SDK Voice Connector infrastructure.<br />Units: Count |
| `CustomerToVcRtpBytes` | The number of bytes sent from the customer to the Amazon Chime SDK Voice Connector infrastructure in RTP packets.<br />Units: Count |
| `CustomerToVcRtcpPackets` | The number of RTCP packets sent from the customer to the Amazon Chime SDK Voice Connector infrastructure.<br />Units: Count |
| `CustomerToVcRtcpBytes` | The number of bytes sent from the customer to the Amazon Chime SDK Voice Connector infrastructure in RTCP packets.<br />Units: Count |
| `CustomerToVcPacketsLost` | The number of packets lost in transit from the customer to the Amazon Chime SDK Voice Connector infrastructure. Values are sent every minute until the call ends. The value count is cumulative.<br />Units: Count |
| `CustomerToVcJitter` | The average jitter for packets sent from the customer to the Amazon Chime SDK Voice Connector infrastructure.<br />Units: Microseconds |
| `VcToCustomerRtpPackets` | The number of RTP packets sent from the Amazon Chime SDK Voice Connector infrastructure to the customer.<br />Units: Count |
| `VcToCustomerRtpBytes` | The number of bytes sent from the Amazon Chime SDK Voice Connector infrastructure to the customer in RTP packets.<br />Units: Count |
| `VcToCustomerRtcpPackets` | The number of RTCP packets sent from the Amazon Chime SDK Voice Connector infrastructure to the customer.<br />Units: Count |
| `VcToCustomerRtcpBytes` | The number of bytes sent from the Amazon Chime SDK Voice Connector infrastructure to the customer in RTCP packets.<br />Units: Count |
| `VcToCustomerPacketsLost` | The number of packets lost in transit from the Amazon Chime SDK Voice Connector infrastructure to the customer. Values are sent every minute until the call ends. The value count is cumulative.<br />Units: Count |
| `VcToCustomerJitter` | The average jitter for packets sent from the Amazon Chime SDK Voice Connector infrastructure to the customer.<br />Units: Microseconds |
| `RTTBetweenVcAndCustomer` | The average round-trip time between the customer and the Amazon Chime SDK Voice Connector infrastructure.<br />Units: Microseconds |
| `MOSBetweenVcAndCustomer` | The estimated Mean opinion score (MOS) associated with voice streams between the customer and the Amazon Chime SDK Voice Connector infrastructure.<br />Units: Score between 1.0-4.4. A higher score indicates better perceived audio quality. |
| `RemoteToVcRtpPackets` | The number of RTP packets sent from the remote end to the Amazon Chime SDK Voice Connector infrastructure.<br />Units: Count |
| `RemoteToVcRtpBytes` | The number of bytes sent from the remote end to the Amazon Chime SDK Voice Connector infrastructure in RTP packets.<br />Units: Count |
| `RemoteToVcRtcpPackets` | The number of RTCP packets sent from the remote end to the Amazon Chime SDK Voice Connector infrastructure.<br />Units: Count |
| `RemoteToVcRtcpBytes` | The number of bytes sent from the remote end to the Amazon Chime SDK Voice Connector infrastructure in RTCP packets.<br />Units: Count |
| `RemoteToVcPacketsLost` | The number of packets lost in transit from the remote end to the Amazon Chime SDK Voice Connector infrastructure. Values are sent every minute until the call ends. The value count is cumulative.<br />Units: Count |
| `RemoteToVcJitter` | The average jitter for packets sent from the remote end to the Amazon Chime SDK Voice Connector infrastructure.<br />Units: Microseconds |
| `VcToRemoteRtpPackets` | The number of RTP packets sent from the Amazon Chime SDK Voice Connector infrastructure to the remote end.<br />Units: Count |
| `VcToRemoteRtpBytes` | The number of bytes sent from the Amazon Chime SDK Voice Connector infrastructure to the remote end in RTP packets.<br />Units: Count |
| `VcToRemoteRtcpPackets` | The number of RTCP packets sent from the Amazon Chime SDK Voice Connector infrastructure to the remote end.<br />Units: Count |
| `VcToRemoteRtcpBytes` | The number of bytes sent from the Amazon Chime SDK Voice Connector infrastructure to the remote end in RTCP packets.<br />Units: Count |
| `VcToRemotePacketsLost` | The number of packets lost in transit from the Amazon Chime SDK Voice Connector infrastructure to the remote end. Values are sent every minute until the call ends. The value count is cumulative.<br />Units: Count |
| `VcToRemoteJitter` | The average jitter for packets sent from the Amazon Chime SDK Voice Connector infrastructure to the remote end.<br />Units: Microseconds |
| `RTTBetweenVcAndRemote` | The average round-trip time between the remote end and the Amazon Chime SDK Voice Connector infrastructure.<br />Units: Microseconds |
| `MOSBetweenVcAndRemote` | The estimated Mean opinion score (MOS) associated with voice streams between the remote end and the Amazon Chime SDK Voice Connector infrastructure.<br />Units: Units: Score between 1.0-4.4. A higher score indicates better perceived audio quality. |

## CloudWatch dimensions for the Amazon Chime SDK
<a name="cw-dimensions"></a>

The CloudWatch dimensions that you can use with the Amazon Chime SDK are listed as follows.

| Dimension | Description |
| --- | --- |
| `VoiceConnectorId` | The identifier of the Amazon Chime SDK Voice Connector to display metrics for. |
| `Region` | The AWS Region associated with the event. |

## CloudWatch logs for the Amazon Chime SDK
<a name="cw-logs"></a>

You can configure your Amazon Chime SDK Voice Connectors to send metrics to CloudWatch Logs. When you do, you can also receive media-quality metric logs for those Voice Connectors.

The Amazon Chime SDK sends detailed metrics once per minute. The Amazon Chime SDK sends them for all the calls made with the configured Voice Connectors, and it sends them to a CloudWatch Logs log group that we create for you.

The log group name uses this format: `/aws/ChimeVoiceConnectorLogs/${{{VoiceConnectorID}}}`.

For more information about configuring Voice Connectors to send metrics, see [Editing Amazon Chime SDK Voice Connector settings](edit-voicecon.md).

**Note**
Packet loss metrics accumulate for the duration of a call. For example, if a packet loss occurs at 11:01, that loss value carries forward for the remaining minutes of the call. At the end of the call, you receive a single packet-loss metric.

The Amazon Chime SDK includes the following fields in the logs, in JSON format.

| Field | Description |
| --- | --- |
| voice\_connector\_id | The Amazon Chime SDK Voice Connector ID carrying the call. |
| event\_timestamp | The time when the metrics are emitted, in number of milliseconds since the UNIX epoch (midnight on January 1, 1970) in UTC. |
| call\_id | Corresponds to the Transaction ID. |
| from\_sip\_user | The initiating user for the call. |
| from\_country | The initiating country for the call. |
| to\_sip\_user | The receiving user for the call. |
| to\_country | The receiving country for the call. |
| endpoint\_id | An opaque identifier indicating the other endpoint of the call. Use with CloudWatch Logs Insights. For more information, see [Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) in the *Amazon CloudWatch Logs User Guide*. |
| aws\_region | The AWS Region for the call. |
| cust2vc\_rtp\_packets | The number of RTP packets sent from the customer to the Amazon Chime SDK Voice Connector infrastructure. |
| cust2vc\_rtp\_bytes | The number of bytes sent from the customer to the Amazon Chime SDK Voice Connector infrastructure in RTP packets. |
| cust2vc\_rtcp\_packets | The number of RTCP packets sent from the customer to the Amazon Chime SDK Voice Connector infrastructure. |
| cust2vc\_rtcp\_bytes | The number of bytes sent from the customer to the Amazon Chime SDK Voice Connector infrastructure in RTCP packets. |
| cust2vc\_packets\_lost | The number of packets lost in transit from the customer to the Amazon Chime SDK Voice Connector infrastructure. Values are sent every minute until the call ends. The value count is cumulative. |
| cust2vc\_jitter | The average jitter for packets sent from the customer to the Amazon Chime SDK Voice Connector infrastructure. |
| vc2cust\_rtp\_packets | The number of RTP packets sent from the Amazon Chime SDK Voice Connector infrastructure to the customer. |
| vc2cust\_rtp\_bytes | The number of bytes sent from the Amazon Chime SDK Voice Connector infrastructure to the customer in RTP packets. |
| vc2cust\_rtcp\_packets | The number of RTCP packets sent from the Amazon Chime SDK Voice Connector infrastructure to the customer. |
| vc2cust\_rtcp\_bytes | The number of bytes sent from the Amazon Chime SDK Voice Connector infrastructure to the customer in RTCP packets. |
| vc2cust\_packets\_lost | The number of packets lost in transit from the Amazon Chime SDK Voice Connector infrastructure to the customer. Values are sent every minute until the call ends. The value count is cumulative. |
| vc2cust\_jitter | The average jitter for packets sent from the Amazon Chime SDK Voice Connector infrastructure to the customer. |
| rtt\_btwn\_vc\_and\_cust | The average round-trip time between the customer and the Amazon Chime SDK Voice Connector infrastructure. |
| mos\_btwn\_vc\_and\_cust | The estimated Mean opinion score (MOS) associated with voice streams between the customer and the Amazon Chime SDK Voice Connector infrastructure. |
| rem2vc\_rtp\_packets | The number of RTP packets sent from the remote end to the Amazon Chime SDK Voice Connector infrastructure. |
| rem2vc\_rtp\_bytes | The number of bytes sent from the remote end to the Amazon Chime SDK Voice Connector infrastructure in RTP packets. |
| rem2vc\_rtcp\_packets | The number of RTCP packets sent from the remote end to the Amazon Chime SDK Voice Connector infrastructure. |
| rem2vc\_rtcp\_bytes | The number of bytes sent from the remote end to the Amazon Chime SDK Voice Connector infrastructure in RTCP packets. |
| rem2vc\_packets\_lost | The number of packets lost in transit from the remote end to the Amazon Chime SDK Voice Connector infrastructure. Values are sent every minute until the call ends. The value count is cumulative. |
| rem2vc\_jitter | The average jitter for packets sent from the remote end to the Amazon Chime SDK Voice Connector infrastructure. |
| vc2rem\_rtp\_packets | The number of RTP packets sent from the Amazon Chime SDK Voice Connector infrastructure to the remote end. |
| vc2rem\_rtp\_bytes | The number of bytes sent from the Amazon Chime SDK Voice Connector infrastructure to the remote end in RTP packets. |
| vc2rem\_rtcp\_packets | The number of RTCP packets sent from the Amazon Chime SDK Voice Connector infrastructure to the remote end. |
| vc2rem\_rtcp\_bytes | The number of bytes sent from the Amazon Chime SDK Voice Connector infrastructure to the remote end in RTCP packets. |
| vc2rem\_packets\_lost | The number of packets lost in transit from the Amazon Chime SDK Voice Connector infrastructure to the remote end. Values are sent every minute until the call ends. The value count is cumulative. |
| vc2rem\_jitter | The average jitter for packets sent from the Amazon Chime SDK Voice Connector infrastructure to the remote end. |
| rtt\_btwn\_vc\_and\_rem | The average round-trip time between the remote end and the Amazon Chime SDK Voice Connector infrastructure. |
| mos\_btwn\_vc\_and\_rem | The estimated Mean opinion score (MOS) associated with voice streams between the remote end and the Amazon Chime SDK Voice Connector infrastructure. |

**SIP message logs**
You can opt to receive SIP message logs for your Amazon Chime SDK Voice Connector. When you do, the Amazon Chime SDK captures inbound and outbound SIP messages and sends them to a CloudWatch Logs log group that is created for you. The log group name is `/aws/ChimeVoiceConnectorSipMessages/${{{VoiceConnectorID}}}`. The following fields are included in the logs, in JSON format.

| Field | Description |
| --- | --- |
| voice\_connector\_id | The Amazon Chime SDK Voice Connector ID. |
| aws\_region | The AWS Region associated with the event. |
| event\_timestamp | The time when the message is captured, in number of milliseconds since the UNIX epoch (midnight on January 1, 1970) in UTC. |
| call\_id | The Amazon Chime SDK Voice Connector call ID. |
| sip\_message | The full SIP message that is captured. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
