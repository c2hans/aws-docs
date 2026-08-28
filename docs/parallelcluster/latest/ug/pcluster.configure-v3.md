---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/pcluster.configure-v3.html
---

# `pcluster configure`
<a name="pcluster.configure-v3"></a>

Begins an interactive configuration wizard for AWS ParallelCluster version 3. For more information, see [Configure and create a cluster with the AWS ParallelCluster command line interface](install-v3-configuring.md).

```
pcluster configure [-h]
                 --config {{CONFIG}}
                [--debug]
                [--region {{REGION}}]
```

## Named arguments
<a name="pcluster-v3.configure.namedargs"></a>

**-h, --help**
Shows the help text for `pcluster configure`.

**--config {{CONFIG}}**
Path to output the generated config file.

**--debug**
Turn on debug logging.

**--region, -r {{REGION}}**
Specifies the AWS Region to use. The Region must be specified, using the [Region](image-builder-configuration-file-v3.md#yaml-build-image-Region) setting in the image configuration file, the `AWS_DEFAULT_REGION` environment variable, the `region` setting in the `[default]` section of the `~/.aws/config` file, or the `--region` parameter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
