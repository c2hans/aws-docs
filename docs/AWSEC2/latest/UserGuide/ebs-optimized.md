---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html
---

# Amazon EBS-optimized instance types

Amazon EBS–optimized instances use an optimized configuration stack and provide additional, dedicated bandwidth for Amazon EBS I/O. This optimization provides the best performance for your EBS volumes by minimizing contention between Amazon EBS I/O and other traffic from your instance.

When attached to an EBS–optimized instance, General Purpose SSD (`gp2` and `gp3`) volumes are designed to deliver at least 90 percent of their provisioned IOPS performance 99 percent of the time in a given year, and Provisioned IOPS SSD (`io1` and `io2`) volumes are designed to deliver at least 90 percent of their provisioned IOPS performance 99.9 percent of the time in a given year. Throughput Optimized HDD (`st1`) and Cold HDD (`sc1`) deliver at least 90 percent of their expected throughput performance 99 percent of the time in a given year. Non-compliant periods are approximately uniformly distributed, targeting 99 percent of expected total throughput each hour. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide*.

Some instance types are **EBS-optimized by default**, and there is no need to enable it and no effect if you attempt to disable it. Other instance types optionally **support EBS optimization** and you can enable it during or after launch for an [ additional hourly fee](https://aws.amazon.com/ec2/previous-generation/#EBS-optimized_instances). Some instance types do not support EBS optimization.

For detailed instance type specifications and features, see the [Amazon EC2 Instance Types Guide](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html).

**Considerations**
+ An instance's EBS performance is bounded by the instance type's performance limits, or the aggregated performance of its attached volumes, whichever is smaller. To achieve maximum EBS performance, an instance must have attached volumes that provide a combined performance equal to or greater than the maximum instance performance. For example, to achieve `80,000` IOPS for `r6i.16xlarge`, the instance must have at least `5` `gp2` volumes provisioned with `16,000` IOPS each (`5` volumes x `16,000` IOPS = `80,000` IOPS), or it can have `1` `gp3` volume provisioned with `80,000` IOPS. We recommend that you choose an instance type that provides more dedicated Amazon EBS throughput than your application needs; otherwise, the connection between Amazon EBS and Amazon EC2 can become a performance bottleneck.
+ The maximum number of Amazon EBS volumes that you can attach to an instance depends on the instance type and instance size. For more information, see [Amazon EBS volume limits for Amazon EC2 instances](volume_limits.md).
+ The maximum IOPS and throughput limits are interdependent. Depending on your I/O size, you might reach one limit before the other, which can affect overall performance. For optimal results, consider both limits when planning your workload.

## EBS-optimized by default
<a name="current"></a>

The following instance types are EBS–optimized by default. There is no need to enable EBS optimization and no effect if you disable EBS optimization.

**Topics**
+ [General purpose](#current-general-purpose)
+ [Compute optimized](#current-compute-optimized)
+ [Memory optimized](#current-memory-optimized)
+ [Storage optimized](#current-storage-optimized)
+ [Accelerated computing](#current-accelerated-computing)
+ [High-performance computing](#current-high-performance-computing)

### General purpose
<a name="current-general-purpose"></a>

**Note**
M8a, M8g, M8gd, M8i, M8id, M8i-flex, M9g, M9gd instance types support configurable bandwidth weightings. With these instance types, you can optimize an instance's bandwidth for either networking performance or Amazon EBS performance. The following table shows the default Amazon EBS bandwidth performance for these instance types. For more information, see [EC2 instance bandwidth weighting configuration](configure-bandwidth-weighting.md).

<table>
<thead>
  <tr><th>Instance size</th><th>Baseline bandwidth (Mbps)</th><th>Maximum bandwidth (Mbps)</th><th>Baseline throughput (MB/s, 128 KiB I/O)</th><th>Maximum throughput (MB/s, 128 KiB I/O)</th><th>Baseline IOPS (16 KiB I/O)</th><th>Maximum IOPS (16 KiB I/O)</th></tr>
</thead>
<tbody>
  <tr><td>a1.medium <sup>1</sup></td><td>300</td><td>3500</td><td>37.50</td><td>437.50</td><td>2500</td><td>20000</td></tr>
  <tr><td>a1.large <sup>1</sup></td><td>525</td><td>3500</td><td>65.62</td><td>437.50</td><td>4000</td><td>20000</td></tr>
  <tr><td>a1.xlarge <sup>1</sup></td><td>800</td><td>3500</td><td>100.00</td><td>437.50</td><td>6000</td><td>20000</td></tr>
  <tr><td>a1.2xlarge <sup>1</sup></td><td>1750</td><td>3500</td><td>218.75</td><td>437.50</td><td>10000</td><td>20000</td></tr>
  <tr><td>a1.4xlarge <sup>2</sup></td><td colspan="2">3500</td><td colspan="2">437.5</td><td colspan="2">20000</td></tr>
  <tr><td>a1.metal <sup>2</sup></td><td colspan="2">3500</td><td colspan="2">437.5</td><td colspan="2">20000</td></tr>
  <tr><td>m4.large <sup>2</sup></td><td colspan="2">450</td><td colspan="2">56.25</td><td colspan="2">3600</td></tr>
  <tr><td>m4.xlarge <sup>2</sup></td><td colspan="2">750</td><td colspan="2">93.75</td><td colspan="2">6000</td></tr>
  <tr><td>m4.2xlarge <sup>2</sup></td><td colspan="2">1000</td><td colspan="2">125.0</td><td colspan="2">8000</td></tr>
  <tr><td>m4.4xlarge <sup>2</sup></td><td colspan="2">2000</td><td colspan="2">250.0</td><td colspan="2">16000</td></tr>
  <tr><td>m4.10xlarge <sup>2</sup></td><td colspan="2">4000</td><td colspan="2">500.0</td><td colspan="2">32000</td></tr>
  <tr><td>m4.16xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">65000</td></tr>
  <tr><td>m5.large <sup>1</sup></td><td>650</td><td>4750</td><td>81.25</td><td>593.75</td><td>3600</td><td>18750</td></tr>
  <tr><td>m5.xlarge <sup>1</sup></td><td>1150</td><td>4750</td><td>143.75</td><td>593.75</td><td>6000</td><td>18750</td></tr>
  <tr><td>m5.2xlarge <sup>1</sup></td><td>2300</td><td>4750</td><td>287.50</td><td>593.75</td><td>12000</td><td>18750</td></tr>
  <tr><td>m5.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">18750</td></tr>
  <tr><td>m5.8xlarge <sup>2</sup></td><td colspan="2">6800</td><td colspan="2">850.0</td><td colspan="2">30000</td></tr>
  <tr><td>m5.12xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>m5.16xlarge <sup>2</sup></td><td colspan="2">13600</td><td colspan="2">1700.0</td><td colspan="2">60000</td></tr>
  <tr><td>m5.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>m5.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>m5a.large <sup>1</sup></td><td>650</td><td>2880</td><td>81.25</td><td>360.00</td><td>3600</td><td>16000</td></tr>
  <tr><td>m5a.xlarge <sup>1</sup></td><td>1085</td><td>2880</td><td>135.62</td><td>360.00</td><td>6000</td><td>16000</td></tr>
  <tr><td>m5a.2xlarge <sup>1</sup></td><td>1580</td><td>2880</td><td>197.50</td><td>360.00</td><td>8333</td><td>16000</td></tr>
  <tr><td>m5a.4xlarge <sup>2</sup></td><td colspan="2">2880</td><td colspan="2">360.0</td><td colspan="2">16000</td></tr>
  <tr><td>m5a.8xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>m5a.12xlarge <sup>2</sup></td><td colspan="2">6780</td><td colspan="2">847.5</td><td colspan="2">30000</td></tr>
  <tr><td>m5a.16xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>m5a.24xlarge <sup>2</sup></td><td colspan="2">13750</td><td colspan="2">1718.75</td><td colspan="2">60000</td></tr>
  <tr><td>m5ad.large <sup>1</sup></td><td>650</td><td>2880</td><td>81.25</td><td>360.00</td><td>3600</td><td>16000</td></tr>
  <tr><td>m5ad.xlarge <sup>1</sup></td><td>1085</td><td>2880</td><td>135.62</td><td>360.00</td><td>6000</td><td>16000</td></tr>
  <tr><td>m5ad.2xlarge <sup>1</sup></td><td>1580</td><td>2880</td><td>197.50</td><td>360.00</td><td>8333</td><td>16000</td></tr>
  <tr><td>m5ad.4xlarge <sup>2</sup></td><td colspan="2">2880</td><td colspan="2">360.0</td><td colspan="2">16000</td></tr>
  <tr><td>m5ad.8xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>m5ad.12xlarge <sup>2</sup></td><td colspan="2">6780</td><td colspan="2">847.5</td><td colspan="2">30000</td></tr>
  <tr><td>m5ad.16xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>m5ad.24xlarge <sup>2</sup></td><td colspan="2">13750</td><td colspan="2">1718.75</td><td colspan="2">60000</td></tr>
  <tr><td>m5d.large <sup>1</sup></td><td>650</td><td>4750</td><td>81.25</td><td>593.75</td><td>3600</td><td>18750</td></tr>
  <tr><td>m5d.xlarge <sup>1</sup></td><td>1150</td><td>4750</td><td>143.75</td><td>593.75</td><td>6000</td><td>18750</td></tr>
  <tr><td>m5d.2xlarge <sup>1</sup></td><td>2300</td><td>4750</td><td>287.50</td><td>593.75</td><td>12000</td><td>18750</td></tr>
  <tr><td>m5d.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">18750</td></tr>
  <tr><td>m5d.8xlarge <sup>2</sup></td><td colspan="2">6800</td><td colspan="2">850.0</td><td colspan="2">30000</td></tr>
  <tr><td>m5d.12xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>m5d.16xlarge <sup>2</sup></td><td colspan="2">13600</td><td colspan="2">1700.0</td><td colspan="2">60000</td></tr>
  <tr><td>m5d.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>m5d.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>m5dn.large <sup>1</sup></td><td>650</td><td>4750</td><td>81.25</td><td>593.75</td><td>3600</td><td>18750</td></tr>
  <tr><td>m5dn.xlarge <sup>1</sup></td><td>1150</td><td>4750</td><td>143.75</td><td>593.75</td><td>6000</td><td>18750</td></tr>
  <tr><td>m5dn.2xlarge <sup>1</sup></td><td>2300</td><td>4750</td><td>287.50</td><td>593.75</td><td>12000</td><td>18750</td></tr>
  <tr><td>m5dn.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">18750</td></tr>
  <tr><td>m5dn.8xlarge <sup>2</sup></td><td colspan="2">6800</td><td colspan="2">850.0</td><td colspan="2">30000</td></tr>
  <tr><td>m5dn.12xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>m5dn.16xlarge <sup>2</sup></td><td colspan="2">13600</td><td colspan="2">1700.0</td><td colspan="2">60000</td></tr>
  <tr><td>m5dn.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>m5dn.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>m5n.large <sup>1</sup></td><td>650</td><td>4750</td><td>81.25</td><td>593.75</td><td>3600</td><td>18750</td></tr>
  <tr><td>m5n.xlarge <sup>1</sup></td><td>1150</td><td>4750</td><td>143.75</td><td>593.75</td><td>6000</td><td>18750</td></tr>
  <tr><td>m5n.2xlarge <sup>1</sup></td><td>2300</td><td>4750</td><td>287.50</td><td>593.75</td><td>12000</td><td>18750</td></tr>
  <tr><td>m5n.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">18750</td></tr>
  <tr><td>m5n.8xlarge <sup>2</sup></td><td colspan="2">6800</td><td colspan="2">850.0</td><td colspan="2">30000</td></tr>
  <tr><td>m5n.12xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>m5n.16xlarge <sup>2</sup></td><td colspan="2">13600</td><td colspan="2">1700.0</td><td colspan="2">60000</td></tr>
  <tr><td>m5n.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>m5n.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>m5zn.large <sup>1</sup></td><td>800</td><td>3170</td><td>100.00</td><td>396.25</td><td>3333</td><td>13333</td></tr>
  <tr><td>m5zn.xlarge <sup>1</sup></td><td>1564</td><td>3170</td><td>195.50</td><td>396.25</td><td>6667</td><td>13333</td></tr>
  <tr><td>m5zn.2xlarge <sup>2</sup></td><td colspan="2">3170</td><td colspan="2">396.25</td><td colspan="2">13333</td></tr>
  <tr><td>m5zn.3xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>m5zn.6xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>m5zn.12xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>m5zn.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>m6a.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m6a.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m6a.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m6a.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m6a.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m6a.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m6a.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m6a.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m6a.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>m6a.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>m6a.metal <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>m6g.medium <sup>1</sup></td><td>315</td><td>4750</td><td>39.38</td><td>593.75</td><td>2500</td><td>20000</td></tr>
  <tr><td>m6g.large <sup>1</sup></td><td>630</td><td>4750</td><td>78.75</td><td>593.75</td><td>3600</td><td>20000</td></tr>
  <tr><td>m6g.xlarge <sup>1</sup></td><td>1188</td><td>4750</td><td>148.50</td><td>593.75</td><td>6000</td><td>20000</td></tr>
  <tr><td>m6g.2xlarge <sup>1</sup></td><td>2375</td><td>4750</td><td>296.88</td><td>593.75</td><td>12000</td><td>20000</td></tr>
  <tr><td>m6g.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>m6g.8xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>m6g.12xlarge <sup>2</sup></td><td colspan="2">14250</td><td colspan="2">1781.25</td><td colspan="2">50000</td></tr>
  <tr><td>m6g.16xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>m6g.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>m6gd.medium <sup>1</sup></td><td>315</td><td>4750</td><td>39.38</td><td>593.75</td><td>2500</td><td>20000</td></tr>
  <tr><td>m6gd.large <sup>1</sup></td><td>630</td><td>4750</td><td>78.75</td><td>593.75</td><td>3600</td><td>20000</td></tr>
  <tr><td>m6gd.xlarge <sup>1</sup></td><td>1188</td><td>4750</td><td>148.50</td><td>593.75</td><td>6000</td><td>20000</td></tr>
  <tr><td>m6gd.2xlarge <sup>1</sup></td><td>2375</td><td>4750</td><td>296.88</td><td>593.75</td><td>12000</td><td>20000</td></tr>
  <tr><td>m6gd.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>m6gd.8xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>m6gd.12xlarge <sup>2</sup></td><td colspan="2">14250</td><td colspan="2">1781.25</td><td colspan="2">50000</td></tr>
  <tr><td>m6gd.16xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>m6gd.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>m6i.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m6i.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m6i.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m6i.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m6i.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m6i.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m6i.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m6i.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m6i.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>m6i.metal <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>m6id.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m6id.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m6id.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m6id.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m6id.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m6id.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m6id.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m6id.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m6id.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>m6id.metal <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>m6idn.large <sup>1</sup></td><td>1562</td><td>25000</td><td>195.31</td><td>3125.00</td><td>6250</td><td>100000</td></tr>
  <tr><td>m6idn.xlarge <sup>1</sup></td><td>3125</td><td>25000</td><td>390.62</td><td>3125.00</td><td>12500</td><td>100000</td></tr>
  <tr><td>m6idn.2xlarge <sup>1</sup></td><td>6250</td><td>25000</td><td>781.25</td><td>3125.00</td><td>25000</td><td>100000</td></tr>
  <tr><td>m6idn.4xlarge <sup>1</sup></td><td>12500</td><td>25000</td><td>1562.50</td><td>3125.00</td><td>50000</td><td>100000</td></tr>
  <tr><td>m6idn.8xlarge <sup>2</sup></td><td colspan="2">25000</td><td colspan="2">3125.0</td><td colspan="2">100000</td></tr>
  <tr><td>m6idn.12xlarge <sup>2</sup></td><td colspan="2">37500</td><td colspan="2">4687.5</td><td colspan="2">150000</td></tr>
  <tr><td>m6idn.16xlarge <sup>2</sup></td><td colspan="2">50000</td><td colspan="2">6250.0</td><td colspan="2">200000</td></tr>
  <tr><td>m6idn.24xlarge <sup>2</sup></td><td colspan="2">75000</td><td colspan="2">9375.0</td><td colspan="2">300000</td></tr>
  <tr><td>m6idn.32xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">400000</td></tr>
  <tr><td>m6idn.metal <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">400000</td></tr>
  <tr><td>m6in.large <sup>1</sup></td><td>1562</td><td>25000</td><td>195.31</td><td>3125.00</td><td>6250</td><td>100000</td></tr>
  <tr><td>m6in.xlarge <sup>1</sup></td><td>3125</td><td>25000</td><td>390.62</td><td>3125.00</td><td>12500</td><td>100000</td></tr>
  <tr><td>m6in.2xlarge <sup>1</sup></td><td>6250</td><td>25000</td><td>781.25</td><td>3125.00</td><td>25000</td><td>100000</td></tr>
  <tr><td>m6in.4xlarge <sup>1</sup></td><td>12500</td><td>25000</td><td>1562.50</td><td>3125.00</td><td>50000</td><td>100000</td></tr>
  <tr><td>m6in.8xlarge <sup>2</sup></td><td colspan="2">25000</td><td colspan="2">3125.0</td><td colspan="2">100000</td></tr>
  <tr><td>m6in.12xlarge <sup>2</sup></td><td colspan="2">37500</td><td colspan="2">4687.5</td><td colspan="2">150000</td></tr>
  <tr><td>m6in.16xlarge <sup>2</sup></td><td colspan="2">50000</td><td colspan="2">6250.0</td><td colspan="2">200000</td></tr>
  <tr><td>m6in.24xlarge <sup>2</sup></td><td colspan="2">75000</td><td colspan="2">9375.0</td><td colspan="2">300000</td></tr>
  <tr><td>m6in.32xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">400000</td></tr>
  <tr><td>m6in.metal <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">400000</td></tr>
  <tr><td>m7a.medium <sup>1</sup></td><td>325</td><td>10000</td><td>40.62</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>m7a.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m7a.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m7a.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m7a.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m7a.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m7a.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m7a.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m7a.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m7a.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>m7a.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>m7a.metal-48xl <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>m7g.medium <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>m7g.large <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m7g.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m7g.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m7g.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m7g.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m7g.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m7g.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m7g.metal <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m7gd.medium <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>m7gd.large <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m7gd.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m7gd.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m7gd.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m7gd.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m7gd.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m7gd.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m7gd.metal <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m7i.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m7i.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m7i.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m7i.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m7i.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m7i.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m7i.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m7i.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m7i.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>m7i.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m7i.metal-48xl <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>m7i-flex.large <sup>1</sup></td><td>312</td><td>10000</td><td>39.06</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>m7i-flex.xlarge <sup>1</sup></td><td>625</td><td>10000</td><td>78.12</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m7i-flex.2xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m7i-flex.4xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m7i-flex.8xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m7i-flex.12xlarge <sup>1</sup></td><td>7500</td><td>15000</td><td>937.50</td><td>1875.00</td><td>30000</td><td>60000</td></tr>
  <tr><td>m7i-flex.16xlarge <sup>1</sup></td><td>10000</td><td>20000</td><td>1250.00</td><td>2500.00</td><td>40000</td><td>80000</td></tr>
  <tr><td>m8a.medium <sup>1</sup></td><td>325</td><td>10000</td><td>40.62</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>m8a.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m8a.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m8a.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m8a.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m8a.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m8a.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m8a.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m8a.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8a.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8a.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8a.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8azn.medium <sup>1</sup></td><td>625</td><td>15000</td><td>78.12</td><td>1875.00</td><td>2500</td><td>60000</td></tr>
  <tr><td>m8azn.large <sup>1</sup></td><td>1250</td><td>15000</td><td>156.25</td><td>1875.00</td><td>5000</td><td>60000</td></tr>
  <tr><td>m8azn.xlarge <sup>1</sup></td><td>2500</td><td>15000</td><td>312.50</td><td>1875.00</td><td>10000</td><td>60000</td></tr>
  <tr><td>m8azn.3xlarge <sup>1</sup></td><td>7500</td><td>15000</td><td>937.50</td><td>1875.00</td><td>30000</td><td>60000</td></tr>
  <tr><td>m8azn.6xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m8azn.12xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8azn.24xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8azn.metal-12xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8azn.metal-24xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8g.medium <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>m8g.large <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m8g.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m8g.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m8g.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m8g.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m8g.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m8g.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m8g.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8g.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8g.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8g.metal-48xl <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8gb.medium <sup>1</sup></td><td>1562</td><td>25000</td><td>195.31</td><td>3125.00</td><td>7500</td><td>120000</td></tr>
  <tr><td>m8gb.large <sup>1</sup></td><td>3125</td><td>25000</td><td>390.62</td><td>3125.00</td><td>15000</td><td>120000</td></tr>
  <tr><td>m8gb.xlarge <sup>1</sup></td><td>6250</td><td>25000</td><td>781.25</td><td>3125.00</td><td>30000</td><td>120000</td></tr>
  <tr><td>m8gb.2xlarge <sup>1</sup></td><td>12500</td><td>25000</td><td>1562.50</td><td>3125.00</td><td>60000</td><td>120000</td></tr>
  <tr><td>m8gb.4xlarge <sup>2</sup></td><td colspan="2">25000</td><td colspan="2">3125.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8gb.8xlarge <sup>2</sup></td><td colspan="2">50000</td><td colspan="2">6250.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8gb.12xlarge <sup>2</sup></td><td colspan="2">75000</td><td colspan="2">9375.0</td><td colspan="2">360000</td></tr>
  <tr><td>m8gb.16xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">480000</td></tr>
  <tr><td>m8gb.24xlarge <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>m8gb.48xlarge <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>m8gb.metal-24xl <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>m8gb.metal-48xl <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>m8gd.medium <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>m8gd.large <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m8gd.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m8gd.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m8gd.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m8gd.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m8gd.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m8gd.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m8gd.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8gd.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8gd.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8gd.metal-48xl <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8gn.medium <sup>1</sup></td><td>760</td><td>10000</td><td>95.00</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>m8gn.large <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>5000</td><td>40000</td></tr>
  <tr><td>m8gn.xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>10000</td><td>40000</td></tr>
  <tr><td>m8gn.2xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m8gn.4xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m8gn.8xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m8gn.12xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8gn.16xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>m8gn.24xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8gn.48xlarge <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>m8gn.metal-24xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8gn.metal-48xl <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>m8i.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m8i.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m8i.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m8i.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m8i.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m8i.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m8i.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m8i.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8i.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>m8i.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8i.96xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">480000</td></tr>
  <tr><td>m8i.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8i.metal-96xl <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">480000</td></tr>
  <tr><td>m8id.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m8id.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m8id.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m8id.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m8id.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m8id.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m8id.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m8id.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8id.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>m8id.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8id.96xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">480000</td></tr>
  <tr><td>m8id.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8id.metal-96xl <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">480000</td></tr>
  <tr><td>m8i-flex.large <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>m8i-flex.xlarge <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m8i-flex.2xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m8i-flex.4xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m8i-flex.8xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m8i-flex.12xlarge <sup>1</sup></td><td>7500</td><td>15000</td><td>937.50</td><td>1875.00</td><td>30000</td><td>60000</td></tr>
  <tr><td>m8i-flex.16xlarge <sup>1</sup></td><td>10000</td><td>20000</td><td>1250.00</td><td>2500.00</td><td>40000</td><td>80000</td></tr>
  <tr><td>m8in.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m8in.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m8in.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m8in.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m8in.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m8in.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m8in.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m8in.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8in.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>m8in.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8in.96xlarge <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>m8in.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8in.metal-96xl <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>m8idn.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m8idn.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m8idn.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m8idn.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m8idn.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m8idn.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m8idn.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>m8idn.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8idn.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>m8idn.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8idn.96xlarge <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>m8idn.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8idn.metal-96xl <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>m8ine.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>m8ine.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>m8ine.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>m8ine.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>m8ine.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>m8ine.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>m8ib.large <sup>1</sup></td><td>1563</td><td>25000</td><td>195.38</td><td>3125.00</td><td>7500</td><td>120000</td></tr>
  <tr><td>m8ib.xlarge <sup>1</sup></td><td>3125</td><td>25000</td><td>390.62</td><td>3125.00</td><td>15000</td><td>120000</td></tr>
  <tr><td>m8ib.2xlarge <sup>1</sup></td><td>6250</td><td>25000</td><td>781.25</td><td>3125.00</td><td>30000</td><td>120000</td></tr>
  <tr><td>m8ib.4xlarge <sup>1</sup></td><td>12500</td><td>25000</td><td>1562.50</td><td>3125.00</td><td>60000</td><td>120000</td></tr>
  <tr><td>m8ib.8xlarge <sup>2</sup></td><td colspan="2">25000</td><td colspan="2">3125.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8ib.12xlarge <sup>2</sup></td><td colspan="2">37500</td><td colspan="2">4687.5</td><td colspan="2">180000</td></tr>
  <tr><td>m8ib.16xlarge <sup>2</sup></td><td colspan="2">50000</td><td colspan="2">6250.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8ib.24xlarge <sup>2</sup></td><td colspan="2">75000</td><td colspan="2">9375.0</td><td colspan="2">360000</td></tr>
  <tr><td>m8ib.32xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">480000</td></tr>
  <tr><td>m8ib.48xlarge <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>m8ib.96xlarge <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>m8ib.metal-48xl <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>m8ib.metal-96xl <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>m8idb.large <sup>1</sup></td><td>1563</td><td>25000</td><td>195.38</td><td>3125.00</td><td>7500</td><td>120000</td></tr>
  <tr><td>m8idb.xlarge <sup>1</sup></td><td>3125</td><td>25000</td><td>390.62</td><td>3125.00</td><td>15000</td><td>120000</td></tr>
  <tr><td>m8idb.2xlarge <sup>1</sup></td><td>6250</td><td>25000</td><td>781.25</td><td>3125.00</td><td>30000</td><td>120000</td></tr>
  <tr><td>m8idb.4xlarge <sup>1</sup></td><td>12500</td><td>25000</td><td>1562.50</td><td>3125.00</td><td>60000</td><td>120000</td></tr>
  <tr><td>m8idb.8xlarge <sup>2</sup></td><td colspan="2">25000</td><td colspan="2">3125.0</td><td colspan="2">120000</td></tr>
  <tr><td>m8idb.12xlarge <sup>2</sup></td><td colspan="2">37500</td><td colspan="2">4687.5</td><td colspan="2">180000</td></tr>
  <tr><td>m8idb.16xlarge <sup>2</sup></td><td colspan="2">50000</td><td colspan="2">6250.0</td><td colspan="2">240000</td></tr>
  <tr><td>m8idb.24xlarge <sup>2</sup></td><td colspan="2">75000</td><td colspan="2">9375.0</td><td colspan="2">360000</td></tr>
  <tr><td>m8idb.32xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">480000</td></tr>
  <tr><td>m8idb.48xlarge <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>m8idb.96xlarge <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>m8idb.metal-48xl <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>m8idb.metal-96xl <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>m9g.medium <sup>1</sup></td><td>380</td><td>12000</td><td>47.50</td><td>1500.00</td><td>2500</td><td>48000</td></tr>
  <tr><td>m9g.large <sup>1</sup></td><td>760</td><td>12000</td><td>95.00</td><td>1500.00</td><td>3600</td><td>48000</td></tr>
  <tr><td>m9g.xlarge <sup>1</sup></td><td>1500</td><td>12000</td><td>187.50</td><td>1500.00</td><td>6000</td><td>48000</td></tr>
  <tr><td>m9g.2xlarge <sup>1</sup></td><td>3000</td><td>12000</td><td>375.00</td><td>1500.00</td><td>12000</td><td>48000</td></tr>
  <tr><td>m9g.4xlarge <sup>1</sup></td><td>6000</td><td>12000</td><td>750.00</td><td>1500.00</td><td>24000</td><td>48000</td></tr>
  <tr><td>m9g.8xlarge <sup>2</sup></td><td colspan="2">12000</td><td colspan="2">1500.0</td><td colspan="2">48000</td></tr>
  <tr><td>m9g.12xlarge <sup>2</sup></td><td colspan="2">18000</td><td colspan="2">2250.0</td><td colspan="2">72000</td></tr>
  <tr><td>m9g.16xlarge <sup>2</sup></td><td colspan="2">24000</td><td colspan="2">3000.0</td><td colspan="2">96000</td></tr>
  <tr><td>m9g.24xlarge <sup>2</sup></td><td colspan="2">36000</td><td colspan="2">4500.0</td><td colspan="2">144000</td></tr>
  <tr><td>m9g.48xlarge <sup>2</sup></td><td colspan="2">72000</td><td colspan="2">9000.0</td><td colspan="2">288000</td></tr>
  <tr><td>m9g.metal-48xl <sup>2</sup></td><td colspan="2">72000</td><td colspan="2">9000.0</td><td colspan="2">288000</td></tr>
  <tr><td>m9gd.medium <sup>1</sup></td><td>380</td><td>12000</td><td>47.50</td><td>1500.00</td><td>2500</td><td>48000</td></tr>
  <tr><td>m9gd.large <sup>1</sup></td><td>760</td><td>12000</td><td>95.00</td><td>1500.00</td><td>3600</td><td>48000</td></tr>
  <tr><td>m9gd.xlarge <sup>1</sup></td><td>1500</td><td>12000</td><td>187.50</td><td>1500.00</td><td>6000</td><td>48000</td></tr>
  <tr><td>m9gd.2xlarge <sup>1</sup></td><td>3000</td><td>12000</td><td>375.00</td><td>1500.00</td><td>12000</td><td>48000</td></tr>
  <tr><td>m9gd.4xlarge <sup>1</sup></td><td>6000</td><td>12000</td><td>750.00</td><td>1500.00</td><td>24000</td><td>48000</td></tr>
  <tr><td>m9gd.8xlarge <sup>2</sup></td><td colspan="2">12000</td><td colspan="2">1500.0</td><td colspan="2">48000</td></tr>
  <tr><td>m9gd.12xlarge <sup>2</sup></td><td colspan="2">18000</td><td colspan="2">2250.0</td><td colspan="2">72000</td></tr>
  <tr><td>m9gd.16xlarge <sup>2</sup></td><td colspan="2">24000</td><td colspan="2">3000.0</td><td colspan="2">96000</td></tr>
  <tr><td>m9gd.24xlarge <sup>2</sup></td><td colspan="2">36000</td><td colspan="2">4500.0</td><td colspan="2">144000</td></tr>
  <tr><td>m9gd.48xlarge <sup>2</sup></td><td colspan="2">72000</td><td colspan="2">9000.0</td><td colspan="2">288000</td></tr>
  <tr><td>m9gd.metal-48xl <sup>2</sup></td><td colspan="2">72000</td><td colspan="2">9000.0</td><td colspan="2">288000</td></tr>
  <tr><td>mac1.metal <sup>2</sup></td><td colspan="2">14000</td><td colspan="2">1750.0</td><td colspan="2">80000</td></tr>
  <tr><td>mac2.metal <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">55000</td></tr>
  <tr><td>mac2-m1ultra.metal <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">55000</td></tr>
  <tr><td>mac2-m2.metal <sup>2</sup></td><td colspan="2">8000</td><td colspan="2">1000.0</td><td colspan="2">55000</td></tr>
  <tr><td>mac2-m2pro.metal <sup>2</sup></td><td colspan="2">8000</td><td colspan="2">1000.0</td><td colspan="2">55000</td></tr>
  <tr><td>mac-m3ultra.metal <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">55000</td></tr>
  <tr><td>mac-m4.metal <sup>2</sup></td><td colspan="2">8000</td><td colspan="2">1000.0</td><td colspan="2">55000</td></tr>
  <tr><td>mac-m4pro.metal <sup>2</sup></td><td colspan="2">8000</td><td colspan="2">1000.0</td><td colspan="2">55000</td></tr>
  <tr><td>mac-m4max.metal <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">55000</td></tr>
  <tr><td>t3.nano <sup>1</sup></td><td>43</td><td>2085</td><td>5.38</td><td>260.62</td><td>250</td><td>11800</td></tr>
  <tr><td>t3.micro <sup>1</sup></td><td>87</td><td>2085</td><td>10.88</td><td>260.62</td><td>500</td><td>11800</td></tr>
  <tr><td>t3.small <sup>1</sup></td><td>174</td><td>2085</td><td>21.75</td><td>260.62</td><td>1000</td><td>11800</td></tr>
  <tr><td>t3.medium <sup>1</sup></td><td>347</td><td>2085</td><td>43.38</td><td>260.62</td><td>2000</td><td>11800</td></tr>
  <tr><td>t3.large <sup>1</sup></td><td>695</td><td>2780</td><td>86.88</td><td>347.50</td><td>4000</td><td>15700</td></tr>
  <tr><td>t3.xlarge <sup>1</sup></td><td>695</td><td>2780</td><td>86.88</td><td>347.50</td><td>4000</td><td>15700</td></tr>
  <tr><td>t3.2xlarge <sup>1</sup></td><td>695</td><td>2780</td><td>86.88</td><td>347.50</td><td>4000</td><td>15700</td></tr>
  <tr><td>t3a.nano <sup>1</sup></td><td>45</td><td>2085</td><td>5.62</td><td>260.62</td><td>250</td><td>11800</td></tr>
  <tr><td>t3a.micro <sup>1</sup></td><td>90</td><td>2085</td><td>11.25</td><td>260.62</td><td>500</td><td>11800</td></tr>
  <tr><td>t3a.small <sup>1</sup></td><td>175</td><td>2085</td><td>21.88</td><td>260.62</td><td>1000</td><td>11800</td></tr>
  <tr><td>t3a.medium <sup>1</sup></td><td>350</td><td>2085</td><td>43.75</td><td>260.62</td><td>2000</td><td>11800</td></tr>
  <tr><td>t3a.large <sup>1</sup></td><td>695</td><td>2780</td><td>86.88</td><td>347.50</td><td>4000</td><td>15700</td></tr>
  <tr><td>t3a.xlarge <sup>1</sup></td><td>695</td><td>2780</td><td>86.88</td><td>347.50</td><td>4000</td><td>15700</td></tr>
  <tr><td>t3a.2xlarge <sup>1</sup></td><td>695</td><td>2780</td><td>86.88</td><td>347.50</td><td>4000</td><td>15700</td></tr>
  <tr><td>t4g.nano <sup>1</sup></td><td>43</td><td>2085</td><td>5.38</td><td>260.62</td><td>250</td><td>11800</td></tr>
  <tr><td>t4g.micro <sup>1</sup></td><td>87</td><td>2085</td><td>10.88</td><td>260.62</td><td>500</td><td>11800</td></tr>
  <tr><td>t4g.small <sup>1</sup></td><td>174</td><td>2085</td><td>21.75</td><td>260.62</td><td>1000</td><td>11800</td></tr>
  <tr><td>t4g.medium <sup>1</sup></td><td>347</td><td>2085</td><td>43.38</td><td>260.62</td><td>2000</td><td>11800</td></tr>
  <tr><td>t4g.large <sup>1</sup></td><td>695</td><td>2780</td><td>86.88</td><td>347.50</td><td>4000</td><td>15700</td></tr>
  <tr><td>t4g.xlarge <sup>1</sup></td><td>695</td><td>2780</td><td>86.88</td><td>347.50</td><td>4000</td><td>15700</td></tr>
  <tr><td>t4g.2xlarge <sup>1</sup></td><td>695</td><td>2780</td><td>86.88</td><td>347.50</td><td>4000</td><td>15700</td></tr>
  <tr><td>t8i.nano <sup>1</sup></td><td>43</td><td>5000</td><td>5.38</td><td>625.00</td><td>250</td><td>20000</td></tr>
  <tr><td>t8i.micro <sup>1</sup></td><td>87</td><td>5000</td><td>10.88</td><td>625.00</td><td>500</td><td>20000</td></tr>
  <tr><td>t8i.small <sup>1</sup></td><td>174</td><td>5000</td><td>21.75</td><td>625.00</td><td>1500</td><td>20000</td></tr>
  <tr><td>t8i.medium <sup>1</sup></td><td>347</td><td>5000</td><td>43.38</td><td>625.00</td><td>2000</td><td>20000</td></tr>
  <tr><td>t9g.nano <sup>1</sup></td><td>43</td><td>6000</td><td>5.38</td><td>750.00</td><td>250</td><td>20000</td></tr>
  <tr><td>t9g.micro <sup>1</sup></td><td>87</td><td>6000</td><td>10.88</td><td>750.00</td><td>500</td><td>20000</td></tr>
  <tr><td>t9g.small <sup>1</sup></td><td>174</td><td>6000</td><td>21.75</td><td>750.00</td><td>1000</td><td>20000</td></tr>
  <tr><td>t9g.medium <sup>1</sup></td><td>347</td><td>6000</td><td>43.38</td><td>750.00</td><td>2000</td><td>20000</td></tr>
</tbody>
</table>

<sup>1</sup> These instances can sustain the maximum performance for 30 minutes at least once every 24 hours, after which they revert to their baseline performance.

<sup>2</sup> These instances can sustain their stated performance indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these instances.

### Compute optimized
<a name="current-compute-optimized"></a>

**Note**
C8a, C8g, C8gd, C8i, C8id, C8i-flex, C9g, C9gd instance types support configurable bandwidth weightings. With these instance types, you can optimize an instance's bandwidth for either networking performance or Amazon EBS performance. The following table shows the default Amazon EBS bandwidth performance for these instance types. For more information, see [EC2 instance bandwidth weighting configuration](configure-bandwidth-weighting.md).

<table>
<thead>
  <tr><th>Instance size</th><th>Baseline bandwidth (Mbps)</th><th>Maximum bandwidth (Mbps)</th><th>Baseline throughput (MB/s, 128 KiB I/O)</th><th>Maximum throughput (MB/s, 128 KiB I/O)</th><th>Baseline IOPS (16 KiB I/O)</th><th>Maximum IOPS (16 KiB I/O)</th></tr>
</thead>
<tbody>
  <tr><td>c4.large <sup>2</sup></td><td colspan="2">500</td><td colspan="2">62.5</td><td colspan="2">4000</td></tr>
  <tr><td>c4.xlarge <sup>2</sup></td><td colspan="2">750</td><td colspan="2">93.75</td><td colspan="2">6000</td></tr>
  <tr><td>c4.2xlarge <sup>2</sup></td><td colspan="2">1000</td><td colspan="2">125.0</td><td colspan="2">8000</td></tr>
  <tr><td>c4.4xlarge <sup>2</sup></td><td colspan="2">2000</td><td colspan="2">250.0</td><td colspan="2">16000</td></tr>
  <tr><td>c4.8xlarge <sup>2</sup></td><td colspan="2">4000</td><td colspan="2">500.0</td><td colspan="2">32000</td></tr>
  <tr><td>c5.large <sup>1</sup></td><td>650</td><td>4750</td><td>81.25</td><td>593.75</td><td>4000</td><td>20000</td></tr>
  <tr><td>c5.xlarge <sup>1</sup></td><td>1150</td><td>4750</td><td>143.75</td><td>593.75</td><td>6000</td><td>20000</td></tr>
  <tr><td>c5.2xlarge <sup>1</sup></td><td>2300</td><td>4750</td><td>287.50</td><td>593.75</td><td>10000</td><td>20000</td></tr>
  <tr><td>c5.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>c5.9xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>c5.12xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>c5.18xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>c5.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>c5.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>c5a.large <sup>1</sup></td><td>200</td><td>3170</td><td>25.00</td><td>396.25</td><td>800</td><td>13300</td></tr>
  <tr><td>c5a.xlarge <sup>1</sup></td><td>400</td><td>3170</td><td>50.00</td><td>396.25</td><td>1600</td><td>13300</td></tr>
  <tr><td>c5a.2xlarge <sup>1</sup></td><td>800</td><td>3170</td><td>100.00</td><td>396.25</td><td>3200</td><td>13300</td></tr>
  <tr><td>c5a.4xlarge <sup>1</sup></td><td>1580</td><td>3170</td><td>197.50</td><td>396.25</td><td>6600</td><td>13300</td></tr>
  <tr><td>c5a.8xlarge <sup>2</sup></td><td colspan="2">3170</td><td colspan="2">396.25</td><td colspan="2">13300</td></tr>
  <tr><td>c5a.12xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>c5a.16xlarge <sup>2</sup></td><td colspan="2">6300</td><td colspan="2">787.5</td><td colspan="2">26700</td></tr>
  <tr><td>c5a.24xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>c5ad.large <sup>1</sup></td><td>200</td><td>3170</td><td>25.00</td><td>396.25</td><td>800</td><td>13300</td></tr>
  <tr><td>c5ad.xlarge <sup>1</sup></td><td>400</td><td>3170</td><td>50.00</td><td>396.25</td><td>1600</td><td>13300</td></tr>
  <tr><td>c5ad.2xlarge <sup>1</sup></td><td>800</td><td>3170</td><td>100.00</td><td>396.25</td><td>3200</td><td>13300</td></tr>
  <tr><td>c5ad.4xlarge <sup>1</sup></td><td>1580</td><td>3170</td><td>197.50</td><td>396.25</td><td>6600</td><td>13300</td></tr>
  <tr><td>c5ad.8xlarge <sup>2</sup></td><td colspan="2">3170</td><td colspan="2">396.25</td><td colspan="2">13300</td></tr>
  <tr><td>c5ad.12xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>c5ad.16xlarge <sup>2</sup></td><td colspan="2">6300</td><td colspan="2">787.5</td><td colspan="2">26700</td></tr>
  <tr><td>c5ad.24xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>c5d.large <sup>1</sup></td><td>650</td><td>4750</td><td>81.25</td><td>593.75</td><td>4000</td><td>20000</td></tr>
  <tr><td>c5d.xlarge <sup>1</sup></td><td>1150</td><td>4750</td><td>143.75</td><td>593.75</td><td>6000</td><td>20000</td></tr>
  <tr><td>c5d.2xlarge <sup>1</sup></td><td>2300</td><td>4750</td><td>287.50</td><td>593.75</td><td>10000</td><td>20000</td></tr>
  <tr><td>c5d.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>c5d.9xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>c5d.12xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>c5d.18xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>c5d.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>c5d.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>c5n.large <sup>1</sup></td><td>650</td><td>4750</td><td>81.25</td><td>593.75</td><td>4000</td><td>20000</td></tr>
  <tr><td>c5n.xlarge <sup>1</sup></td><td>1150</td><td>4750</td><td>143.75</td><td>593.75</td><td>6000</td><td>20000</td></tr>
  <tr><td>c5n.2xlarge <sup>1</sup></td><td>2300</td><td>4750</td><td>287.50</td><td>593.75</td><td>10000</td><td>20000</td></tr>
  <tr><td>c5n.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>c5n.9xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>c5n.18xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>c5n.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>c6a.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c6a.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c6a.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c6a.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c6a.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c6a.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>c6a.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c6a.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c6a.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>c6a.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>c6a.metal <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>c6g.medium <sup>1</sup></td><td>315</td><td>4750</td><td>39.38</td><td>593.75</td><td>2500</td><td>20000</td></tr>
  <tr><td>c6g.large <sup>1</sup></td><td>630</td><td>4750</td><td>78.75</td><td>593.75</td><td>3600</td><td>20000</td></tr>
  <tr><td>c6g.xlarge <sup>1</sup></td><td>1188</td><td>4750</td><td>148.50</td><td>593.75</td><td>6000</td><td>20000</td></tr>
  <tr><td>c6g.2xlarge <sup>1</sup></td><td>2375</td><td>4750</td><td>296.88</td><td>593.75</td><td>12000</td><td>20000</td></tr>
  <tr><td>c6g.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>c6g.8xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>c6g.12xlarge <sup>2</sup></td><td colspan="2">14250</td><td colspan="2">1781.25</td><td colspan="2">50000</td></tr>
  <tr><td>c6g.16xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>c6g.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>c6gd.medium <sup>1</sup></td><td>315</td><td>4750</td><td>39.38</td><td>593.75</td><td>2500</td><td>20000</td></tr>
  <tr><td>c6gd.large <sup>1</sup></td><td>630</td><td>4750</td><td>78.75</td><td>593.75</td><td>3600</td><td>20000</td></tr>
  <tr><td>c6gd.xlarge <sup>1</sup></td><td>1188</td><td>4750</td><td>148.50</td><td>593.75</td><td>6000</td><td>20000</td></tr>
  <tr><td>c6gd.2xlarge <sup>1</sup></td><td>2375</td><td>4750</td><td>296.88</td><td>593.75</td><td>12000</td><td>20000</td></tr>
  <tr><td>c6gd.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>c6gd.8xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>c6gd.12xlarge <sup>2</sup></td><td colspan="2">14250</td><td colspan="2">1781.25</td><td colspan="2">50000</td></tr>
  <tr><td>c6gd.16xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>c6gd.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>c6gn.medium <sup>1</sup></td><td>760</td><td>9500</td><td>95.00</td><td>1187.50</td><td>2500</td><td>40000</td></tr>
  <tr><td>c6gn.large <sup>1</sup></td><td>1235</td><td>9500</td><td>154.38</td><td>1187.50</td><td>5000</td><td>40000</td></tr>
  <tr><td>c6gn.xlarge <sup>1</sup></td><td>2375</td><td>9500</td><td>296.88</td><td>1187.50</td><td>10000</td><td>40000</td></tr>
  <tr><td>c6gn.2xlarge <sup>1</sup></td><td>4750</td><td>9500</td><td>593.75</td><td>1187.50</td><td>20000</td><td>40000</td></tr>
  <tr><td>c6gn.4xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>c6gn.8xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>c6gn.12xlarge <sup>2</sup></td><td colspan="2">28500</td><td colspan="2">3562.5</td><td colspan="2">120000</td></tr>
  <tr><td>c6gn.16xlarge <sup>2</sup></td><td colspan="2">38000</td><td colspan="2">4750.0</td><td colspan="2">160000</td></tr>
  <tr><td>c6i.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c6i.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c6i.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c6i.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c6i.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c6i.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>c6i.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c6i.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c6i.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>c6i.metal <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>c6id.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c6id.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c6id.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c6id.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c6id.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c6id.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>c6id.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c6id.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c6id.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>c6id.metal <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>c6in.large <sup>1</sup></td><td>1562</td><td>25000</td><td>195.31</td><td>3125.00</td><td>6250</td><td>100000</td></tr>
  <tr><td>c6in.xlarge <sup>1</sup></td><td>3125</td><td>25000</td><td>390.62</td><td>3125.00</td><td>12500</td><td>100000</td></tr>
  <tr><td>c6in.2xlarge <sup>1</sup></td><td>6250</td><td>25000</td><td>781.25</td><td>3125.00</td><td>25000</td><td>100000</td></tr>
  <tr><td>c6in.4xlarge <sup>1</sup></td><td>12500</td><td>25000</td><td>1562.50</td><td>3125.00</td><td>50000</td><td>100000</td></tr>
  <tr><td>c6in.8xlarge <sup>2</sup></td><td colspan="2">25000</td><td colspan="2">3125.0</td><td colspan="2">100000</td></tr>
  <tr><td>c6in.12xlarge <sup>2</sup></td><td colspan="2">37500</td><td colspan="2">4687.5</td><td colspan="2">150000</td></tr>
  <tr><td>c6in.16xlarge <sup>2</sup></td><td colspan="2">50000</td><td colspan="2">6250.0</td><td colspan="2">200000</td></tr>
  <tr><td>c6in.24xlarge <sup>2</sup></td><td colspan="2">75000</td><td colspan="2">9375.0</td><td colspan="2">300000</td></tr>
  <tr><td>c6in.32xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">400000</td></tr>
  <tr><td>c6in.metal <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">400000</td></tr>
  <tr><td>c7a.medium <sup>1</sup></td><td>325</td><td>10000</td><td>40.62</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>c7a.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c7a.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c7a.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c7a.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c7a.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c7a.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>c7a.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c7a.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c7a.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>c7a.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>c7a.metal-48xl <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>c7g.medium <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>c7g.large <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c7g.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c7g.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c7g.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c7g.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c7g.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>c7g.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c7g.metal <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c7gd.medium <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>c7gd.large <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c7gd.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c7gd.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c7gd.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c7gd.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c7gd.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>c7gd.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c7gd.metal <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c7gn.medium <sup>1</sup></td><td>521</td><td>10000</td><td>65.12</td><td>1250.00</td><td>2083</td><td>40000</td></tr>
  <tr><td>c7gn.large <sup>1</sup></td><td>1042</td><td>10000</td><td>130.25</td><td>1250.00</td><td>4167</td><td>40000</td></tr>
  <tr><td>c7gn.xlarge <sup>1</sup></td><td>2083</td><td>10000</td><td>260.38</td><td>1250.00</td><td>8333</td><td>40000</td></tr>
  <tr><td>c7gn.2xlarge <sup>1</sup></td><td>4167</td><td>10000</td><td>520.88</td><td>1250.00</td><td>16667</td><td>40000</td></tr>
  <tr><td>c7gn.4xlarge <sup>1</sup></td><td>8333</td><td>10000</td><td>1041.62</td><td>1250.00</td><td>33333</td><td>40000</td></tr>
  <tr><td>c7gn.8xlarge <sup>1</sup></td><td>16667</td><td>20000</td><td>2083.38</td><td>2500.00</td><td>66667</td><td>80000</td></tr>
  <tr><td>c7gn.12xlarge <sup>1</sup></td><td>25000</td><td>30000</td><td>3125.00</td><td>3750.00</td><td>100000</td><td>120000</td></tr>
  <tr><td>c7gn.16xlarge <sup>1</sup></td><td>33333</td><td>40000</td><td>4166.62</td><td>5000.00</td><td>133333</td><td>160000</td></tr>
  <tr><td>c7gn.metal <sup>1</sup></td><td>33333</td><td>40000</td><td>4166.62</td><td>5000.00</td><td>133333</td><td>160000</td></tr>
  <tr><td>c7i.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c7i.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c7i.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c7i.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c7i.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c7i.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>c7i.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c7i.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c7i.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>c7i.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c7i.metal-48xl <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>c7i-flex.large <sup>1</sup></td><td>312</td><td>10000</td><td>39.06</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>c7i-flex.xlarge <sup>1</sup></td><td>625</td><td>10000</td><td>78.12</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c7i-flex.2xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c7i-flex.4xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c7i-flex.8xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c7i-flex.12xlarge <sup>1</sup></td><td>7500</td><td>15000</td><td>937.50</td><td>1875.00</td><td>30000</td><td>60000</td></tr>
  <tr><td>c7i-flex.16xlarge <sup>1</sup></td><td>10000</td><td>20000</td><td>1250.00</td><td>2500.00</td><td>40000</td><td>80000</td></tr>
  <tr><td>c8a.medium <sup>1</sup></td><td>325</td><td>10000</td><td>40.62</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>c8a.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c8a.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c8a.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c8a.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c8a.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c8a.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>c8a.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c8a.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c8a.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8a.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c8a.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8g.medium <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>c8g.large <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c8g.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c8g.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c8g.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c8g.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c8g.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>c8g.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c8g.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c8g.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8g.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c8g.metal-48xl <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8gb.medium <sup>1</sup></td><td>1562</td><td>25000</td><td>195.31</td><td>3125.00</td><td>7500</td><td>120000</td></tr>
  <tr><td>c8gb.large <sup>1</sup></td><td>3125</td><td>25000</td><td>390.62</td><td>3125.00</td><td>15000</td><td>120000</td></tr>
  <tr><td>c8gb.xlarge <sup>1</sup></td><td>6250</td><td>25000</td><td>781.25</td><td>3125.00</td><td>30000</td><td>120000</td></tr>
  <tr><td>c8gb.2xlarge <sup>1</sup></td><td>12500</td><td>25000</td><td>1562.50</td><td>3125.00</td><td>60000</td><td>120000</td></tr>
  <tr><td>c8gb.4xlarge <sup>2</sup></td><td colspan="2">25000</td><td colspan="2">3125.0</td><td colspan="2">120000</td></tr>
  <tr><td>c8gb.8xlarge <sup>2</sup></td><td colspan="2">50000</td><td colspan="2">6250.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8gb.12xlarge <sup>2</sup></td><td colspan="2">75000</td><td colspan="2">9375.0</td><td colspan="2">360000</td></tr>
  <tr><td>c8gb.16xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">480000</td></tr>
  <tr><td>c8gb.24xlarge <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>c8gb.48xlarge <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>c8gb.metal-24xl <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>c8gb.metal-48xl <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>c8gd.medium <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>c8gd.large <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c8gd.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c8gd.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c8gd.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c8gd.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c8gd.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>c8gd.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c8gd.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c8gd.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8gd.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c8gd.metal-48xl <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8gn.medium <sup>1</sup></td><td>760</td><td>10000</td><td>95.00</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>c8gn.large <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>5000</td><td>40000</td></tr>
  <tr><td>c8gn.xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>10000</td><td>40000</td></tr>
  <tr><td>c8gn.2xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c8gn.4xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c8gn.8xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c8gn.12xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c8gn.16xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>c8gn.24xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8gn.48xlarge <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>c8gn.metal-24xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8gn.metal-48xl <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>c8i.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c8i.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c8i.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c8i.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c8i.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c8i.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>c8i.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c8i.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c8i.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>c8i.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8i.96xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">480000</td></tr>
  <tr><td>c8i.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8i.metal-96xl <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">480000</td></tr>
  <tr><td>c8id.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c8id.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c8id.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c8id.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c8id.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c8id.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>c8id.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c8id.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c8id.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>c8id.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8id.96xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">480000</td></tr>
  <tr><td>c8id.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8id.metal-96xl <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">480000</td></tr>
  <tr><td>c8i-flex.large <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>c8i-flex.xlarge <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c8i-flex.2xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c8i-flex.4xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c8i-flex.8xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c8i-flex.12xlarge <sup>1</sup></td><td>7500</td><td>15000</td><td>937.50</td><td>1875.00</td><td>30000</td><td>60000</td></tr>
  <tr><td>c8i-flex.16xlarge <sup>1</sup></td><td>10000</td><td>20000</td><td>1250.00</td><td>2500.00</td><td>40000</td><td>80000</td></tr>
  <tr><td>c8in.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c8in.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c8in.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c8in.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c8in.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c8in.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>c8in.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>c8in.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>c8in.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>c8in.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8in.96xlarge <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>c8in.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8in.metal-96xl <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>c8ine.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>c8ine.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>c8ine.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>c8ine.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>c8ine.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>c8ine.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>c8ib.large <sup>1</sup></td><td>1563</td><td>25000</td><td>195.38</td><td>3125.00</td><td>7500</td><td>120000</td></tr>
  <tr><td>c8ib.xlarge <sup>1</sup></td><td>3125</td><td>25000</td><td>390.62</td><td>3125.00</td><td>15000</td><td>120000</td></tr>
  <tr><td>c8ib.2xlarge <sup>1</sup></td><td>6250</td><td>25000</td><td>781.25</td><td>3125.00</td><td>30000</td><td>120000</td></tr>
  <tr><td>c8ib.4xlarge <sup>1</sup></td><td>12500</td><td>25000</td><td>1562.50</td><td>3125.00</td><td>60000</td><td>120000</td></tr>
  <tr><td>c8ib.8xlarge <sup>2</sup></td><td colspan="2">25000</td><td colspan="2">3125.0</td><td colspan="2">120000</td></tr>
  <tr><td>c8ib.12xlarge <sup>2</sup></td><td colspan="2">37500</td><td colspan="2">4687.5</td><td colspan="2">180000</td></tr>
  <tr><td>c8ib.16xlarge <sup>2</sup></td><td colspan="2">50000</td><td colspan="2">6250.0</td><td colspan="2">240000</td></tr>
  <tr><td>c8ib.24xlarge <sup>2</sup></td><td colspan="2">75000</td><td colspan="2">9375.0</td><td colspan="2">360000</td></tr>
  <tr><td>c8ib.32xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">480000</td></tr>
  <tr><td>c8ib.48xlarge <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>c8ib.96xlarge <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>c8ib.metal-48xl <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>c8ib.metal-96xl <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>c9g.medium <sup>1</sup></td><td>380</td><td>12000</td><td>47.50</td><td>1500.00</td><td>2500</td><td>48000</td></tr>
  <tr><td>c9g.large <sup>1</sup></td><td>760</td><td>12000</td><td>95.00</td><td>1500.00</td><td>3600</td><td>48000</td></tr>
  <tr><td>c9g.xlarge <sup>1</sup></td><td>1500</td><td>12000</td><td>187.50</td><td>1500.00</td><td>6000</td><td>48000</td></tr>
  <tr><td>c9g.2xlarge <sup>1</sup></td><td>3000</td><td>12000</td><td>375.00</td><td>1500.00</td><td>12000</td><td>48000</td></tr>
  <tr><td>c9g.4xlarge <sup>1</sup></td><td>6000</td><td>12000</td><td>750.00</td><td>1500.00</td><td>24000</td><td>48000</td></tr>
  <tr><td>c9g.8xlarge <sup>2</sup></td><td colspan="2">12000</td><td colspan="2">1500.0</td><td colspan="2">48000</td></tr>
  <tr><td>c9g.12xlarge <sup>2</sup></td><td colspan="2">18000</td><td colspan="2">2250.0</td><td colspan="2">72000</td></tr>
  <tr><td>c9g.16xlarge <sup>2</sup></td><td colspan="2">24000</td><td colspan="2">3000.0</td><td colspan="2">96000</td></tr>
  <tr><td>c9g.24xlarge <sup>2</sup></td><td colspan="2">36000</td><td colspan="2">4500.0</td><td colspan="2">144000</td></tr>
  <tr><td>c9g.48xlarge <sup>2</sup></td><td colspan="2">72000</td><td colspan="2">9000.0</td><td colspan="2">288000</td></tr>
  <tr><td>c9g.metal-48xl <sup>2</sup></td><td colspan="2">72000</td><td colspan="2">9000.0</td><td colspan="2">288000</td></tr>
  <tr><td>c9gd.medium <sup>1</sup></td><td>380</td><td>12000</td><td>47.50</td><td>1500.00</td><td>2500</td><td>48000</td></tr>
  <tr><td>c9gd.large <sup>1</sup></td><td>760</td><td>12000</td><td>95.00</td><td>1500.00</td><td>3600</td><td>48000</td></tr>
  <tr><td>c9gd.xlarge <sup>1</sup></td><td>1500</td><td>12000</td><td>187.50</td><td>1500.00</td><td>6000</td><td>48000</td></tr>
  <tr><td>c9gd.2xlarge <sup>1</sup></td><td>3000</td><td>12000</td><td>375.00</td><td>1500.00</td><td>12000</td><td>48000</td></tr>
  <tr><td>c9gd.4xlarge <sup>1</sup></td><td>6000</td><td>12000</td><td>750.00</td><td>1500.00</td><td>24000</td><td>48000</td></tr>
  <tr><td>c9gd.8xlarge <sup>2</sup></td><td colspan="2">12000</td><td colspan="2">1500.0</td><td colspan="2">48000</td></tr>
  <tr><td>c9gd.12xlarge <sup>2</sup></td><td colspan="2">18000</td><td colspan="2">2250.0</td><td colspan="2">72000</td></tr>
  <tr><td>c9gd.16xlarge <sup>2</sup></td><td colspan="2">24000</td><td colspan="2">3000.0</td><td colspan="2">96000</td></tr>
  <tr><td>c9gd.24xlarge <sup>2</sup></td><td colspan="2">36000</td><td colspan="2">4500.0</td><td colspan="2">144000</td></tr>
  <tr><td>c9gd.48xlarge <sup>2</sup></td><td colspan="2">72000</td><td colspan="2">9000.0</td><td colspan="2">288000</td></tr>
  <tr><td>c9gd.metal-48xl <sup>2</sup></td><td colspan="2">72000</td><td colspan="2">9000.0</td><td colspan="2">288000</td></tr>
</tbody>
</table>

<sup>1</sup> These instances can sustain the maximum performance for 30 minutes at least once every 24 hours, after which they revert to their baseline performance.

<sup>2</sup> These instances can sustain their stated performance indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these instances.

### Memory optimized
<a name="current-memory-optimized"></a>

**Note**
R8a, R8g, R8gd, R8i, R8id, R8i-flex, R9g, R9gd, X8g, X8aedz, X8i instance types support configurable bandwidth weightings. With these instance types, you can optimize an instance's bandwidth for either networking performance or Amazon EBS performance. The following table shows the default Amazon EBS bandwidth performance for these instance types. For more information, see [EC2 instance bandwidth weighting configuration](configure-bandwidth-weighting.md).
For maximum IOPS performance with U7i instances, we recommend that you use io2 BlockExpress volumes.

<table>
<thead>
  <tr><th>Instance size</th><th>Baseline bandwidth (Mbps)</th><th>Maximum bandwidth (Mbps)</th><th>Baseline throughput (MB/s, 128 KiB I/O)</th><th>Maximum throughput (MB/s, 128 KiB I/O)</th><th>Baseline IOPS (16 KiB I/O)</th><th>Maximum IOPS (16 KiB I/O)</th></tr>
</thead>
<tbody>
  <tr><td>r4.large <sup>2</sup></td><td colspan="2">425</td><td colspan="2">53.125</td><td colspan="2">3000</td></tr>
  <tr><td>r4.xlarge <sup>2</sup></td><td colspan="2">850</td><td colspan="2">106.25</td><td colspan="2">6000</td></tr>
  <tr><td>r4.2xlarge <sup>2</sup></td><td colspan="2">1700</td><td colspan="2">212.5</td><td colspan="2">12000</td></tr>
  <tr><td>r4.4xlarge <sup>2</sup></td><td colspan="2">3500</td><td colspan="2">437.5</td><td colspan="2">18750</td></tr>
  <tr><td>r4.8xlarge <sup>2</sup></td><td colspan="2">7000</td><td colspan="2">875.0</td><td colspan="2">37500</td></tr>
  <tr><td>r4.16xlarge <sup>2</sup></td><td colspan="2">14000</td><td colspan="2">1750.0</td><td colspan="2">75000</td></tr>
  <tr><td>r5.large <sup>1</sup></td><td>650</td><td>4750</td><td>81.25</td><td>593.75</td><td>3600</td><td>18750</td></tr>
  <tr><td>r5.xlarge <sup>1</sup></td><td>1150</td><td>4750</td><td>143.75</td><td>593.75</td><td>6000</td><td>18750</td></tr>
  <tr><td>r5.2xlarge <sup>1</sup></td><td>2300</td><td>4750</td><td>287.50</td><td>593.75</td><td>12000</td><td>18750</td></tr>
  <tr><td>r5.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">18750</td></tr>
  <tr><td>r5.8xlarge <sup>2</sup></td><td colspan="2">6800</td><td colspan="2">850.0</td><td colspan="2">30000</td></tr>
  <tr><td>r5.12xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>r5.16xlarge <sup>2</sup></td><td colspan="2">13600</td><td colspan="2">1700.0</td><td colspan="2">60000</td></tr>
  <tr><td>r5.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>r5.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>r5a.large <sup>1</sup></td><td>650</td><td>2880</td><td>81.25</td><td>360.00</td><td>3600</td><td>16000</td></tr>
  <tr><td>r5a.xlarge <sup>1</sup></td><td>1085</td><td>2880</td><td>135.62</td><td>360.00</td><td>6000</td><td>16000</td></tr>
  <tr><td>r5a.2xlarge <sup>1</sup></td><td>1580</td><td>2880</td><td>197.50</td><td>360.00</td><td>8333</td><td>16000</td></tr>
  <tr><td>r5a.4xlarge <sup>2</sup></td><td colspan="2">2880</td><td colspan="2">360.0</td><td colspan="2">16000</td></tr>
  <tr><td>r5a.8xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>r5a.12xlarge <sup>2</sup></td><td colspan="2">6780</td><td colspan="2">847.5</td><td colspan="2">30000</td></tr>
  <tr><td>r5a.16xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>r5a.24xlarge <sup>2</sup></td><td colspan="2">13570</td><td colspan="2">1696.25</td><td colspan="2">60000</td></tr>
  <tr><td>r5ad.large <sup>1</sup></td><td>650</td><td>2880</td><td>81.25</td><td>360.00</td><td>3600</td><td>16000</td></tr>
  <tr><td>r5ad.xlarge <sup>1</sup></td><td>1085</td><td>2880</td><td>135.62</td><td>360.00</td><td>6000</td><td>16000</td></tr>
  <tr><td>r5ad.2xlarge <sup>1</sup></td><td>1580</td><td>2880</td><td>197.50</td><td>360.00</td><td>8333</td><td>16000</td></tr>
  <tr><td>r5ad.4xlarge <sup>2</sup></td><td colspan="2">2880</td><td colspan="2">360.0</td><td colspan="2">16000</td></tr>
  <tr><td>r5ad.8xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>r5ad.12xlarge <sup>2</sup></td><td colspan="2">6780</td><td colspan="2">847.5</td><td colspan="2">30000</td></tr>
  <tr><td>r5ad.16xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>r5ad.24xlarge <sup>2</sup></td><td colspan="2">13570</td><td colspan="2">1696.25</td><td colspan="2">60000</td></tr>
  <tr><td>r5b.large <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>5417</td><td>43333</td></tr>
  <tr><td>r5b.xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>10833</td><td>43333</td></tr>
  <tr><td>r5b.2xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>21667</td><td>43333</td></tr>
  <tr><td>r5b.4xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">43333</td></tr>
  <tr><td>r5b.8xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">86667</td></tr>
  <tr><td>r5b.12xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">130000</td></tr>
  <tr><td>r5b.16xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">173333</td></tr>
  <tr><td>r5b.24xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">260000</td></tr>
  <tr><td>r5b.metal <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">260000</td></tr>
  <tr><td>r5d.large <sup>1</sup></td><td>650</td><td>4750</td><td>81.25</td><td>593.75</td><td>3600</td><td>18750</td></tr>
  <tr><td>r5d.xlarge <sup>1</sup></td><td>1150</td><td>4750</td><td>143.75</td><td>593.75</td><td>6000</td><td>18750</td></tr>
  <tr><td>r5d.2xlarge <sup>1</sup></td><td>2300</td><td>4750</td><td>287.50</td><td>593.75</td><td>12000</td><td>18750</td></tr>
  <tr><td>r5d.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">18750</td></tr>
  <tr><td>r5d.8xlarge <sup>2</sup></td><td colspan="2">6800</td><td colspan="2">850.0</td><td colspan="2">30000</td></tr>
  <tr><td>r5d.12xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>r5d.16xlarge <sup>2</sup></td><td colspan="2">13600</td><td colspan="2">1700.0</td><td colspan="2">60000</td></tr>
  <tr><td>r5d.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>r5d.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>r5dn.large <sup>1</sup></td><td>650</td><td>4750</td><td>81.25</td><td>593.75</td><td>3600</td><td>18750</td></tr>
  <tr><td>r5dn.xlarge <sup>1</sup></td><td>1150</td><td>4750</td><td>143.75</td><td>593.75</td><td>6000</td><td>18750</td></tr>
  <tr><td>r5dn.2xlarge <sup>1</sup></td><td>2300</td><td>4750</td><td>287.50</td><td>593.75</td><td>12000</td><td>18750</td></tr>
  <tr><td>r5dn.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">18750</td></tr>
  <tr><td>r5dn.8xlarge <sup>2</sup></td><td colspan="2">6800</td><td colspan="2">850.0</td><td colspan="2">30000</td></tr>
  <tr><td>r5dn.12xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>r5dn.16xlarge <sup>2</sup></td><td colspan="2">13600</td><td colspan="2">1700.0</td><td colspan="2">60000</td></tr>
  <tr><td>r5dn.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>r5dn.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>r5n.large <sup>1</sup></td><td>650</td><td>4750</td><td>81.25</td><td>593.75</td><td>3600</td><td>18750</td></tr>
  <tr><td>r5n.xlarge <sup>1</sup></td><td>1150</td><td>4750</td><td>143.75</td><td>593.75</td><td>6000</td><td>18750</td></tr>
  <tr><td>r5n.2xlarge <sup>1</sup></td><td>2300</td><td>4750</td><td>287.50</td><td>593.75</td><td>12000</td><td>18750</td></tr>
  <tr><td>r5n.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">18750</td></tr>
  <tr><td>r5n.8xlarge <sup>2</sup></td><td colspan="2">6800</td><td colspan="2">850.0</td><td colspan="2">30000</td></tr>
  <tr><td>r5n.12xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>r5n.16xlarge <sup>2</sup></td><td colspan="2">13600</td><td colspan="2">1700.0</td><td colspan="2">60000</td></tr>
  <tr><td>r5n.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>r5n.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>r6a.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r6a.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r6a.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r6a.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r6a.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r6a.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>r6a.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r6a.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r6a.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>r6a.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>r6a.metal <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>r6g.medium <sup>1</sup></td><td>315</td><td>4750</td><td>39.38</td><td>593.75</td><td>2500</td><td>20000</td></tr>
  <tr><td>r6g.large <sup>1</sup></td><td>630</td><td>4750</td><td>78.75</td><td>593.75</td><td>3600</td><td>20000</td></tr>
  <tr><td>r6g.xlarge <sup>1</sup></td><td>1188</td><td>4750</td><td>148.50</td><td>593.75</td><td>6000</td><td>20000</td></tr>
  <tr><td>r6g.2xlarge <sup>1</sup></td><td>2375</td><td>4750</td><td>296.88</td><td>593.75</td><td>12000</td><td>20000</td></tr>
  <tr><td>r6g.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>r6g.8xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>r6g.12xlarge <sup>2</sup></td><td colspan="2">14250</td><td colspan="2">1781.25</td><td colspan="2">50000</td></tr>
  <tr><td>r6g.16xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>r6g.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>r6gd.medium <sup>1</sup></td><td>315</td><td>4750</td><td>39.38</td><td>593.75</td><td>2500</td><td>20000</td></tr>
  <tr><td>r6gd.large <sup>1</sup></td><td>630</td><td>4750</td><td>78.75</td><td>593.75</td><td>3600</td><td>20000</td></tr>
  <tr><td>r6gd.xlarge <sup>1</sup></td><td>1188</td><td>4750</td><td>148.50</td><td>593.75</td><td>6000</td><td>20000</td></tr>
  <tr><td>r6gd.2xlarge <sup>1</sup></td><td>2375</td><td>4750</td><td>296.88</td><td>593.75</td><td>12000</td><td>20000</td></tr>
  <tr><td>r6gd.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>r6gd.8xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>r6gd.12xlarge <sup>2</sup></td><td colspan="2">14250</td><td colspan="2">1781.25</td><td colspan="2">50000</td></tr>
  <tr><td>r6gd.16xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>r6gd.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>r6i.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r6i.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r6i.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r6i.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r6i.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r6i.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>r6i.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r6i.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r6i.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>r6i.metal <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>r6id.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r6id.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r6id.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r6id.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r6id.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r6id.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>r6id.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r6id.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r6id.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>r6id.metal <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>r6idn.large <sup>1</sup></td><td>1562</td><td>25000</td><td>195.31</td><td>3125.00</td><td>6250</td><td>100000</td></tr>
  <tr><td>r6idn.xlarge <sup>1</sup></td><td>3125</td><td>25000</td><td>390.62</td><td>3125.00</td><td>12500</td><td>100000</td></tr>
  <tr><td>r6idn.2xlarge <sup>1</sup></td><td>6250</td><td>25000</td><td>781.25</td><td>3125.00</td><td>25000</td><td>100000</td></tr>
  <tr><td>r6idn.4xlarge <sup>1</sup></td><td>12500</td><td>25000</td><td>1562.50</td><td>3125.00</td><td>50000</td><td>100000</td></tr>
  <tr><td>r6idn.8xlarge <sup>2</sup></td><td colspan="2">25000</td><td colspan="2">3125.0</td><td colspan="2">100000</td></tr>
  <tr><td>r6idn.12xlarge <sup>2</sup></td><td colspan="2">37500</td><td colspan="2">4687.5</td><td colspan="2">150000</td></tr>
  <tr><td>r6idn.16xlarge <sup>2</sup></td><td colspan="2">50000</td><td colspan="2">6250.0</td><td colspan="2">200000</td></tr>
  <tr><td>r6idn.24xlarge <sup>2</sup></td><td colspan="2">75000</td><td colspan="2">9375.0</td><td colspan="2">300000</td></tr>
  <tr><td>r6idn.32xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">400000</td></tr>
  <tr><td>r6idn.metal <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">400000</td></tr>
  <tr><td>r6in.large <sup>1</sup></td><td>1562</td><td>25000</td><td>195.31</td><td>3125.00</td><td>6250</td><td>100000</td></tr>
  <tr><td>r6in.xlarge <sup>1</sup></td><td>3125</td><td>25000</td><td>390.62</td><td>3125.00</td><td>12500</td><td>100000</td></tr>
  <tr><td>r6in.2xlarge <sup>1</sup></td><td>6250</td><td>25000</td><td>781.25</td><td>3125.00</td><td>25000</td><td>100000</td></tr>
  <tr><td>r6in.4xlarge <sup>1</sup></td><td>12500</td><td>25000</td><td>1562.50</td><td>3125.00</td><td>50000</td><td>100000</td></tr>
  <tr><td>r6in.8xlarge <sup>2</sup></td><td colspan="2">25000</td><td colspan="2">3125.0</td><td colspan="2">100000</td></tr>
  <tr><td>r6in.12xlarge <sup>2</sup></td><td colspan="2">37500</td><td colspan="2">4687.5</td><td colspan="2">150000</td></tr>
  <tr><td>r6in.16xlarge <sup>2</sup></td><td colspan="2">50000</td><td colspan="2">6250.0</td><td colspan="2">200000</td></tr>
  <tr><td>r6in.24xlarge <sup>2</sup></td><td colspan="2">75000</td><td colspan="2">9375.0</td><td colspan="2">300000</td></tr>
  <tr><td>r6in.32xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">400000</td></tr>
  <tr><td>r6in.metal <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">400000</td></tr>
  <tr><td>r7a.medium <sup>1</sup></td><td>325</td><td>10000</td><td>40.62</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>r7a.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r7a.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r7a.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r7a.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r7a.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r7a.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>r7a.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r7a.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r7a.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>r7a.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>r7a.metal-48xl <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>r7g.medium <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>r7g.large <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r7g.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r7g.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r7g.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r7g.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r7g.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>r7g.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r7g.metal <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r7gd.medium <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>r7gd.large <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r7gd.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r7gd.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r7gd.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r7gd.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r7gd.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>r7gd.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r7gd.metal <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r7i.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r7i.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r7i.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r7i.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r7i.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r7i.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>r7i.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r7i.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r7i.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>r7i.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r7i.metal-48xl <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>r7iz.large <sup>1</sup></td><td>792</td><td>10000</td><td>99.00</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r7iz.xlarge <sup>1</sup></td><td>1584</td><td>10000</td><td>198.00</td><td>1250.00</td><td>6667</td><td>40000</td></tr>
  <tr><td>r7iz.2xlarge <sup>1</sup></td><td>3168</td><td>10000</td><td>396.00</td><td>1250.00</td><td>13333</td><td>40000</td></tr>
  <tr><td>r7iz.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r7iz.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r7iz.12xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">76000</td></tr>
  <tr><td>r7iz.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r7iz.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>r7iz.metal-16xl <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r7iz.metal-32xl <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>r8a.medium <sup>1</sup></td><td>325</td><td>10000</td><td>40.62</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>r8a.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r8a.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r8a.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r8a.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r8a.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r8a.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>r8a.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r8a.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r8a.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8a.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r8a.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8g.medium <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>r8g.large <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r8g.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r8g.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r8g.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r8g.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r8g.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>r8g.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r8g.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r8g.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8g.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r8g.metal-48xl <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8gb.medium <sup>1</sup></td><td>1562</td><td>25000</td><td>195.31</td><td>3125.00</td><td>7500</td><td>120000</td></tr>
  <tr><td>r8gb.large <sup>1</sup></td><td>3125</td><td>25000</td><td>390.62</td><td>3125.00</td><td>15000</td><td>120000</td></tr>
  <tr><td>r8gb.xlarge <sup>1</sup></td><td>6250</td><td>25000</td><td>781.25</td><td>3125.00</td><td>30000</td><td>120000</td></tr>
  <tr><td>r8gb.2xlarge <sup>1</sup></td><td>12500</td><td>25000</td><td>1562.50</td><td>3125.00</td><td>60000</td><td>120000</td></tr>
  <tr><td>r8gb.4xlarge <sup>2</sup></td><td colspan="2">25000</td><td colspan="2">3125.0</td><td colspan="2">120000</td></tr>
  <tr><td>r8gb.8xlarge <sup>2</sup></td><td colspan="2">50000</td><td colspan="2">6250.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8gb.12xlarge <sup>2</sup></td><td colspan="2">75000</td><td colspan="2">9375.0</td><td colspan="2">360000</td></tr>
  <tr><td>r8gb.16xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">480000</td></tr>
  <tr><td>r8gb.24xlarge <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>r8gb.48xlarge <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>r8gb.metal-24xl <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>r8gb.metal-48xl <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>r8gd.medium <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>r8gd.large <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r8gd.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r8gd.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r8gd.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r8gd.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r8gd.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>r8gd.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r8gd.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r8gd.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8gd.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r8gd.metal-48xl <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8gn.medium <sup>1</sup></td><td>760</td><td>10000</td><td>95.00</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>r8gn.large <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>5000</td><td>40000</td></tr>
  <tr><td>r8gn.xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>10000</td><td>40000</td></tr>
  <tr><td>r8gn.2xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r8gn.4xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r8gn.8xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r8gn.12xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r8gn.16xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>r8gn.24xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8gn.48xlarge <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>r8gn.metal-24xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8gn.metal-48xl <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>r8i.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r8i.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r8i.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r8i.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r8i.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r8i.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>r8i.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r8i.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r8i.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>r8i.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8i.96xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">480000</td></tr>
  <tr><td>r8i.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8i.metal-96xl <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">480000</td></tr>
  <tr><td>r8id.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r8id.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r8id.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r8id.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r8id.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r8id.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>r8id.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r8id.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r8id.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>r8id.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8id.96xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">480000</td></tr>
  <tr><td>r8id.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8id.metal-96xl <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">480000</td></tr>
  <tr><td>r8i-flex.large <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>r8i-flex.xlarge <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r8i-flex.2xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r8i-flex.4xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r8i-flex.8xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r8i-flex.12xlarge <sup>1</sup></td><td>7500</td><td>15000</td><td>937.50</td><td>1875.00</td><td>30000</td><td>60000</td></tr>
  <tr><td>r8i-flex.16xlarge <sup>1</sup></td><td>10000</td><td>20000</td><td>1250.00</td><td>2500.00</td><td>40000</td><td>80000</td></tr>
  <tr><td>r8in.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r8in.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r8in.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r8in.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r8in.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r8in.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>r8in.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r8in.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r8in.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>r8in.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8in.96xlarge <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>r8in.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8in.metal-96xl <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>r8idn.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>r8idn.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>r8idn.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>r8idn.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>r8idn.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>r8idn.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>r8idn.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>r8idn.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>r8idn.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>r8idn.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8idn.96xlarge <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>r8idn.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8idn.metal-96xl <sup>2</sup></td><td colspan="2">120000</td><td colspan="2">15000.0</td><td colspan="2">480000</td></tr>
  <tr><td>r8ib.large <sup>1</sup></td><td>1563</td><td>25000</td><td>195.38</td><td>3125.00</td><td>7500</td><td>120000</td></tr>
  <tr><td>r8ib.xlarge <sup>1</sup></td><td>3125</td><td>25000</td><td>390.62</td><td>3125.00</td><td>15000</td><td>120000</td></tr>
  <tr><td>r8ib.2xlarge <sup>1</sup></td><td>6250</td><td>25000</td><td>781.25</td><td>3125.00</td><td>30000</td><td>120000</td></tr>
  <tr><td>r8ib.4xlarge <sup>1</sup></td><td>12500</td><td>25000</td><td>1562.50</td><td>3125.00</td><td>60000</td><td>120000</td></tr>
  <tr><td>r8ib.8xlarge <sup>2</sup></td><td colspan="2">25000</td><td colspan="2">3125.0</td><td colspan="2">120000</td></tr>
  <tr><td>r8ib.12xlarge <sup>2</sup></td><td colspan="2">37500</td><td colspan="2">4687.5</td><td colspan="2">180000</td></tr>
  <tr><td>r8ib.16xlarge <sup>2</sup></td><td colspan="2">50000</td><td colspan="2">6250.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8ib.24xlarge <sup>2</sup></td><td colspan="2">75000</td><td colspan="2">9375.0</td><td colspan="2">360000</td></tr>
  <tr><td>r8ib.32xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">480000</td></tr>
  <tr><td>r8ib.48xlarge <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>r8ib.96xlarge <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>r8ib.metal-48xl <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>r8ib.metal-96xl <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>r8idb.large <sup>1</sup></td><td>1563</td><td>25000</td><td>195.38</td><td>3125.00</td><td>7500</td><td>120000</td></tr>
  <tr><td>r8idb.xlarge <sup>1</sup></td><td>3125</td><td>25000</td><td>390.62</td><td>3125.00</td><td>15000</td><td>120000</td></tr>
  <tr><td>r8idb.2xlarge <sup>1</sup></td><td>6250</td><td>25000</td><td>781.25</td><td>3125.00</td><td>30000</td><td>120000</td></tr>
  <tr><td>r8idb.4xlarge <sup>1</sup></td><td>12500</td><td>25000</td><td>1562.50</td><td>3125.00</td><td>60000</td><td>120000</td></tr>
  <tr><td>r8idb.8xlarge <sup>2</sup></td><td colspan="2">25000</td><td colspan="2">3125.0</td><td colspan="2">120000</td></tr>
  <tr><td>r8idb.12xlarge <sup>2</sup></td><td colspan="2">37500</td><td colspan="2">4687.5</td><td colspan="2">180000</td></tr>
  <tr><td>r8idb.16xlarge <sup>2</sup></td><td colspan="2">50000</td><td colspan="2">6250.0</td><td colspan="2">240000</td></tr>
  <tr><td>r8idb.24xlarge <sup>2</sup></td><td colspan="2">75000</td><td colspan="2">9375.0</td><td colspan="2">360000</td></tr>
  <tr><td>r8idb.32xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">480000</td></tr>
  <tr><td>r8idb.48xlarge <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>r8idb.96xlarge <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>r8idb.metal-48xl <sup>2</sup></td><td colspan="2">150000</td><td colspan="2">18750.0</td><td colspan="2">720000</td></tr>
  <tr><td>r8idb.metal-96xl <sup>2</sup></td><td colspan="2">300000</td><td colspan="2">37500.0</td><td colspan="2">1440000</td></tr>
  <tr><td>r9g.medium <sup>1</sup></td><td>380</td><td>12000</td><td>47.50</td><td>1500.00</td><td>2500</td><td>48000</td></tr>
  <tr><td>r9g.large <sup>1</sup></td><td>760</td><td>12000</td><td>95.00</td><td>1500.00</td><td>3600</td><td>48000</td></tr>
  <tr><td>r9g.xlarge <sup>1</sup></td><td>1500</td><td>12000</td><td>187.50</td><td>1500.00</td><td>6000</td><td>48000</td></tr>
  <tr><td>r9g.2xlarge <sup>1</sup></td><td>3000</td><td>12000</td><td>375.00</td><td>1500.00</td><td>12000</td><td>48000</td></tr>
  <tr><td>r9g.4xlarge <sup>1</sup></td><td>6000</td><td>12000</td><td>750.00</td><td>1500.00</td><td>24000</td><td>48000</td></tr>
  <tr><td>r9g.8xlarge <sup>2</sup></td><td colspan="2">12000</td><td colspan="2">1500.0</td><td colspan="2">48000</td></tr>
  <tr><td>r9g.12xlarge <sup>2</sup></td><td colspan="2">18000</td><td colspan="2">2250.0</td><td colspan="2">72000</td></tr>
  <tr><td>r9g.16xlarge <sup>2</sup></td><td colspan="2">24000</td><td colspan="2">3000.0</td><td colspan="2">96000</td></tr>
  <tr><td>r9g.24xlarge <sup>2</sup></td><td colspan="2">36000</td><td colspan="2">4500.0</td><td colspan="2">144000</td></tr>
  <tr><td>r9g.48xlarge <sup>2</sup></td><td colspan="2">72000</td><td colspan="2">9000.0</td><td colspan="2">288000</td></tr>
  <tr><td>r9g.metal-48xl <sup>2</sup></td><td colspan="2">72000</td><td colspan="2">9000.0</td><td colspan="2">288000</td></tr>
  <tr><td>r9gd.medium <sup>1</sup></td><td>380</td><td>12000</td><td>47.50</td><td>1500.00</td><td>2500</td><td>48000</td></tr>
  <tr><td>r9gd.large <sup>1</sup></td><td>760</td><td>12000</td><td>95.00</td><td>1500.00</td><td>3600</td><td>48000</td></tr>
  <tr><td>r9gd.xlarge <sup>1</sup></td><td>1500</td><td>12000</td><td>187.50</td><td>1500.00</td><td>6000</td><td>48000</td></tr>
  <tr><td>r9gd.2xlarge <sup>1</sup></td><td>3000</td><td>12000</td><td>375.00</td><td>1500.00</td><td>12000</td><td>48000</td></tr>
  <tr><td>r9gd.4xlarge <sup>1</sup></td><td>6000</td><td>12000</td><td>750.00</td><td>1500.00</td><td>24000</td><td>48000</td></tr>
  <tr><td>r9gd.8xlarge <sup>2</sup></td><td colspan="2">12000</td><td colspan="2">1500.0</td><td colspan="2">48000</td></tr>
  <tr><td>r9gd.12xlarge <sup>2</sup></td><td colspan="2">18000</td><td colspan="2">2250.0</td><td colspan="2">72000</td></tr>
  <tr><td>r9gd.16xlarge <sup>2</sup></td><td colspan="2">24000</td><td colspan="2">3000.0</td><td colspan="2">96000</td></tr>
  <tr><td>r9gd.24xlarge <sup>2</sup></td><td colspan="2">36000</td><td colspan="2">4500.0</td><td colspan="2">144000</td></tr>
  <tr><td>r9gd.48xlarge <sup>2</sup></td><td colspan="2">72000</td><td colspan="2">9000.0</td><td colspan="2">288000</td></tr>
  <tr><td>r9gd.metal-48xl <sup>2</sup></td><td colspan="2">72000</td><td colspan="2">9000.0</td><td colspan="2">288000</td></tr>
  <tr><td>u-3tb1.56xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>u-6tb1.56xlarge <sup>2</sup></td><td colspan="2">38000</td><td colspan="2">4750.0</td><td colspan="2">160000</td></tr>
  <tr><td>u-6tb1.112xlarge <sup>2</sup></td><td colspan="2">38000</td><td colspan="2">4750.0</td><td colspan="2">160000</td></tr>
  <tr><td>u-6tb1.metal <sup>2</sup></td><td colspan="2">38000</td><td colspan="2">4750.0</td><td colspan="2">160000</td></tr>
  <tr><td>u-9tb1.112xlarge <sup>2</sup></td><td colspan="2">38000</td><td colspan="2">4750.0</td><td colspan="2">160000</td></tr>
  <tr><td>u-9tb1.metal <sup>2</sup></td><td colspan="2">38000</td><td colspan="2">4750.0</td><td colspan="2">160000</td></tr>
  <tr><td>u-12tb1.112xlarge <sup>2</sup></td><td colspan="2">38000</td><td colspan="2">4750.0</td><td colspan="2">160000</td></tr>
  <tr><td>u-12tb1.metal <sup>2</sup></td><td colspan="2">38000</td><td colspan="2">4750.0</td><td colspan="2">160000</td></tr>
  <tr><td>u-18tb1.112xlarge <sup>2</sup></td><td colspan="2">38000</td><td colspan="2">4750.0</td><td colspan="2">160000</td></tr>
  <tr><td>u-18tb1.metal <sup>2</sup></td><td colspan="2">38000</td><td colspan="2">4750.0</td><td colspan="2">160000</td></tr>
  <tr><td>u-24tb1.112xlarge <sup>2</sup></td><td colspan="2">38000</td><td colspan="2">4750.0</td><td colspan="2">160000</td></tr>
  <tr><td>u-24tb1.metal <sup>2</sup></td><td colspan="2">38000</td><td colspan="2">4750.0</td><td colspan="2">160000</td></tr>
  <tr><td>u7i-6tb.112xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">560000</td></tr>
  <tr><td>u7i-8tb.112xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">560000</td></tr>
  <tr><td>u7i-12tb.224xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">560000</td></tr>
  <tr><td>u7in-16tb.224xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">560000</td></tr>
  <tr><td>u7in-24tb.224xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">560000</td></tr>
  <tr><td>u7in-32tb.224xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">560000</td></tr>
  <tr><td>u7inh-32tb.480xlarge <sup>2</sup></td><td colspan="2">160000</td><td colspan="2">20000.0</td><td colspan="2">840000</td></tr>
  <tr><td>x1.16xlarge <sup>2</sup></td><td colspan="2">7000</td><td colspan="2">875.0</td><td colspan="2">40000</td></tr>
  <tr><td>x1.32xlarge <sup>2</sup></td><td colspan="2">14000</td><td colspan="2">1750.0</td><td colspan="2">80000</td></tr>
  <tr><td>x1e.xlarge <sup>2</sup></td><td colspan="2">500</td><td colspan="2">62.5</td><td colspan="2">3700</td></tr>
  <tr><td>x1e.2xlarge <sup>2</sup></td><td colspan="2">1000</td><td colspan="2">125.0</td><td colspan="2">7400</td></tr>
  <tr><td>x1e.4xlarge <sup>2</sup></td><td colspan="2">1750</td><td colspan="2">218.75</td><td colspan="2">10000</td></tr>
  <tr><td>x1e.8xlarge <sup>2</sup></td><td colspan="2">3500</td><td colspan="2">437.5</td><td colspan="2">20000</td></tr>
  <tr><td>x1e.16xlarge <sup>2</sup></td><td colspan="2">7000</td><td colspan="2">875.0</td><td colspan="2">40000</td></tr>
  <tr><td>x1e.32xlarge <sup>2</sup></td><td colspan="2">14000</td><td colspan="2">1750.0</td><td colspan="2">80000</td></tr>
  <tr><td>x2gd.medium <sup>1</sup></td><td>315</td><td>4750</td><td>39.38</td><td>593.75</td><td>2500</td><td>20000</td></tr>
  <tr><td>x2gd.large <sup>1</sup></td><td>630</td><td>4750</td><td>78.75</td><td>593.75</td><td>3600</td><td>20000</td></tr>
  <tr><td>x2gd.xlarge <sup>1</sup></td><td>1188</td><td>4750</td><td>148.50</td><td>593.75</td><td>6000</td><td>20000</td></tr>
  <tr><td>x2gd.2xlarge <sup>1</sup></td><td>2375</td><td>4750</td><td>296.88</td><td>593.75</td><td>12000</td><td>20000</td></tr>
  <tr><td>x2gd.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>x2gd.8xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>x2gd.12xlarge <sup>2</sup></td><td colspan="2">14250</td><td colspan="2">1781.25</td><td colspan="2">60000</td></tr>
  <tr><td>x2gd.16xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>x2gd.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>x2idn.16xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">173333</td></tr>
  <tr><td>x2idn.24xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">260000</td></tr>
  <tr><td>x2idn.32xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">260000</td></tr>
  <tr><td>x2idn.metal <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">260000</td></tr>
  <tr><td>x2iedn.xlarge <sup>1</sup></td><td>2500</td><td>20000</td><td>312.50</td><td>2500.00</td><td>8125</td><td>65000</td></tr>
  <tr><td>x2iedn.2xlarge <sup>1</sup></td><td>5000</td><td>20000</td><td>625.00</td><td>2500.00</td><td>16250</td><td>65000</td></tr>
  <tr><td>x2iedn.4xlarge <sup>1</sup></td><td>10000</td><td>20000</td><td>1250.00</td><td>2500.00</td><td>32500</td><td>65000</td></tr>
  <tr><td>x2iedn.8xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">65000</td></tr>
  <tr><td>x2iedn.16xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">130000</td></tr>
  <tr><td>x2iedn.24xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">195000</td></tr>
  <tr><td>x2iedn.32xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">260000</td></tr>
  <tr><td>x2iedn.metal <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">260000</td></tr>
  <tr><td>x2iezn.2xlarge <sup>2</sup></td><td colspan="2">3170</td><td colspan="2">396.25</td><td colspan="2">13333</td></tr>
  <tr><td>x2iezn.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>x2iezn.6xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>x2iezn.8xlarge <sup>2</sup></td><td colspan="2">12000</td><td colspan="2">1500.0</td><td colspan="2">55000</td></tr>
  <tr><td>x2iezn.12xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>x2iezn.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>x8g.medium <sup>1</sup></td><td>315</td><td>10000</td><td>39.38</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>x8g.large <sup>1</sup></td><td>630</td><td>10000</td><td>78.75</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>x8g.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>x8g.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>x8g.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>x8g.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>x8g.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>x8g.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>x8g.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>x8g.48xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>x8g.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>x8g.metal-48xl <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">240000</td></tr>
  <tr><td>x8aedz.large <sup>1</sup></td><td>1250</td><td>15000</td><td>156.25</td><td>1875.00</td><td>5000</td><td>60000</td></tr>
  <tr><td>x8aedz.xlarge <sup>1</sup></td><td>2500</td><td>15000</td><td>312.50</td><td>1875.00</td><td>10000</td><td>60000</td></tr>
  <tr><td>x8aedz.3xlarge <sup>1</sup></td><td>7500</td><td>15000</td><td>937.50</td><td>1875.00</td><td>30000</td><td>60000</td></tr>
  <tr><td>x8aedz.6xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>x8aedz.12xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>x8aedz.24xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>x8aedz.metal-12xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>x8aedz.metal-24xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>x8i.large <sup>1</sup></td><td>650</td><td>10000</td><td>81.25</td><td>1250.00</td><td>3600</td><td>40000</td></tr>
  <tr><td>x8i.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>x8i.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>12000</td><td>40000</td></tr>
  <tr><td>x8i.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>x8i.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>x8i.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>x8i.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>x8i.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>x8i.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>x8i.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>x8i.64xlarge <sup>2</sup></td><td colspan="2">70000</td><td colspan="2">8750.0</td><td colspan="2">320000</td></tr>
  <tr><td>x8i.96xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">480000</td></tr>
  <tr><td>x8i.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>x8i.metal-96xl <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">480000</td></tr>
  <tr><td>z1d.large <sup>1</sup></td><td>800</td><td>3170</td><td>100.00</td><td>396.25</td><td>3333</td><td>13333</td></tr>
  <tr><td>z1d.xlarge <sup>1</sup></td><td>1580</td><td>3170</td><td>197.50</td><td>396.25</td><td>6667</td><td>13333</td></tr>
  <tr><td>z1d.2xlarge <sup>2</sup></td><td colspan="2">3170</td><td colspan="2">396.25</td><td colspan="2">13333</td></tr>
  <tr><td>z1d.3xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>z1d.6xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>z1d.12xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>z1d.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
</tbody>
</table>

<sup>1</sup> These instances can sustain the maximum performance for 30 minutes at least once every 24 hours, after which they revert to their baseline performance.

<sup>2</sup> These instances can sustain their stated performance indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these instances.

### Storage optimized
<a name="current-storage-optimized"></a>

<table>
<thead>
  <tr><th>Instance size</th><th>Baseline bandwidth (Mbps)</th><th>Maximum bandwidth (Mbps)</th><th>Baseline throughput (MB/s, 128 KiB I/O)</th><th>Maximum throughput (MB/s, 128 KiB I/O)</th><th>Baseline IOPS (16 KiB I/O)</th><th>Maximum IOPS (16 KiB I/O)</th></tr>
</thead>
<tbody>
  <tr><td>d2.xlarge <sup>2</sup></td><td colspan="2">750</td><td colspan="2">93.75</td><td colspan="2">6000</td></tr>
  <tr><td>d2.2xlarge <sup>2</sup></td><td colspan="2">1000</td><td colspan="2">125.0</td><td colspan="2">8000</td></tr>
  <tr><td>d2.4xlarge <sup>2</sup></td><td colspan="2">2000</td><td colspan="2">250.0</td><td colspan="2">16000</td></tr>
  <tr><td>d2.8xlarge <sup>2</sup></td><td colspan="2">4000</td><td colspan="2">500.0</td><td colspan="2">32000</td></tr>
  <tr><td>d3.xlarge <sup>1</sup></td><td>850</td><td>2800</td><td>106.25</td><td>350.00</td><td>5000</td><td>15000</td></tr>
  <tr><td>d3.2xlarge <sup>1</sup></td><td>1700</td><td>2800</td><td>212.50</td><td>350.00</td><td>10000</td><td>15000</td></tr>
  <tr><td>d3.4xlarge <sup>2</sup></td><td colspan="2">2800</td><td colspan="2">350.0</td><td colspan="2">15000</td></tr>
  <tr><td>d3.8xlarge <sup>2</sup></td><td colspan="2">5000</td><td colspan="2">625.0</td><td colspan="2">30000</td></tr>
  <tr><td>d3en.xlarge <sup>1</sup></td><td>850</td><td>2800</td><td>106.25</td><td>350.00</td><td>5000</td><td>15000</td></tr>
  <tr><td>d3en.2xlarge <sup>1</sup></td><td>1700</td><td>2800</td><td>212.50</td><td>350.00</td><td>10000</td><td>15000</td></tr>
  <tr><td>d3en.4xlarge <sup>2</sup></td><td colspan="2">2800</td><td colspan="2">350.0</td><td colspan="2">15000</td></tr>
  <tr><td>d3en.6xlarge <sup>2</sup></td><td colspan="2">4000</td><td colspan="2">500.0</td><td colspan="2">25000</td></tr>
  <tr><td>d3en.8xlarge <sup>2</sup></td><td colspan="2">5000</td><td colspan="2">625.0</td><td colspan="2">30000</td></tr>
  <tr><td>d3en.12xlarge <sup>2</sup></td><td colspan="2">7000</td><td colspan="2">875.0</td><td colspan="2">40000</td></tr>
  <tr><td>h1.2xlarge <sup>2</sup></td><td colspan="2">1750</td><td colspan="2">218.75</td><td colspan="2">12000</td></tr>
  <tr><td>h1.4xlarge <sup>2</sup></td><td colspan="2">3500</td><td colspan="2">437.5</td><td colspan="2">20000</td></tr>
  <tr><td>h1.8xlarge <sup>2</sup></td><td colspan="2">7000</td><td colspan="2">875.0</td><td colspan="2">40000</td></tr>
  <tr><td>h1.16xlarge <sup>2</sup></td><td colspan="2">14000</td><td colspan="2">1750.0</td><td colspan="2">80000</td></tr>
  <tr><td>i3.large <sup>2</sup></td><td colspan="2">425</td><td colspan="2">53.125</td><td colspan="2">3000</td></tr>
  <tr><td>i3.xlarge <sup>2</sup></td><td colspan="2">850</td><td colspan="2">106.25</td><td colspan="2">6000</td></tr>
  <tr><td>i3.2xlarge <sup>2</sup></td><td colspan="2">1700</td><td colspan="2">212.5</td><td colspan="2">12000</td></tr>
  <tr><td>i3.4xlarge <sup>2</sup></td><td colspan="2">3500</td><td colspan="2">437.5</td><td colspan="2">16000</td></tr>
  <tr><td>i3.8xlarge <sup>2</sup></td><td colspan="2">7000</td><td colspan="2">875.0</td><td colspan="2">32500</td></tr>
  <tr><td>i3.16xlarge <sup>2</sup></td><td colspan="2">14000</td><td colspan="2">1750.0</td><td colspan="2">65000</td></tr>
  <tr><td>i3.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>i3en.large <sup>1</sup></td><td>576</td><td>4750</td><td>72.10</td><td>593.75</td><td>3000</td><td>20000</td></tr>
  <tr><td>i3en.xlarge <sup>1</sup></td><td>1153</td><td>4750</td><td>144.20</td><td>593.75</td><td>6000</td><td>20000</td></tr>
  <tr><td>i3en.2xlarge <sup>1</sup></td><td>2307</td><td>4750</td><td>288.39</td><td>593.75</td><td>12000</td><td>20000</td></tr>
  <tr><td>i3en.3xlarge <sup>1</sup></td><td>3800</td><td>4750</td><td>475.00</td><td>593.75</td><td>15000</td><td>20000</td></tr>
  <tr><td>i3en.6xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>i3en.12xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>i3en.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>i3en.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>i4g.large <sup>1</sup></td><td>625</td><td>10000</td><td>78.12</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>i4g.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>5000</td><td>40000</td></tr>
  <tr><td>i4g.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>10000</td><td>40000</td></tr>
  <tr><td>i4g.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>i4g.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>i4g.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>i4i.large <sup>1</sup></td><td>625</td><td>10000</td><td>78.12</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>i4i.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>5000</td><td>40000</td></tr>
  <tr><td>i4i.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>10000</td><td>40000</td></tr>
  <tr><td>i4i.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>i4i.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>i4i.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>i4i.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>i4i.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>i4i.32xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>i4i.metal <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>i7i.large <sup>1</sup></td><td>625</td><td>10000</td><td>78.12</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>i7i.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>5000</td><td>40000</td></tr>
  <tr><td>i7i.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>10000</td><td>40000</td></tr>
  <tr><td>i7i.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>i7i.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>i7i.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>i7i.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>i7i.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>i7i.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>i7i.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>i7i.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>i7ie.large <sup>1</sup></td><td>625</td><td>10000</td><td>78.12</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>i7ie.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>5000</td><td>40000</td></tr>
  <tr><td>i7ie.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>10000</td><td>40000</td></tr>
  <tr><td>i7ie.3xlarge <sup>1</sup></td><td>3750</td><td>10000</td><td>468.75</td><td>1250.00</td><td>15000</td><td>40000</td></tr>
  <tr><td>i7ie.6xlarge <sup>1</sup></td><td>7500</td><td>10000</td><td>937.50</td><td>1250.00</td><td>30000</td><td>40000</td></tr>
  <tr><td>i7ie.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>i7ie.18xlarge <sup>2</sup></td><td colspan="2">22500</td><td colspan="2">2812.5</td><td colspan="2">90000</td></tr>
  <tr><td>i7ie.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>i7ie.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>i7ie.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>i7ie.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>i8g.large <sup>1</sup></td><td>625</td><td>10000</td><td>78.12</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>i8g.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>5000</td><td>40000</td></tr>
  <tr><td>i8g.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>10000</td><td>40000</td></tr>
  <tr><td>i8g.4xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>i8g.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>i8g.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>i8g.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>i8g.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>i8g.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>i8g.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>i8g.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>i8ge.large <sup>1</sup></td><td>625</td><td>10000</td><td>78.12</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>i8ge.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>5000</td><td>40000</td></tr>
  <tr><td>i8ge.2xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>10000</td><td>40000</td></tr>
  <tr><td>i8ge.3xlarge <sup>1</sup></td><td>3750</td><td>10000</td><td>468.75</td><td>1250.00</td><td>15000</td><td>40000</td></tr>
  <tr><td>i8ge.6xlarge <sup>1</sup></td><td>7500</td><td>10000</td><td>937.50</td><td>1250.00</td><td>30000</td><td>40000</td></tr>
  <tr><td>i8ge.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>i8ge.18xlarge <sup>2</sup></td><td colspan="2">22500</td><td colspan="2">2812.5</td><td colspan="2">90000</td></tr>
  <tr><td>i8ge.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>i8ge.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>i8ge.metal-24xl <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>i8ge.metal-48xl <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>im4gn.large <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>5000</td><td>40000</td></tr>
  <tr><td>im4gn.xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>10000</td><td>40000</td></tr>
  <tr><td>im4gn.2xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>im4gn.4xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>im4gn.8xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>im4gn.16xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>is4gen.medium <sup>1</sup></td><td>625</td><td>10000</td><td>78.12</td><td>1250.00</td><td>2500</td><td>40000</td></tr>
  <tr><td>is4gen.large <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>5000</td><td>40000</td></tr>
  <tr><td>is4gen.xlarge <sup>1</sup></td><td>2500</td><td>10000</td><td>312.50</td><td>1250.00</td><td>10000</td><td>40000</td></tr>
  <tr><td>is4gen.2xlarge <sup>1</sup></td><td>5000</td><td>10000</td><td>625.00</td><td>1250.00</td><td>20000</td><td>40000</td></tr>
  <tr><td>is4gen.4xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>is4gen.8xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
</tbody>
</table>

<sup>1</sup> These instances can sustain the maximum performance for 30 minutes at least once every 24 hours, after which they revert to their baseline performance.

<sup>2</sup> These instances can sustain their stated performance indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these instances.

### Accelerated computing
<a name="current-accelerated-computing"></a>

<table>
<thead>
  <tr><th>Instance size</th><th>Baseline bandwidth (Mbps)</th><th>Maximum bandwidth (Mbps)</th><th>Baseline throughput (MB/s, 128 KiB I/O)</th><th>Maximum throughput (MB/s, 128 KiB I/O)</th><th>Baseline IOPS (16 KiB I/O)</th><th>Maximum IOPS (16 KiB I/O)</th></tr>
</thead>
<tbody>
  <tr><td>dl1.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>dl2q.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>f2.6xlarge <sup>2</sup></td><td colspan="2">7500</td><td colspan="2">937.5</td><td colspan="2">30000</td></tr>
  <tr><td>f2.12xlarge <sup>2</sup></td><td colspan="2">15000</td><td colspan="2">1875.0</td><td colspan="2">60000</td></tr>
  <tr><td>f2.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>g3.4xlarge <sup>2</sup></td><td colspan="2">3500</td><td colspan="2">437.5</td><td colspan="2">20000</td></tr>
  <tr><td>g3.8xlarge <sup>2</sup></td><td colspan="2">7000</td><td colspan="2">875.0</td><td colspan="2">40000</td></tr>
  <tr><td>g3.16xlarge <sup>2</sup></td><td colspan="2">14000</td><td colspan="2">1750.0</td><td colspan="2">80000</td></tr>
  <tr><td>g4ad.xlarge <sup>1</sup></td><td>400</td><td>3170</td><td>50.00</td><td>396.25</td><td>1700</td><td>13333</td></tr>
  <tr><td>g4ad.2xlarge <sup>1</sup></td><td>800</td><td>3170</td><td>100.00</td><td>396.25</td><td>3400</td><td>13333</td></tr>
  <tr><td>g4ad.4xlarge <sup>1</sup></td><td>1580</td><td>3170</td><td>197.50</td><td>396.25</td><td>6700</td><td>13333</td></tr>
  <tr><td>g4ad.8xlarge <sup>2</sup></td><td colspan="2">3170</td><td colspan="2">396.25</td><td colspan="2">13333</td></tr>
  <tr><td>g4ad.16xlarge <sup>2</sup></td><td colspan="2">6300</td><td colspan="2">787.5</td><td colspan="2">26667</td></tr>
  <tr><td>g4dn.xlarge <sup>1</sup></td><td>950</td><td>3500</td><td>118.75</td><td>437.50</td><td>3000</td><td>20000</td></tr>
  <tr><td>g4dn.2xlarge <sup>1</sup></td><td>1150</td><td>3500</td><td>143.75</td><td>437.50</td><td>6000</td><td>20000</td></tr>
  <tr><td>g4dn.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>g4dn.8xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>g4dn.12xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>g4dn.16xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>g4dn.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>g5.xlarge <sup>1</sup></td><td>700</td><td>3500</td><td>87.50</td><td>437.50</td><td>3000</td><td>15000</td></tr>
  <tr><td>g5.2xlarge <sup>1</sup></td><td>850</td><td>3500</td><td>106.25</td><td>437.50</td><td>3500</td><td>15000</td></tr>
  <tr><td>g5.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>g5.8xlarge <sup>2</sup></td><td colspan="2">16000</td><td colspan="2">2000.0</td><td colspan="2">65000</td></tr>
  <tr><td>g5.12xlarge <sup>2</sup></td><td colspan="2">16000</td><td colspan="2">2000.0</td><td colspan="2">65000</td></tr>
  <tr><td>g5.16xlarge <sup>2</sup></td><td colspan="2">16000</td><td colspan="2">2000.0</td><td colspan="2">65000</td></tr>
  <tr><td>g5.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>g5.48xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>g5g.xlarge <sup>1</sup></td><td>1188</td><td>4750</td><td>148.50</td><td>593.75</td><td>6000</td><td>20000</td></tr>
  <tr><td>g5g.2xlarge <sup>1</sup></td><td>2375</td><td>4750</td><td>296.88</td><td>593.75</td><td>12000</td><td>20000</td></tr>
  <tr><td>g5g.4xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>g5g.8xlarge <sup>2</sup></td><td colspan="2">9500</td><td colspan="2">1187.5</td><td colspan="2">40000</td></tr>
  <tr><td>g5g.16xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>g5g.metal <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>g6.xlarge <sup>1</sup></td><td>1000</td><td>5000</td><td>125.00</td><td>625.00</td><td>4000</td><td>20000</td></tr>
  <tr><td>g6.2xlarge <sup>1</sup></td><td>2000</td><td>5000</td><td>250.00</td><td>625.00</td><td>8000</td><td>20000</td></tr>
  <tr><td>g6.4xlarge <sup>2</sup></td><td colspan="2">8000</td><td colspan="2">1000.0</td><td colspan="2">32000</td></tr>
  <tr><td>g6.8xlarge <sup>2</sup></td><td colspan="2">16000</td><td colspan="2">2000.0</td><td colspan="2">64000</td></tr>
  <tr><td>g6.12xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>g6.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>g6.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>g6.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>g6e.xlarge <sup>1</sup></td><td>1000</td><td>5000</td><td>125.00</td><td>625.00</td><td>4000</td><td>20000</td></tr>
  <tr><td>g6e.2xlarge <sup>1</sup></td><td>2000</td><td>5000</td><td>250.00</td><td>625.00</td><td>8000</td><td>20000</td></tr>
  <tr><td>g6e.4xlarge <sup>2</sup></td><td colspan="2">8000</td><td colspan="2">1000.0</td><td colspan="2">32000</td></tr>
  <tr><td>g6e.8xlarge <sup>2</sup></td><td colspan="2">16000</td><td colspan="2">2000.0</td><td colspan="2">64000</td></tr>
  <tr><td>g6e.12xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>g6e.16xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>g6e.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>g6e.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>g6f.large <sup>1</sup></td><td>936</td><td>5000</td><td>117.00</td><td>625.00</td><td>3750</td><td>20000</td></tr>
  <tr><td>g6f.xlarge <sup>1</sup></td><td>1000</td><td>5000</td><td>125.00</td><td>625.00</td><td>4000</td><td>20000</td></tr>
  <tr><td>g6f.2xlarge <sup>1</sup></td><td>2000</td><td>5000</td><td>250.00</td><td>625.00</td><td>8000</td><td>20000</td></tr>
  <tr><td>g6f.4xlarge <sup>2</sup></td><td colspan="2">6000</td><td colspan="2">750.0</td><td colspan="2">24000</td></tr>
  <tr><td>gr6.4xlarge <sup>2</sup></td><td colspan="2">8000</td><td colspan="2">1000.0</td><td colspan="2">32000</td></tr>
  <tr><td>gr6.8xlarge <sup>2</sup></td><td colspan="2">16000</td><td colspan="2">2000.0</td><td colspan="2">64000</td></tr>
  <tr><td>gr6f.4xlarge <sup>2</sup></td><td colspan="2">8000</td><td colspan="2">1000.0</td><td colspan="2">32000</td></tr>
  <tr><td>g7.2xlarge <sup>1</sup></td><td>4000</td><td>8000</td><td>500.00</td><td>1000.00</td><td>16000</td><td>32000</td></tr>
  <tr><td>g7.4xlarge <sup>2</sup></td><td colspan="2">8000</td><td colspan="2">1000.0</td><td colspan="2">32000</td></tr>
  <tr><td>g7.8xlarge <sup>2</sup></td><td colspan="2">16000</td><td colspan="2">2000.0</td><td colspan="2">64000</td></tr>
  <tr><td>g7.12xlarge <sup>2</sup></td><td colspan="2">20000</td><td colspan="2">2500.0</td><td colspan="2">80000</td></tr>
  <tr><td>g7.24xlarge <sup>2</sup></td><td colspan="2">40000</td><td colspan="2">5000.0</td><td colspan="2">160000</td></tr>
  <tr><td>g7.48xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">320000</td></tr>
  <tr><td>g7e.2xlarge <sup>1</sup></td><td>2000</td><td>5000</td><td>250.00</td><td>625.00</td><td>8000</td><td>20000</td></tr>
  <tr><td>g7e.4xlarge <sup>2</sup></td><td colspan="2">8000</td><td colspan="2">1000.0</td><td colspan="2">32000</td></tr>
  <tr><td>g7e.8xlarge <sup>2</sup></td><td colspan="2">16000</td><td colspan="2">2000.0</td><td colspan="2">64000</td></tr>
  <tr><td>g7e.12xlarge <sup>2</sup></td><td colspan="2">25000</td><td colspan="2">3125.0</td><td colspan="2">100000</td></tr>
  <tr><td>g7e.24xlarge <sup>2</sup></td><td colspan="2">50000</td><td colspan="2">6250.0</td><td colspan="2">200000</td></tr>
  <tr><td>g7e.48xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">400000</td></tr>
  <tr><td>inf1.xlarge <sup>1</sup></td><td>1190</td><td>4750</td><td>148.75</td><td>593.75</td><td>4000</td><td>20000</td></tr>
  <tr><td>inf1.2xlarge <sup>1</sup></td><td>1190</td><td>4750</td><td>148.75</td><td>593.75</td><td>6000</td><td>20000</td></tr>
  <tr><td>inf1.6xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>inf1.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>inf2.xlarge <sup>1</sup></td><td>1250</td><td>10000</td><td>156.25</td><td>1250.00</td><td>6000</td><td>40000</td></tr>
  <tr><td>inf2.8xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">40000</td></tr>
  <tr><td>inf2.24xlarge <sup>2</sup></td><td colspan="2">30000</td><td colspan="2">3750.0</td><td colspan="2">120000</td></tr>
  <tr><td>inf2.48xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>p3dn.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>p4d.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>p4de.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
  <tr><td>p5.4xlarge <sup>2</sup></td><td colspan="2">10000</td><td colspan="2">1250.0</td><td colspan="2">32500</td></tr>
  <tr><td>p5.48xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">260000</td></tr>
  <tr><td>p5e.48xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">260000</td></tr>
  <tr><td>p5en.48xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">400000</td></tr>
  <tr><td>p6-b200.48xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">400000</td></tr>
  <tr><td>p6-b300.48xlarge <sup>2</sup></td><td colspan="2">100000</td><td colspan="2">12500.0</td><td colspan="2">400000</td></tr>
  <tr><td>p6e-gb200.36xlarge <sup>2</sup></td><td colspan="2">60000</td><td colspan="2">7500.0</td><td colspan="2">240000</td></tr>
  <tr><td>trn1.2xlarge <sup>1</sup></td><td>5000</td><td>20000</td><td>625.00</td><td>2500.00</td><td>16250</td><td>65000</td></tr>
  <tr><td>trn1.32xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">260000</td></tr>
  <tr><td>trn1n.32xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">260000</td></tr>
  <tr><td>trn2.3xlarge <sup>2</sup></td><td colspan="2">5000</td><td colspan="2">625.0</td><td colspan="2">16250</td></tr>
  <tr><td>trn2.48xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">260000</td></tr>
  <tr><td>trn2u.48xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">260000</td></tr>
  <tr><td>trn3.48xlarge <sup>2</sup></td><td colspan="2">80000</td><td colspan="2">10000.0</td><td colspan="2">260000</td></tr>
  <tr><td>vt1.3xlarge <sup>1</sup></td><td>2375</td><td>4750</td><td>296.88</td><td>593.75</td><td>10000</td><td>20000</td></tr>
  <tr><td>vt1.6xlarge <sup>2</sup></td><td colspan="2">4750</td><td colspan="2">593.75</td><td colspan="2">20000</td></tr>
  <tr><td>vt1.24xlarge <sup>2</sup></td><td colspan="2">19000</td><td colspan="2">2375.0</td><td colspan="2">80000</td></tr>
</tbody>
</table>

<sup>1</sup> These instances can sustain the maximum performance for 30 minutes at least once every 24 hours, after which they revert to their baseline performance.

<sup>2</sup> These instances can sustain their stated performance indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these instances.

### High-performance computing
<a name="current-high-performance-computing"></a>

| Instance size | Baseline bandwidth (Mbps) | Maximum bandwidth (Mbps) | Baseline throughput (MB/s, 128 KiB I/O) | Maximum throughput (MB/s, 128 KiB I/O) | Baseline IOPS (16 KiB I/O) | Maximum IOPS (16 KiB I/O) |
| --- | --- | --- | --- | --- | --- | --- |
| hpc6a.48xlarge 1 | 87 | 2085 | 10.88 | 260.62 | 500 | 11000 |
| hpc6id.32xlarge 1 | 87 | 2085 | 10.88 | 260.62 | 500 | 11000 |
| hpc7a.12xlarge 1 | 87 | 2085 | 10.88 | 260.62 | 500 | 11000 |
| hpc7a.24xlarge 1 | 87 | 2085 | 10.88 | 260.62 | 500 | 11000 |
| hpc7a.48xlarge 1 | 87 | 2085 | 10.88 | 260.62 | 500 | 11000 |
| hpc7a.96xlarge 1 | 87 | 2085 | 10.88 | 260.62 | 500 | 11000 |
| hpc7g.4xlarge 1 | 87 | 2085 | 10.88 | 260.62 | 500 | 11000 |
| hpc7g.8xlarge 1 | 87 | 2085 | 10.88 | 260.62 | 500 | 11000 |
| hpc7g.16xlarge 1 | 87 | 2085 | 10.88 | 260.62 | 500 | 11000 |
| hpc8a.96xlarge 1 | 87 | 2085 | 10.88 | 260.62 | 500 | 11000 |

<sup>1</sup> These instances can sustain the maximum performance for 30 minutes at least once every 24 hours, after which they revert to their baseline performance.

<sup>2</sup> These instances can sustain their stated performance indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these instances.

## EBS optimization supported
<a name="previous"></a>

The following instance types support EBS optimization but EBS optimization is not enabled by default. You must enable EBS optimization, at an [additional hourly fee](https://aws.amazon.com/ec2/previous-generation/#EBS-optimized_instances), during or after launch to achieve the level of EBS performance described.

| Instance size | Maximum bandwidth (Mbps) | Maximum throughput (MB/s, 128 KiB I/O) | Maximum IOPS (16 KiB I/O) |
| --- | --- | --- | --- |
| c1.xlarge | 1000 | 125.0 | 8000 |
| c3.xlarge | 500 | 62.5 | 4000 |
| c3.2xlarge | 1000 | 125.0 | 8000 |
| c3.4xlarge | 2000 | 250.0 | 16000 |
| i2.xlarge | 500 | 62.5 | 4000 |
| i2.2xlarge | 1000 | 125.0 | 8000 |
| i2.4xlarge | 2000 | 250.0 | 16000 |
| m1.large | 500 | 62.5 | 4000 |
| m1.xlarge | 1000 | 125.0 | 8000 |
| m2.2xlarge | 500 | 62.5 | 4000 |
| m2.4xlarge | 1000 | 125.0 | 8000 |
| m3.xlarge | 500 | 62.5 | 4000 |
| m3.2xlarge | 1000 | 125.0 | 8000 |
| r3.xlarge | 500 | 62.5 | 4000 |
| r3.2xlarge | 1000 | 125.0 | 8000 |
| r3.4xlarge | 2000 | 250.0 | 16000 |

**Note**
The `i2.8xlarge`, `c3.8xlarge`, and `r3.8xlarge` instances do not have dedicated EBS bandwidth and therefore do not offer EBS optimization. On these instances, network traffic and Amazon EBS traffic share the same 10-gigabit network interface.
