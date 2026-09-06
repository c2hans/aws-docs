---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/networking.html
---

# Networking
<a name="networking"></a>

 An Outpost deployment depends on a resilient connection to its anchor AZ for management, monitoring, and service operations to function properly. You should provision your on-premises network to provide redundant network connections for each Outpost rack and reliable connectivity back to the anchor points in the AWS cloud. Also consider network paths between the application workloads running on the Outpost and the other on-premises and cloud systems they communicate with – how will you route this traffic in your network?

**Topics**
+ [Network attachment](network-attachment.md)
+ [Anchor connectivity](anchor-connectivity.md)
+ [Application/workload routing](applicationworkload-routing.md)
