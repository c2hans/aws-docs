---
source_url: https://docs.aws.amazon.com/whitepapers/latest/semiconductor-design-on-aws/match-compute-resources-to-workload-requirements.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Match compute resources to workload requirements
<a name="match-compute-resources-to-workload-requirements"></a>

AWS offers many different configurations of virtual and bare metal servers (such as cores, memory, storage, and network bandwidth) known as [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2) (Amazon EC2) instances. Customers choose instance types that match the compute needs of their jobs. Combined with the on-demand nature of the AWS Cloud, you can get precisely the compute infrastructure you need, for the exact job you need to run, and for only the time you need it.

Amazon EC2 instances are available in many different sizes and configurations. These configurations are built to support jobs that require both large and small memory footprints, high core counts of the latest generation processors, and storage requirements from high input/output operations per second (IOPS) to high throughput. By [right-sizing](https://aws.amazon.com/aws-cost-management/aws-cost-optimization/right-sizing/) the instance to the unit of work for which it is best suited, you can achieve higher performance at lower overall cost. You no longer need to purchase cluster hardware that is entirely configured to meet the demands of just a few of your most demanding jobs. Instead, you can launch instances that match the characteristics of your desired workload into dynamically scalable compute clusters that are uniquely optimized for specific workloads or stages of chip development.

For example, consider a situation where you’re developing a critical IP core and need to perform gate-level simulations for a few weeks. In this example, you might need to have a cluster of 100 compute servers (representing over 2,000 CPU cores) with a specific memory-to-core ratio and a specific storage configuration. With AWS, you can deploy and run this cluster, dedicated and purpose-built only for this task, for only as long as the simulations require, and then terminate the cluster when that stage of your project is complete.

Consider another situation in which you have multiple semiconductor design teams working in different geographic regions, each using their own locally-installed EDA IT infrastructure. This geographic diversity of engineering teams has productivity benefits for modern chip design, but it can create challenges in managing large-scale EDA infrastructure; for example, to efficiently use globally-licensed EDA software. By using AWS to augment or replace these geographically separated IT resources, you can pool all of your global EDA licenses in a smaller number of locations using scalable, on-demand clusters on AWS. As a result, you can more rapidly complete critical batch workloads, such as static timing analysis, DRC, and physical verification.
