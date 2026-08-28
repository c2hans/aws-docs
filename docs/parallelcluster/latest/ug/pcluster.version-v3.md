---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/pcluster.version-v3.html
---

# `pcluster version`
<a name="pcluster.version-v3"></a>

Displays the version of AWS ParallelCluster.

```
pcluster version [-h] [--debug]
```

## Named arguments
<a name="pcluster-v3.version.namedargs"></a>

**-h, --help**
Shows the help text for `pcluster version`.

**--debug**
Enables debug logging.

**Example using AWS ParallelCluster version 3.1.4:**

```
$ pcluster version
{
  "version": "3.1.4"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
