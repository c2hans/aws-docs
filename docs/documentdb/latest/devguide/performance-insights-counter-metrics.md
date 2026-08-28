---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/performance-insights-counter-metrics.html
---

# Performance Insights for counter metrics
<a name="performance-insights-counter-metrics"></a>

Counter metrics are operating system metrics in the Performance Insights dashboard. To help identify and analyze performance problems, you can correlate counter metrics with DB load.

## Performance Insights operating system counters
<a name="performance-insights-counter-metrics-counters"></a>

The following operating system counters are available with Amazon DocumentDB Performance Insights.

| Counter | Type | Metric |
| --- | --- | --- |
| active | memory | os.memory.active |
| buffers | memory | os.memory.buffers |
| cached | memory | os.memory.cached |
| dirty | memory | os.memory.dirty |
| free | memory | os.memory.free |
| inactive | memory | os.memory.inactive |
| mapped | memory | os.memory.mapped |
| pageTables | memory | os.memory.pageTables |
| slab | memory | os.memory.slab |
| total | memory | os.memory.total |
| writeback | memory | os.memory.writeback |
| idle | cpuUtilization | os.cpuUtilization.idle |
| system | cpuUtilization | os.cpuUtilization.system |
| total | cpuUtilization | os.cpuUtilization.total |
| user | cpuUtilization | os.cpuUtilization.user |
| wait | cpuUtilization | os.cpuUtilization.wait |
| one | loadAverageMinute | os.loadAverageMinute.one |
| fifteen | loadAverageMinute | os.loadAverageMinute.fifteen |
| five | loadAverageMinute | os.loadAverageMinute.five |
| cached | swap | os.swap.cached |
| free | swap | os.swap.free |
| in | swap | os.swap.in |
| out | swap | os.swap.out |
| total | swap | os.swap.total |
| rx | network | os.network.rx |
| tx | network | os.network.tx |
| numVCPUs | general | os.general.numVCPUs |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
