---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster-config.html
---

# `pcluster-config`
<a name="pcluster-config"></a>

Updates the AWS ParallelCluster configuration file.

```
pcluster-config [ -h ] [convert]
```

For command-specific flags, run: `pcluster-config [command] –h`.

## Named arguments
<a name="pcluster-config.named.arguments"></a>

**-h, --help**
Shows the help text for `pcluster-config`.

**Note**
The `pcluster-config` command was added in AWS ParallelCluster version 2.9.0.

### Sub-commands
<a name="pcluster-config-subcommands"></a>

#### `pcluster-config convert`
<a name="pcluster-config-convert"></a>

```
pcluster-config convert [ -h ] [ -c {{CONFIG_FILE}} ] [ -t {{CLUSTER_TEMPLATE}} ]
                        [ -o {{OUTPUT_FILE}} ]
```

##### Named arguments
<a name="pcluster-config.convert.namedarg"></a>

**-h, --help**
Shows the help text for `pcluster-config convert`.

**-c {{CONFIG\_FILE}}, --config-file {{CONFIG\_FILE}}**
Specifies the path of the configuration file to read.
Defaults to `~/.parallelcluster/config`.
For more information, see [Configuring AWS ParallelCluster](getting-started-configuring-parallelcluster.md).

**-t {{CLUSTER\_TEMPLATE}}, --cluster-template {{CLUSTER\_TEMPLATE}}**
Indicates the [`[cluster]` section](cluster-definition.md) to use. If this argument is not specified, `pcluster-config convert` will use the [`cluster_template`](global.md#cluster-template) setting in the [`[global]` section](global.md). If that isn't specified, then the `[cluster default]` section is used.

**-o {{OUTPUT\_FILE}}, --output {{OUTPUT\_FILE}}**
Specifies the path of the converted configuration file to be written. By default, the output is written to `STDOUT`.

Example:

```
$ pcluster-config convert -t alpha -o ~/.parallelcluster/multiinstance
```

Converts the cluster configuration specified in the `[cluster alpha]` section of `~/.parallelcluster/config`, writing the converted configuration file to `~/.parallelcluster/multiinstance`.
