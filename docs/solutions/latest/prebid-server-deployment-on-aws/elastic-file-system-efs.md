---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/elastic-file-system-efs.html
---

# Elastic File System (EFS)
<a name="elastic-file-system-efs"></a>

## Percent of I/O utilization
<a name="percent-of-io-utilization"></a>
+ The alarm changes state if the I/O utilization is equal to or greater than 100% for 1 minute, indicating the need for additional capacity.
+ If this metric is at 100% often, then consider moving the application to an EFS using the Max I/O performance mode.
+ Metric: `PercentIOLimit` >= 100%
