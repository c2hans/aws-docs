---
source_url: https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-limits.html
---

# Amazon Kinesis Video Streams with WebRTC service quotas
<a name="kvswebrtc-limits"></a>

Kinesis Video Streams with WebRTC has the following service quotas:

**Important**
The following service quotas are either soft **[s]**, which can be increased, or hard **[h]**, which can't be increased. You will see [s] and [h] next to individual service quota in the tables below.

**Note**
TPS stands for *transactions per second*.

**Topics**
+ [Control plane API service quotas](#limits-control-plane)
+ [Signaling API service quotas](#limits-signaling-service)
+ [TURN service quotas](#limits-turn-service)
+ [WebRTC ingestion service quotas](#limits-ingestion)
+ [Troubleshooting](#troubleshooting)

## Control plane API service quotas
<a name="limits-control-plane"></a>

The following section describes service quotas for the control plane APIs.

| API | Maximum API request rate per AWS account | Maximum number of channels per AWS account per AWS Region | Maximum API request per channel |
| --- | --- | --- | --- |
| CreateSignalingChannel | 50 TPS [s] | [See the AWS documentation website for more details](http://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-limits.html)  | N/A |
| DeleteSignalingChannel | 50 TPS [h] | N/A | 5 TPS [h] |
| DescribeMediaStorageConfiguration | 50 TPS [h] | N/A | 5 TPS [h] |
| DescribeSignalingChannel | 300 TPS [h] | N/A | 5 TPS [h] |
| GetSignalingChannelEndpoint | 300 TPS [h] | N/A | N/A |
| ListSignalingChannels | 50 TPS [h] | N/A | N/A |
| ListTagsForResource | 50 TPS [h]  | N/A | 5 TPS [h] |
| TagResource | 50 TPS [h]  | N/A | 5 TPS [h] |
| UntagResource | 50 TPS [h]  | N/A | 5 TPS [h] |
| UpdateMediaStorageConfiguration | 10 TPS [h] | N/A | 5 TPS [h] |
| UpdateSignalingChannel | 50 TPS [h] | N/A | 5 TPS [h] |

## Signaling API service quotas
<a name="limits-signaling-service"></a>

The following section describes service quotas for the signaling component in Kinesis Video Streams with WebRTC. For more information, see [How it works](kvswebrtc-how-it-works.md).

| API | Maximum GO\_AWAY message grace period prior to terminating connection | Maximum API request rate per channel | Maximum number of concurrent connections per channel | Maximum connection duration | Maximum idle connection timeout period |
| --- | --- | --- | --- | --- | --- |
| ConnectAsMaster | 1 minute (h) | 3 TPS (h) | 1 (h) | 1 hour (h) | 10 minutes (h) |
| ConnectAsViewer | 1 minute (h) | 3 TPS (h) | 10 (s) | 1 hour (h) | 10 minutes (h) |

| API | Maximum API request rate | Maximum message payload size |
| --- | --- | --- |
| SendAlexaOffertoMaster | [See the AWS documentation website for more details](http://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-limits.html) | N/A |
| SendICECandidate | 20 TPS per WebSocket connection (h) | 10k (h) |
| SendSDPAnswer | 5 TPS per WebSocket connection (h) | 10k (h) |
| SendSDPOffer | 5 TPS per WebSocket connection (h) | 10k (h) |

## TURN service quotas
<a name="limits-turn-service"></a>

The following section describes service quotas for the Traversal Using Relays around NAT (TURN) component in Kinesis Video Streams with WebRTC. For more information, see [How it works](kvswebrtc-how-it-works.md).

| API or parameter | Value |
| --- | --- |
| GetIceServerConfig |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/kvswebrtc-limits.html)  |
| Bit Rate | 5Mbps (h) |
| Credential Lifecycle | 5 minutes (h) |
| Number of allocations | 50 per signaling channel (h) |

## WebRTC ingestion service quotas
<a name="limits-ingestion"></a>

The following section describes service quotas for the media recording component in Amazon Kinesis Video Streams WebRTC. For more information, see [Use Amazon Kinesis Video Streams with WebRTC to ingest and store media](webrtc-ingestion.md).

**JoinStorageSession**
+ API:
  + Per AWS account - 50 TPS (h)
  + Per channel - 2 TPS (h)
+ Streaming session quotas:
  + Bit rate - 1 Mbps (s)
  + Session duration - 1 hour (h)
  + Idle timeout - 3 minutes (h)

**JoinStorageSessionAsViewer**
+ API:
  + Per AWS account - 50 TPS (h)
  + Per channel - 2 TPS (h)
+ Streaming session quotas:
  + Max concurrent clients in a session - 3 count (h)
  + Session duration - 1 hour (h)
  + Idle timeout - 1 minutes (h)

## Troubleshooting
<a name="troubleshooting"></a>

You can only connect **one** master and **one or more** viewers to a single signaling channel.

It isn't possible to connect multiple masters to a single signaling channel.
