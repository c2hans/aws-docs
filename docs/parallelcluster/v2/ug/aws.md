---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/aws.html
---

# `[aws]` section
<a name="aws"></a>

**(Optional)** Used to select the AWS Region.

Cluster creation uses this priority order to select the AWS Region for a new cluster:

1. `-r` or `--region` parameter to [`pcluster create`](pluster.create.md).

1. `AWS_DEFAULT_REGION` environment variable.

1. `aws_region_name` setting in `[aws]` section of AWS ParallelCluster config file (default location is `~/.parallelcluster/config`.) This is the location updated by the [`pcluster configure`](pcluster.configure.md) command.

1. `region` setting in `[default]` section of AWS CLI config file (`~/.aws/config`.)

**Note**
Before AWS ParallelCluster version 2.10.0, these settings were required and applied to all clusters.

To store credentials, you can use the environment, IAM roles for Amazon EC2, or the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html), rather than saving credentials into the AWS ParallelCluster config file.

```
[aws]
aws_region_name = {{Region}}
```

[Update policy: This setting is not analyzed during an update.](using-pcluster-update.md#update-policy-setting-ignored)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
