---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/scaling-section.html
---

# `[scaling]` section
<a name="scaling-section"></a>

**Topics**
+ [`scaledown_idletime`](#scaledown-idletime)

Specifies settings that define how the compute nodes scale.

The format is `[scaling {{scaling-name}}]`. {{scaling-name}} must start with a letter, contain no more than 30 characters, and only contain letters, numbers, hyphens (-), and underscores (\_).

```
[scaling custom]
scaledown_idletime = 10
```

## `scaledown_idletime`
<a name="scaledown-idletime"></a>

**(Optional)** Specifies the amount of time in minutes without a job, after which the compute node terminates.

This parameter isn't used if `awsbatch` is the scheduler.

The default value is `10`.

```
scaledown_idletime = 10
```

[Update policy: The compute fleet must be stopped for this setting to be changed for an update.](using-pcluster-update.md#update-policy-compute-fleet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
