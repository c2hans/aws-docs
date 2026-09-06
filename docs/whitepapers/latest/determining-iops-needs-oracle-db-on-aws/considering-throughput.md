---
source_url: https://docs.aws.amazon.com/whitepapers/latest/determining-iops-needs-oracle-db-on-aws/considering-throughput.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Considering throughput
<a name="considering-throughput"></a>

 In addition to determining the right IOPS, it is also important to make sure your instance configuration can handle the throughput needs of your database. *Throughput* is the measure of the transfer of bits across the network between the EC2 instance running your database and the Amazon EBS volumes that store the data. The amount of available throughput relates directly to the network bandwidth that is available to the EC2 instance and the capability of Amazon EBS to receive data.

 Amazon EBS–optimized instances consistently achieve the given level of performance. For more information, refer to [Instance Types that Support EBS Optimization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html#ebs-optimization-support) in the *Amazon EC2 User Guide for Linux Instances*. You can find more about Amazon EC2–Amazon EBS configuration in the [Amazon EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-ec2-config.html). In addition to bandwidth availability, there are other considerations that affect which EC2 instance you should choose for your Oracle Database. These considerations include your database license, virtual CPUs available, and memory size.
