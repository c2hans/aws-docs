---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hadoop-container-yarn.html
---

# YARN container bin packing
<a name="Hadoop-container-yarn"></a>

Starting with Amazon EMR version 7.9.0, container bin-packing policy is now available for the YARN capacity scheduler, which is built on top of YARN's multi-node placement policy. Although the feature is disabled by default, when activated, YARN prioritizes filling up a single node with containers before expanding to other cluster nodes, while respecting a predefined packing threshold defined by the configuration `yarn.scheduler.capacity.multi-node-placement.container.bin-packing.percentage`.

The container bin-packing policy offers several benefits as compared to the default uniform container allocation strategy:
+ It Reduces cluster resource fragmentation.
+ It potentially accelerates cluster scale-down operations by launching containers on limited number of nodes when there is available resources on those nodes, hence leaving other nodes idle, which can then be scaled down – thus leading to better cost savings for dynamically scaling a cluster.

## Enable the feature
<a name="enable-feature"></a>

To enable the container bin-packing feature in Amazon EMR, you can add the following YARN site classification:

```
[
	{
		"Classification": "yarn-site",
		"Properties": {
		"yarn.scheduler.capacity.multi-node-placement.container.bin-packing.percentage": "{{integer value from 1-100}}"
		}
	}
]
```

## Considerations
<a name="considerations"></a>
+ The feature is exclusively available for the YARN capacity-scheduler.
+ Enabling the feature automatically activates YARN multi-node placement scheduling strategy.
+ There can be potential performance degradation due to concentrated resource utilization on a limited number of nodes.
+ With this feature, custom auto-scaling policies demonstrate better scale-down operations, compared to managed scaling policy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
