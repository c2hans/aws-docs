---
source_url: https://docs.aws.amazon.com/whitepapers/latest/financial-services-grid-computing/x86-instances.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# x86 instances
<a name="x86-instances"></a>

Each vCPU on x86-based Amazon EC2 instances is thread on the processor, except for C7a, R7a, M7a, T2, and m3.medium instances. Each thread is represented as a virtual CPU (vCPU) on the instance. An instance has a default number of CPU cores, which varies according to instance type.

 To ensure that each vCPU is used effectively, it’s important to understand the behavior of the calculations running in the HPC environment. If all processes are single-threaded, a good initial strategy is to have the scheduler assign one process per vCPU on each instance. However, if the calculations require multithreading, tuning might be required to maximize the use of vCPUs without introducing excessive CPU context switching.

 By default, most x86 based Amazon EC2 instances have hyperthreading (HT) enabled. You can disable HT either at boot or at runtime if the workload performs better without it, which you can establish through benchmarking. The [Disabling Intel Hyper-Threading Technology on Amazon Linux](https://aws.amazon.com/blogs/compute/disabling-intel-hyper-threading-technology-on-amazon-linux/) blog post has an explanation of the methods you can use to configure HT on an Amazon Linux instance. The [Amazon EC2 documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-specify-cpu-options.html) shows how to specify CPU options during instance launch and this includes setting the number of threads per physical core.

 Another potential optimization is over-subscription. This approach is useful when you know processes spend time on non-CPU intensive activities, such as waiting on data transfers or loading binaries into memory. For example, if this overhead is estimated at 10%, you might be able to schedule one additional task on the host for every 10 vCPUs to achieve higher CPU utilization and throughput.
