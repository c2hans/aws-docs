---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.version.html
---

# `pcluster version`
<a name="pcluster.version"></a>

Displays the AWS ParallelCluster version.

```
pcluster version [ -h ]
```

For command-specific flags, run: `pcluster [command] –-help`.

## Named arguments
<a name="pcluster.version.named.arguments"></a>

**-h, --help**
Shows the help text for `pcluster version`.

When the command is called and begins polling for the status of that call, it's safe to use "Ctrl-C" to exit. You can return to viewing the current status by calling `pcluster status mycluster`.

```
$ pcluster version
2.11.7
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
