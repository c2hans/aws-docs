---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/well-architected-best-practices-fsx-windows/sustainability-pillar.html
---

# Sustainability pillar
<a name="sustainability-pillar"></a>

The sustainability pillar of the AWS Well-Architected Framework focuses on minimizing the environmental impacts of running cloud workloads. The following recommendations can help you meet the** **sustainability design principles and architectural best practices for Amazon FSx for Windows File Server.

**Key focus areas**
+ Shared responsibility model for sustainability
+ Understanding impact
+ Maximizing utilization to minimize required resources and reduce downstream impacts

## Understand your impact
<a name="understand-your-impact"></a>
+ Track Amazon FSx for Windows File Server metrics to understand the impact of current consumption and any configuration changes you apply.

## Maximize utilization
<a name="maximize-utilization"></a>
+ Automatically scale the storage and throughput capacity of your FSx for Windows File Server file systems based on utilization metrics. For more information, see:
  + [Increasing the storage capacity of an FSx for Windows File Server file system dynamically ](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-capacity.html#automate-storage-capacity-increase)in the Amazon FSx documentation.
  + [How to modify throughput capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-throughput-capacity.html#increase-throughput-capacity) in the Amazon FSx documentation.
  + [Amazon FSx for Windows File Server - Automatic Storage and Throughput Capacity Scaling](https://www.youtube.com/watch?v=1p0tnll1l14) on the AWS YouTube channel.
