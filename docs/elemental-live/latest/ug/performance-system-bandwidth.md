---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/performance-system-bandwidth.html
---

# System bandwidth
<a name="performance-system-bandwidth"></a>

System bandwidth is the rate at which network and data traffic moves between process on each core, and between those cores and memory.

## Impact of system bandwidth issues
<a name="performance-system-bandwidth-impact"></a>

Typically, system bandwidth rates don't create performance problems on Elemental Live appliances.

One of the ways that you know there are memory bandwidth problems on the appliance is through error messages in the logs. For more information, see [Assessing performance with logging messages](performance-via-logs.md).

If you suspect that system bandwidth is causing these problems, reduce density on the appliance.

## Measuring system bandwidth
<a name="performance-system-bandwidth-measure"></a>

The `amd_bandwidth` utility is included in Elemental Live versions 2.18.6 and later.

It shows the outbound bandwidth for each socket on the appliance. For example:

```
$ sudo amd_bandwidth
Collecting bandwidth data for 10 seconds...
Socket0 bandwidth: 7.43645 GB/s
Socket1 bandwidth: 19.0827 GB/s
```

## Expected rates
<a name="performance-system-bandwidth-expected"></a>

The following guidelines apply for system bandwidth:
+ Single-socket L8xx appliances have a maximum bandwidth of 90 GBps
+ Dual-socket L8xx appliances have a maximum bandwidth of 140 GBps

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
