---
source_url: https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/use-enhanced-networking-ec2-instance-types.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Use enhanced networking EC2 instance types
<a name="use-enhanced-networking-ec2-instance-types"></a>

Choosing the right instance type on Amazon EC2 ensures system reliability as well as efficient usage of infrastructure. EC2 provides a wide selection of instance types optimized to fit different use cases. Instance types comprise varying combinations of CPU, memory, storage, and networking capacity and give you the flexibility to choose the appropriate mix of resources for your applications. These enhanced networking instance types ensure that the SIP workloads running on them have access to consistent bandwidth and comparatively lower aggregate latency. A recent addition to Amazon EC2 is the availability of the Elastic Network Adapter (ENA) that provides up to 100 Gbps of bandwidth. The latest catalog of EC2 instance types and associated features can be found on the [EC2 instance types page](https://aws.amazon.com/ec2/instance-types/).

 For most customers, the latest generation of [Compute Optimized instances](https://aws.amazon.com/ec2/instance-types/) should provide the best value for the cost. For example, the C5N supports the new Elastic Network Adapter with bandwidth up to 100 Gbps with millions of packets per second (PPS). Most real-time applications would also benefit from using the [Intel Data Plane Developer Kit ](http://www.intel.com/content/www/us/en/communications/data-plane-development-kit.html) (DPDK) which can greatly boost network packet processing.

 However, it is always a best practice to benchmark the various EC2 instance types according to your requirements to see which instance type works best for you. Benchmarking also enables you to find other configuration parameters, such as the maximum number of calls a certain instance type can process at a time.
