---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf-network.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# Network
<a name="perf-network"></a>

 Since the network is between all workload components, it can have great impacts, both positive and negative, on workload performance and behavior. There are also workloads that are heavily dependent on network performance such as high performance computing (HPC) where deep network understanding is important to increase cluster performance. Determine the workload requirements for bandwidth, latency, jitter, and throughput.

 On AWS, networking is virtualized and is available in a number of different types and configurations. This makes it efficient to match your networking operations with your needs. AWS offers product features (for example, Enhanced Networking, Amazon EBS-optimized instances, Amazon S3 transfer acceleration, and dynamic Amazon CloudFront) to optimize network traffic. AWS also offers networking features (for example, Amazon Route 53 latency routing, Amazon VPC endpoints, AWS Direct Connect, and AWS Global Accelerator) to reduce network distance or jitter.

 The following question focuses on these considerations for performance efficiency.

| PERF 5:  How do you configure your networking solution? |
| --- |
|  The most efficient network solution for a workload varies based on latency, throughput requirements, jitter, and bandwidth. Physical constraints, such as user or on-premises resources, determine location options. These constraints can be offset with edge locations or resource placement.  |

 You must consider location when deploying your network. You can choose to place resources close to where they will be used to reduce distance. Use networking metrics to make changes to networking configuration as the workload evolves. By taking advantage of Regions, placement groups, and edge services, you can significantly improve performance. Cloud based networks can be quickly re-built or modified, so evolving your network architecture over time is necessary to maintain performance efficiency.
