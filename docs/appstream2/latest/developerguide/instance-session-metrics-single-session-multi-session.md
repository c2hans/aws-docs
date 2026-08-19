---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/instance-session-metrics-single-session-multi-session.html
---

# Instance and Session Performance Metrics for Single-session and Multi-session Fleets
<a name="instance-session-metrics-single-session-multi-session"></a>

The following are instance and session performance metrics for single-session and multi-session fleets.

| Metric | Description | Dimensions | Statistics | Units |
| --- | --- | --- | --- | --- |
| CpuUtilizationInstance | The percentage of allocated compute units that are currently in use on the instance. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Percent |
| MemoryUtilizationInstance | The percentage of allocated physical memory units that are currently in use on the instance. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Percent |
|  PagingFileUtilizationInstance  | The percentage of the paging file that is currently in use to extend the memory (RAM) capacity. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Percent |
|  DiskUtilizationInstance  | The percentage of the instance's available disk storage capacity that is currently in use. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Percent |
| GpuUtilizationInstance | The percentage of the GPU resource used on the instance. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Percent |
| CpuQueueLength | The number of threads waiting for CPU time on the instance. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Count |
| DiskIoQueueLength | The number of pending I/O requests waiting to be processed by the disk on the instance. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Count |
| MemoryPageHardFaults | The rate of hard page faults on the instance. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Count/Second |
| CpuUtilizationSession | The percentage of allocated compute units that are currently in use by the session. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId, SessionId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Percent |
|  MemoryUtilizationSession  | The percentage of allocated physical memory units that are currently in use by the session. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId, SessionId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Percent |
| DiskReadOperations | The number of disk read operations per instance. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Count |
| DiskWriteOperations | The number of disk write operations per instance. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Count |
| InSessionLatency | The round-trip time between the client and the instance. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId, SessionId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Milliseconds |
| UDPPacketLossRate | The percentage of UDP packets lost in traffic from the gateway to the client. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId, SessionId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Percent |
| TCPRetransmissionRate | The percentage of TCP segments that were retransmitted from the gateway to the client. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId, SessionId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Percent |
| Bandwidth | The rate of data transferred from the gateway to the client (outbound). | [Fleet]<br />[UserId]<br />[FleetName, InstanceId, SessionId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Kilobits/Second |
| BandwidthInbound | The rate of data transferred from the client to the gateway (inbound). | [Fleet]<br />[UserId]<br />[FleetName, InstanceId, SessionId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Kilobits/Second |
| CongestionWindow | The size of the congestion window at the gateway for traffic flowing to the client. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId, SessionId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Bytes |
| ConnectionDuration | The duration of the streaming connection. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId, SessionId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Seconds |
| FramesPerSecond | The number of frames sent per second from the instance to the client. | [Fleet]<br />[UserId]<br />[FleetName, InstanceId, SessionId]<br />[FleetName, InstanceId, SessionId, UserId] | Average, Minimum, Maximum | Count |
| MetadataNoToken | The number of times the instance metadata service was accessed without a token (IMDSv1). This metric helps identify workloads that have not yet migrated to IMDSv2. | [Fleet]<br />[ImageBuilder]<br />[AppBlockBuilder] | Sum | Count |
| MetadataNoTokenRejected | The number of times an IMDSv1 request to the instance metadata service was rejected. This metric is available when the instance is configured to require IMDSv2. | [Fleet]<br />[ImageBuilder]<br />[AppBlockBuilder] | Sum | Count |

**Note**
All metrics are available for the Windows Server operating system. For the remaining set of supported operating systems, only the following metrics are available: `UDPPacketLossRate`, `TCPRetransmissionRate`, `BandwidthInbound`, `CongestionWindow`, `ConnectionDuration`, `MetadataNoToken`, and `MetadataNoTokenRejected`.
