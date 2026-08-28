---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing-starting.html
---

# Starting a Neptune Analytics graph
<a name="managing-starting"></a>

 You can start a Neptune Analytics graph that has been stopped to resume normal operations. The started graph automatically deploys with the latest engine version, ensuring you benefit from the newest capabilities and security updates.

 All graph data, configurations, and identifiers are preserved during the start operation. The graph endpoint remains the same, so your applications can reconnect without configuration changes.

------
#### [ AWS Console ]

 Choose the graph you want to start, then choose **Start graph** from the drop-down **Actions** menu. The graph must be in `STOPPED` state to be started.

 The graph status will change from `STOPPED` to `STARTING`, and finally to `AVAILABLE` when the operation has completed.

------
#### [ CLI/API ]

 You can call the `start-graph` CLI command, or the [StartGraph](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_StartGraph.html) API operation. The graph must be in the `STOPPED` state to be started.

```
aws neptune-graph start-graph --graph-identifier g-sample
```

 The graph status will change from `STOPPED` to `STARTING`, and finally to `AVAILABLE` when the operation has completed.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
